"""GitHub scraper implementation."""

import base64
import logging
import os
from datetime import datetime
from typing import List, Optional
import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models import ContentItem, SourceType, GitHubSourceConfig

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """Scraper for GitHub events and releases."""

    def __init__(self, sources: List[GitHubSourceConfig], http_client: httpx.AsyncClient):
        """Initialize GitHub scraper.

        Args:
            sources: List of GitHub source configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    def _get_headers(self) -> dict:
        """Get request headers with optional authentication.

        Returns:
            dict: HTTP headers
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Horizon-Aggregator"
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch GitHub content items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            if source.type == "user_events" and source.username:
                user_items = await self._fetch_user_events(source, since)
                items.extend(user_items)
            elif source.type == "repo_releases" and source.owner and source.repo:
                release_items = await self._fetch_repo_releases(source, since)
                items.extend(release_items)
            elif source.type == "repo_search" and source.query:
                repo_items = await self._fetch_repo_search(source, since)
                items.extend(repo_items)
            elif source.type == "trending":
                trending_items = await self._fetch_trending(source)
                items.extend(trending_items)

        return items

    async def _fetch_user_events(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch public events for a user.

        Args:
            source: GitHub source configuration
            since: Only fetch events after this time

        Returns:
            List[ContentItem]: Event content items
        """
        url = f"{self.base_url}/users/{source.username}/events/public"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            events = response.json()

            for event in events:
                created_at = datetime.fromisoformat(
                    event["created_at"].replace("Z", "+00:00")
                )

                if created_at < since:
                    continue

                # Filter interesting event types
                event_type = event["type"]
                if event_type not in [
                    "PushEvent", "CreateEvent", "ReleaseEvent",
                    "PublicEvent", "WatchEvent"
                ]:
                    continue

                item = self._parse_event(event, source)
                if item:
                    items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching GitHub events for %s: %s", source.username, e)

        return items

    def _parse_event(self, event: dict, source: GitHubSourceConfig) -> Optional[ContentItem]:
        """Parse GitHub event into ContentItem.

        Args:
            event: GitHub event data
            username: GitHub username

        Returns:
            Optional[ContentItem]: Parsed content item or None
        """
        event_type = event["type"]
        event_id = event["id"]
        created_at = datetime.fromisoformat(event["created_at"].replace("Z", "+00:00"))
        username = source.username

        repo_name = event["repo"]["name"]
        repo_url = f"https://github.com/{repo_name}"

        # Generate title and content based on event type
        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            title = f"{username} pushed {len(commits)} commit(s) to {repo_name}"
            content = "\n".join([c.get("message", "") for c in commits[:3]])
        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type", "repository")
            title = f"{username} created {ref_type} in {repo_name}"
            content = event["payload"].get("description", "")
        elif event_type == "ReleaseEvent":
            release = event["payload"].get("release", {})
            title = f"{username} released {release.get('tag_name', '')} in {repo_name}"
            content = release.get("body", "")
            repo_url = release.get("html_url", repo_url)
        elif event_type == "PublicEvent":
            title = f"{username} made {repo_name} public"
            content = ""
        elif event_type == "WatchEvent":
            title = f"{username} starred {repo_name}"
            content = ""
        else:
            return None

        return ContentItem(
            id=self._generate_id("github", "event", event_id),
            source_type=SourceType.GITHUB,
            title=title,
            url=repo_url,
            content=content,
            author=username,
            published_at=created_at,
            profile=source.profile,
            metadata={
                "event_type": event_type,
                "repo": repo_name,
                "category": source.category,
            }
        )

    async def _fetch_repo_releases(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch releases for a repository.

        Args:
            source: GitHub source configuration
            since: Only fetch releases after this time

        Returns:
            List[ContentItem]: Release content items
        """
        owner, repo = source.owner, source.repo
        url = f"{self.base_url}/repos/{owner}/{repo}/releases"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            releases = response.json()

            for release in releases:
                published_at = datetime.fromisoformat(
                    release["published_at"].replace("Z", "+00:00")
                )

                if published_at < since:
                    continue

                item = ContentItem(
                    id=self._generate_id("github", "release", str(release["id"])),
                    source_type=SourceType.GITHUB,
                    title=f"{owner}/{repo} released {release['tag_name']}",
                    url=release["html_url"],
                    content=release.get("body", ""),
                    author=release["author"]["login"],
                    published_at=published_at,
                    profile=source.profile,
                    metadata={
                        "repo": f"{owner}/{repo}",
                        "tag": release["tag_name"],
                        "prerelease": release.get("prerelease", False),
                        "category": source.category,
                    }
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching releases for %s/%s: %s", owner, repo, e)

        return items

    async def _fetch_repo_search(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Search recently active AI repositories and use README text as body content."""
        since_date = since.date().isoformat()
        query = source.query.strip()
        if "pushed:" not in query:
            query = f"{query} pushed:>={since_date}"
        if source.min_stars and "stars:" not in query:
            query = f"{query} stars:>={source.min_stars}"

        params = {
            "q": query,
            "sort": source.sort,
            "order": source.order,
            "per_page": min(max(source.max_results, 1), 30),
        }
        items: List[ContentItem] = []

        try:
            response = await self.client.get(
                f"{self.base_url}/search/repositories",
                params=params,
                headers=self._get_headers(),
                follow_redirects=True,
            )
            response.raise_for_status()
            repos = response.json().get("items", [])

            for repo in repos[: source.max_results]:
                pushed_raw = repo.get("pushed_at") or repo.get("updated_at")
                if not pushed_raw:
                    continue
                pushed_at = datetime.fromisoformat(pushed_raw.replace("Z", "+00:00"))
                if pushed_at < since:
                    continue

                full_name = repo.get("full_name")
                if not full_name or "/" not in full_name:
                    continue
                stars = int(repo.get("stargazers_count") or 0)
                if source.min_stars and stars < source.min_stars:
                    continue

                readme = ""
                if source.fetch_readme:
                    readme = await self._fetch_repo_readme(full_name, source.readme_max_chars)
                description = (repo.get("description") or "").strip()
                if not readme and not description:
                    continue

                content_lines = [
                    f"GitHub repository activity: {full_name}",
                    f"Stars: {stars}",
                    f"Forks: {repo.get('forks_count') or 0}",
                    f"Open issues: {repo.get('open_issues_count') or 0}",
                    f"Primary language: {repo.get('language') or 'unknown'}",
                    f"Last pushed: {pushed_raw}",
                ]
                if description:
                    content_lines.extend(["", f"Description: {description}"])
                if readme:
                    content_lines.extend(["", "README excerpt:", readme])

                items.append(
                    ContentItem(
                        id=self._generate_id("github", "repo_search", str(repo.get("id"))),
                        source_type=SourceType.GITHUB,
                        title=f"{full_name} active on GitHub",
                        url=repo.get("html_url") or f"https://github.com/{full_name}",
                        content="\n".join(content_lines),
                        author=repo.get("owner", {}).get("login") or full_name.split("/")[0],
                        published_at=pushed_at,
                        profile=source.profile,
                        metadata={
                            "repo": full_name,
                            "stars": stars,
                            "forks": repo.get("forks_count") or 0,
                            "open_issues": repo.get("open_issues_count") or 0,
                            "language": repo.get("language"),
                            "pushed_at": pushed_raw,
                            "search_query": query,
                            "category": source.category,
                        },
                    )
                )
        except httpx.HTTPError as e:
            logger.warning("Error searching GitHub repositories for %s: %s", source.query, e)

        return items

    async def _fetch_trending(self, source: GitHubSourceConfig) -> List[ContentItem]:
        """Fetch GitHub daily trending repositories and use README text as body content."""
        params = {"since": "daily"}
        if source.query:
            params["spoken_language_code"] = source.query
        items: List[ContentItem] = []

        try:
            response = await self.client.get(
                "https://github.com/trending",
                params=params,
                headers={"Accept": "text/html", "User-Agent": "Horizon-Aggregator"},
                follow_redirects=True,
                timeout=20.0,
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            logger.warning("Error fetching GitHub trending repositories: %s", e)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        repos = soup.select("article.Box-row")
        now = datetime.now().astimezone()

        for rank, repo_el in enumerate(repos[: max(source.max_results, 1)], start=1):
            link = repo_el.select_one("h2 a")
            if not link or not link.get("href"):
                continue
            full_name = link.get("href", "").strip("/").replace(" ", "")
            if "/" not in full_name:
                continue

            description_el = repo_el.select_one("p")
            description = description_el.get_text(" ", strip=True) if description_el else ""
            language_el = repo_el.select_one('[itemprop="programmingLanguage"]')
            language = language_el.get_text(" ", strip=True) if language_el else None

            stars = 0
            stars_link = repo_el.select_one(f'a[href="/{full_name}/stargazers"]')
            if stars_link:
                stars_text = stars_link.get_text(" ", strip=True).replace(",", "")
                try:
                    stars = int(stars_text)
                except ValueError:
                    stars = 0

            stars_today = None
            for span in repo_el.select("span"):
                text = span.get_text(" ", strip=True)
                if "stars today" in text or "star today" in text:
                    stars_today = text
                    break

            readme = ""
            if source.fetch_readme:
                readme = await self._fetch_repo_readme(full_name, source.readme_max_chars)
            if not readme and not description:
                continue

            content_lines = [
                f"GitHub daily trending rank: #{rank}",
                f"Repository: {full_name}",
                f"Stars: {stars}",
                f"Stars today: {stars_today or 'unknown'}",
                f"Primary language: {language or 'unknown'}",
            ]
            if description:
                content_lines.extend(["", f"Description: {description}"])
            if readme:
                content_lines.extend(["", "README excerpt:", readme])

            items.append(
                ContentItem(
                    id=self._generate_id("github", "trending", full_name),
                    source_type=SourceType.GITHUB,
                    title=f"GitHub daily #{rank}: {full_name}",
                    url=f"https://github.com/{full_name}",
                    content="\n".join(content_lines),
                    author=full_name.split("/")[0],
                    published_at=now,
                    profile=source.profile,
                    metadata={
                        "repo": full_name,
                        "rank": rank,
                        "stars": stars,
                        "stars_today": stars_today,
                        "language": language,
                        "category": source.category,
                    },
                )
            )

        return items

    async def _fetch_repo_readme(self, full_name: str, max_chars: int) -> str:
        """Fetch a repository README through the GitHub API and return markdown text."""
        try:
            response = await self.client.get(
                f"{self.base_url}/repos/{full_name}/readme",
                headers=self._get_headers(),
                follow_redirects=True,
            )
            response.raise_for_status()
            payload = response.json()
            encoded = payload.get("content") or ""
            if not encoded:
                return ""
            decoded = base64.b64decode(encoded).decode("utf-8", errors="replace")
            return decoded.strip()[:max_chars]
        except Exception as e:
            logger.info("Could not fetch README for %s: %s", full_name, e)
            return ""


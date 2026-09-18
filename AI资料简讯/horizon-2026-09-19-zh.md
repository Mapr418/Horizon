# Horizon 每日速递 - 2026-09-19

> 从 53 条内容中筛选出 10 条重要资讯。

---

**AI 前沿简讯**
1. [Cloudflare 开源 security-audit-skill，登顶 GitHub 日榜](#item-tech-news-1) ⭐️ 8.0/10
2. [GitHub 每日趋势 \#2：Anthropic 的 Claude Code](#item-tech-news-2) ⭐️ 8.0/10
3. [openai-python 发布 v3.15.0：新增 Agent 会话设置、音频模型选项、Responses WebSocket 会话与提示缓存预热等 API 能力](#item-tech-news-3) ⭐️ 8.0/10
4. [Realtime-Venus 开源：inclusionAI 发布 9B 音视频全双工交互模型的两个 checkpoint](#item-tech-news-4) ⭐️ 8.0/10
5. [GitHub 日榜 \#3：阿里开源 Open Code Review，确定性管线 + LLM Agent 的 AI 代码审查 CLI](#item-tech-news-5) ⭐️ 7.0/10
6. [GitHub 日榜 \#5：腾讯 BrowserSkill —— 让 AI Agent 借用你已登录的浏览器](#item-tech-news-6) ⭐️ 7.0/10
7. [openai-python v3.16.0 发布：新增 Webhook 端点管理，弃用 MCP connector\_id](#item-tech-news-7) ⭐️ 7.0/10
8. [Claude Code 在缺少 CLAUDE.md 时改读 AGENTS.md](#item-tech-news-8) ⭐️ 7.0/10
9. [Anthropic 确认运营湿实验室：让自家模型做真实生物实验](#item-tech-news-9) ⭐️ 7.0/10
10. [安全团队据称用 Claude 在 72 小时内链式攻破 OpenAI 社区论坛并进入内部仓库](#item-tech-news-10) ⭐️ 7.0/10

---

## AI 前沿简讯

<a id="item-tech-news-1"></a>
### [Cloudflare 开源 security-audit-skill，登顶 GitHub 日榜](https://github.com/cloudflare/security-audit-skill) ⭐️ 8.0/10

Cloudflare 开源仓库 cloudflare/security-audit-skill 成为 GitHub 每日趋势第 1 名，当前 13,575 stars、单日新增 3,019 stars，主语言为 JavaScript，采用 MIT 许可证。按 README 描述，它是一个“编码代理技能”（coding-agent skill），把编码代理变成安全审计员，通过编排互相隔离的代理依次完成六个阶段：侦察（产出 architecture.md 与 coverage-ledger.json）、以覆盖台账驱动的漏洞搜寻、候选验证、结构化输出（把 confirmed、needs\_validation、rejected 三类记录写入 findings.json 并按 report-schema.json 校验）、独立记录复核，以及目标中立的报告生成（REPORT.md、FINDINGS-DETAIL.md、NEEDS-VALIDATION.md）。它强调对抗式验证：检查某条发现的代理绝不是发现它的代理，且每个唯一候选都交给一个全新验证器尝试证伪；三类结论的语义也被明确区分——confirmed 需要完整来源链路和有界的观测结果，needs\_validation 只记录一个确切未解决事实且不带严重性评级，rejected 则是被证伪的候选。工具链包含零依赖的 validate-coverage-ledger.cjs 与 validate-findings.cjs，前者在台账创建后及每次更新后运行，后者在第 4 阶段和第 5 阶段替换记录后运行；同一仓库的多次运行是累加式的，会利用此前的台账和发现去覆盖缺口、重新验证变更过的源码，而不把陈旧或未解决的工作当成已覆盖。安装方式为 npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit（加 --global 可做用户级安装），使用时用自然语言触发，例如“security audit this codebase”或“find security vulnerabilities in ./src”。README 说明该技能是 Cloudflare 漏洞发现框架（vulnerability discovery harness）的起点，相关系统已发展为多阶段、集群级体系，细节见 Cloudflare 博客文章《Build your own vulnerability harness》。使用门槛包括：一个支持工具调用与并行子代理的编码代理、用于校验器的 Node.js，以及一个操作系统级沙箱——必须禁用外部网络、使用经过清洗的白名单环境、强制资源限制并只允许写入分配的临时路径，否则工作流会把线索保留为 needs\_validation 而不执行目标代码。

github · cloudflare · 9月18日 23:30

**「背景与技术语境」** 这里的“skill”（技能）指编码代理可加载的一套指令与脚本包，通常通过 skills.sh 提供的 Skills CLI 以 npx skills add 安装，代理在识别到“安全审计”“找漏洞”“渗透测试这个代码库”等触发语时自动启用。该技能把软件安全审计中的经典做法——先画信任边界与输入面、再按覆盖清单分配检查项、最后由独立方复核——翻译成多代理工作流，并用 JSON Schema 加零依赖校验脚本把“发现”变成机器可读、可复算的记录。它也是 Cloudflare 自身漏洞发现框架的公开雏形，README 提到该框架后来长成多阶段、面向整个机群（fleet-wide）的系统，而这个仓库保留了单仓库起步版本。技能内置了多份攻击面分类文件，覆盖内存安全与二进制、AI/LLM（提示注入、代理与工具、输出处理）、Web 协议与认证、客户端、供应链与发布、云与部署、RPC 与消息、资源耗尽与可用性、数据隔离与生命周期、桌面/移动与本地 IPC 等方向，便于按目标类型挑选检查类别。

**「对读者意味着什么」** 对学习者和开发者而言，这是一个可以直接上手研究“多代理如何做安全审计”的完整样本：能读到分阶段的提示词组织方式、覆盖台账的数据结构、发现校验器的实现，以及如何用“证伪优先”的独立验证降低误报。它同时说明了一条趋势：安全工具正在从单次静态扫描转向可重复运行、可累加、结果带来源链路与严重性门槛的代理工作流，README 中“单次运行大致只能发现多次运行总计约一半漏洞”的表述也提示复盖度需要靠迭代而非一次跑完。接下来值得关注的是 Cloudflare 那篇漏洞框架博客里的系统化描述、仓库是否随实践更新攻击面分类与校验器，以及其他团队对这套技能在真实代码库上的第三方评测与误报率反馈。

**标签**: `#coding agents`, `#security audit`, `#open-source`, `#Cloudflare`, `#GitHub trending`

---

<a id="item-tech-news-2"></a>
### [GitHub 每日趋势 \#2：Anthropic 的 Claude Code](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 的 Claude Code 今日位列 GitHub 每日趋势榜第 2 名，共获得 146,271 颗星，单日新增 442 颗星，主语言为 TypeScript。README 明确将其定位为“生活在终端里的智能体编码工具”，它能理解代码库，通过自然语言命令执行常规任务、解释复杂代码并处理 Git 工作流。该工具可在终端、IDE 中使用，也可在 GitHub 上通过 @claude 调用。安装方式已更新：npm 安装被标记为弃用，官方推荐 macOS/Linux 使用 curl 脚本或 Homebrew，Windows 使用 PowerShell 脚本或 WinGet。仓库还包含多个插件，用以通过自定义命令和智能体扩展功能。README 也说明了数据收集与使用政策：Claude Code 会收集反馈，包括代码接受或拒绝等使用数据、相关对话数据以及通过 /bug 命令提交的反馈。隐私保护措施包括对敏感信息设置有限保留期、限制用户会话数据访问，并明确承诺不将反馈用于模型训练。更多安装、卸载和故障排查细节可查阅官方设置文档，数据使用政策则链接至 code.claude.com 的相关页面。

github · anthropics · 9月18日 23:30

**「背景」** Claude Code 是 Anthropic 推出的官方开发者工具，属于“代理式编码”（agentic coding）产品类别，即让大语言模型以自主智能体方式在真实开发环境中执行多步任务。该工具可通过 npm 包 @anthropic-ai/claude-code 安装，但 README 已将该方式标记为弃用，推荐使用独立安装脚本或系统包管理器，反映出该工具正从实验性 npm 包转向更稳定的产品化分发。其核心机制是让模型读取项目代码库，根据自然语言指令规划并执行修改、解释和 Git 操作，而不是仅提供代码补全。GitHub 仓库本身还承担插件生态和问题反馈入口的角色，与官方文档站点 code.claude.com 配合使用。

**「影响」** 对开发者和 AI 学习者来说，Claude Code 的持续高热度表明终端内的智能体编码工作流正在成为主流实践，而不仅是实验性演示。值得关注的是安装方式从 npm 转向系统级安装脚本和包管理器，这可能影响团队在 CI、容器和开发机上的部署方式。接下来应留意官方文档中关于权限模型、数据保留政策以及插件生态的更新，因为这些细节直接决定企业环境能否合规采用。

**标签**: `#Claude Code`, `#agentic coding`, `#GitHub trending`, `#Anthropic`, `#developer tools`

---

<a id="item-tech-news-3"></a>
### [openai-python 发布 v3.15.0：新增 Agent 会话设置、音频模型选项、Responses WebSocket 会话与提示缓存预热等 API 能力](https://github.com/openai/openai-python/releases/tag/v3.15.0) ⭐️ 8.0/10

OpenAI 官方 Python SDK openai-python 发布 v3.15.0，版本对比区间为 v3.14.1 至 v3.15.0，发布日期为 2026-09-18，本次更新以 API 功能新增为主。功能项共五项：agent session model settings（\#3882）、audio-mini model choices（\#3886）、compaction progress events（\#3866）、managed Responses WebSocket sessions（\#3887）、prompt-cache prewarming（\#3888），每条均附有对应的 PR 与 commit 链接。Bug 修复一项：preserve chat stream moderation results（\#3864），即保留聊天流式响应中的审核结果。此外还有两项杂项维护：clarify incoming SIP call ID usage（\#3885）与 update image request examples（\#3889）；文档方面移除了 realtime 模块中不存在的类型导入（\#3869）。值得注意的是，这组条目显示 SDK 正在围绕会话生命周期做扩展，包括 Agent 会话的模型设置、Responses 的托管 WebSocket 会话、与上下文压缩相关的进度事件，以及提示缓存预热。发布说明本身只给出功能条目标题与链接，未披露具体参数、模型版本号、配额或价格信息，实际用法需要进入对应 PR 或 commit 查看。

github · openai-sdks\[bot\] · 9月18日 00:52

**「背景」** openai-python 是 OpenAI 官方维护的 Python 客户端库，封装 OpenAI 的 REST 与流式接口，是 Python 开发者调用 OpenAI 模型的主要入口之一，其 changelog 由 openai-sdks 机器人按版本自动生成并发布在 GitHub Releases。Responses API 是 OpenAI 在 Chat Completions 之外提供的接口形态，本次条目中出现的“托管 WebSocket 会话”“Agent 会话模型设置”“压缩进度事件”都属于该接口运行时行为层面的能力。提示缓存预热（prompt-cache prewarming）从命名上与 OpenAI 既有的提示缓存机制相关——该机制用于复用重复的输入前缀以降低延迟和成本，但本次发布说明未给出预热的触发方式与具体收益。

**「影响与下一步」** 对使用 Python SDK 的开发者而言，升级到 v3.15.0 后可直接使用新增的 API 字段与类型，尤其是 Agent 会话配置、Responses WebSocket 会话和提示缓存预热，这几项直接关系到长会话场景下的延迟、连接管理与成本控制。建议先查阅 \#3882、\#3886、\#3866、\#3887、\#3888 等 PR 确认参数与默认行为，再评估是否需要同步升级依赖并检查 CI 兼容性。接下来值得关注的是 OpenAI 是否发布对应的 API 文档更新、配额与计费说明，以及 compaction progress events 与 prompt-cache prewarming 在实际负载下的效果验证。

**标签**: `#OpenAI`, `#openai-python`, `#API/SDK`, `#Responses API`, `#prompt caching`

---

<a id="item-tech-news-4"></a>
### [Realtime-Venus 开源：inclusionAI 发布 9B 音视频全双工交互模型的两个 checkpoint](https://www.reddit.com/r/LocalLLaMA/comments/1wjtav9/inclusionairealtimevenus_hugging_face/) ⭐️ 8.0/10

inclusionAI 在 Hugging Face 上线了 Realtime-Venus 系统的两个 checkpoint，该消息由 Reddit 用户 /u/jacek2023 在 r/LocalLLaMA 转发。其中 Realtime-Venus-Omni 是 9B 的音视频交互模型，它会持续“观看”和“聆听”，自行决定是否回应以及何时回应，并在同一条因果时间轴上生成文本与语音；README 明确说明它是在 MiniCPM-o 4.5 基础上适配而来，支持主动交互、语义打断处理和免训练的长视频记忆。Realtime-Venus-Audio 则是同一流式骨干上的音频聚焦版本，用于音频理解以及音频驱动的对话，输出可以是文本也可以是语音。两个目录都同时包含模型权重和自定义的 Hugging Face Transformers 代码，而异步运行时 Realtime-Venus-Harness 及其外部工具集成并不在模型仓库里，而是放在 GitHub 仓库。README 列出的亮点还包括：原生全双工对话（边说话边感知，并区分附和式反馈、打断、纠正和话题重定向）、Omni-Proactive 主动交互（持续处理时间对齐的视频与音频，事件触发即发起回应而无需用户提示）、以及 Delegation 机制——在共享因果时间轴上发出流内的 &lt;delegate&gt; 请求并消费异步后端结果，使外部任务不阻塞当前对话。长视频记忆部分描述为：归档视觉信息量大的时刻，检索与查询相关且不冗余的证据，再重组对应的音视频上下文，全过程无需额外训练；语音输出则通过捆绑的 Token2wav 资源和参考音色生成。需要提示的是，转发帖与所摘录的 README 内容都没有给出基准测试分数、与同类模型的对比或第三方评测，因此目前只能确认功能设计与开源形式，性能结论仍待验证。

reddit · r/LocalLLaMA · /u/jacek2023 · 9月18日 15:27

**「背景与术语」** 实时全双工交互模型与常见的轮次式对话不同：用户说完再回复的范式下，模型可以在安静时慢慢计算；而全双工要求模型在持续接收音频（本项目中还有视频）的同时输出语音，并自行判断何时该开口、何时被打断，这通常依赖共享的“因果时间轴”来对齐输入与输出。README 把 Realtime-Venus 定位为在 MiniCPM-o 4.5 基础上适配的系统；MiniCPM-o 是 OpenBMB 维护的端侧多模态模型系列，以较小参数量支持视觉、语音等多模态输入与语音输出，这也解释了为什么本次发布的 omni checkpoint 只有 9B。另一个值得注意的工程结构是：模型本身只负责在时间轴上发出 &lt;delegate&gt; 委派请求，真正执行外部工具调用的是 GitHub 上的 Realtime-Venus-Harness 运行时，模型权重与运行时代码被有意分成了两个仓库。

**「影响与下一步」** 对做多模态和实时语音应用的学生与开发者来说，这提供了一个可直接下载的 9B 级音视频全双工开源权重，配合仓库中的自定义 Transformers 代码，具备本地实验主动交互、打断处理和长视频记忆的可行性，而不必依赖闭源实时 API。同时要看到，摘要中没有任何基准数据、硬件需求或许可证说明，免训练长视频记忆的效果也只能靠自测验证，因此短期内的实际价值取决于社区复现结果。接下来值得关注的是官方技术报告或模型卡是否补齐评测与许可证信息、GitHub 上的 Realtime-Venus-Harness 是否易于部署，以及是否出现针对打断、主动回应时延和长视频检索质量的第三方评测。

**标签**: `#open-source model`, `#multimodal`, `#real-time interaction`, `#audio-visual`, `#Hugging Face`

---

<a id="item-tech-news-5"></a>
### [GitHub 日榜 \#3：阿里开源 Open Code Review，确定性管线 + LLM Agent 的 AI 代码审查 CLI](https://github.com/alibaba/open-code-review) ⭐️ 7.0/10

阿里巴巴在 GitHub 上开源的 AI 代码审查 CLI 工具 alibaba/open-code-review 登上 GitHub 日榜第 3 位，仓库累计 36,623 stars、单日新增 2,724 stars，主语言为 Go。该工具脱胎于阿里集团内部官方 AI 代码审查助手，README 称其两年间服务了数万名开发者并识别出数百万个代码缺陷，经大规模验证后孵化成开源项目，用户只需配置一个模型端点即可开始使用。工作机制上，它读取 Git diff，把改动的文件交给可配置的 LLM，由具备工具调用能力的 Agent 生成行级精度的结构化评审意见；Agent 可以读取完整文件内容、检索代码库、查看其他改动文件以获取上下文，从而做更深入的审查而非只看 diff 表面；此外 \`ocr scan\` 命令可审查整个文件，用于审计陌生代码库或没有有意义 diff 的目录。其核心设计是「确定性工程 × Agent」混合架构：文件选择、文件打包（例如把 message\_en.properties 与 message\_zh.properties 捆成同一审查单元）等不许出错的步骤由工程逻辑而非语言模型来保证。README 还提到内建多语言规则集，覆盖 NPE、线程安全、XSS、SQL 注入等问题，并兼容 OpenAI 与 Anthropic 接口。项目给出了 AACR-Bench 基准：由 50 个热门开源仓库、200 个真实 Pull Request、10 种编程语言构建，80 多名资深工程师交叉验证并标注 1,505 条真实问题，数据集发布在 Hugging Face 的 Alibaba-Aone/aacr-bench。README 声称在相同底层模型下，相比通用 Agent（如 Claude Code）其 Precision 与 F1 显著更高、token 消耗约为 1/9 且速度更快，但 Recall 更低，这是刻意偏向精度、减少噪音的取舍。工具支持 Windows、macOS、Linux，npm 包名为 @alibaba-group/open-code-review，并列出 Claude Code、Codex、Cursor、Kimi Code 等支持或兼容的 Agent 环境。

github · alibaba · 9月18日 23:30

**「背景知识」** Open Code Review 属于「AI 代码审查」这类开发者工具：传统方案依赖静态分析规则或人工评审，近年常见做法是把改动 diff 交给大语言模型生成评审意见。它针对的正是纯语言驱动架构的痛点——README 列出通用 Agent 做代码审查时的三类常见问题：大改动集下「抄近路」只审查部分文件导致覆盖不全、报告的问题与真实代码位置漂移、以及自然语言 Skill 难以调试、质量随提示词小幅变化而波动。F1、Precision（精确率）、Recall（召回率）是评估这类工具的常用指标：精确率越高表示误报越少，召回率越高表示漏报越少，F1 是两者的调和平均，因此「高精度、低召回」意味着宁可少报也不愿制造大量待人工分流的告警。阿里把内部使用两年的工具开源并配套放出 AACR-Bench 数据集，属于国内大厂把内部 AI 工程能力对外开放的一类动作。

**「影响与下一步」** 对开发者和学生而言，这是一个可直接接入自有模型端点的开源 CLI：能作为 CI 环节的自动审查器试用，也能借其「确定性工程 + Agent」的分工思路，理解如何用工程约束弥补纯提示词的不可控。需要留意的是，目前可获取的 README 摘录在「Smart file bundling」一节处即被截断，benchmark 对比图与具体数值未在文本中给出，因此 F1、Precision、Recall 与 token 数字仍是官方自述，缺少第三方复现。接下来值得关注官方技术文档与 benchmark 细节、AACR-Bench 数据集的可复现程度，以及它在真实仓库中的误报率和 CI 延迟表现。

**标签**: `#GitHub-trending`, `#open-source`, `#code-review`, `#LLM-Agent`, `#Alibaba`

---

<a id="item-tech-news-6"></a>
### [GitHub 日榜 \#5：腾讯 BrowserSkill —— 让 AI Agent 借用你已登录的浏览器](https://github.com/Tencent/BrowserSkill) ⭐️ 7.0/10

腾讯开源的 BrowserSkill 登上 GitHub 日榜第 5，仓库为 TypeScript 项目，累计 5,265 stars，单日新增 1,319 stars。它是一个「本地 CLI（bsk）+ 浏览器扩展」的组合，用来把 Cursor、Claude Code、Codex、OpenClaw、CodeBuddy、WorkBuddy、Pi、Hermes Agent、DeepSeek Harness 等 AI agent 接到你「已经登录」的浏览器上。其核心机制是显式借用标签页：agent 若要操作你已打开的某个标签页，必须先显式借用，任务完成后归还，其余浏览器内容不受影响。浏览器任务运行在一个独立且可见的 Agent Window 中，因此用户自己的浏览与工作不会被打断。任何能够调用 shell 的 agent 都可以通过 bsk CLI 使用它，不锁定特定模型、agent 框架或 harness。项目内置 human-in-loop：当任务遇到验证码、登录、确认弹窗等只能由人完成的步骤时，agent 可以请你接管，之后继续执行。运行环境方面，支持 macOS（Apple Silicon 与 Intel）、Linux（x64 与 ARM64）、Windows x64；浏览器支持 Chrome 与 Microsoft Edge，其他 Chromium 内核浏览器在支持未打包 Chromium 扩展的前提下预计可用，Firefox 仍在计划中。安装路径包括把 AGENT\_INSTALL.md 交给 agent 自动完成，或手动安装 CLI 与商店扩展，再用 bsk install-skill 选择目标 harness 安装技能；如果需要整页长截图，可用 Quick actions → Full-page screenshot，或让 agent 执行 bsk screenshot --session &lt;id&gt; --full-page --out page.png。

github · Tencent · 9月18日 23:30

**「背景补充」** 传统浏览器自动化（如无头浏览器方案）通常启动一个全新的浏览器实例与全新配置，因此没有你日常的登录态、Cookie 与扩展，遇到需要账号的站点往往要另建测试账号。BrowserSkill 走的是另一条路：复用你真实浏览器的登录状态，通过本地 bsk CLI/daemon 与浏览器扩展通信，再由 agent harness 中的「skill」把 bsk 的用法教给模型。这种「CLI + 扩展 + skill 说明文件」的分层，是当前 agent 工具生态的常见做法——工具本身与模型解耦，任何能调 shell 的 agent 理论上都能接入。项目由腾讯开源，当前仅提供 README 层面的机制说明，尚未见公开的基准评测或正式技术报告。

**「影响与后续关注」** 对正在做 agent 产品的开发者来说，这个项目把「如何安全地把 agent 接入真人登录态」做成了一个可复用的现成方案，显式借用/归还标签页与 human-in-loop 接管机制，是比无头浏览器更贴近真实业务场景的交互模型。对企业与个人用户而言，让 agent 进入已登录浏览器意味着权限与隐私边界需要重新评估，README 中并未给出更细的权限沙箱说明，值得在实际使用前核实。接下来可关注 Firefox 支持何时落地、是否有更完整的权限模型文档，以及第三方对其稳定性与安全性的实测反馈。

**标签**: `#AI agents`, `#browser automation`, `#open source`, `#GitHub trending`, `#developer tools`

---

<a id="item-tech-news-7"></a>
### [openai-python v3.16.0 发布：新增 Webhook 端点管理，弃用 MCP connector\_id](https://github.com/openai/openai-python/releases/tag/v3.16.0) ⭐️ 7.0/10

OpenAI 官方 Python SDK 发布 v3.16.0，版本对比区间为 v3.15.0 至 v3.16.0，发布日期标注为 2026-09-18。本次更新包含两项变更：一是 Features 项下新增“webhook endpoint management”（Webhook 端点管理），对应 PR \#3892，合并提交为 9a11f6e；二是 Chores 项下将 MCP 的 connector\_id 标记为弃用（deprecate MCP connector\_id），对应 PR \#3894，合并提交为 1ccaf07。也就是说，这个版本在 SDK 层面引入了对 Webhook 端点的管理能力，同时开始收缩 MCP 连接器标识字段的使用。发布说明本身只给出了变更条目、PR 号和提交哈希，并未展开新的方法名、参数结构、Webhook 事件类型或鉴权方式等接口细节，也没有说明 connector\_id 弃用的具体替代字段、时间表或移除版本。因此要落地使用，需要进一步查看仓库 README、OpenAI API reference 或对应 OpenAPI 规范 diff。由于没有附带社区评论，目前无法从讨论中判断开发者对这两项变更的实际反馈与迁移难度。

github · openai-sdks\[bot\] · 9月18日 14:52

**「背景说明」** openai-python 是 OpenAI 维护的官方 Python 客户端库，其 API 层通常跟随 OpenAI 的接口规范同步演进，因此版本号中出现的 Features/Chores 条目往往直接映射到服务端 API 的新增能力或字段调整。Webhook 是一种由服务端在事件发生时主动向开发者指定地址推送通知的机制，把“端点管理”纳入 SDK，意味着开发者可以不再只靠控制台或手写 HTTP 请求来创建和维护回调地址。MCP（Model Context Protocol）是用于把模型连接到外部工具与数据源的协议，connector\_id 是其中用于标识某个连接器的字段；本次发布说明仅写明该字段进入弃用状态，未说明替代方案与移除节奏。

**「影响与关注点」** 对使用 OpenAI API 的 Python 开发者来说，最直接的动作是检查代码中是否依赖 MCP 的 connector\_id 字段，并留意后续版本是否出现替代写法或报错；同时可评估是否把 Webhook 端点的创建与维护迁移到 SDK 内完成，以简化服务端事件接收集成。对产品与平台团队而言，这类 SDK 侧的端点管理能力通常意味着 Webhook 会成为更正式的一等集成方式，值得同步梳理回调签名校验、重试与幂等处理等工程细节。下一步应关注官方 API reference 与 SDK 文档中的具体参数说明、connector\_id 的替代字段公告，以及后续版本是否正式移除该字段。

**标签**: `#openai-python`, `#SDK release`, `#API webhooks`, `#MCP deprecation`, `#developer tooling`

---

<a id="item-tech-news-8"></a>
### [Claude Code 在缺少 CLAUDE.md 时改读 AGENTS.md](https://code.claude.com/docs/en/changelog) ⭐️ 7.0/10

根据官方 Claude Code 变更日志条目及 Hacker News 讨论，Claude Code 现在会在项目没有 CLAUDE.md 的情况下回退读取 AGENTS.md；这是面向 AI 编码代理指令文件互操作性的具体产品行为更新，HN 上该条目获得 372 分和 142 条评论。该改动本身很小，但直接触及多代理协作中的常见摩擦：开发者以往常通过把 CLAUDE.md 软链接到 AGENTS.md，或反过来，让 Claude Code 与 Codex 等不同代理共用同一套项目指令。讨论中有人指出，这只是“最低限度”的兼容，不再需要软链接；也有人引用 Shopify 相关报道称，有管理者曾考虑禁用 Claude Code，直到它读取 AGENTS.md 与 .agents/skills 等内容。评论还提出一个尚未澄清的边界问题：这次回退是否只针对项目级 AGENTS.md，还是也覆盖用户级 ~/AGENTS.md 或 ~/.agents/AGENTS.md。现有材料没有给出实现细节、版本号或更细的读取优先级，因此应把该更新理解为兼容性行为调整，而非模型能力跃迁。可核对的官方入口是 https://code.claude.com/docs/en/changelog。

hackernews · datadrivenangel · 9月18日 21:00 · [社区讨论](https://news.ycombinator.com/item?id=49760187)

**「背景」** Claude Code 是 Anthropic 的编码代理产品，项目级 CLAUDE.md 用于存放它对代码库的偏好、命令和约束。评论中提到，Codex 创建的项目会带有 AGENTS.md；AGENTS.md 因而成为跨代理共享项目说明的常见做法。此前若同一仓库同时使用 Claude Code 和其他代理，常见做法是维护两份内容或建立软链接；本次更新试图减少这种重复配置。

**「影响」** 对同时使用 Claude Code、Codex 等工具的开发者，这一改动可减少维护 CLAUDE.md 与 AGENTS.md 两份指令的成本，但用户级配置是否生效仍不明确。接下来值得关注官方是否补充读取优先级、用户级路径支持，以及其他编码代理是否跟进支持 AGENTS.md。若你的仓库仍依赖软链接，建议先在小型项目中验证实际读取行为，再清理兼容层。

**「社区讨论」** 社区反应偏务实：有评论认为这是“绝对的最低限度”，并打算删除软链接；也有人分享 Claude Code 在只有 AGENTS.md 时一度找不到指令、被提示后才去检查该文件。另有评论引用 The New Stack 报道称，Shopify 的 Lütke 曾表示考虑禁用 Claude Code，直到它改变行为并读取 AGENTS.md 和 .agents/skills 等，这使讨论超出单一产品兼容性而涉及代理配置标准的博弈。还有评论追问该回退是否支持 ~/AGENTS.md 或 ~/.agents/AGENTS.md，目前未见官方在材料中明确回答。

**标签**: `#Claude Code`, `#AI coding agents`, `#AGENTS.md`, `#developer tools`, `#Anthropic`

---

<a id="item-tech-news-9"></a>
### [Anthropic 确认运营湿实验室：让自家模型做真实生物实验](https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/) ⭐️ 7.0/10

Anthropic 已确认，它运营着一个湿实验室（wet lab），可以让自家 AI 模型在真实环境中执行物理实验。Anthropic 生命科学负责人 Eric Kauderer-Abrams 对路透社表示：“我们认为，要做生物学，最终的检验仍是、并且在相当长时间内仍将是真实的实验室工作”，并明确说“我们今天确实在这么做”；他补充说，该实验室的运作方式与多数生物技术实验室类似，Anthropic 自己做一些研究，同时也与外部伙伴合作。这条消息并不算突然：Anthropic 在今年 4 月收购了隐身状态的 AI 生物技术公司 Coefficient Bio。Anthropic 拒绝透露湿实验室具体在做什么，只表示其重点不是药物发现——它不希望给人留下与制药行业竞争的印象，因为它在制药业有众多大型客户与合作伙伴，例如它刚刚宣布与诺和诺德（Novo Nordisk）在联合药物发现上展开合作。同一周，Anthropic 还推出了生命科学验证计划（Life Sciences Verification Program），让经过审核的生物领域研究者能使用其最强模型。报道也将这一动作与 Anthropic 内部的安全争论并置：研究员 Jacob Coxon 辞职并警告“构建 AI 的人真心相信它可能在本十年末杀死我们所有人”，而 Anthropic 自己的对齐负责人估计 AI 在未来十年内灭绝人类的概率高于 10%；CEO Dario Amodei 上周末发帖呼吁行业放慢脚步并建立自我监管，且多次把生物恐怖主义列为 AI 最大风险之一。投资人、AI 编程创业公司创始人 Chamath Palihapitiya 在 X 上半开玩笑地写道：那个出品了“我们都要死了”和“现在就监管我”等“热门作品”的团队，正在旧金山建一个湿实验室。由于原文正文被截断，实验室做哪些具体课题、有哪些模型参与、实验规模和产出均未披露。

rss · TechCrunch AI · 9月18日 23:13

**「背景知识」** 湿实验室指配备细胞培养、移液、测序等物理操作条件、能真正动手做生物实验的实验室，与只做计算模拟的干实验室（dry lab）相对；对一个以语言模型见长的公司来说，自建湿实验室意味着把“模型提出假设—真实实验验证—结果回喂模型”的闭环搬进自己手里。Coefficient Bio 是 Anthropic 在今年 4 月收购的一家隐身阶段 AI 生物技术公司，是这条湿实验室线的主要人员与能力来源。Anthropic 设有专门的生命科学团队，并已在商业侧与制药企业合作（如与诺和诺德的联合药物发现），因此它以“不碰药物发现”来划清与客户的边界。这也属于近两年 AI-for-science 的更大趋势：前沿实验室从纯软件模型，逐步向可自证假设的实验能力延伸。

**「影响与关注点」** 对开发者和研究者而言，这条消息的价值在于它把“AI 做科学”的争论从论文与基准推到了真实实验环节：模型能力若要在生物学上被验证，就需要物理实验的反馈回路，这可能影响未来模型评估、数据集和工具链的设计方向。对生物医药从业者和创业者来说，值得关注的是 Anthropic 如何定位自己——强调不做药物发现、同时推出面向研究者的生命科学验证计划，说明它更可能走“平台与访问权限”路线，而非直接竞争。接下来应关注三件事：生命科学验证计划的资格与配额说明、与诺和诺德等合作的公开成果、以及湿实验室是否发布技术报告或论文；同时，公开的安全争论（辞职研究员、对齐负责人给出的风险估计、CEO 的自我监管呼吁）会让这类实验能力持续处于舆论与监管聚光灯下。

**标签**: `#Anthropic`, `#AI-for-science`, `#biology`, `#frontier-labs`, `#industry-news`

---

<a id="item-tech-news-10"></a>
### [安全团队据称用 Claude 在 72 小时内链式攻破 OpenAI 社区论坛并进入内部仓库](https://the-decoder.com/security-researchers-used-anthropics-claude-to-hack-openais-internal-systems-in-under-72-hours/) ⭐️ 7.0/10

安全公司 Hacktron 的三名研究人员据称使用 Anthropic 的 Claude 模型，在不到 72 小时内通过 OpenAI 社区论坛 community.openai.com 链式利用两个漏洞，进入 OpenAI 内部系统与 GitHub 代码仓库。攻击路径分两步：其一是论坛用于处理上传 HEIC 图片的 libheif 库存在漏洞，Hacktron 称修复补丁在原始源码中已存在约一年却未被标记为安全问题，论坛所运行的 Debian 软件包仍缺少该修复，一个构造的图片文件即可让研究者在服务器上执行自己的代码；其二是 OpenAI 中央单点登录（SSO）系统的配置错误，使控制论坛服务器的人可以冒充活跃论坛成员，接管其 ChatGPT 与 Codex 账户，且该缺陷不限于论坛，任何使用 OpenAI 登录的被攻陷服务都会带来同样访问权限。研究者用一名员工的 Codex 账户在内部 monorepo 中提交了一个无害的 pull request 作为访问证明，并表示没有查看任何敏感数据。他们称最初用 Claude Opus 4.8 构建出了可用的漏洞利用，但只能在不开启 ASLR（内存攻击常用防护）的情况下生效，多次会话均无法产出开启 ASLR 后仍可靠的版本；7 月 24 日晚 Anthropic 发布 Claude Opus 5 后，新模型在三小时内为本地 Mac 生成了可用 exploit，随后适配到 Discourse 服务器环境。研究者随后让 Claude 以自主循环方式攻击自己的测试实例——由于模型拒绝对真实系统编写攻击代码，他们把目标包装成基准任务，四小时后 agent 接管了服务器；在相关任务上，他们还观察到其表现相对 OpenAI 的 GPT-5.6 Sol 有明显提升。OpenAI 在收到报告约 14 小时后确认修复，Discourse 也在数日内作出回应。

rss · The Decoder · 9月18日 17:20

**「背景：漏洞链、ASLR 与 SSO」** Hacktron 是一个以漏洞利用自动化为方向的安全研究团队，此次项目被其命名为 “HEIF Heist”，核心是把 AI 模型当作漏洞发现与利用生成的执行者，而非仅做代码审计。技术上，libheif 是处理 HEIC/HEIF 图片格式的开源库，图片解析器长期是内存破坏类漏洞的高发入口，因为服务端会自动解析用户上传的文件；ASLR 则是操作系统随机化内存布局的常见防护，能否在开启 ASLR 时稳定利用是区分“理论 PoC”与“实战 exploit”的关键门槛。SSO（单点登录）机制让用户用同一个 OpenAI 账号登录论坛等第三方服务，一旦论坛服务器被控制，签名令牌与身份信任链就可能被用来冒充真实用户，从而横向进入 ChatGPT、Codex 等关联账户。论坛本身由 Discourse 这一开源社区论坛软件驱动，这也解释了为何漏洞会同时影响论坛方与 Discourse 项目。

**「影响与下一步关注」** 这起事件的关键信号不在单个漏洞，而在成本结构的变化：Hacktron 称整个项目由三人用两个月完成、AI 花费不足 3000 美元，把攻击适配到每个新目标只需一到两天，且在覆盖 Slack、Meta、GitHub Enterprise 等目标的测试中，只有 Shopify 察觉了异常活动，尽管出现了数千次图片上传和反复的图片处理崩溃。对开发者和产品团队而言，直接可行动项是核查自建服务中图像处理等解析类依赖的补丁状态，并审视 SSO 信任边界——尤其是“第三方服务被攻陷即可冒充用户”这类设计假设。接下来值得关注的是完整技术报告的披露细节、Anthropic 与 OpenAI 的官方回应，以及此类 AI 驱动漏洞研究是否会推动模型方强化滥用防护与基准测试中的攻击性任务边界。

**标签**: `#AI security`, `#Anthropic Claude`, `#OpenAI`, `#vulnerability chaining`, `#AI cyberattacks`

---


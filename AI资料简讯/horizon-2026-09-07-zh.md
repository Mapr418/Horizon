# Horizon 每日速递 - 2026-09-07

> 从 7 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [LG 智能电视被曝熄屏录音并探测局域网设备](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 内部视角：编码智能体与递归自我改进](#item-tech-news-2) ⭐️ 8.0/10
3. [欧盟可修复性法规遭智能手机厂商普遍无视](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [LG 智能电视被曝熄屏录音并探测局域网设备](https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html) ⭐️ 8.0/10

据报道，LG 智能电视存在严重的隐私问题：即使在屏幕关闭状态下也会记录音频，并主动探测本地网络中的其他设备。这些行为引发了用户对智能电视厂商默认收集数据的广泛质疑，不少用户表示后悔让电视联网。评论中提到，一位网友五年前就因 LG 条款要求授予任意数据权限而选择不同意，并一直禁用所有网络功能；如今更多人考虑通过 OpenLGTV 等逆向工程项目定制固件，以夺回对设备的控制权。目前尚不清楚 LG 是否会修复这些问题或做出解释，但相关演示视频已在社区中广泛传播。

hackernews · chris\_overseas · 9月7日 07:03 · [社区讨论](https://news.ycombinator.com/item?id=49594878)

**「背景」** 据 Gamers Nexus 发布的一段约 135 分钟的调查视频，LG 智能电视在屏幕关闭、看似已关机的情况下，仍会持续扫描家庭网络、绘制附近设备信息，并记录麦克风音频。这一行为与电视的语音识别和本地网络发现功能有关，但即使用户未主动启用相关操作，测试中仍观察到活动。相关报告在 Reddit 等技术社区引发大量讨论，许多用户表示已断开电视的网络连接或考虑改用其他品牌。

**「影响」** 已购买 LG 智能电视并连接网络的用户，其家庭语音与设备信息可能在不知情时被采集；担心隐私的用户可将电视断网或改用外接机顶盒以降低风险。

**「社区讨论」** 评论一致强烈批评 LG 的做法，多位网友表示后悔购买或已长期禁用网络功能；有网友推荐通过 OpenLGTV 等逆向工程项目自定义固件，也有评论调侃报道此事的网站自身也关联大量隐私追踪合作方。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with screen off and snooping on local devices - Notebookcheck News</a></li>

</ul>
</details>

**标签**: `#privacy`, `#smart-tv`, `#security`, `#IoT`, `#LG`

---

<a id="item-tech-news-2"></a>
### [OpenAI 内部视角：编码智能体与递归自我改进](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 在 2026 年发布文章《Research acceleration: The view inside OpenAI》，介绍公司内部研究团队如何大规模使用编码智能体，并展示研究人员日均 AI 支出从 2 月的接近 0 美元升至 8 月底约 600 美元，其中 7 月底后增长明显加快。Simon Willison 推测这一加速可能源于员工获得了后来以 GPT-6 Astra 名称发布的模型访问权限。同时，OpenAI 还发布由首席科学家 Jakub Pachocki 撰写的《An Alien Mind》，两篇文章都围绕递归自我改进（RSI）展开，Willison 认为这可能是 OpenAI 对 AGI 的新定义。这些内容显示 OpenAI 正把智能体工程视为加速自身研究的重要工具。

rss · Simon Willison · 9月6日 23:57

**「背景」** OpenAI 于 2026 年 9 月将“递归式自我改进”（Recursive Self-Improvement，RSI）标记为其新的 AGI 方向之一，并发布了内部研究报告及首席科学家 Jakub Pachocki 撰写的《An Alien Mind》。Pachocki 在文中指出，目前还没有 AI 实验室能足够好地解决对齐与监控问题，从而在最大速度下负责任地扩展前沿模型；他预计进展可能持续进入 RSI 阶段，并呼吁建立共享安全基线、加强国际协调。RSI 通常指系统通过改进自身能力形成加速发展循环，这为理解 OpenAI 研究团队使用编码代理来加速研究提供了背景。

**「影响」** 这一披露意味着 OpenAI 内部已把编码智能体作为 AI 研究加速的核心基础设施：截至 2026 年 8 月中旬，研究人员的智能体推理日均成本中位数已超过 600 美元，前 10%高用量者日均超过 7000 美元，显示机构正将大量资源转向以“递归自我改进”为核心的 AGI 路线，也表明智能体工程已成为其研究团队日常工作中不可逆的支出与效率杠杆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/an-alien-mind/">An Alien Mind | OpenAI</a></li>
<li><a href="https://aitoolsreview.co.uk/insights/openai-alien-mind-recursive-self-improvement">OpenAI&#x27;s &quot;An Alien Mind&quot;: Pachocki&#x27;s RSI Warning (September 2026)</a></li>
<li><a href="https://www.unite.ai/in-an-alien-mind-openais-jakub-pachocki-urges-shared-safety-bars/">In &quot;An Alien Mind,&quot; OpenAI&#x27;s Jakub Pachocki Urges Shared Safety Bars</a></li>
<li><a href="https://www.firstpost.com/tech/openai-says-it-has-reached-goal-of-building-an-automated-ai-research-intern-14043658.html">OpenAI Says It Has Reached Goal of Building an Automated AI Research Intern</a></li>
<li><a href="https://www.datastudios.org/post/openai-automated-research-intern-coding-agents-research-acceleration-ai-researcher">OpenAI Says It Has Reached an Automated Research Intern: Coding Agents, 3.1 Agent-Workdays per Human Day, Research Acceleration, and the Road to an AI Researcher</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI research`, `#agentic engineering`, `#recursive self-improvement`, `#coding agents`

---

<a id="item-tech-news-3"></a>
### [欧盟可修复性法规遭智能手机厂商普遍无视](https://www.theregister.com/personal-tech/2026/09/07/smartphone-makers-dont-bother-to-comply-with-eu-repairability-requirements/5294532) ⭐️ 7.0/10

据《The Register》2026 年 9 月 7 日报道，智能手机厂商普遍无视欧盟关于可修复性的法规要求，引发对监管执行机制的热议。报道显示，许多厂商并未在设计和售后层面满足欧盟“维修权”规定，执法不确定但可能面临处罚。社区评论强调，法规只有配合快速、透明和有效的制裁才能发挥作用，而欧盟在处理类似法规时历史上进展缓慢。此事关系到欧盟消费者能否真正获得更耐用的设备与更容易更换的电池。

hackernews · mdp2021 · 9月7日 11:46 · [社区讨论](https://news.ycombinator.com/item?id=49597189)

**「背景」** 欧盟针对智能手机和平板电脑的维修性法规于一年前生效，要求制造商提供维修信息、备件以及更长的软件支持，并逐步推动电池可更换设计。然而，据 Right to Repair Europe 报告，超过 80%的设备仍未提供必要的维修信息，显示出合规率严重不足。这一背景有助于理解为何围绕执法力度和监管有效性的讨论仍在持续。

**「社区讨论」** 评论中主要分歧在于执行力度：有观点认为监管需要强有力的制裁作为后盾，也有人因法规实施时间尚短而愿意给予宽容，并推测欧盟可能因资源或等待澄清而暂缓行动。另有评论强调，对大多数使用者而言，可轻易更换电池才是最实际的需求，但像 Fairphone 这样的厂商仍属少数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/personal-tech/2026/09/07/smartphone-makers-dont-bother-to-comply-with-eu-repairability-requirements/5294532">Smartphone makers don&#x27;t bother to comply with EU repairability ...</a></li>

</ul>
</details>

**标签**: `#repairability`, `#EU regulation`, `#smartphones`, `#right-to-repair`, `#hardware`

---


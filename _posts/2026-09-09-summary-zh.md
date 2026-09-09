---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 46 条内容中筛选出 10 条重要资讯。

---

**AI 前沿简讯**
1. [Google DeepMind 发布 AlphaGenome Atlas：人类基因组约 90 亿单碱基变异效应预测图谱](#item-tech-news-1) ⭐️ 9.0/10
2. [Meta 公开个人 AI 智能体 Muse：分层防注入成安全主线，隐私顾虑未消](#item-tech-news-2) ⭐️ 8.0/10
3. [Google DeepMind 发布 AlphaGenome Atlas：覆盖人类 DNA 单碱基变化的预测图谱](#item-tech-news-3) ⭐️ 8.0/10
4. [Meta 发布个人 AI 代理 Muse：能替你订行程、付款，但这次需要用户交出更多信任](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI 研究员被指施压数学家剔除 Anthropic 合著者；OpenAI 回应并发布 AI 证明](#item-tech-news-5) ⭐️ 8.0/10
6. [GitHub 日榜第一：一个让编程 Agent 不再长篇大论的 ADHD 友好 skill](#item-tech-news-6) ⭐️ 7.0/10
7. [GitHub 日榜 \#2：diagram-design——让 Claude Code、Codex 输出“设计不讨厌”的编辑级 HTML/SVG 图表](#item-tech-news-7) ⭐️ 7.0/10
8. [openai-python v3.9.0 发布：新增提示词缓存诊断并修复 API 事件字段](#item-tech-news-8) ⭐️ 7.0/10
9. [黑客窃取 Claude 订阅用户的 Token：安全事件与账户滥用详情](#item-tech-news-9) ⭐️ 7.0/10
10. [GitHub 日榜 \#3：OpenAI 弃用 Codex Skills 目录仓库，流量引向 Plugins 仓库](#item-tech-news-10) ⭐️ 5.0/10

---

## AI 前沿简讯

<a id="item-tech-news-1"></a>
### [Google DeepMind 发布 AlphaGenome Atlas：人类基因组约 90 亿单碱基变异效应预测图谱](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) ⭐️ 9.0/10

Google DeepMind 正式发布 AlphaGenome Atlas：一个覆盖人类基因组中约 90 亿种可能单核苷酸变异的预测平台，官方称其为迄今最全面的遗传变异分子效应目录。该平台面向学术研究免费开放，可通过网站门户、AlphaGenome API 以及 Google Antigravity 中的技能访问，底层为超过 1PB 的预计算数据集，规模约为 AlphaFold Database 的 30 倍。为方便研究者快速定位关键变异，DeepMind 同步发布 AlphaGenome Variant Impact（AVI）评分，将 AlphaGenome 与 AlphaMissense 两类模型的预测合并为单一数字，并同时适用于占基因组 2%的编码区和占 98%的非编码区。据官方介绍，AVI 在多种变异致病性与罕见病基准上达到目前最佳水平；每个评分还附带特征归因，可指出 RNA 剪接、基因表达等哪些分子过程最可能被破坏，并配置了超过 2500 个 DNA 序列 motif 及其位置信息。在应用案例中，外部合作者使用 AVI 在罕见病研究中定位到影响 DNM1 基因、与癫痫性脑病相关的剪接变异，英国埃克塞特大学 Gareth Hawkes 还在英国生物库 5.4 万余名参与者的全基因组数据中多识别出 22%的非编码遗传关联，包括与衰老和氧感应相关的 PLA2G7、EGLN1 调控变异。官方表示，AlphaGenome Atlas 的设计经过社区协作，目标是让无编程经验的研究者也能进行大规模变异排序、注释和机制解读。

rss · Google DeepMind Blog · 9月8日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49610641)

**「背景」** AlphaGenome 是 DeepMind 此前推出的 AI 模型，用于预测遗传变异如何影响基因调控等生物学过程；AlphaMissense 则专注于蛋白质编码区错义突变的影响判断。人类基因组中约有 90 亿个可能的单碱基变异，实验室难以逐一验证，因此需要大规模预计算来辅助解读。2022 年 DeepMind 扩展 AlphaFold Database 时，把约 19 万实验解析的蛋白质结构扩充到 2 亿多个结构预测，证明“数据库加无需编程的门户”可大幅降低科研使用门槛；AlphaGenome Atlas 正是把同一模式扩展到全基因组变异效应预测。

**「影响」** 对学习者和开发者来说，AlphaGenome Atlas 把模型输出变成可检索、可按 AVI 评分排序、可解释功能归因的资源，显著降低进入基因组学分析的门槛，也为非编码变异研究提供了新的大型基础数据。对研究社区而言，如果该数据集与 API 经过第三方复现检验，它有可能像 AlphaFold Database 一样成为生命科学基础设施。下一步值得关注的是官方是否公布完整技术报告和基准细节、API 配额与使用限制，以及如何说明训练和评估所依赖的保守性标签——这些直接决定预测能否真正带来超出已有先验的新生物学发现。

**「社区讨论」** Hacker News 评论中，有用户指出基因组规模模型的基准标签可能出自保守性，因此难以区分模型是在学习真实机制还是在“重读先验”；另一位用户认为全基因组变异效应预测令人兴奋，但生物学尚未成熟，AlphaFold 本身仍不完美，也无法可靠指导类似 GFP 融合是否有效这样的具体实验。还有评论分享了在病毒上做完整组合突变实验的对照链接，也有人讨论封面图像的艺术家来源；整体态度是谨慎看好，核心质疑集中在标签依赖和预测的可验证性。

**标签**: `#DeepMind`, `#AlphaGenome Atlas`, `#genomics`, `#AI for science`, `#variant prediction`

---

<a id="item-tech-news-2"></a>
### [Meta 公开个人 AI 智能体 Muse：分层防注入成安全主线，隐私顾虑未消](https://ai.meta.com/muse/) ⭐️ 8.0/10

Meta 在 https://ai.meta.com/muse/ 公开了名为 Muse 的个人 AI 智能体，定位是面向用户个人信息与日常任务的 agent 产品；由于本次可获取的官方正文内容有限，最具体的信息来自 Hacker News 社区对安全与隐私的讨论。评论者 simonw 转引 Meta AI 团队 David Singleton 的说明，称团队重点防御提示注入，并采用分层机制：模型被训练识别并抵抗注入，harness 会标记来源不可信的内容，确定性代码检查输出结果，智能体不可达的位置还运行一组分类器。另一部分评论表达强烈不信任，认为交出个人生活数据等同于为 Meta 的数据收集提供便利，宁可自建同类智能体；也有评论者把 Muse 视为更完善、有技术支持的 OpenClaw 类 agent，肯定大厂把这类工具做成可支持产品的价值。目前尚未看到模型能力、API、开放地区或定价等具体材料，因此后续应关注 Meta 是否发布官方技术说明、系统卡和实际访问入口。总体看，Muse 不只是一款新聊天助手，而是个人数据密集型 agent 走向主流化的代表性信号，安全隔离和数据权限将成为用户与社区选择产品的关键。

hackernews · yks · 9月8日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49615537)

**「背景」** Muse 所属的“个人 AI agent”形态，指用户授权模型访问日历、消息、邮件等私人数据并代为完成任务；与一次性问答相比，它的风险面更大。“提示注入”是这类产品面对的首要威胁：网页、邮件或文档等不可信来源中夹带的指令，可能诱导模型读取本不该读的数据，或执行越权操作。Meta 的公开回应展示的是系统级防线，而不是单靠模型拒绝：训练阶段加强模型抵抗力，运行时由 harness 标记不可信内容、确定性代码检查结果，并在智能体无法触达的位置部署分类器。个人 agent 的可用性，取决于这条链路能否覆盖从不可信数据进入、模型推理到调用工具或 API 的整个过程。

**「影响」** 对产品构建者而言，Muse 的出现意味着头部厂商开始主动承担个人数据 agent 的安全叙事，分层防注入会逐步成为这类产品的基础架构而非附加功能。对普通用户和 AI 学习者来说，隐私信任可能成为比模型参数更关键的准入门槛；Meta 能否公布足够透明的数据使用、保存与删除机制，将直接影响这类产品能否走出早期采用者圈层。下一步值得关注的是官方是否发布安全技术报告或系统卡，以及第三方对 Muse 与 OpenClaw 等自托管 agent 的权限控制和实际效果对比。

**「社区讨论」** Hacker News 上的态度大致分两派：一派认可 Meta 与大厂能把 agent 做成可支持产品，并引用 David Singleton 的分层防注入设计作为正面证据；另一派则拒绝把个人数据交给 Meta，担心数据被长期推断、销售或滥用。还有评论者半开玩笑地声称 Meta 抄袭了自己正在做的同类项目，反映出个人 agent 方向已有不少独立开发者同时布局，而真正的竞争壁垒很可能落在隐私信任与系统安全能力上。

**标签**: `#AI agent`, `#Meta`, `#product launch`, `#prompt injection`, `#privacy`

---

<a id="item-tech-news-3"></a>
### [Google DeepMind 发布 AlphaGenome Atlas：覆盖人类 DNA 单碱基变化的预测图谱](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10

Google DeepMind 正式发布了 AlphaGenome Atlas。官方博客标题称它是一张“预测人类基因组中每一种可能的 DNA 碱基变化”的高分辨率图谱，并给出了独立访问入口 deepmind.google/science/alphagenome/atlas。从 Hacker News 讨论看，至少有一位用户在 affiliation 栏填 None 后成功进入工具，说明当前访问入口并不强制要求机构身份。社区评论还提到图谱数据处理涉及非编码 DNA，但能否真正解释启动子序列仍是疑问。本次提供的源文本只有官方链接和讨论，没有文章正文，因此训练规模、致病性评分、数据批量下载方式，以及它与既有 AlphaGenome API 的关系，都需要继续查阅官方博客和 Atlas 页面才能判断。

hackernews · utiiiD · 9月8日 14:55 · [社区讨论](https://news.ycombinator.com/item?id=49611251)

**「项目背景」** AlphaGenome 属于 Google DeepMind 在生物序列预测方向上的工具，其前序工作包括 AlphaFold（蛋白质结构预测）和 AlphaMissense（错义变异致病性预测）。AlphaGenome Atlas 的设计目标是把 DNA 层面的单碱基变化预测组织成一张可查询的图谱，让研究者不必自己运行模型，就能检索特定基因组位置的预测结果。与传统只报告是否致病的变异分类相比，这类工具试图覆盖更广的非编码区域，但真正能解释的调控机制仍需要专门验证。

**「对读者与开发者的意义」** 对遗传学、精准医学和 AI-for-science 学习者来说，这次发布是观察“模型研究成果如何转成可查询的科学数据库”的典型例子。下一步值得关注的是官方是否公开完整的模型卡、评分列定义、原始数据下载和 API 配额，以及 Atlas 对启动子等非编码调控区域的解释是否能通过第三方验证。

**「社区讨论」** Hacker News 用户的核心分歧在于“是不是真正的新信息”：有人质疑它是否只是把已经可以通过 API 访问的 AlphaGenome 结果预计算好并做成更广泛的入口，并不是新的科学发现。也有用户询问能否用 23andMe 数据配合 Atlas 寻找致病突变，另有人提醒不要因“affiliation”输入框退缩，并附上了面向科学家用户的演示视频链接。

**标签**: `#Google DeepMind`, `#AlphaGenome`, `#genomics`, `#DNA variant prediction`, `#AI for science`

---

<a id="item-tech-news-4"></a>
### [Meta 发布个人 AI 代理 Muse：能替你订行程、付款，但这次需要用户交出更多信任](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/) ⭐️ 8.0/10

Meta 于本周正式面向美国用户推出个人 AI 代理 Muse，定位是“ChatGPT 时代之后”能实际代办事务的 agent，而不仅仅是聊天问答。Muse 需要连接用户日常使用的邮箱、日历、支付、健康健身、智能家居、餐饮、购物、音乐和活动等应用与服务，可代发邮件、订旅行、降低账单、填写表单、把食谱 Reels 转成购物清单、发派对邀请，并通过 Link by Stripe 完成结账；Shopify 的 Shop Pay 和 1Password 集成也即将加入。产品由 Meta 自家模型 Muse Spark 驱动，首批通过网页 muse.ai、iOS/Android 应用以及 WhatsApp 聊天提供，随后将进入 Meta AI 眼镜；基础功能免费，但开通需绑定支付卡，付费套餐 Power 为每月 20 美元、Maximum 为每月 100 美元，应用内还会显示使用量余量提醒。Meta 宣称 Muse 运行在独立的 Muse Secure VM 中，配有系统级隔离的 Sentinel 安全代理，用户离开应用后代理仍可继续工作，也会学习对话内容以主动提出建议。Meta 同时表示 Muse 看不到用户密码和支付方式，也不会把对话和数据用于广告系统，并发布了技术说明供安全专家审查。文章特别指出，这次发布距 Meta 因社交媒体消费者伤害达成 180 亿美元多州和解不到两周，因此核心悬念不是功能，而是用户是否愿意再次向一家隐私记录不佳的公司开放邮箱、支付与生活数据。

rss · TechCrunch AI · 9月8日 19:00

**「背景」** 当前行业正从单纯的聊天机器人转向“代理时代”：大型公司和创业公司都在尝试让 AI 跨应用执行真实任务，入口可以是 AI 浏览器、聊天应用，也可以像 Muse 这样自成产品的代理。Muse 的产品机制是让用户逐个选择并连接第三方应用，使授权过程更透明；如果目标服务没有现成连接器但有公开 API，Muse 可使用用户提供的凭证建立连接，没有 API 时则通过浏览器接管操作。Meta 过去在隐私方面有过多次处罚和争议，包括 FTC 和解、Cambridge Analytica 数据丑闻、可读密码存储问题，以及持续多年的未成年人伤害诉讼，这些历史包袱直接影响了 Muse 这类高权限代理能否被消费者接受。

**「影响」** 对 AI 学习者和产品开发者而言，Muse 提供了一个近期可拆解的范例：消费者 AI 代理如何设计逐步授权、如何选择 API/浏览器两种接管方式、又如何用独立的“安全虚拟机”隔离敏感操作，值得对照 Meta 当天发布的技术说明继续研究。对消费级 Agent 赛道来说，Meta 用免费策略以及 WhatsApp、AI 眼镜等高频入口抢占场景，会直接加剧与 Claude Cowork、Gemini Spark 以及苹果 iMessage/SMS/WhatsApp 集成路线的竞争。后续应关注安全专家对 Muse Secure VM 与 Sentinel 的独立审查结论、真实订阅转化率，以及美国监管部门和公众是否因 Meta 的历史隐私问题而放慢采用。

**标签**: `#Meta`, `#AI agent`, `#consumer AI`, `#privacy`, `#product launch`

---

<a id="item-tech-news-5"></a>
### [OpenAI 研究员被指施压数学家剔除 Anthropic 合著者；OpenAI 回应并发布 AI 证明](https://the-decoder.com/openai-researcher-allegedly-pressured-mathematician-to-drop-anthropic-co-author-from-math-breakthrough-paper/) ⭐️ 8.0/10

数学家 Tristan Buckmaster 公开指控，OpenAI 研究员 Sébastien Bubeck 曾施压他，要求从一篇基于 AI 辅助取得的 Navier-Stokes 数学突破论文中剔除其合著者、现任 Anthropic 数学家的 Levent Alpöge；Buckmaster 拒绝后，Bubeck 据称问他“为什么要毁掉自己的职业生涯”。据 Buckmaster 称，他和 Alpöge 整个项目期间都把草稿放进了 OpenAI Codex 会话，而 OpenAI 声称内部模型已用相同思路产出了约 100 页带外力 Navier-Stokes 证明，但未就训练数据问题给出直接回答。OpenAI 否认这些指控，Bubeck 表示研究者和代理在其成果公开发布前没有看到过两人的工作，也没有访问特定用户数据，但承认不能排除“去标识化数据”曾用于改进模型。OpenAI 随后官方发布了自己的 Navier-Stokes 结果，称证明由约 10,000 个协同 AI 代理在 88 小时内完成，使用一个被描述为“明显强于 GPT-6 Astra”的内部模型，并已用 Lean 做了形式化验证；研究负责人 Mark Chen 表示仅计算成本就达数百万美元。OpenAI 开发者 Noam Brown 将这次计算开销与 o3、ARC-AGI 和 2025 年数学奥赛的成本对比，预言一年后任何人都能用约 20 美元的 ChatGPT 订阅获得同等级别的解题能力。OpenAI 官方博客还表示，它在 9 月 1 日听到传闻后开始这项工作，9 月 6 日完成 Lean 验证，之后才提议与两人联合发布并承认其优先权，且它后来发现对方解决的是受迫 Euler 问题而非 Navier-Stokes。Buckmaster 则在 Mastodon 上回应说，OpenAI 等于承认使用了他们得出结果之后的训练数据，并反问用客户数据去“抢跑”客户是否合乎伦理。

rss · The Decoder · 9月8日 19:23

**「背景知识」** Navier-Stokes 方程是描述流体运动的偏微分方程，也是 Clay 数学研究所七个“千禧年大奖问题”之一，每个问题悬赏一百万美元；严格证明其光滑解是否存在或是否会产生奇点，是数学界长期未解的核心难题。Buckmaster 和 Alpöge 使用包括 Anthropic Claude 和 OpenAI Codex（运行 GPT-5.6 Sol）在内的多种 AI 模型进行研究，在 8 月中旬取得若干突破，并认为自己在一个特定的 Navier-Stokes 变体上找到结果；其中受迫 Euler 方程与带外力 Navier-Stokes 的区别在于精确证明的对象不同，OpenAI 强调双方的结果在数学上并不相同。

**「影响与关注点」** 这一事件表明，前沿数学发现正从“纯人类智力竞赛”转变为包含 AI 代理、客户数据、计算资源与机构利益冲突的复杂生态，研究者需要更警惕把未发表草稿放入商业 AI 产品可能带来的数据使用和抢先发表风险。对学习者和开发者而言，值得关注的是 OpenAI 是否发布该证明的完整技术报告、Lean 形式化代码和模型/数据使用细节，以及 Buckmaster 与 Alpöge 是否正式发布并验证自己的 Euler 或 Navier-Stokes 结果；这些将直接检验“10,000 个代理在 88 小时内证明千禧年问题”这一说法的可信度。

**标签**: `#OpenAI`, `#Anthropic`, `#Navier-Stokes`, `#AI research ethics`, `#Authorship dispute`

---

<a id="item-tech-news-6"></a>
### [GitHub 日榜第一：一个让编程 Agent 不再长篇大论的 ADHD 友好 skill](https://github.com/ayghri/i-have-adhd) ⭐️ 7.0/10

GitHub 今日趋势第一是 ayghri/i-have-adhd 仓库，作者 ayghri，当前 30,373 stars、今日新增 656 stars，仓库主语言标注为 Python。它不是模型，而是一套给编程 Agent（主要是 Claude Code）使用的“skill/plugin”：README 的核心主张是“动作优先、步骤编号、不要 ‘Hope this helps\!’”，并用 Before/After 对比展示同样的修改请求，从一段铺垫式回复变为“运行 npm install jsonwebtoken@latest，然后编辑 src/auth.ts:42”并列出 1-2-3 步。项目给出 10 条规则，例如以下一步行动开头、多步骤任务编号、每次回复重申状态、给出具体分钟估计、列表不超过 5 项、不写开场白和结束语；完整规则在 skills/i-have-adhd/SKILL.md。安装方式是复制粘贴一句话到 CLI 提示词，或通过 claude plugin marketplace 安装；用户可 fork 编辑 SKILL.md 后替换上游版本。项目基于《The Adult ADHD Tool Kit》改编，采用 MIT 协议，README 已提供中/日/葡/越/韩/泰等多语言。它能在开源社区快速走红，反映开发者普遍对 Claude 类编程 Agent 冗长、铺垫式回答的真实痛点。

github · ayghri · 9月9日 00:17 · [社区讨论](https://news.ycombinator.com/item?id=49610631)

**「背景知识」** Claude Code 等编程 Agent 通过称为 skill/plugin 的附加指令文件（如 SKILL.md、CLAUDE.md/AGENTS.md）调整模型回答风格，本质是系统提示词的一部分。该项目正是把“ADHD 友好输出”整理成这种可安装的 skill，并非改变模型本身；因此效果取决于模型在长会话中是否持续遵循这套规则。理解这一点，就能明白为什么安装说明要求把仓库的 AGENTS.md 引入代理配置，也解释了 Before/After 示例是把同样任务改写成更短、更可执行的步骤。

**「对开发者的影响」** 对开发者：如果你正在被 Claude 的冗长输出困扰，可先用这个 skill 测试是否显著减少噪音；它是零成本的可逆配置，也可以 fork 改造成自定义风格。这个项目的热度本身是一个生态信号：模型能力之外，输出纪律与工具链可配置性已经成为社区关注的竞争维度，值得继续观察 Anthropic 后续模型是否会原生改善长文风，或继续依赖 CLAUDE.md/skill 这类外部约束。

**「社区讨论」** Hacker News 评论里，开发者普遍认同 Claude 尤其容易啰嗦，并戏称这类问题是“Claudism”，例如坚持先讲做了什么、再特意声明没做什么（“我编辑了 this.py and that.py，但没有编辑 README，也没有提交”）。有用户实测感到该 skill 只能维持几轮简洁，随后模型会回到原来的冗长模式；也有用户对“把安装指令直接粘贴进 CLI”这种分发方式表示警惕，担心可能变成新的提示注入或供应链风险。

**标签**: `#open-source`, `#coding-agents`, `#claude`, `#developer-tools`, `#productivity`

---

<a id="item-tech-news-7"></a>
### [GitHub 日榜 \#2：diagram-design——让 Claude Code、Codex 输出“设计不讨厌”的编辑级 HTML/SVG 图表](https://github.com/cathrynlavery/diagram-design) ⭐️ 7.0/10

由 Cathryn Lavery 维护的 cathrynlavery/diagram-design 登上 GitHub 日趋势第 2 名：仓库现有 34,765 星、今日 +710 星，主体语言为 HTML，面向 Claude Code、Codex、Factory Droid、Pi 以及 Agent Skills 兼容宿主提供图表生成技能。README 正文把类型数写成 39 种，而仓库简介写的是 38 种；无论哪个口径，它都以“自包含 HTML + SVG”的方式输出图，明确反对 Mermaid 生成出的通用圆角框风格，并提出“No shadows. No Mermaid slop.”的美学标准。v2.0 新增以 shared-memory hub 为核心的 Loop/flywheel 类型，v2.3 加入语义化系统模式和可选无障碍动效，v2.5.10 又扩充了 Sankey、fishbone、Wardley map、kanban、user journey、deployment、dependency graph、UML class、story map、database schema 十种布局语法。每类模板都有 minimal light、minimal dark、full-editorial 三种静态变体，无构建步骤、无 JavaScript、无外部图片依赖，并可按指定格式、尺寸和细致程度重绘 draw.io 或 Mermaid 源文件。作者表示这套 skill 能读取网站后在约 60 秒内匹配品牌配色，设计上刻意保留低密度（目标 4/10）、限制强调色数量，以保证图表的编辑级质感。仓库地址：https://github.com/cathrynlavery/diagram-design 。

github · cathrynlavery · 9月9日 00:17

**「背景」** diagram-design 属于 AI 编码代理的“技能（Skill）”：Claude Code、Codex、Pi 这类 agent 在终端或代码环境里执行编程任务，若直接让它们画图，常见结果是用 Mermaid 等工具输出通用方框/箭头；作者希望用一整套排版约束替代这种默认行为。README 的核心机制是“语义模式与布局解耦”：队列、策略轨迹或信任边界等行为可映射到最接近的既有图表类型，不必为每个场景新增图型；所有模板以可被浏览器直接打开的 HTML/SVG 静态文件交付，避免 Figma 手工调整。

**「影响」** 对开发者和 AI 产品设计者，这个仓库示范了如何通过受控模板而非自由文本生成，让 AI 代理的输出稳定达到设计稿质量；对学习 Agent Skill 生态的人，它是“把领域知识打包给 agent”的可运行案例。下一步可观察它是否能被 Claude Code/Codex 以外的宿主广泛采用，以及社区是否会贡献更多图表语法或字体/本地化适配。

**标签**: `#diagram-design`, `#claude-code`, `#codex`, `#open-source`, `#ai-agents`

---

<a id="item-tech-news-8"></a>
### [openai-python v3.9.0 发布：新增提示词缓存诊断并修复 API 事件字段](https://github.com/openai/openai-python/releases/tag/v3.9.0) ⭐️ 7.0/10

OpenAI Python SDK v3.9.0 于 2026 年 9 月 5 日正式发布，本次版本是在 v3.8.0 基础上的增量更新。新版本主要为 API 增加了提示词缓存诊断能力（prompt cache diagnostics），让调用方能够直接获取与缓存命中相关的信息。同时，它修正了函数调用补全事件中的字段定义（对应 openapi-545），使流式函数参数事件字段更准确。在缺陷修复方面，本次更新会接受不完整的 Web 搜索调用状态，避免因状态缺失而报错，并拒绝溢出的服务器重试延迟，防止极端重试等待时间影响客户端稳定性。其他改动包括在文档中补充限流与模型过载响应的说明（SDK-235），以及将构建流程迁移到 forked steady。整体而言，这是一次面向 API 调用稳定性和可观测性的兼容性更新，建议使用 OpenAI API 的 Python 开发者关注官方更新日志并升级 SDK。

github · openai-sdks\[bot\] · 9月8日 16:42

**「背景」** OpenAI Python SDK 是 OpenAI 官方提供的 Python 客户端库，用于调用 GPT 系列模型的补全、嵌入、函数调用和 Web 搜索等 REST API。提示词缓存是服务端优化机制，可复用相同请求前缀的计算结果以降低延迟和成本，而本次新增的诊断选项意味着开发者能更清楚地观察到缓存是否生效。函数调用补全事件则以事件流方式返回函数参数，字段命名不一致会导致客户端解析异常，因此本次修正字段定义对依赖流式函数调用的开发者很关键。

**「影响」** 对 AI 开发者和使用 OpenAI API 的产品团队来说，这次更新主要提升了 API 的可靠性与可观测性：提示词缓存诊断可以帮助优化 prompt 结构以充分利用缓存，而 Web 搜索状态和重试延迟的修复则减少生产环境中的异常边界情况。建议关注提示词缓存诊断的具体字段文档和示例，在升级后实测相关指标，并留意是否有后续版本补充更详细的缓存计费说明。

**标签**: `#OpenAI`, `#Python SDK`, `#API update`, `#release`

---

<a id="item-tech-news-9"></a>
### [黑客窃取 Claude 订阅用户的 Token：安全事件与账户滥用详情](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/) ⭐️ 7.0/10

据 TechCrunch 报道，英国东萨塞克斯的独立 AI 顾问 Grant De Swardt 在 8 月 4 日发现自己的 Claude Max 20x 账户在未工作时 Token 用量持续上升；在禁用所有关联工具、暂停 Cowork 任务、关闭 Dispatch/云执行的受控间隔内，用量仍从 45% 增至 55%。Anthropic 调查后告诉他，一个被入侵的 Claude 会话密钥被用来铸造未授权的 Claude Code OAuth 令牌，账户可能被第三方服务用于处理他人活动，或是凭证/会话数据在用户不知情的情况下被窃取，或账户曾连接外部服务。Anthropic 最终暂停了账户、使所有会话和服务端 Claude Code 令牌失效，并为其 200 美元/月订阅的剩余时间退还了 44.49 英镑。De Swardt 表示账户约两周后恢复，但因缺乏逐项用量明细和寻求帮助困难，他已取消订阅转而使用 Cursor，并认为其他模型“没有太大不同或更好”。Anthropic 在给其他受影响用户的邮件中确认，有恶意行为者使用常见信息窃取恶意软件（infostealer）从用户电脑窃取 Claude 登录会话，再利用这些会话消耗账户额度；恶意软件并非来自 Claude 本身。Anthropic 拒绝就用户如何识别滥用行为发表评论。

rss · TechCrunch AI · 9月8日 21:10

**「背景知识」** Claude Max 是 Anthropic 面向重度用户的高阶订阅方案，其中“20x”意味着在特定时间窗口内提供约 20 倍的对话使用量，以 Token 额度形式计费。Claude Code 是 Anthropic 的命令行编程工具，支持通过 OAuth 令牌进行服务端认证和远程执行。信息窃取型恶意软件（infostealer）会安装到用户电脑上，窃取已保存的密码、会话数据和登录凭证。Anthropic 的账户支持通常只跟踪总用量而不提供逐项用量明细，这使得异常消耗难以被用户及时察觉。

**「影响与关注点」** 这一事件揭示了 Claude 订阅用户面临的实际安全风险：即使没有主动使用，账户也可能因会话或令牌泄露而被第三方消耗额度，且用户缺少逐项用量工具来主动发现异常。对 AI 学习者和开发者而言，应重视本地环境安全，避免下载来源不明的软件或点击可疑广告，并定期检查账户活跃会话和授权应用。接下来值得关注 Anthropic 是否会推出更细粒度的用量透明工具、会话管理功能，以及官方关于令牌泄露和恶意软件防护的更明确指引。

**标签**: `#AI security`, `#Claude`, `#Anthropic`, `#token theft`, `#subscription abuse`

---

<a id="item-tech-news-10"></a>
### [GitHub 日榜 \#3：OpenAI 弃用 Codex Skills 目录仓库，流量引向 Plugins 仓库](https://github.com/openai/skills) ⭐️ 5.0/10

GitHub 日榜第 3 名的 openai/skills 仓库实际是 OpenAI 官方发布的 Codex 技能目录，但 README 已明确标注 deprecated（弃用）。该仓库目前 26,503 stars，今日增加 490 stars，主语言为 Python，简介为 “Skills Catalog for Codex”。官方指引用户转向新的 OpenAI Plugins 仓库（github.com/openai/plugins）获取最新的 Codex skill 与 plugin 示例，并推荐阅读 plugins build 指南了解如何创建 skill-only plugin。仓库内容解释了 Agent Skills 为“可被 AI 代理发现和使用的指令、脚本、资源文件夹”，Codex 用它把团队或个人的重复任务封装成可复用能力。技能按 .system、.curated、.experimental 分类：.system 中的技能会随最新 Codex 自动安装，curated/experimental 技能可借助 Codex 内的 $skill-installer 安装。由于它只是一个迁移引导仓库，本次上榜更值得关注的是 OpenAI 将 skills 与 plugins 能力统一收口这一生态信号，不代表有新的技能发布。

github · openai · 9月9日 00:17

**「背景」** Codex 是 OpenAI 面向终端用户的编程智能体/命令行工具，能在终端中完成编码、文件修改与仓库操作；Agent Skills 是让模型按说明自动调用某个任务能力的一整套文件夹，包含指令、脚本和资源。该 skills 仓库此前用来集中维护 Codex 可直接使用的 skill 示例，而 OpenAI 当前正把 skill 与 plugin 的开发文档都整合进 plugins 体系，因此官方把旧目录标记为弃用并引导用户去新仓库。

**「影响」** 对学习者，旧技能 collection 仍可作为理解 skill 结构和安装方式的历史样例，但新项目应直接参考 openai/plugins 与官方插件构建文档。对构建 Codex 工作流的开发者，观察重点是插件系统是否成为 skill 的唯一入口，以及 agentskills.io 开放标准在多智能体框架之间能否通用。

**标签**: `#GitHub`, `#OpenAI`, `#Codex`, `#Agent Skills`, `#Plugins`

---
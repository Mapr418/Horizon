---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 47 条内容中筛选出 10 条重要资讯。

---

**AI 前沿简讯**
1. [OpenAI 发布 Navier–Stokes 千禧年问题求解帖，热议集中在证明归属与模型能力跃升](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepMind 发布 AlphaGenome Atlas：覆盖人类基因组全部单核苷酸变异影响的预测地图](#item-tech-news-2) ⭐️ 9.0/10
3. [Meta 发布个人 AI 智能体 Muse：连接日常应用代办任务，隐私信任成最大悬念](#item-tech-news-3) ⭐️ 9.0/10
4. [Google DeepMind 发布 AlphaGenome Atlas：面向基因组学的预测资源上线，但社区对其创新性存疑](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI 被指施压数学家撤下 Anthropic 合著者，并公布约一万智能体证明 Navier-Stokes 结果](#item-tech-news-5) ⭐️ 8.0/10
6. [让 Claude 别再说废话：开源技能 i-have-adhd 登顶 GitHub 日榜](#item-tech-news-6) ⭐️ 7.0/10
7. [“diagram-design”登顶趋势：为 Claude Code、Codex 等 AI 代理提供编辑级 HTML+SVG 图表模板](#item-tech-news-7) ⭐️ 7.0/10
8. [Claude 订阅令牌遭窃：黑客悄悄消耗用户额度，Anthropic 指向信息窃取恶意软件](#item-tech-news-8) ⭐️ 7.0/10
9. [Cognition 估值升至 480 亿美元，AI 编程助手赛道“赢家通吃”论再受挑战](#item-tech-news-9) ⭐️ 7.0/10
10. [OpenAI 弃用 Codex Skills 目录仓库，迁移至 OpenAI Plugins](#item-tech-news-10) ⭐️ 6.0/10

---

## AI 前沿简讯

<a id="item-tech-news-1"></a>
### [OpenAI 发布 Navier–Stokes 千禧年问题求解帖，热议集中在证明归属与模型能力跃升](https://openai.com/index/navier-stokes-solution/) ⭐️ 9.0/10

OpenAI 官网（openai.com/index/navier-stokes-solution/）发布题为《On the Navier–Stokes Millennium Prize Problem》的帖子，社区引述帖文称：一个内部 OpenAI 系统给出的证明显示，描述流体运动的 Navier–Stokes 方程可以在有限时间内发展出奇点，从而涉及千禧年大奖难题中的存在性与光滑性问题。当前可见材料只有标题、社区评论和引述，没有原文技术细节或评审信息，因此不能独立验证证明是否成立、是否经过同行评审、是否开放完整过程。围绕帖子的 Hacker News 讨论同时出现了多条具体线索：有评论提问这是否就是那个“据称基于他人真实工作和提示词”的案例，并附上 HN、Bluesky 与 NYU 研究者声明链接；有评论指出，埋没在争议中的核心消息是 OpenAI 声称一个训练不到两周的内部模型，在数学能力上达到一周前才公开的 Astra 模型的两倍以上；还有人转述陶哲轩的观察，认为“某人正在研究某问题”的传闻本身就足以触发大规模 AI 努力去抢先压平问题，可能让研究者不再公开分享有前景的方向。整体来看，这条新闻更适合被理解为前沿实验室能力声明与科学研究伦理争议的混合事件，而不是经过验证的数学结论。接下来值得关注的是，OpenAI 是否会放出完整证明、训练配置、模型卡和可复现流程，以及流体力学和偏微分方程领域专家是否给出正式鉴定。

hackernews · tedsanders · 9月8日 17:13 · [社区讨论](https://news.ycombinator.com/item?id=49613262)

**「背景」** Navier–Stokes 存在性与光滑性问题是克雷数学研究所 2000 年公布的七个千禧年大奖难题之一，它询问：给定光滑且足够好的初始条件，三维不可压缩 Navier–Stokes 方程是否总能存在全局光滑解，还是会在有限时间内出现速度或压力趋向无穷的“奇点”。按传统规则，任何正式解答都需要发表在认可的数学期刊并经同行评审，才能获得 100 万美元奖金，因此 AI 系统直接宣称“证明有限时间奇点”并不等于千禧年问题被官方解决。OpenAI 通常以发布技术报告和模型能力展示来介绍内部进展，这次的特殊之处在于它以数学证明作为能力宣传素材，而非以传统数学论文流程提交给数学界。

**「影响与下一步」** 对学习者和研究者来说，真正的信号不是“AI 已解决千禧年难题”，而是前沿实验室开始把内部模型的原创数学证明当作能力宣传材料，说明模型在数学推理和科学研究中的角色可能从辅助工具加速变成“主动解题者”。如果 OpenAI 后续公开完整可验证的证明，流体力学和 PDE 社区的反应将比发布帖本身更关键；若没有公开，这件事就更接近技术宣传与伦理事件，而非可复核的科学成果。建议关注官方 technical report、模型卡、验证脚本以及外部数学家复核意见，而不是仅凭标题判断结论是否成立。

**「社区讨论」** 评论中主要有三种声音：一是质疑成果来源，有人问这是否就是那个“据称基于他人真实工作和提示词”的案例，并附上 NYU 声明等链接；二是惊叹模型能力提升速度，认为即使进步只限于数学，训练不到两周就达到 Astra 两倍以上也是惊人事件；三是担忧研究文化受损，陶哲轩的意见被总结为“关于某人研究方向的传闻就可能触发 AI 抢跑式解决，最终让研究者不再公开分享方向”。此外也有观点提醒，自然科学研究与形式化计算不同，物理世界中的问题不能只靠计算得出答案。

**标签**: `#OpenAI`, `#math reasoning`, `#Navier-Stokes`, `#frontier lab update`, `#technical report`

---

<a id="item-tech-news-2"></a>
### [DeepMind 发布 AlphaGenome Atlas：覆盖人类基因组全部单核苷酸变异影响的预测地图](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) ⭐️ 9.0/10

Google DeepMind 今日发布 AlphaGenome Atlas，官方称其为目前最全面的基因变异分子效应目录，包含人类基因组约 90 亿个单核苷酸变异（即每一种可能的单字母 DNA 改变）的预测结果，并通过面向学术研究的免费网站门户开放。该资源基于 DeepMind 的 AlphaGenome 模型大规模预计算，同时引入 AVI 分数，把 AlphaGenome 的调控预测与 AlphaMissense 的蛋白影响评分合并为单个数值，便于研究者快速排序变异；每个 AVI 分数还附带生物学特征归因，并收录超过 2500 个 DNA 序列 motif。官方数据显示，AlphaGenome Atlas 是一个 1 PB 级数据集，规模是 AlphaFold Database 的 30 倍以上。合作案例方面，Broad Institute 与 GREGoR Consortium 团队用 AVI 排序找到此前被遗漏的 DNM1 罕见病相关变异，实验验证表明该变异制造了错误剪接位点；Exeter 大学的 Gareth Hawkes 使用 UK Biobank 超过 54,000 人的全基因组数据，按预测分子效应分组稀有变异后多识别出 22% 的非编码遗传关联，涉及 PLA2G7、EGLN1 等蛋白，并将其进一步用于 BMI 研究。访问渠道包括网站门户、AlphaGenome API，以及 Google Antigravity 中的技能。

rss · Google DeepMind Blog · 9月8日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49610641)

**「背景」** AlphaGenome 是 DeepMind 此前发布的 AI 模型，用于预测遗传变异如何影响剪接、基因表达等分子生物学过程；AlphaMissense 则专注预测改变蛋白序列的错义变异影响。AlphaGenome Atlas 的思路类似于 2022 年扩展后的 AlphaFold Database：预先计算大量预测结果，做成一个把 DNA 序列变异、调控元件和蛋白功能联系起来的“地图集”，让没有编程经验的研究者也能直接浏览和查询海量基因组数据。

**「影响」** 对 AI 学习者和基因组研究者而言，这个平台把约 90 亿变异从“按需查询模型”变成可浏览、可排序的公共资源，显著降低变异解读门槛；AVI 同时覆盖编码区和非编码区，对罕见病变异优先级筛选和复杂性状关联研究尤其有参考价值。由于目前信息主要来自官方博客，下一步应关注配套技术报告、详细基准与标签来源说明，以及 API 或数据下载的实际授权和配额限制。

**「社区讨论」** 有评论指出，全基因组图谱的基准标签若来自保守性分析，就难以区分预测结果是否只是在重复已有先验；也有研究者对实际效用持保留态度，认为 AlphaFold 本身尚不能回答类似“我的 GFP 融合蛋白能否工作”这种具体问题，因此更大规模的基因组预测需谨慎对待。另有评论提到，有人在病毒上做了类似的“突变所有位点”实验，并将官方头图与生成艺术来源进行了关联说明。

**标签**: `#AlphaGenome Atlas`, `#DeepMind`, `#AI for science`, `#genomics`, `#variant prediction`

---

<a id="item-tech-news-3"></a>
### [Meta 发布个人 AI 智能体 Muse：连接日常应用代办任务，隐私信任成最大悬念](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/) ⭐️ 9.0/10

Meta 于本周二正式发布面向美国消费者的个人 AI 智能体 Muse。它不再是聊天问答产品，而是连接用户日常使用的邮件、日历、支付、健康健身、智能家居、餐饮购物、音乐活动等应用与服务，代替用户执行发邮件、订旅行、降账单、填表格、发邀请、按食谱生成购物清单、购物等任务；结账环节通过 Stripe Link 完成，并称附带购买保护，Shopify Shop Pay 和 1Password 集成也即将上线。Muse 由 Meta 自研模型 Muse Spark 驱动，提供内置连接器；若服务无现成集成但有公共 API，用户可提供凭据新建连接，否则 Muse 可通过浏览器访问服务。产品将通过网页 muse.ai、iOS/Android 应用和 WhatsApp 对话提供，随后进入 Meta 智能眼镜；采用免费层加订阅制，推出 Power（20 美元/月）与 Maximum（100 美元/月）两档，且开始使用需要绑定支付卡。Meta 强调 Muse 运行在独立安全的 Muse Secure VM 中，由 Sentinel 代理在系统层面隔离保护，无法看到密码与支付方式，也不会把对话和数据用于 Meta 广告系统，但这些安全声明仍需安全专家进一步审查。此次发布距离 Meta 就社交媒体消费者伤害与多州达成 180 亿美元和解不到两周，因此外界普遍关注消费者是否愿意为“可代办任务的 AI”交出更多个人数据。

rss · TechCrunch AI · 9月8日 19:00

**「背景补充」** Muse 属于“能做事”的 AI 智能体（agentic AI）而非传统聊天机器人，是 Meta 在 ChatGPT 时代之后押注的下一个消费 AI 范式。它背后是 Meta 自研模型 Muse Spark，并用连接器、API 和浏览器三种方式访问第三方服务；这种主动连接用户私人数据的模式，与苹果在 iMessage、SMS 和 WhatsApp 中嵌入 AI，以及 Gemini Spark、Claude Cowork 等竞品的方向一致。Meta 希望用可命名、可自选头像的个性化设定缓和隐私顾虑，但 Meta 过去涉及隐私罚款、数据泄露和国会听证的历史，正是理解本次信任讨论的关键背景。

**「影响分析」** 对 AI 学习者和产品开发者来说，Muse 的价值在于示范了消费级 AI Agent 的产品形态：预置连接器、公共 API 和浏览器兜底、启用前逐项授权、按用量分层订阅，以及把支付卡同时作为计费和启动门槛。更值得关注的是 Meta 在个人智能体数据与广告系统之间划出的隔离承诺是否经得起独立安全审查；接下来应关注安全研究人员对 Muse Secure VM 的验证、真实连接器生态的扩展速度，以及免费额度耗尽后用户对付费订阅的实际留存情况。

**标签**: `#Meta`, `#AI agent`, `#consumer AI`, `#product launch`, `#trust`

---

<a id="item-tech-news-4"></a>
### [Google DeepMind 发布 AlphaGenome Atlas：面向基因组学的预测资源上线，但社区对其创新性存疑](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10

Google DeepMind 通过官方博客发布了 AlphaGenome Atlas，一个面向基因组学的预测性资源。现有社区讨论指出，这次发布本质上是在公开一个“预测缓存（cache）”，而不是新的模型权重或详细方法说明；官方博客没有深入交代该缓存的原始数据来源，也没有正面回应“这些预测是否可信”这一核心问题。评论者进一步提到，真正支撑该资源的同行评审论文发表于 1 月，Nature 论文编号为 s41586-025-10014-0。多位基因组学领域人士认为，AlphaGenome 相对此前 SOTA 模型 Borzoi 几乎没有实质提升，当前热度更多来自“Alpha”品牌前缀。感兴趣的开发者仍可以前往 Atlas 网页提交申请，有评论者表示在“affiliation”一栏填“None”即可直接进入。总体来看，这是 DeepMind 在生命科学基础设施上的又一次产品化动作，但学术新颖性和方法透明性是后续需要验证的内容。

hackernews · utiiiD · 9月8日 14:55 · [社区讨论](https://news.ycombinator.com/item?id=49611251)

**「背景知识」** AlphaGenome Atlas 是 Google DeepMind 在计算基因组学方向推出的预测资源入口；这类资源通常把 DNA 序列与基因表达、调控等表型预测结果整理成可供查询的数据集，目标用户是实验与计算生物学家。基因组学预测任务中长期存在多种深度学习方法，Borzoi 等模型已被视为重要的精度基准。此次发布的“Atlas”更像一个集中式的预测结果浏览与访问门户，而不是包含完整训练流程和权重发布的新模型，因此需要配合论文和模型卡才能评估其真正价值。

**「影响分析」** 对于研究者和产品构建者，AlphaGenome Atlas 降低了获取大规模非编码区预测结果的访问门槛，尤其适合需要快速查询调控区域影响的实验组。但社区批评提示，仅凭“DeepMind 发布”不足以判断该方法领先，必须同步阅读 Nature 论文、核对缓存来源与评价基准，避免在未经第三方评测的情况下直接用其预测指导实验。接下来值得关注的不是 Atlas 页面本身，而是官方是否会公开完整的模型卡、数据版本、局限说明以及针对 Borzoi 等模型的系统对比。

**「社区讨论」** Hacker News 评论呈现明显分歧：有人认为该贴被点赞主要是“Alpha”前缀的品牌效应，并指出 AlphaGenome 相对 Borzoi 几乎无改进；也有人呼吁关注启动子序列等具体生物学机制是否被模型覆盖。还有用户反馈，Atlas 登录页中的 affiliation 字段可填“None”，实际访问门槛不高。

**标签**: `#Google DeepMind`, `#AlphaGenome`, `#genomics AI`, `#model release`, `#AI research`

---

<a id="item-tech-news-5"></a>
### [OpenAI 被指施压数学家撤下 Anthropic 合著者，并公布约一万智能体证明 Navier-Stokes 结果](https://the-decoder.com/openai-researcher-allegedly-pressured-mathematician-to-drop-anthropic-co-author-from-math-breakthrough-paper/) ⭐️ 8.0/10

据 The Decoder 报道，数学家 Tristan Buckmaster 公开发表声明，指控 OpenAI 在得知他与 Levent Alpöge 使用 AI 协助推进 Navier-Stokes 方程研究后，对其施压，并要求在论文中撤下在 Anthropic 工作的合著者 Alpöge。Buckmaster 称，他和 Alpöge 从 8 月中旬开始使用 Claude 与跑在 Codex 上的 GPT-5.6 Sol 等模型取得多项突破，并曾把全部草稿放进 Codex 会话中；OpenAI 方面先是提出联合发布或由 Buckmaster 单独发表的方案，据说 Sébastien Bubeck 两次要求移除 Alpöge，并说出“你为什么要毁掉自己的职业生涯”，但 OpenAI 否认这些指控。同一事件中，OpenAI 公布了自己求解 Navier-Stokes 相关问题的结果，称证明由约 10,000 个协同 AI 智能体在 88 小时内生成，使用一个被描述为“比 GPT-6 Astra 显著更强”的内部模型，并已在 Lean 中完成形式化。OpenAI 研究负责人 Mark Chen 表示，仅计算成本就达“数百万美元”；公司声明称没有以任何方式看过 Buckmaster 与 Alpöge 的工作，成果路径与细节也不同，但同时承认“不能完全排除”去标识化的用户数据帮助改进了模型。由于相关论文尚未正式发表或完成独立验证，事件中的关键事实、数据使用边界、以及证明本身的正确性目前都仍需进一步确认。

rss · The Decoder · 9月8日 19:23

**「背景知识」** Navier-Stokes 方程是描述流体运动的核心方程，也是克莱数学研究所列出的七个“千禧年大奖难题”之一，每个难题附带 100 万美元奖金；这一难题的关键挑战通常被理解为证明解在长时间内的光滑性与唯一性是否始终成立。本次事件还反映出 AI 辅助数学研究的新趋势：研究者不再只把大模型当作计算工具，而是让模型参与提出路径、写草稿、甚至用 Lean 这样的交互式定理证明器做可机器校验的证明；OpenAI 主张其智能体系统能以集中调度、大规模并发的方式逼近此类公开难题。

**「影响与后续看点」** 对数学、AI 与科研伦理三个领域而言，这个案子标志着一个新的冲突场景：当“使用 AI 工具的独立研究者”与“提供工具的 AI 公司”几乎同时宣称解决同一经典难题时，谁拥有优先级、谁可以使用用户在平台上的草稿数据，都会成为必须回答的问题。对学习者和开发者来说，接下来值得关注的是 OpenAI 是否公布完整的可验证 Lean 证明与提示记录，以及 Buckmaster 和 Alpöge 是否在后续发表中公开更多会话与模型使用细节；这些证据会比单方面声明更能说明“一万个智能体 88 小时解难题”究竟是真突破还是营销叙事。

**标签**: `#OpenAI`, `#Navier-Stokes`, `#AI research`, `#research ethics`, `#math proof`

---

<a id="item-tech-news-6"></a>
### [让 Claude 别再说废话：开源技能 i-have-adhd 登顶 GitHub 日榜](https://github.com/ayghri/i-have-adhd) ⭐️ 7.0/10

GitHub 日榜第一的 ayghri/i-have-adhd 是一个面向 Claude Code 等编码助手的 skill/plugin，目标是让助手不再把答案埋在大段解释里，而是输出“动作优先、步骤编号、删除客套话”的简短回复。该仓库当前有 30,274 stars，今日新增 422 stars，作者为 ayghri，元数据主要语言是 Python。README 用 before/after 示例展示核心变化：改前回复包含“Great question\! Let me think…”和“Hope this helps\!”，改后回复则直接写“Run npm install jsonwebtoken@latest，然后编辑 src/auth.ts:42”并给出编号步骤。SKILL.md 列出了 10 条规则，包括先用下一步动作开头、多步骤任务编号、列表不超过 5 项、给出具体时间估算、不说前言、不重复总结等。仓库同时提供了简体中文、葡萄牙语、日语、越南语、韩语、泰语等多个语言的 README，并以 MIT 协议开源。安装方式是把一段提示词复制给 CLI agent，让它从 https://github.com/ayghri/i-have-adhd 安装技能，并参考仓库中的 AGENTS.md。这个项目之所以成为日榜热门，不来自新模型发布，而是开发者对 Claude 等 coding agent 冗长文风的一次集中表达，以及一套可复用的提示工程/技能封装。项目相关 HN 评论区也主要围绕 Claude 的啰嗦问题展开讨论。

github · ayghri · 9月8日 23:29 · [社区讨论](https://news.ycombinator.com/item?id=49610631)

**「背景」** Claude Code 是 Anthropic 的命令行编码代理，支持通过 plugin marketplace 安装“skills/skill”：这类技能本质上是一份 SKILL.md 指令文件或插件，会被注入模型上下文，用来持续约束输出格式；用户也可以使用全局 CLAUDE.md 写入类似偏好。i-have-adhd 把这个思路产品化，并不要求使用者真的确诊多动症，而是借用 ADHD 行为干预中常见的“动作优先、步骤拆分、减少无关内容”原则，让模型每次都先给出下一步可执行的操作。理解这个机制后，就能明白它走红的原因：它属于 agent 交互风格控制层上的轻量示例，而不是新的基础模型或评测基准。

**「影响与看点」** 对学习者和开发者来说，这个项目展示了如何用极低成本改变 agent 行为：不依赖新模型，只靠一份 Markdown 技能文件就能显著压缩输出。它同时提醒大家，LLM 对格式指令的遵从可能并不持久；HN 上已有用户实测称这种简洁只能维持几轮，之后又会退回默认啰嗦模式。后续值得关注的方向包括：作者是否加入 hook 形式的强制注入、Anthropic 是否在新模型中原生改善风格控制，以及 Claude Code 的 skill/plugin 机制是否会成为更多开发者工具效仿的标准做法。

**「社区讨论」** HN 评论区的基本共识是 Claude 的冗长确实是真实痛点：TomGarden 说最常用的后续指令是“一次只说一件事”和“太多文字”，ryandrake 则抱怨 Claude 喜欢反复解释“我改了 a.py 和 b.py，但没有改 README，也没有提交”这类“不做什么”的否定信息，jp57 甚至质疑 Anthropic 内部是否真的用这种风格沟通。用户 sleazebreeze 实测后表示该技能通常只能保持简洁几轮，之后模型又会恢复啰嗦，除非用 hook 对每条回复都强制注入。另有评论对 README 中“把安装命令直接复制进 CLI prompt”的分发方式表示警惕。

**标签**: `#AI coding agents`, `#Claude`, `#prompt engineering`, `#open-source`, `#developer tools`

---

<a id="item-tech-news-7"></a>
### [“diagram-design”登顶趋势：为 Claude Code、Codex 等 AI 代理提供编辑级 HTML+SVG 图表模板](https://github.com/cathrynlavery/diagram-design) ⭐️ 7.0/10

cathrynlavery/diagram-design 登上 GitHub 每日趋势第 2 名，仓库当前共 34707 stars，今日新增 1020 stars，主要语言为 HTML。作者为 littlemight.com 的 Cathryn Lavery，项目定位是“给你的 AI 编码代理用来生成编辑级图表”的模板合集：自包含的 HTML+SVG，无需构建步骤、无需 JavaScript、无外部图片依赖，可直接在浏览器中打开。README 说明其支持 Claude Code、Codex、Factory Droid、Pi 以及任何兼容 Agent Skills 的主机，并宣称“无阴影、无 Mermaid 垃圾输出”。项目提供 39 种图表类型，其中架构图、流程图、时序图、ER 图、状态机、泳道图、象限图、雷达图、时间线、环形飞轮等均有三种静态变体（极简浅色、极简深色、全编辑风格）。新版本 2.5.10 增加了 Sankey、鱼骨图、Wardley map、看板、用户旅程、部署、依赖图、UML 类图、故事地图、数据库 schema 等十种布局语法；2.3 加入语义系统模式和可选的无障碍动效，默认输出仍为静态 HTML。项目还强调“语义模式把行为与布局分离”，因此队列、策略追踪、信任边界等概念可以复用现有图表类型，无需持续扩充类型数量。核心使用方式是把它作为 Claude Code skill，让代理读取你的网站后约 60 秒内匹配品牌风格输出高质量图表，并能把 draw.io 或 Mermaid 源文件按指定格式、尺寸、细节程度重绘。

github · cathrynlavery · 9月8日 23:29

**「背景」** Claude Code、Codex 等“agentic coding”工具支持通过 skill 或类似机制注入可复用的工作流程，让模型在生成代码以外还能按固定模板产出结构化资产。diagram-design 正是把“高质量信息图式”做成一组 skill 模板，让代理直接编写自包含的 HTML+SVG 图表文件；相较依赖 Mermaid、Figma 或手调 CSS 的常见做法，它试图解决 AI 生成图表“看起来通用、无法直接进产品页面”的痛点。项目强调所有图表都是“静态 HTML 默认，动效可选”，因此可以在绝大多数 Web 环境零依赖嵌入。

**「影响」** 对开发者、技术写作者和 AI agent 用户来说，这个项目提供了一个低门槛的方式，让 Claude Code、Codex 等代理在 60 秒内产出风格一致、可直接发布到站点的架构图、流程图和数据模型图，能明显减少“从模型拿到粗糙图表后再去 Figma 返工”的时间。对 AI 生态更重要的信号是：它展示了 Agent Skills 这类“给模型套固定输出模板”的范式正在产生真实的产品级产出，而不是停留在玩具示例层面。当前值得关注的是项目后续新增的布局语法和语义模式兼容性，以及在更多 host（如 Factory Droid、Pi）上的实际表现与社区插件支持。

**标签**: `#open-source`, `#diagrams`, `#AI tools`, `#Claude Code`, `#GitHub trending`

---

<a id="item-tech-news-8"></a>
### [Claude 订阅令牌遭窃：黑客悄悄消耗用户额度，Anthropic 指向信息窃取恶意软件](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/) ⭐️ 7.0/10

英国独立 AI 顾问 Grant De Swardt 的 Claude Max 20x 订阅在 8 月 4 日出现异常：当天他没有工作，token 用量却持续攀升。第二天他停用所有关联服务、暂停 Cowork 任务并禁用云执行后，用量仍在受控时段从 45% 上升到 55%。Anthropic 调查后告知，一枚被窃的 Claude 会话密钥被用来铸造未经授权的 Claude Code OAuth 令牌，账户“似乎被一个未经授权的第三方服务用来处理他人的活动”，但公司无法确定访问来源。Anthropic 随后暂停了他的付费账户、使所有会话和服务器端 Claude Code 令牌失效，并就剩余订阅时间退还 £44.49；约两周后账户恢复。De Swardt 表示缺少明细用量和难以获得及时支持让他失去信任，最终取消 Claude，改用支持多模型与开源模型的 Cursor。在 Reddit 与 GitHub 上，还有多名用户报告类似情况，包括未经同意自动升级、12 分钟内用量从 0 增至 49%，以及连续几天未使用却烧光额度。Anthropic 发给部分用户的邮件称，常见信息窃取恶意软件会窃取 Claude 登录会话并消耗配额，但恶意软件并非来自 Claude 使用本身，而可能来自下载被感染软件或点击恶意广告。Anthropic 拒绝说明用户如何识别这类误用，De Swardt 认为在缺少逐项用量工具的情况下，用户几乎无法自我保护。

rss · TechCrunch AI · 9月8日 21:10

**「背景」** Claude Max 20x 是 Anthropic 面向重度用户的付费订阅档，约 $200/月，按 token 用量计费，适合需要大量 Claude Code、Cowork 等代理任务的用户。Claude Code 是 Anthropic 的编程代理，可通过本地 CLI 或云端执行任务；OAuth 令牌与服务器端会话令牌用于授权，一旦会话密钥落到攻击者手中，就可能被用来铸造新令牌并消耗订阅额度。信息窃取恶意软件（infostealer）专门窃取浏览器保存的密码、会话和登录数据，通常是用户下载被感染软件或点击恶意广告时被安装，这不代表攻击来自 Claude 本身。

**「影响」** 对依赖 Claude Max 或 Claude Code 自动化的个人开发者和创业公司来说，这起事件提醒：令牌与登录会话是实际资产，应避免连接来源不明的第三方服务，也不能忽视本地设备可能感染恶意软件的风险。目前 Anthropic 不提供逐项用量明细，用户很难自行发现盗刷，因此值得关注官方是否将推出用量审计、会话管理或更强的异常检测；在此之间，解除可疑授权、定期登出并检查设备安全是更直接的防护手段。

**标签**: `#AI security`, `#Claude`, `#token theft`, `#account compromise`, `#Anthropic`

---

<a id="item-tech-news-9"></a>
### [Cognition 估值升至 480 亿美元，AI 编程助手赛道“赢家通吃”论再受挑战](https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/) ⭐️ 7.0/10

Cognition，开发 AI 编程助手 Devin 的创业公司，宣布完成 20 亿美元融资，估值达 480 亿美元，较 5 月上一轮 260 亿美元估值仅过四个月。本轮由 Andreessen Horowitz、Accel、Founders Fund、General Catalyst 和 Avenir 共同领投；Cognition 称 5 月融资后其年化运行率收入从 4.92 亿美元增至 9 亿美元，但未说明计算方法。文章将这一估值与 Cursor 对标：Cursor 曾在 4 月按约 500 亿美元估值谈判融资，随后以 600 亿美元出售给 SpaceX，彼时其年化收入已超 20 亿美元；按指标推算，Cognition 当前收入倍数约 53 倍，高于 Cursor 春季出售时约 25 倍。Cursor 据报因严重算力受限而被 SpaceX 收购，而 Cognition 也可能面临类似问题：其租用英伟达服务器集群的年成本高达数亿美元，The Information 测算今年现金消耗可能达 8 亿美元。Cognition 正基于开源模型训练自研模型，以逐步降低对 OpenAI 和 Anthropic 第三方模型的依赖；The Information 预计该公司 2026 年底年化收入可达 40 亿至 50 亿美元，而 Cursor 在同一时点被追踪可超 60 亿美元。其客户包括 Mercedes-Benz、NASA、Goldman Sachs 和 Citi，公司由 Scott Wu 于 2024 年创立。

rss · TechCrunch AI · 9月8日 21:04

**「背景知识」** Cognition 是专注于软件工程的 AI agent 公司，核心产品 Devin 被定位为可独立完成编程与部分开发流程的“AI 软件工程师”；这类产品需要大规模 GPU 进行推理和训练，因此商业模式高度依赖算力与模型成本。“年化运行率收入”是一种把当月收入乘以 12 得到的估算指标，适合衡量快速增长但尚未稳定的初创公司，常被投资人和媒体用于横向比较。Cursor 是同赛道最接近的竞品，其出售给 SpaceX 的背景，以及 Cognition 持续高倍数融资，共同表明前沿 AI 编程市场在模型层和产品层仍有多个竞争者在争夺份额。

**「影响与看点」** 对开发者和学习者来说，这个消息说明 AI 编程助手正在从“调用第三方模型做补全”转向“训练自研模型+重度算力投入”的产品形态，未来可用性和定价会与底层推理成本更紧密绑定。对创业者和企业决策者，Cursor 与 Cognition 的高估值未必代表通用 agent 已成熟，而是代表资本押注代码生成需求足够大；下一步值得观察的是 Cognition 自研模型上线后的基准与价格、其在企业客户中的渗透率，以及是否出现类似 Cursor 的算力约束公告。

**标签**: `#AI coding`, `#Cognition`, `#funding`, `#Devin`, `#AI industry`

---

<a id="item-tech-news-10"></a>
### [OpenAI 弃用 Codex Skills 目录仓库，迁移至 OpenAI Plugins](https://github.com/openai/skills) ⭐️ 6.0/10

OpenAI 官方 GitHub 仓库 openai/skills（Skills Catalog for Codex）在今日趋势榜排名第 3，主语言为 Python，已获 26,491 stars，今日新增约 490 stars。README 中显著提示该仓库已弃用（deprecated）：Codex skills 和插件示例已转移到 OpenAI Plugins 仓库（https://github.com/openai/plugins）；若想给 Codex 添加自己的 skills，应遵循官方 Build plugins 指南，其中包含创建 skill-only plugin 的说明。该仓库原本是供 Codex 发现和使用的 Agent Skills 目录，Agent Skills 被描述为由指令、脚本和资源组成的文件夹，可以一次编写、多处使用。安装方式上，.system 下技能会在最新版 Codex 自动安装，.curated 与 .experimental 技能需要在 Codex 中通过 $skill-installer 按名称或 GitHub 目录 URL 安装，安装后需重启 Codex 生效。本次变化更像面向 Codex 用户的生态迁移信号，而不是新能力或新发布，后续重点应放在新的 plugins 仓库与官方插件构建文档。旧仓库仍保留每个技能目录内 LICENSE.txt，用户须注意单个技能采用各自许可。

github · openai · 9月8日 23:29

**「来龙去脉」** OpenAI Codex 是 OpenAI 的智能体编程工具，可通过插件和 skills 为任务打包可重复使用的能力。Agent Skills 是包含指令、脚本与资源的文件夹，设计为一次编写、随处使用的开放概念，相关链接还指向 agentskills.io 开放标准。此前 openai/skills 仓库集中展示给 Codex 使用的技能目录；此次公告将它并入更通用的插件工作流，说明官方维护重心已从独立 skills 目录转向 plugin 体系。

**「影响与观察点」** 对使用 Codex 的开发者而言，下载或提交 skill 前应优先查看 openai/plugins 仓库和官方 Build plugins 指南，不要再依赖本仓库的后续更新。对学习智能体工程的人，这提供了观察厂商如何收敛“技能/插件”抽象的机会；下一步可关注 OpenAI Plugins 仓库的内容、Codex 插件文档是否把 skill-only plugin 作为唯一推荐路径，以及社区是否继续维护 agentskills.io 开放标准。

**标签**: `#OpenAI`, `#Codex`, `#Plugins`, `#Developer Tools`, `#Ecosystem Update`

---
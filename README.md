<!-- 本文件由 scripts/build.py 生成，请勿手改。要改内容请编辑 data/ 或 templates/ 后重新生成。 -->

# Awesome LLM Storytelling · 让大模型讲好故事

> 用大模型讲故事的开源方法合集：skill、agent 框架、应用和研究代码。小说、网文、短篇、剧本、互动叙事、同人仿写，以及把真实事件写得像小说一样好看的非虚构叙事，都收。
>
> Open-source methods for getting LLMs to tell stories: agent skills, harnesses, apps and research code for novels, short stories, scripts, interactive fiction, fan fiction and narrative nonfiction.

这里只收一类项目：故事主要由大模型写出来，项目本身提供的是讲故事的方法或原则，比如怎么先规划再写、怎么让长篇不吃书、怎么让多个 agent 分工审稿、怎么学一部作品的写法、怎么把一条新闻写成有悬念又不编造事实的故事。下载、发布、翻译、通用润色、标题模板这些周边工具不收。

每个项目都按故事类型归类，并标出它用了哪些方法，方便横向比较同一种方法在不同项目里怎么落地。

收录 692 个项目：249 个 skill 和提示词、423 个框架和应用、20 个研究代码 · 元数据更新于 2026-10-15

**图例**：🌟 精选 · 📝 提示词 · ⚙️ 框架 · 🧩 应用 · 🎓 研究代码 · 💤 超过 180 天未更新 · 📦 已归档 · ⚠️ 仓库失效

> [!NOTE]
> 「人工核对」指核对过仓库说明、目录结构和分类，不等于实测过写作效果。skill 和应用可能附带脚本，安装前请先读一遍说明。

## 目录

- [本周新增](#new)（0）
- [精选：从这里开始](#featured)（21）
- [按故事类型](#by-group)
  - [长篇小说 · 网文](#group-novel)（342）
  - [短篇 · 故事](#group-short)（36）
  - [剧本 · 短剧 · 影视](#group-script)（75）
  - [互动叙事 · 游戏 · 角色扮演](#group-interactive)（184）
  - [仿写 · 同人 · 风格迁移](#group-imitation)（15）
  - [通用叙事方法](#group-general)（40）
- [按创作方法查找](#by-method)
- [相关资源](#resources)
- [收录徽章](#badge)

<a id="new"></a>
## 本周新增

本周暂无新增。发现好项目欢迎[推荐](../../issues/new?template=submit-skill.yml)。

<a id="featured"></a>
## 精选：从这里开始

每种故事类型里方法最扎实、最有代表性的项目，第一次来可以先看这些。

- [inkos](https://github.com/Narcooo/inkos) ★10.3k · 长篇小说 · 网文：统一 harness 管长短篇、剧本、同人仿写、互动影游；长篇用 truth files 记设定、伏笔和角色状态，每章写后审计→修订→状态回写
- [oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) ★7.6k · 长篇小说 · 网文：扫榜找题材、拆爆款提节奏与素材，再按细纲逐章写；设定、大纲、追踪分文件落盘，状态卡分开作者真相与读者已知，写后脚本查 AI 句式
- [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) ★7.5k · 长篇小说 · 网文：Claude Code 长篇网文插件：分阶段初始化设定与总纲、拆卷纲章纲，写章后多维审查并把事实提交进状态库与 RAG，可查伏笔角色，附只读面板
- [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) ★6.2k · 长篇小说 · 网文：本地部署的长篇小说生成应用：用雪花法从核心创意逐级展开卷、弧、场景、章纲到正文，管理角色/势力/物品/伏笔状态，AI 流程可在画布上改
- [autonovel](https://github.com/NousResearch/autonovel) ★1.6k · 长篇小说 · 网文：仿 autoresearch 的改—评—留弃循环：设定、人物、大纲、文风、canon 打分过阈值，逐章起草评分重写，再经对抗删改、读者评审团和 Opus 审稿
- [RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT) ★999 · 长篇小说 · 网文：用自然语言模拟 LSTM：每步写一段正文和下一段计划，改写短期记忆，段落摘要存入可语义检索的长期记忆；人可选改计划共写任意长度小说
- [neuro-book](https://github.com/notnotype/neuro-book) ★744 · 长篇小说 · 网文：长篇写作 IDE：时间线切面事件溯源推算世界状态，伏笔承诺账本，leader/writer 等多 agent 分工写章，llmlint 规则查 AI 味
- [lengdu](https://github.com/asass-11/lengdu) ★39 · 短篇 · 故事：中文短篇创作与冷读：先写完正文，再由独立校准 Agent 和全新读者 Agent 首读，检验看懂、流畅、好看
- [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) ★1.7k · 剧本 · 短剧 · 影视：从 47 本编剧书与 23 卷剧本蒸馏 26 个 skill：结构、Truby、场景、对白、剧集圣经、编剧室与改编，附中美日韩法剧作和戏曲案例
- [short-drama](https://github.com/0xsline/short-drama) ★1.4k · 剧本 · 短剧 · 影视：短剧编剧 skill：选题立项→故事骨架→角色与四层反派→分集目录（钩子、付费卡点）→逐集写剧本→五维评分审查→合规审核
- [dramatron](https://github.com/google-deepmind/dramatron) ★1.1k · 剧本 · 短剧 · 影视：从一句 logline 层级展开：先生成标题、人物、情节节拍和地点描述，再逐场生成对白，作者可在每一层编辑重写
- [Marinara-Engine](https://github.com/Pasta-Devs/Marinara-Engine) ★712 · 互动叙事 · 游戏 · 角色扮演：角色扮演与游戏引擎：AI 游戏主持带队伍/任务/战斗，可按需安装叙事导演、连续性检查、世界状态与关系追踪、长期记忆、Lorebook 维护等代理
- [OpenStory](https://github.com/ZJU-LLMs/OpenStory) ★430 · 互动叙事 · 游戏 · 角色扮演：多智能体故事世界推演框架：角色按感知→计划→执行→反思插件自主行动演出剧情，玩家可下指令、回溯分支；WorldKernel 一句话生成角色、地点与规则
- [AI4VisualNovel](https://github.com/ttsmallHot/AI4VisualNovel) ★102 · 互动叙事 · 游戏 · 角色扮演：视觉小说多 agent 框架：制片、编剧、演员、美术分工，先出大纲再生成拓扑排序的 DAG 分支剧情图，演员 agent 按人设演对白并审立绘，导出可玩游戏
- [Sonder_Engine](https://github.com/N0819/Sonder_Engine) ★59 · 互动叙事 · 游戏 · 角色扮演：互动小说引擎：导演裁定客观因果，感知层决定每个角色能知道什么，角色代理只凭私有记忆行动，叙述者只写玩家可见部分，再统一提交状态
- [harnessNovel](https://github.com/XTmingyue/harnessNovel) ★187 · 仿写 · 同人 · 风格迁移：先对参考小说分三阶段拆书（结构、世界观、情节单元、文风），把情节抽象成叙事模式，再按核心玩法→舞台路线→章纲→正文仿写，章节级去 AI 味
- [longzu.skillls](https://github.com/zuoyou12/longzu.skillls) ★11 · 仿写 · 同人 · 风格迁移：江南、烽火戏诸侯文风蒸馏 skill：全文统计 1465 万字语料加等距精读，得出共享叙事骨架和可替换语言皮肤，支持风格杂交，附审计脚本和盲测
- [sepia](https://github.com/Nanako0129/sepia) ★3.2k · 通用叙事方法：按 StoryScope 论文测出的 AI 小说结构特征分三遍修：先改叙事架构（不点题、松因果链、后置揭示），再改段落流和表层措辞
- [WriteHERE](https://github.com/principia-ai/WriteHERE) ★976 · 通用叙事方法：异构递归规划：把写作任务动态拆成检索、推理、撰写三类子任务，边分解边执行并按上下文调整，小说与长报告共用一套引擎
- [creative-writing-skills](https://github.com/haowjy/creative-writing-skills) ★512 · 通用叙事方法：muse 主代理调度头脑风暴、角色模拟、大纲、写手、批评、编辑和读者模拟等子代理，从已有文字提炼文风文件，写后批评修订并同步知识库
- [doc-story-generation](https://github.com/yangkevin2/doc-story-generation) ★161 · 通用叙事方法：DOC：先生成前提和多层细纲（重排器挑大纲顺序、检测人物），再按细纲逐段写正文并用控制器保持贴合大纲，产出 3500+ 词长故事

<a id="by-group"></a>
## 按故事类型

<a id="group-novel"></a>
### 长篇小说 · 网文

长篇连载的写作系统：开书、大纲、分章写作、长篇记忆、审稿。

#### skill · 提示词（131）

- 🌟 **[oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)** · ★ 7.6k<br>扫榜找题材、拆爆款提节奏与素材，再按细纲逐章写；设定、大纲、追踪分文件落盘，状态卡分开作者真相与读者已知，写后脚本查 AI 句式<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 中文 · 13 个 skill · MIT</sub><br><sub>💡 同团队另有 DeepSeek Harness 版 oh-story-dsh</sub>

- 🌟 **[webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)** · ★ 7.5k<br>Claude Code 长篇网文插件：分阶段初始化设定与总纲、拆卷纲章纲，写章后多维审查并把事实提交进状态库与 RAG，可查伏笔角色，附只读面板<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-14 · 中文 · 8 个 skill · GPL-3.0</sub><br><sub>💡 master 为 Claude Code 版，新功能在 v8 分支（DeepSeek Harness）</sub>

- **[chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill)** · ★ 3.8k<br>从零生成 10–50 章中文小说：三层问答、创作记忆、每章悬念钩子、自动校验<br><sub>方法：规划 · 理论 · 修订 · 共创</sub><br><sub>更新于 2026-10-06 · 中文 · MIT</sub>

- **[Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill)** · ★ 884<br>网文写作 skill：主路由分派到开头、转场、对白、章末、剧情逻辑、人物一致性、卷纲、去 AI 味等 10 个模块，写前检索本地语料范例<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-28 · 中文</sub><br><sub>💡 README 未写安装方式：SKILL.md 在仓库根目录，把整个仓库放进 skills 目录即可；附 166 篇短篇语料约 11MB，检索脚本需 Python 3</sub>

- **[Openwrite](https://github.com/LiPu-jpg/Openwrite)** · ★ 827<br>DeepSeek Harness 长篇小说插件：统一创作 Agent 加 90 个小说工具，人物、设定、大纲、伏笔存本地，章节走标准审稿 DAG 与去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 中文 · 25 个 skill · Apache-2.0</sub><br><sub>💡 需 DeepSeek Harness（dsh）宿主；preset 内含 oh-story-deslop / long-write / review 等 skill，疑似取自 zenstory-ai/oh-story-claudecode</sub>

- **[awesome-novel-agent](https://github.com/modoojunko/awesome-novel-agent)** · ★ 812<br>总控 agent 按状态文件逐个派 8 个子 agent：卷纲→章纲场景卡→提示词组装→正文→Gate A-F 去 AI 味（不过就重写）→归档更新设定<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-09-25 · 中文 · AGPL-3.0</sub><br><sub>💡 名字带 awesome，但它是创作 agent，不是列表</sub>

- **[novel-creator-skill](https://github.com/leenbj/novel-creator-skill)** · ★ 682<br>每章强制五步门禁（记忆同步→一致性→风格校准→校稿→脚本），配 RAG 回读、知识图谱、进度配额、跨 agent 交叉审稿与事件冷却，两遍去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-03-10 💤 · 中文</sub><br><sub>💡 最后更新 2026-03-10，因 682★ 收录；去 AI 味润色基于 blader/humanizer 方法论</sub>

- **[oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh)** · ★ 521<br>把 Oh Story 小说技能装进 DeepSeek Harness：加了文件树、编辑器、Chat 三栏的小说工作台，另带短剧、小说改游戏、视频解说工作台<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 中文 · 38 个 skill · MIT</sub><br><sub>💡 基于同团队的 zenstory-ai/oh-story-claudecode（打包的 Oh Story 0.8.5，小说技能文件与原版相同）和 novel-to-game，另加 DSH Web 工作台界面和短剧、视频解说技能。只能在 DeepSeek Harness 里用，需要 Node.js 24+；Claude Code 用户用原版</sub>

- **[Novel-Control-Station-Skill](https://github.com/jingtai123/Novel-Control-Station-Skill)** · ★ 424<br>开书访谈后先出完整大纲与人物档案，按真值文档逐章生成控制卡再写，章后回写人物/关系/伏笔/情绪债务等动态状态，按需加载风格模块并三步去 AI 味<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-03-29 💤 · 中文 · MIT</sub><br><sub>💡 最后更新 2026-03-29，因 424★ 收录；附 Codex 连续创作（马拉松）PowerShell runner 模板；作者称已用其写起点连载</sub>

- **[story-skills](https://github.com/danjdewhurst/story-skills)** · ★ 313<br>人物、伏笔、连续性状态都写成带 frontmatter 的 Markdown，CLI 像编译器查死人复出、伏笔先于铺垫等矛盾；24 个 skill 从构思到投稿<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-14 · 英文 · 24 个 skill · MIT</sub>

- **[novel-writer-skills](https://github.com/wordflowlab/novel-writer-skills)** · ★ 265<br>Claude Code 斜杠命令加 Skills：宪法→规格→澄清→计划→任务→写作→分析七步写小说，类型知识和一致性检查自动激活，追踪情节、时间线和关系<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2025-10-20 💤 · 中文 · 13 个 skill · MIT</sub><br><sub>💡 跨平台版是 wordflowlab/novel-writer；2025-10 后没再更新，按 265★ 且被多个派生项目沿用收录</sub>

- **[novel-writing-framework](https://github.com/LAY-lgtm/novel-writing-framework)** · ★ 257<br>五份网文写作方法论：通用长篇流程、番茄快节奏、起点慢热、智斗权谋专项、完稿改良诊断，含三章一轮自检和 AI 指纹量化指标<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-05-31 · 📝 提示词 · 中文 · MIT</sub><br><sub>💡 每份是单独的 .md，需自己放进 skills 目录或手动加载</sub>

- **[Lorn.NovelWriteSkills](https://github.com/lornshrimp/Lorn.NovelWriteSkills)** · ★ 234<br>先把作者文风、作品蓝本、题材研究蒸馏成模板，再走大纲→章节控制卡→正文→审阅去 AI 味闭环；母稿再改写成 13 个平台版本，跑字数和相似度门禁<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-04 · 中文 · 350 个 skill</sub><br><sub>💡 README 只写了 VS Code + GitHub Copilot 用法（.github/skills、.github/prompts 结构）；约 350 个 SKILL.md 也可单独复制到其他 agent；仓库约 22MB，大部分是写作研究资料</sub>

- **[webnovel-writer-opencode](https://github.com/lujih/webnovel-writer-opencode)** · ★ 216<br>webnovel-writer 的 OpenCode 增强版：三层 RAG 组上下文，故事合约约束设定，伏笔债务追踪，6 维审查，借鉴 inkOS 做事件溯源<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-10 · 中文 · 16 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer，另加 8 个 skill：批量写章、重写、修复、删除、导出（EPUB/DOCX/PDF 等）、番茄风和七猫风写作约束、自动发布到番茄；v2.8 起借鉴 inkos 的事件溯源设计。用 npx @cszx/webnovel-writer-opencode init 安装，Claude Code 用户直接用原版</sub>

- **[sumeru](https://github.com/xindoo/sumeru)** · ★ 203<br>网文全流程 7 个 skill：选题（含榜单分析）→世界观大纲→章节批量撰写→时间线/OOC 审查→润色→多平台导出，可断点续写<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2026-08-23 · 中文 · 7 个 skill</sub>

- **[Distilled-Novel-Toolbox](https://github.com/dama-cyber/Distilled-Novel-Toolbox)** · ★ 191<br>网文写作知识库 13 个 skill：题材、人设、世界观、节奏、爽点、情绪、文风、商业化、合规、润色去 AI 味与 AIGC 检测应对<br><sub>方法：理论 · 设定 · 人物 · 去 AI 味</sub><br><sub>更新于 2026-06-09 · 中文 · 13 个 skill</sub><br><sub>💡 README 未写安装方式：把各 novel-* 目录复制到 agent 的 skills 目录即可；每个模块附 test-prompts.json</sub>

- **[novel-kit](https://github.com/t59688/novel-kit)** · ★ 162<br>规范驱动的 40+ 条 /novel 斜杠命令：先建「小说宪法」与 Writer 风格配置，管理角色/地点/势力/伏笔，章节按规划→撰写→审查→润色→确认推进<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2025-12-22 💤 · 中文</sub><br><sub>💡 最后更新 2025-12-22，因 162★ 收录；需配合 novel-kit CLI 初始化项目</sub>

- **[awesome-novel-studio](https://github.com/MJbae/awesome-novel-studio)** · ★ 156<br>先出 3 份提案，再做世界观、带语气表的角色卡和 25 集节拍设计；写每集前汇总前两集时间线与伏笔，写后 6 个代理并行做 16 轴润色<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-04-14 💤 · 英文 · 10 个 skill · Apache-2.0</sub>

- **[tianming-skill](https://github.com/zy-zmc/tianming-skill)** · ★ 154<br>长篇协同创作指令系统：用五份知识库约束世界观与人物，按「天命：大纲/目录/正文/体检/存档」逐步推进<br><sub>方法：规划 · 设定 · 记忆 · 风格</sub><br><sub>更新于 2026-06-06 · 中文</sub><br><sub>💡 CC BY-NC-SA 4.0 非商用许可；README 同时推广作者的同名桌面软件</sub>

- **[book-genesis-studio](https://github.com/felipelobomotta-blip/book-genesis-studio)** · ★ 143<br>整本书写作 skill：立项简报→人物、章节计划与事实账本→逐章起草，盲读模拟读者评首章、每 5 章查连续性，审计加十项量表限次修订<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-09 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 按用户所用语言写作；附 32 章葡语样书，评分为自评</sub>

- **[novel-harness](https://github.com/manhai934/novel-harness)** · ★ 131<br>网文陪写 harness：开书规划，把章节拆成作者自己填的写作块，审稿去 AI 味，维护角色状态、伏笔和章节摘要<br><sub>方法：规划 · 记忆 · 去 AI 味 · 共创</sub><br><sub>更新于 2026-08-06 · 中文 · 6 个 skill</sub><br><sub>💡 附本地 Studio Dashboard（需 Python + Node）；可选知识包从作者服务器（阿里云 OSS）下载 zip</sub>

- **[Claude-Book](https://github.com/ThomasHoussin/Claude-Book)** · ★ 124<br>多 agent 写小说：只读 bible 加按章版本化 state，规划→写作→文风/人物/连续性三审循环≤3 轮，用本地小模型困惑度改写降 AI 痕迹<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-01-22 💤 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 perplexity-improver 需约 16GB 显存跑 Ministral-3-8B；book-analyzer 可从源书拆出 bible</sub>

- **[ai-novel-writer](https://github.com/Jieice/ai-novel-writer)** · ★ 116<br>网文 skill 套装：开书建项目出大纲人设，拆参考书学文风，毒点检测与冲突设计，写完同步降重并更新项目文件，另有 90 年代乡土、港综专用写作器<br><sub>方法：规划 · 理论 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-04-22 · 中文 · 17 个 skill</sub><br><sub>💡 整理自 Linux.do 用户 user2609 分享的流程，README 写安装到 Trae；仓库是作者工作目录，混有具体作品、参考小说原文、网页存档、BypassAIGC 降重和番茄自动发布脚本</sub>

- **[novel2agent-jp](https://github.com/kgmkm/novel2agent-jp)** · ★ 105<br>日语小说 skill：企划、世界观、角色、情节写进 TOML 并用脚本校验，编辑和作家分工执笔，再让多个 LLM 从逻辑、文体、考据、读者视角交叉推敲<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-09-25 · 日文 · MIT</sub><br><sub>💡 旧名 novel2hermes_jp；也支持 Hermes、goose；附 40 多项的角色表、插图提示词和 pixiv/カクヨム 投稿格式转换</sub>

- **[ani-book-skill](https://github.com/ExplosiveCoderflome/ani-book-skill)** · ★ 102<br>故事发动机→卷/章计划→单章正文→修订审查→连续性回灌，事实和伏笔验收后才进长期状态；拆书笔记可按章接入上下文，支持同人续写与跨书设定复用<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 中文 · Apache-2.0</sub>

- **[padwriter](https://github.com/cheyann4399/padwriter)** · ★ 98<br>节拍写作 skill：收件箱想法自动分级入 L1/L2/L3 设定库，按卷梗概→节拍索引→分镜卡→设定合规校验→初稿→AI 痕迹自检→洁本出章<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-04 · 中文</sub><br><sub>💡 仓库只含 skill；同名安卓语音写作 App 只有 APK（Releases），需向作者要测试 Key</sub>

- **[dsh-novel-writer](https://github.com/akira399/dsh-novel-writer)** · ★ 93<br>九阶段门禁（选题→设定→人设→大纲→分卷→细纲→正文→修订→完本），世界书关键词注入，事实账本与伏笔/时间线追踪，三层上下文包，附去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-06 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件，需 DSH 0.2.0-rc.2+；可导入导出 SillyTavern 世界书；另有黄金三章诊断、市场调研与模板复制</sub>

- **[long-novel-writer](https://github.com/jiaw-Zh/long-novel-writer)** · ★ 93<br>百万字长篇写作 skill：六层摘要冻结、实体档案、正典账本与 POV 知识边界，写后双 agent 校验，防止设定漂移<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-06-18 · 中文</sub><br><sub>💡 思路来自桌面项目 AI_NovelGenerator；作者另有早期版 jiaw-Zh/long-novel-generator</sub>

- **[chinese-webnovel-skills](https://github.com/tance-mang/chinese-webnovel-skills)** · ★ 84<br>按「平台+频道+题材」参数套用起点/番茄的爽点、打脸四拍和追读节奏，30+ 技能覆盖选题、大纲、金手指、扩写、追读诊断、连贯检查、去 AI 味<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-13 · 中文 · 33 个 skill · MIT</sub><br><sub>💡 另有接自有 API 的终端 CLI 版；含一个短剧剧本技能</sub>

- **[book-writer](https://github.com/tobyilee/book-writer)** · ★ 82<br>Claude Code 写书 harness：调研→计划审批→最多 4 写手并行写章，小说档案由连续性守护维护故事圣经、伏笔与节奏报告，验收后出 EPUB<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-11 · 韩文 · 15 个 skill · MIT</sub><br><sub>💡 韩语；默认是技术书档案，v1.3 起加入小说/实用书/随笔文体档案</sub>

- **[fanqie-novel-skill](https://github.com/304769384-png/fanqie-novel-skill)** · ★ 76<br>番茄长篇写作 skill：写前读状态文件，写后去 AI 味并跑 8 项最小审计（字数、因果链、战斗、对话占比、话疗、循环等）<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-03 · 中文</sub><br><sub>💡 工作流和状态文件（current_state、pending_hooks、character_matrix 等）沿用 Narcooo/inkos，另加番茄平台规则、商业审查和战斗/对话/话疗/循环审计</sub>

- **[DaisyWriter](https://github.com/ricky-theseus/DaisyWriter)** · ★ 75<br>在 webnovel-writer 的开书/规划/写章/审查流程上加扫榜、拆书、批量写、设定审查与去 AI 味，另有中短篇开书→写作→审查流水线<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-07-08 · 中文 · 23 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer（init/plan/write/review 等 8 个），另加扫榜、拆书、批量写、设定审查、去 AI 味、中短篇 5 个 skill 和封面生成；番茄发布取自 amm10090/fanqie-publisher-skill；另含技术博客/公众号/小红书技能</sub>

- **[dreampowers](https://github.com/skyfiredao/dreampowers)** · ★ 73<br>OpenCode 中文小说技能包：14 个 skill，覆盖构思、七维文风问卷、设定文件隔离、大纲伏笔、分场景写作、冷读与一致性审查<br><sub>方法：规划 · 设定 · 修订 · 风格</sub><br><sub>更新于 2026-07-02 · 中文 · 14 个 skill · GPL-3.0</sub><br><sub>💡 依赖 oh-my-openagent；成人场景技能为选装（install.sh --all 才装）</sub>

- **[chinese-longnovel-skill](https://github.com/xiaofeng-928/chinese-longnovel-skill)** · ★ 70<br>中文长篇网文工作流：扫榜开书、范文拆解与文风蒸馏、每 50 章分阶段细纲、事实锁与状态仓库、伏笔追踪、双审查自动修复<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-12 · 中文 · MIT</sub><br><sub>💡 校验脚本需 Python 3；自然化环节内置 Humanizer-zh 规则（已注明来源）</sub>

- **[book-os](https://github.com/forsonny/book-os)** · ★ 66<br>Novel-OS：写作标准（文风、类型指南、叙事技巧）、小说层（前提、计划、决策）、稿件层（大纲、人物档案、逐场景任务）三层上下文引导 AI 写<br><sub>方法：规划 · 理论 · 记忆 · 风格</sub><br><sub>更新于 2025-08-18 💤 · 英文 · MIT</sub>

- **[oh-story-claudecode](https://github.com/qin1473692580-ux/oh-story-claudecode)** · ★ 63<br>oh-story 派生版：扫榜拆文建模块库再写长短篇，正文落盘后过语言门、错别字门、AI 味与跨章连续性守卫，另加后台数据诊断、资料考证和发布<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-01 · 中文 · 18 个 skill · MIT</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode，2026-08 起独立演进、不同步上游；另加 story-data-analyze、story-research、story-explore、story-release-package、story-publish 五个 skill，以及错别字门禁、新题材包、TRAE/WorkBuddy 适配</sub>

- **[ai-fiction-writer](https://github.com/Wooooooooood/ai-fiction-writer)** · ★ 61<br>十个 skill 分管拆文、大纲、角色卡、知识库与世界地图；写前查逻辑矩阵、知情边界和冻结状态防穿帮，写后 9 维去 AI 味评分并四视角审稿<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-10 · 中文 · 10 个 skill · MIT</sub><br><sub>💡 README 只写了克隆仓库，需自行把「纯净版skill/」下各目录放进 agent 的 skills 目录</sub>

- **[The-Crucible-Writing-System-For-Claude](https://github.com/forsonny/The-Crucible-Writing-System-For-Claude)** · ★ 60<br>史诗奇幻长篇插件：问卷生成 9 份规划文档，按 36 拍 Crucible 结构（任务/内火/羁绊三线交织）出章纲，逐场景写作并对照规划防幻觉，每两章自动审稿<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2025-12-21 💤 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 作者自创的 Crucible 结构；Claude Code 插件市场安装；2025-12 后未更新，因结构理论独特而收；存在恶意仿冒仓库 pasteurmonga/The-Crucible-Writing-System-For-Claude，认准本仓库</sub>

- **[ultimate-novel-creation-skill](https://github.com/Fly143/ultimate-novel-creation-skill)** · ★ 50<br>立项→世界观人设→滚动章节规划→单章写作；每章强制跑写后流水线：更新圣经与摘要、金手指/时间/叙事线约束检查、读者审稿、朱雀检测对策，缺步不准写下一章<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 中文 · MIT</sub><br><sub>💡 须先把 system_prompt.md 配成宿主的系统提示词，流程才会被严格执行；写后流水线内置朱雀 AIGC 检测对策</sub>

- **[novel-writer](https://github.com/AI-Practical-Lab/novel-writer)** · ★ 46<br>状态机驱动的长篇 skill：构思→世界观→卷纲→章纲→逐章写，每步跑验证脚本卡关，配 YAML 角色卡、伏笔追踪、检查点回滚和修改经验积累<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-03-18 💤 · 中文 · 10 个 skill</sub><br><sub>💡 也适配 Trae、Antigravity</sub>

- **[craft-companion](https://github.com/qcx1919788736-collab/craft-companion)** · ★ 37<br>小说协作框架：从零或导入旧作建分层知识库，每章走章纲→初稿→执行层自查→评估层复核→仲裁层修订→终版，并回写知识库和检查点<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-07 💤 · 中文 · MIT</sub><br><sub>💡 附小说知识库 MCP 服务器和 CLI；也可在 Cherry Studio 里用</sub>

- **[bmad-book-builder](https://github.com/jblemee/bmad-book-builder)** · ★ 33<br>BMAD 小说模块：8 个 agent 与 17 个流程，每章后跑审稿→圣经更新→逐角色矛盾审计→主题→节奏审计链，用 TTR、句长等指标量化文风<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-01-25 💤 · 英文 · WTFPL</sub><br><sub>💡 需 BMAD 平台；主仓库在作者自建 Forgejo（git.ut0pia.org），GitHub 为 2026-01 快照</sub>

- **[novel-pro](https://github.com/lgz-star/novel-pro)** · ★ 33<br>规划→组稿→写作→观察→结算→审计→修订七角色流水线，事实总账+快照双层真相文件，旧稿逐章接管，未结算禁续写<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-28 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 Narcooo/inkos 的角色拆分与真相文件思路改写为 skill，新增存量接管与逐章结算（见 ACKNOWLEDGEMENTS.md），AGPL-3.0</sub>

- **[mimoCode-story](https://github.com/nihaoshi/mimoCode-story)** · ★ 32<br>MiMo Code 版网文技能包：扫榜、拆文、大纲、正文、去 AI 味、审稿 32 个技能，加 9 重质量门禁、6 类毒点检测和 6 平台对标评分<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-18 · 中文 · 47 个 skill</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode 二次开发，专为小米 MiMo Code 适配，Claude Code 用户用原版即可；一键安装是 curl \| bash</sub>

- **[novel-writer](https://github.com/sailoumili/novel-writer)** · ★ 31<br>统筹队长调度世界、剧情、人物、执笔、复核 5 个子代理：先定《叙事宪法》、世界白皮书和伏笔台账再动笔，复核按三色灯打回重写<br><sub>方法：设定 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-15 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness（DSH）预设插件，只能在 DSH 里用；章节按版本号存档，改稿不覆盖</sub>

- **[thriller](https://github.com/pajama-studio/thriller)** · ★ 31<br>悬疑推理技能包：按子类型走诡计/人物/结构先行路线，追踪人物知情状态与线索公平性（双读者验证、诺克斯检查），七维加权评分改稿，可再转成分支互动小说<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-03-30 💤 · 中文 · 4 个 skill · MIT</sub><br><sub>💡 融合 McKee、Truby、Sanderson 等 25+ 方法与计算叙事论文（对抗式悬念、动态认知逻辑）；含分镜模块与自我进化（GEP）流程；README 英文、技能正文中文；2026-03 后未更新，因方法独特而收</sub>

- **[novel-master](https://github.com/bbroot/novel-master)** · ★ 30<br>OpenClaw 长篇小说 skill：策划书、分卷大纲与细纲、三层伏笔追踪、角色状态机与节点压缩图谱、每章四维审计<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-14 · 中文 · MIT</sub><br><sub>💡 ClawHub 上装到的是 v1，v2 脚本需从 GitHub 获取</sub>

- **[novelops-skill](https://github.com/qiyan233/novelops-skill)** · ★ 30<br>长篇小说状态化流水线：truth files 记设定与角色认知，生成下一章工作包，LLM 起草，审计修订，状态回写，快照 diff<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-28 · 多语言 · MIT</sub><br><sub>💡 基于 Narcooo/inkos 的思路（truth files、审计-修订-状态回写），用纯 Python 标准库重写成不绑宿主的 skill；另加角色知情边界检查、可配置审计规则、快照/diff、同人与番外的 canon 处理。draft 默认调用本地 Ollama。SKILL.md 以英文为主</sub>

- **[vibe-noveling](https://github.com/TulanCN/vibe-noveling)** · ★ 27<br>Claude Code 网文插件：苏格拉底式设定讨论、救猫咪全书规划、雪花法事件卡、写后 AI 味检测、标记返修、知识图谱<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-06-02 · 中文 · 16 个 skill · MIT</sub><br><sub>💡 针对 GLM-5 调优，作者要求关闭思考模式；默认风格基线是男频爽文</sub>

- **[dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin)** · ★ 26<br>DSH 小说工作台：按卷章写正文，角色卡/世界书/关系图和节点式情节规划图作为 AI 可查可改的案头资料，按需检索后讨论、续写、改稿<br><sub>方法：规划 · 设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-11 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 DeepSeek Harness 插件，主要适配 DSH Windows 桌面版；可导入酒馆角色卡、世界书与提示词预设</sub>

- **[dsh-novel-writer](https://github.com/siweina/dsh-novel-writer)** · ★ 24<br>写前一次取齐承接口、细纲、人物卡、待回收伏笔、用语禁词等 16 项材料，写后按六维文笔基线对照原著自检，排出带行号的改稿待办<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 中文 · MIT</sub><br><sub>💡 DSH 插件，也可作 MCP 服务器；随包附 24MB 中文 ONNX 模型本地推理；工具本身不代写，正文由 agent 执笔</sub>

- **[openclaw-novel-writer-skill](https://github.com/alever520/openclaw-novel-writer-skill)** · ★ 24<br>OpenClaw 网文 skill：读全局大纲写七模块章纲并确认，结合写作指南和读者反馈列要点后写正文，15 项自检，读者反馈回写指南<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-04-02 💤 · 中文 · MIT</sub><br><sub>💡 每章自动提交 GitHub，需配置 GitHub Token</sub>

- **[speckit-preset-fiction-book-writing](https://github.com/adaumann/speckit-preset-fiction-book-writing)** · ★ 24<br>把 Spec Kit 规格驱动流程改成写小说：故事简报→结构计划（多种情节框架）→逐场景写作任务，26 个命令覆盖构思到投稿，支持多视角与文风样本<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-07-28 · 英文</sub><br><sub>💡 需 GitHub Spec Kit ≥0.5.0；文风有作者样本或 humanized-ai 两种模式；可导出 DOCX/EPUB/LaTeX</sub>

- **[xt-webnovel-writing](https://github.com/xiaotiewinner/xt-webnovel-writing)** · ★ 22<br>拆参考文本→立书→八步节奏剧情→爽点与四层文笔改写→结构 10 项加反 AI 味 25 项双路体检，命中回滚级硬门就退回重写；写前读、写后存磁盘记忆<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-30 · 中文</sub><br><sub>💡 方法论底本是一篇知乎文章，仓库内存档了全文；仓库没有许可证</sub>

- **[book-writer-skill](https://github.com/kshanxs/book-writer-skill)** · ★ 21<br>英文长篇写作：Story Forge 开书问答，Book Memory Bank 自动维护人物/世界/进度，含节奏蓝图、专项修订与简介/query letter<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-10 · 英文 · MIT</sub>

- **[webfiction-write](https://github.com/qingyabailu-git/webfiction-write)** · ★ 21<br>融合 oh-story 与 webnovel-writer：每章先定读者情绪再写，细纲不足即阻断，提交时写回状态，独立审查未完成标 unverified<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-31 · 中文 · 15 个 skill · MIT</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode 与 lingfengQAQ/webnovel-writer 融合，另加 fiction.py（初始化、章节提交、审查指标、导出）和正文检查脚本；需 Python 3.8+</sub>

- **[dsh-novel-forge](https://github.com/huangziyuan-general/dsh-novel-forge)** · ★ 19<br>代码硬约束长篇：九阶段状态机，细纲未批不许写章，事实账本冲突拒存，写前按预算组装简报，重复句段机审、六维去 AI 味扫描、场景契约防泄底<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件（20 个 novel_* 工具），另附 MCP 目录</sub>

- **[novel-flow-one-by-one](https://github.com/ZhangDongyang800/novel-flow-one-by-one)** · ★ 19<br>6 个协作 skill：脑暴→大纲→逐场景写作→六维审稿→设定同步，总控按状态路由，内置冷白描/系统爽文/怪诞悬疑三种文风<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-07-18 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 README 以 Trae 目录结构为例</sub>

- **[hermes-novel-generator](https://github.com/rwcrosk-arch/hermes-novel-generator)** · ★ 18<br>多智能体写长篇：编排者出大纲和状态 YAML，各角色 agent 互不可见地规划场景策略，叙事者编织成文，再经角色声线检查、设定审计和文风润色<br><sub>方法：记忆 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-04-23 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 为 Hermes Agent 写的 skill，依赖其 delegate_task 派子 agent；附进度看板、EPUB 打包和 diffusers 封面脚本；仓库带 .pyc</sub>

- **[long-novelist-skill](https://github.com/tianshiemo7/long-novelist-skill)** · ★ 17<br>百万字长篇中文小说：13 步配置问答、副本弧线三级大纲、角色状态档案、JSON 伏笔清单、跨会话恢复，附 11 个网文素材库<br><sub>方法：规划 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-06-01 · 中文 · MIT</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill 改写（仓库未注明），另加副本弧线规划、角色状态追踪、伏笔 JSON 清单和网文素材库</sub>

- **[novel-master](https://github.com/dashenbibi/novel-master)** · ★ 17<br>长篇网文协议式 skill：总览、角色档案、世界观、卷纲统一管理，章节按骨架→正文→润色→质检→同步推进，带一致性检查和伏笔追踪<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-03-07 💤 · 中文 · MIT</sub>

- **[novel-skills](https://github.com/PhosAQy/novel-skills)** · ★ 16<br>Claude Code 长篇插件：无大纲不写，先做百章级卷规划和章细纲，写完按 OOC、设定、逻辑、文风、重复五维加权打分决定采纳或人审，事实自动入知识库<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-01-19 💤 · 英文 · MIT</sub><br><sub>💡 只有一个 SKILL.md；README 中英双语</sub>

- **[writeAgent](https://github.com/Ddhjx-code/writeAgent)** · ★ 16<br>Claude Code 多 agent 写长篇：规划→写章→十维度审稿打分定去留→去 AI 味润色→归档故事圣经，逐章循环<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-18 · 中文 · 5 个 skill</sub>

- **[novel-writer-skills](https://github.com/Shine8592/novel-writer-skills)** · ★ 15<br>三个 OpenClaw skill：带情绪弧的章纲→调免费 API 分段批量写章→审计、校对、质量总监三段审查，每章复盘更新经验<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-04-06 💤 · 中文 · 3 个 skill</sub><br><sub>💡 调用 ModelScope、Fyra、Ph8 等免费档第三方 API；仓库无许可证</sub>

- **[silver-novel-skills](https://github.com/jialanhu0915/silver-novel-skills)** · ★ 15<br>男频/女频双系统网文写作：世界观/人物/情节三个框架 agent，按题材加载模板，12 项通用加男女频专项审稿 agent<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-07-07 · 中文 · MIT</sub>

- **[claude-novel-skill](https://github.com/mane23-ai/claude-novel-skill)** · ★ 14<br>长篇小说 skill：人物、物品、主题、地点、冲突节奏、读者体验六类追踪档案，配奇幻/推理/言情/恐怖类型预设，按章-场景指令逐场写作<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-04-07 💤 · 韩文</sub><br><sub>💡 韩语；含韩国网文平台连载与公募投稿流程；README 的克隆地址写成 looki/claude-novel-skill（该仓库不存在）</sub>

- **[novel-skill](https://github.com/mave99a/novel-skill)** · ★ 14<br>小说插件：先问题材设定，再跑 10–15 个 RPG 式抉择定剧情，生成含人物弧线、伏笔矩阵和章纲的计划，逐章写完后导出 EPUB<br><sub>方法：规划 · 风格 · 共创</sub><br><sub>更新于 2026-01-08 💤 · 多语言 · MIT</sub>

- **[opencreator-novel](https://github.com/xwcai999/opencreator-novel)** · ★ 13<br>中文小说 Codex 插件：读者契约与章节控制卡、待兑现承诺账本、确定性校验脚本、整书文学审稿与跨章结构相似度检查、封面<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-09-07 · 中文 · 3 个 skill · Apache-2.0</sub><br><sub>💡 wawa-* 两个子 skill 是非官方的蛙蛙写作投稿/统计适配，可不装</sub>

- **[wangwen-writing-skill-kit](https://github.com/hyi1233/wangwen-writing-skill-kit)** · ★ 13<br>网文方法论技能包：一个调度 skill 按需加载开篇、金手指、简介、伏笔、爽感、人物、节奏、去AI化、拆书等 13 个模块<br><sub>方法：理论 · 人物 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-24 · 中文</sub><br><sub>💡 内容蒸馏自 B 站 UP 主「网文徐掌柜」的拆书视频，含其原话金句</sub>

- **[writing-template-for-ai](https://github.com/hottweelz/writing-template-for-ai)** · ★ 13<br>整本书写作模板：先填问卷生成含人物、逐章大纲、文风指南和质量门槛的蓝图，再每会话写一章、做编辑审读并写交接记录，最后导出 EPUB/PDF<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-06-29 · 📝 提示词 · 英文 · MIT</sub><br><sub>💡 整理自作者已完成的成人文学小说《One Went Silent》的生产流程；附处理黑暗/成人题材的内容指引；也支持 GitHub Copilot</sub>

- **[long-novel-generator](https://github.com/jiaw-Zh/long-novel-generator)** · ★ 12<br>长篇小说 skill：一句话创意扩成 3000 字故事核，建角色动力图谱和世界观状态文件，每次只规划 3-5 章，写完更新角色状态与全书摘要<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-05-07 · 中文</sub><br><sub>💡 基于 YILING0013/AI_NovelGenerator，用 Gemini 把原项目流程蒸馏成 SKILL</sub>

- **[novel-assistant-skill](https://github.com/duiniwukenaihe/novel-assistant-skill)** · ★ 12<br>单入口网文助手：短篇/长篇写作、审阅、拆文、扫榜、导入、去AI味，带任务断点续写、按步召回记忆、改纲影响链和章节扩容迁移<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-08-10 · 中文 · 16 个 skill · MIT</sub><br><sub>💡 基于 worldwonderer/oh-story-claudecode（现 zenstory-ai/oh-story-claudecode），另加单入口路由、工作流断点、记忆召回、影响链与健康门；作者称短篇已稳定、长篇仍在打磨</sub>

- **[plotrail](https://github.com/waylean/plotrail)** · ★ 12<br>长篇工作流两件套：plotrail 建 canon、章节合同、写后连续性审稿和作者改稿偏好；plotrail-intake 诊断精修已有旧稿再交接续写<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-21 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 skill 正文为英文，README 与示例为中文网文</sub>

- **[webnovel-writer-hermes](https://github.com/starMagic/webnovel-writer-hermes)** · ★ 12<br>Hermes Agent 版网文系统：市场扫描与对标拆书定方向，卷/章合同约束写作，context/审稿/数据子 Agent 分工，三级记忆与伏笔债务预算<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-05 · 中文 · 13 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer；需 Hermes Agent，推荐配 DeerFlow 跑子 Agent</sub>

- **[Chinese-WebNovel-Master](https://github.com/TianHengZhuang/Chinese-WebNovel-Master)** · ★ 11<br>中文网文商业化工作流：策划→架构→写作→编辑→发布五角色，配 12 个平台读者偏好、类型套路、钩子与留存框架、故事圣经和连续性检查<br><sub>方法：规划 · 理论 · 记忆 · 多智能体</sub><br><sub>更新于 2026-10-14 · 📝 提示词 · 英文 · MIT</sub><br><sub>💡 SKILL.md 无标准 frontmatter，按角色手动使用；提示词为英文</sub>

- **[dsh-novel-solo](https://github.com/Tkingxiao/dsh-novel-solo)** · ★ 11<br>面向本地量化小模型的写作预设：叙事方法→世界观→名词索引→大纲→目录→人物档案→逐章写，每章七维红黄绿审稿含 AI 腔检查，最后整书复审<br><sub>方法：规划 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-03 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件；精简工具表、禁用 JSON 输出以适配量化模型</sub>

- **[scriveno](https://github.com/hannsxpeter/scriveno)** · ★ 11<br>装进编程 agent 的长篇写作命令集：先建作者 Voice DNA，drafter agent 逐单元用作者声音起草，再做编辑审读、连续性与声音检查，后接出版<br><sub>方法：规划 · 设定 · 修订 · 风格</sub><br><sub>更新于 2026-09-27 · 英文 · MIT</sub><br><sub>💡 npm 包 scriveno；支持 50 种作品类型，不限虚构（也覆盖技术文档、出版、翻译）</sub>

- **[wangwenwrite-skill](https://github.com/Thatgfsj-easyRep/wangwenwrite-skill)** · ★ 11<br>男频系统流网文单文件 skill：黄金三章、爽点节奏公式、系统设定法则、反 AI 味清单、书名公式与平台差异化<br><sub>方法：规划 · 理论 · 设定 · 去 AI 味</sub><br><sub>更新于 2026-05-04 · 中文 · Apache-2.0</sub>

- **[claude-novel-workflow](https://github.com/MintoTsukino/claude-novel-workflow)** · ★ 10<br>canon 驱动的长篇流程：先建角色/世界/术语/时间线/文风/禁用模式文件，多 agent 批量起草并三层审稿，附作者原创 JET 读者情绪框架<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-16 · 📝 提示词 · 多语言</sub><br><sub>💡 日本轻小说作者的工作快照，声明不再维护；附真实连载前 10 话样例（日语），模板与文档为英文</sub>

- **[DSH-Novelist](https://github.com/KurohaneKaoruko/DSH-Novelist)** · ★ 10<br>12 个方法论 skill 和 6 个文风 skill 按需加载，写前组装前十章结尾/人物卡/伏笔/时间线简报，写后跑 25 项正文 lint 与名词核对<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-10 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 预设；skills 本体在子模块 KurohaneKaoruko/Novelist-Skills；附玄幻/悬疑/甜宠工程模板与可选 WebUI</sub>

- **[goink-skills](https://github.com/sigpanic/goink-skills)** · ★ 10<br>Goink 写作 App 的社区技能库：每条 Markdown 技能注入系统提示，现有情绪弧线及重生复仇、末世先知、逐界登顶、奇案升格等网文套路模板<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-09-06 · 📝 提示词 · 中文 · CC-BY-SA-4.0</sub><br><sub>💡 主项目为 sigpanic/goink，App 内可一键安装；目前 6 条技能；CC BY-SA 4.0</sub>

- **[human-novel-writer](https://github.com/huahuakandaima/human-novel-writer)** · ★ 10<br>长篇网文全流程：项目骨架与三总控文件、黄金三章合同、角色入场门禁、每章 8 步循环、拆文选题审稿封面，去AI味双门禁脚本<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-07 · 中文 · MIT</sub><br><sub>💡 整合 oh-story-claudecode、KKKKhazix/human-writing、writing-dna-skill 与贴吧《小说ai行文规范》，另加角色门禁、黄金三章合同和密度检查脚本；朱雀在线检测需腾讯云 API Key，封面依赖 foxtrai 生图 skill</sub>

- **[novel-writer-english](https://github.com/JeroTan/novel-writer-english)** · ★ 10<br>英文版八步写作流程：原则→规格→澄清→章节规划→任务→起草→编辑→审阅，另带只读故事查询 MCP 和场景草稿、编辑、审稿流程<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-09 · 英文 · 28 个 skill · MIT</sub><br><sub>💡 基于 wordflowlab/novel-writer-skills 翻译改写，新增故事查询 MCP、编辑/审稿流程、超长文件拆分和漫画提示词流程</sub>

- **[novel-writing-skill](https://github.com/cnskycn/novel-writing-skill)** · ★ 10<br>长篇连载单文件提示词：大纲 6 步、章节 7 步、人物三锚点、伏笔 P1-P3 分级、六维质检，附追踪与记忆文件模板<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-05-23 · 📝 提示词 · 中文</sub><br><sub>💡 单个 .md 文件，README 按 Trae .trae/skills/ 安装；风格设定偏「孔二狗式」都市江湖叙事</sub>

- **[deepseek-harness-novel-studio](https://github.com/qinpeizhan77/deepseek-harness-novel-studio)** · ★ 9<br>DeepSeek Harness 小说插件：大纲、场景契约、人物状态、伏笔与禁写规则存成项目数据每轮注入，附前提锦标赛、样章验证、状态审查等 skill<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-08-30 · 中文 · 5 个 skill · MIT</sub><br><sub>💡 需 DeepSeek Harness（dsh）作宿主；AI 提出的变更先进待确认清单</sub>

- **[human-like-novel-workbuddy-skill](https://github.com/LittleLollipop/human-like-novel-workbuddy-skill)** · ★ 9<br>写章节计划时从词林、句式、修辞、节奏、叙事手法图库正向注入人类常用素材，按卷→段→章→节逐节写，设定存图库写前取用、写后校验<br><sub>方法：规划 · 理论 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-08-30 · 中文</sub><br><sub>💡 核心是用正向注入代替禁词表来去 AI 味；图数据库模式依赖约 30MB 的 axolotl 图库，推荐 macOS；附错误案例库和机检脚本；仓库无许可证</sub>

- **[novel-creation-skill](https://github.com/skye-z/novel-creation-skill)** · ★ 9<br>中文长篇/同人 skill：提取原著资料、头脑风暴定设定和人物卡，按题材模板和三/五/六幕结构推进，读者欲望驱动、桥接情节过渡，带自检和上下文管理<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-04-08 💤 · 中文 · MIT</sub><br><sub>💡 为 Trae SOLO Web 优化，需智能体有联网搜索和内容提取能力；对同人支持最好</sub>

- **[novel-skills](https://github.com/vicalloy/novel-skills)** · ★ 9<br>长篇小说 skill：用树形 Markdown 摘要（总纲加章节摘要、角色小传、世界观设定）承载剧情，每章写完强制更新相关摘要，写前一次性加载<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-12 💤 · 中文</sub><br><sub>💡 与作者的 Sequoia 项目深度绑定（摘要加载工具在那边）；附一部写到一半的 AI 小说作样例</sub>

- **[novel-writer-skill](https://github.com/liuxiao20051106-prog/novel-writer-skill)** · ★ 9<br>中英双语小说写作 skill：构思、人设、章纲、逐章写作与章节衔接检查、去 AI 味，附草稿量化体检脚本和 11 套追踪模板<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-17 · 多语言 · 2 个 skill · MIT</sub><br><sub>💡 另附 ChatGPT、DeepSeek、Gemini 等网页端的系统提示词用法</sub>

- **[dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft)** · ★ 8<br>口味校准：作者对候选稿逐段点赞/点踩，模型提炼成几百字节偏好档案注入写稿；每章先列多种场景决策方向再分篇写，批注只改被标段落<br><sub>方法：规划 · 修订 · 风格 · 共创</sub><br><sub>更新于 2026-09-30 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 DeepSeek Harness 插件，需 Node 22；写稿上下文只放规律、不放已写正文</sub>

- **[dsh-novel-writing](https://github.com/peterwangze/dsh-novel-writing)** · ★ 8<br>29 个 skill 的网文流水线：协调者统筹选题、大纲、细纲，按看护包生成正文并九维审查，代码门禁拒存离纲章节，再按发布数据回调写作方向<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-16 · 中文 · 29 个 skill</sub><br><sub>💡 基于同作者 peterwangze/claude-writing-workflow 迁移到 DeepSeek Harness；默认人类主笔、AI 出草稿参考，高 AI 参与度会阻断上架；仓库未声明许可证</sub>

- **[novel-creation-omnibus](https://github.com/limingnanyue/novel-creation-omnibus)** · ★ 8<br>55 个按需加载模块的写作 skill：类型模板（规则怪谈、番茄爆文等）、开篇钩子、L1–L4 去 AI 门禁、五专家并行审计与 11 维评分，带技能自进化循环<br><sub>方法：理论 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-25 · 中文 · MIT</sub><br><sub>💡 覆盖长篇网文到短篇；模块与自进化指标数量庞大、术语堆砌，实际效果需自测</sub>

- **[snowflake-writer](https://github.com/vagabondshun/snowflake-writer)** · ★ 8<br>雪花写作法 10 步 skill：一句话→五句结构→人物表→一页梗概→四页大纲→场景表→场景结构→成文，分给 5 个 agent 人格，附文风 RAG<br><sub>方法：规划 · 人物 · 风格</sub><br><sub>更新于 2025-12-18 💤 · 英文 · 3 个 skill · MIT</sub>

- **[ty-xiaoshuo-skill](https://github.com/danieltao118/ty-xiaoshuo-skill)** · ★ 8<br>网文八道工序 skill：创作前检查→细纲→正文→四轨质检→跨章节奏审→更新设定库→前情摘要→阶段回顾，五维评分不达标重写，情节类型轮换防公式化<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-03-28 💤 · 中文</sub><br><sub>💡 质检含去 AI 味；附番茄平台策略和修仙、萌娃题材模板；README 写 MIT 但无许可证文件</sub>

- **[xiaoshuo-studio](https://github.com/Zhao73/xiaoshuo-studio)** · ★ 8<br>长篇工作台+skill 包：问答建书向导生成 canon 与首章 brief，导入参考小说做风格卡，逐章规划→起草→连续性检查→回写 canon→去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-01 · 中文 · 20 个 skill · MIT</sub><br><sub>💡 Web 工作台依赖本地已登录的 Codex CLI；风格学习强调学技法、不克隆作者声线</sub>

- **[huxiuzhi-novel-agent](https://github.com/huxiuzh-ops/huxiuzhi-novel-agent)** · ★ 7<br>主管→规划→写手→编辑角色流写长篇，角色/章节/伏笔/地点/时间线建结构化索引，伏笔登记→逾期警告→回收验证，关键决策交人确认<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-11 💤 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 核心规则在平台无关的 AGENT.md，SKILL.md / CLAUDE.md 只是入口</sub>

- **[Novel-framework](https://github.com/bafeite59/Novel-framework)** · ★ 7<br>Claude Code skill：引导逐模块搭建人物、时间轴、三幕情节节点、情绪起伏、浅/深伏笔、分层结局、风格与内容增减，输出 Mermaid 思维导图框架<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-07-19 · 中文 · MIT</sub><br><sub>💡 只产出故事框架思维导图，不写正文</sub>

- **[NovelGenerator](https://github.com/Dylin-code/NovelGenerator)** · ★ 7<br>两段式 skill：资深编辑七段访谈产出 bible（含三幕结构、人物 want/need），再出大纲，每章跑写手→评论家→修订者子代理最多两轮<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-28 · 中文 · 2 个 skill</sub><br><sub>💡 写手和修订者默认走本地 LM Studio，评论家用 Claude；繁体中文</sub>

- **[novella-xl-15](https://github.com/paradroidlabs/novella-xl-15)** · ★ 7<br>长篇系统提示词：每章先做超详细规划、写完做复盘指导下一章，每章约 8000 字；原 Wordware 流程为标题→改情节→择优→15 章故事线→循环写章<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-08-06 💤 · 📝 提示词 · 英文</sub><br><sub>💡 已停止维护（作者标 deprecated）；Wordware 上的 wordapp 本体不在仓库里，仓库只有系统提示词、输出和评价样例；原流程用 ElevenLabs 生成章节音频；无许可证</sub>

- **[agent-novel](https://github.com/RTY798/agent-novel)** · ★ 6<br>每章先填章节卡（目标·阻力·选择·后果），按 HOT/WARM/COLD 分层加载事实，出节拍由作者定关键选择再写首稿，过事实门禁后更新状态库与章节日志<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-07-24 · 中文 · MIT</sub><br><sub>💡 附零依赖 Node 脚本校验 story-state.json 和章节卡；风格项只作观察，不当退稿依据</sub>

- **[Claude-Code-Novel-Writing](https://github.com/f43a9a/Claude-Code-Novel-Writing)** · ★ 6<br>日语 Claude Code 命令集：企划→世界观→角色→结构→验证→分镜→执笔→审阅八阶段，按作者 MBTI×角色 MBTI×类型×文体×读者层理论库生成<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2025-07-08 💤 · 日文 · MIT</sub><br><sub>💡 2025-07 后未更新；附 AI 作家作品展示站</sub>

- **[claude-novel-skills](https://github.com/fnb666888/claude-novel-skills)** · ★ 6<br>小说 skill：角色表现=个性×情绪×动作×语言、章节=事件×风格×氛围×角色的去耦合组合法，以单一核心体验极端化为目标，配六关去 AI 味<br><sub>方法：理论 · 人物 · 去 AI 味</sub><br><sub>更新于 2026-06-26 · 中文 · MIT</sub>

- **[fanqie-novels-skills](https://github.com/mhkz/fanqie-novels-skills)** · ★ 6<br>番茄爽文版 Claude Code 命令：沿用宪法→规格→澄清→计划→任务→写作→分析七步，加金手指/打脸/爽点节奏五问澄清和敏感词、爽点密度检查<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-02-12 💤 · 中文 · 12 个 skill · MIT</sub><br><sub>💡 基于 wordflowlab/novel-writer；另含番茄榜单抓取和分类建议</sub>

- **[inkcraft-writing-skills](https://github.com/Fei2411/inkcraft-writing-skills)** · ★ 6<br>13 种网文体裁的写作方法库，每个体裁分结构、前三章、场景写法、成文规范、自检清单五份，带体裁自动分流 skill<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-09-12 · 中文 · 14 个 skill</sub><br><sub>💡 CC BY 4.0；由商业产品 InkCraft 的写作材料提炼，不含软件本身</sub>

- **[novel-webfiction](https://github.com/zlbigger/novel-webfiction)** · ★ 6<br>OpenClaw 网文连载 skill：开书问 4 个问题建档，每章先读设定、大纲和最近 3 章再写，正文按章存进 Obsidian<br><sub>方法：规划 · 理论 · 记忆</sub><br><sub>更新于 2026-06-28 · 中文 · MIT</sub><br><sub>💡 单文件、规则较简单，适合轻量连载</sub>

- **[novel-writer-workflow](https://github.com/GonsonInter/novel-writer-workflow)** · ★ 6<br>两阶段小说 skill：构思出宪法后搭大纲和钩子矩阵，按场景走 8 步 SOP，每个场景两轮独立 agent 审到无 P0/P1，脚本扫硬约束，维护跨章四表<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-04-23 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 命令沿用 novel-writer 七步法；作者称用它写完一部约 13 万字的长篇</sub>

- **[novelist](https://github.com/comfuture/novelist)** · ★ 6<br>长篇小说插件：设定、人物、素材、情节、大纲存成带 ID 的 Markdown，按章组装有界上下文，追踪读者已知信息和揭示时机，按类型套路写并独立审阅<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-07-31 · 英文 · 9 个 skill · MIT</sub><br><sub>💡 内置武侠、科幻、时间循环、推理、情感等类型策略；也支持 Antigravity CLI</sub>

- **[novelist.skills](https://github.com/Ink-dark/novelist.skills)** · ★ 6<br>小说 skill：澄清需求后生成梗概、大纲、人物、世界与文风文件，续写守「五零」纪律（零判断、零心理直述等），写完自动七维自检并给出净化稿<br><sub>方法：规划 · 设定 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-07 · 中文 · 2 个 skill</sub><br><sub>💡 能把已有正文逆向解析成设定文件</sub>

- **[open-novel-fanqie](https://github.com/kongxcer555/open-novel-fanqie)** · ★ 6<br>番茄网文长篇流水线 12 个 skill：拆对标书出套路 JSON、换壳选切入点、书名简介与事件、大纲人物设定、细纲、正文、审稿、滚动摘要<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-12 · 中文 · 11 个 skill · MIT</sub><br><sub>💡 原仓库 mosonlab/open-novel-fanqie 已失效，这里是转存；README 里的 git clone 地址要换成 kongxcer555/open-novel-fanqie。脚本依赖 bun，p7 去 AI 味尚未完成</sub>

- **[web-novel-master](https://github.com/tinylion1024/web-novel-master)** · ★ 6<br>网文创作工作流：快速、专业、工业、一次生成四种模式，含 11 个赛道的作者文风卡、套路库、平台定位包和项目初始化与校验脚本<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-07-20 · 中文 · MIT</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill（情节结构、人物塑造、对话、扩写等指南沿用原版），另加四种创作模式、作者文风卡、平台定位包、市场数据和项目管理脚本</sub>

- **[book-writer-mcp](https://github.com/arupmaity1/book-writer-mcp)** · ★ 5<br>写书 MCP 工具集：故事圣经记录人物、场景和情节线，文风指南约束语气、视角和时态，连续性检查找矛盾，逐章写入并导出 docx<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-04-05 💤 · 英文</sub><br><sub>💡 小说和非虚构通用；附封面规格和 KDP 导出</sub>

- **[chinese-novelist-skill](https://github.com/lvyu-cmd/chinese-novelist-skill)** · ★ 5<br>中文长篇小说 skill：五项输入自动生成设定，逐章或子 Agent 并行写作，三层记忆、七维自动校验、章节评分和三级修订<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-17 · 中文</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill，另加 SQLite 持久化、三层记忆、修订模式和 8 个校验/评分脚本；README 里的 clone 地址写成 chinese-novelist-skill-master，要换成本仓库</sub>

- **[claude-novel-writer](https://github.com/zhiliyouxian/claude-novel-writer)** · ★ 5<br>Claude Code 插件：分析参考小说→策划蓝图（选题、世界观、人物、章纲）过审核门→章节写作与审核修订循环→导出，按类型加载知识包<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2025-12-28 💤 · 多语言 · 9 个 skill · MIT</sub><br><sub>💡 8 个 agent、9 个 skill；发布环节还有有声书优化和视频组装；目前只有中文网文知识包</sub>

- **[dsh-novel](https://github.com/ddedook/dsh-novel)** · ★ 5<br>一个工作区一本书：人物/世界/等级/时间线/大纲/章节存进本地 PGlite canon，先开书设定，再用斜杠命令分步写大纲和章节，附题材模板与文风<br><sub>方法：规划 · 设定 · 记忆 · 风格</sub><br><sub>更新于 2026-08-18 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件</sub>

- **[dsh-novel](https://github.com/wbb316/dsh-novel)** · ★ 5<br>开书向导填设定、主角、世界观和三幕大纲，大纲拆成按卷分组的情节点挂到章节，写下一章时自动带上未写情节点、卷纲领和角色关系<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2026-10-06 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件，作者自述练手项目；需 DSH 0.2.0-rc.1+</sub>

- **[fanqie-xiaoshuo-skill](https://github.com/soultt/fanqie-xiaoshuo-skill)** · ★ 5<br>番茄风网文 11 个 skill：设定、总纲与章纲的设计和审查、正文写作和审查、签约潜力评估、日更工作流<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-06-26 · 中文 · 11 个 skill</sub><br><sub>💡 README 安装说明简略；仓库描述里的「包签约」是宣传语，实际是签约评估模板</sub>

- **[general-novel-skill](https://github.com/xiaoyuCR7/general-novel-skill)** · ★ 5<br>长篇网文 skill：每章正文与摘要、角色状态、伏笔、时间线按事务一起提交，7 道去 AI 味闸口，34 题材与多平台规则按需加载<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-13 · 中文 · MIT</sub><br><sub>💡 体量大（47 个脚本、118 份参考、24 个 MCP 工具），附五章示例书和去 AI 味前后对照</sub>

- **[light-novel-creator](https://github.com/Nya-Nya-Hoshino/light-novel-creator)** · ★ 5<br>轻小说创作 skill：先按指定作品/作者建风格档案，维护双区角色卡（固定属性+每章更新）与时间线双写校验，每章写完做 6 维自审<br><sub>方法：人物 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-23 · 中文</sub><br><sub>💡 为 Reasonix 平台编写；ACGN 百科抓取依赖另一个未随仓库提供的 skill；含让 agent 自行搜索安装外部 skill/MCP 的指令，使用前留意</sub>

- **[novel-craft](https://github.com/dongyanyuxuana/novel-craft)** · ★ 5<br>通用小说 skill：主控加 7 个子代理，访谈立项、资料拆分、逐章写作、逐段 17 维审查、修订发布，附 34 位作家技法库<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-06 · 中文 · MIT</sub><br><sub>💡 含成人向场景参考文档，按受众分级启用</sub>

- **[novel-engine](https://github.com/jiangying3222880/novel-engine)** · ★ 5<br>网文写作引擎：拆对标书建素材池，细纲、正文、检验打回、落库四段流水线，管长篇状态，另有短故事模式和 BM25 检索<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 中文 · 12 个 skill</sub><br><sub>💡 门禁、检索、同步脚本需 Python，不装时降级为手动校验；生成的「叙事总览」目录可作为 Obsidian 库查看</sub>

- **[novel-project-strategy](https://github.com/wgwtest/novel-project-strategy)** · ★ 5<br>Codex 长篇项目管理 skill：定义加载顺序、章节状态与同步规则，新会话不读全文也能恢复项目，防止大纲、设定、正文互相漂移<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-18 · 英文 · MIT</sub>

- **[novel-writer-agent](https://github.com/ZBA-z/novel-writer-agent)** · ★ 5<br>番茄网文作家人格 skill：大纲→细纲→正文→打磨→审查，从上传的爆款 txt 蒸馏写法，每章按朱雀检测降 AI 味，每 30 章批量审查<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-11 · 中文</sub><br><sub>💡 主打通过朱雀 AI 检测；附网文词库和对爆款作品的蒸馏库</sub>

- **[NovelClaw](https://github.com/7a-z/NovelClaw)** · ★ 5<br>OpenClaw 网文 skill：先定世界观、人物和 5–10 章大纲，按战斗/情感/悬疑场景切换文风，写完用脚本扫 AI 腔禁用词并自动扩充词库<br><sub>方法：规划 · 风格 · 去 AI 味 · 共创</sub><br><sub>更新于 2026-05-02 · 中文</sub><br><sub>💡 与 iLearn-Lab/NovelClaw 同名但无关；分段写作时会停下来征求反馈</sub>

- **[NovelFlow](https://github.com/DongxUETAFFY/NovelFlow)** · ★ 5<br>长篇小说 skill：用文件系统当长期记忆，按章节远近做金字塔式上下文压缩，每章提交结构化 delta，分自由草稿、标准、生产锁定、断书续完等模式<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-05-20 · 中文 · 2 个 skill · MIT</sub>

- **[novelist-skill](https://github.com/chanceline-max/novelist-skill)** · ★ 5<br>Codex 中文小说 skill：从灵感到卷纲章纲、正文续写与改稿，维护人物、世界观、伏笔、时间线和章节总结文件<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-23 · 中文 · MIT</sub>

- **[Soundingboard](https://github.com/richardelder2/Soundingboard)** · ★ 5<br>以场景为单位的小说工作区：38 个 skill 覆盖情节追问、人物 DNA、对白、感官扩写等；连续性账本追踪设定，修改建议用方括号隔离不动原文<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-09-18 · 英文 · 19 个 skill · MIT</sub><br><sub>💡 默认作者执笔，AI 生成正文要显式进入 Generative 模式</sub>

- **[story-foundry](https://github.com/mmunro3318/story-foundry)** · ★ 5<br>Claude Code 小说工作区：捕获→提炼→生产，子代理按 Truby、Swain 等理论包出大纲和场景卡，起草后批评、出修复单再修订<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2025-09-20 💤 · 英文</sub><br><sub>💡 作者自述是上下文工程实验项目；仓库无许可证</sub>

- **[web-novel-writing-skill](https://github.com/XINGANLIU/web-novel-writing-skill)** · ★ 5<br>网文 10 阶段流水线：灵感、世界观、人物、总纲、卷纲、章纲、黄金三章、正文、质检、状态同步，含人物漂移和反派降智检查<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-06-11 · 中文 · MIT</sub>

- **[novel-craft](https://github.com/chaserr/novel-craft)** · ★ 4<br>Claude Code 长篇写作与审稿插件：5 个 skill + 12 个 agent，用 RTK.md 定题材风格，管大纲、前情、伏笔、人物档案和逐章审稿<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-18 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 作者另有同流程的桌面版 novel-craft-studio</sub>

- **[Novelist-Skills](https://github.com/KurohaneKaoruko/Novelist-Skills)** · ★ 2<br>18 个 SKILL：工程初始化、人物/世界观/文风卡建档、情节节奏与章节细纲、行文铁律、连续性检查、改稿，加词级/句式级去 AI 味特征库和 6 种类型文风<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-10 · 中文 · 18 个 skill · MIT</sub>

- **[clark-typer](https://github.com/niyongsheng/clark-typer)** · ★ 0<br>硬科幻长篇 skill 流程：选题→设定（科学三层标注）→人物→大纲，写作/文学+科学审稿/润色/读者盲读循环，可回溯状态机加 sqlite-vec 一致性扫描<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-08-24 · 中文 · 20 个 skill</sub><br><sub>💡 仓库根目录同时放着作者自己的创作产物（0-角色档案…7-正文），/typer-init 可重置；支持导入外部作品续写/二创；附 Web 工作台；无许可证</sub>

#### 框架 · 应用（207）

- 🌟 **[inkos](https://github.com/Narcooo/inkos)** · ★ 10.3k<br>统一 harness 管长短篇、剧本、同人仿写、互动影游；长篇用 truth files 记设定、伏笔和角色状态，每章写后审计→修订→状态回写<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-10 · ⚙️ 框架 · 多语言 · 21 个 skill · AGPL-3.0</sub>

- 🌟 **[AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator)** · ★ 6.2k<br>本地部署的长篇小说生成应用：用雪花法从核心创意逐级展开卷、弧、场景、章纲到正文，管理角色/势力/物品/伏笔状态，AI 流程可在画布上改<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 main 分支已经重写（Next.js + FastAPI + MongoDB），旧版留在 old 分支，两版数据不兼容</sub>

- 🌟 **[autonovel](https://github.com/NousResearch/autonovel)** · ★ 1.6k<br>仿 autoresearch 的改—评—留弃循环：设定、人物、大纲、文风、canon 打分过阈值，逐章起草评分重写，再经对抗删改、读者评审团和 Opus 审稿<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-03-20 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 无 License；附 CRAFT.md / ANTI-SLOP.md 等写作原则文档；示例成书在 autonovel/bells 分支；导出阶段另有排版、插画和 ElevenLabs 有声书</sub>

- 🌟 **[neuro-book](https://github.com/notnotype/neuro-book)** · ★ 744<br>长篇写作 IDE：时间线切面事件溯源推算世界状态，伏笔承诺账本，leader/writer 等多 agent 分工写章，llmlint 规则查 AI 味<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · 28 个 skill · AGPL-3.0</sub><br><sub>💡 AGPL-3.0；当前分支按 v2 方案重建中，可用版本在 master；去 AI 味 lint 另有独立仓库 notnotype/llmlint</sub>

- **[AI-Novel-Writing-Assistant](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant)** · ★ 3.2k<br>长篇小说创作工作台：自动导演从灵感推进到开书、世界观、角色、章节规划、正文与检查，含拆书、写法引擎、反 AI 规则、RAG 知识库和短篇流程<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 2 个 skill</sub><br><sub>💡 有 Windows 桌面版，也能从源码部署；能把已写章节延展成漫画分镜和短剧素材。作者另有 ani-book-skill（已收）</sub>

- **[MuMuAINovel](https://github.com/xiamuceer-j/MuMuAINovel)** · ★ 3.2k<br>小说创作 Web 应用：向导生成大纲、角色、世界观和职业等级体系，逐章生成并按分析重写，带伏笔追踪、拆书、自定义文风和可编辑 Prompt 模板<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 中文 · 7 个 skill · GPL-3.0</sub><br><sub>💡 Docker + PostgreSQL 部署；README 有大量 API 中转站赞助广告；内置 story-* skill 搬自 oh-story-claudecode</sub>

- **[gpt-author](https://github.com/mshumer/gpt-author)** · ★ 2.5k<br>先生成多个情节并选出最佳再改进，写出指定章数的故事线并再改一轮，逐章参考前文写作，最后生成封面打包 EPUB<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2024-04-03 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 2023 年的早期代表作，Jupyter/Colab 笔记本；另有更简化的 Claude 3 版本</sub>

- **[ainovel-cli](https://github.com/voocel/ainovel-cli)** · ★ 2.2k<br>全自动长篇小说生成 CLI：确定性引擎调度 Architect/Writer/Editor 三个代理，卷弧滚动规划、七维评审、步骤级断点恢复，可随时插入修改意见<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-15 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 主打一句话全自动成书；想逐章把关可开 /review on。可在 TUI 里看着写，也可 headless 跑在服务器上</sub>

- **[arboris-novel](https://github.com/t59688/arboris-novel)** · ★ 1.6k<br>写作网页应用：角色/地点/派系设定库，AI 把灵感整理成主线蓝图和章节纲要，按纲要生成章节并抽取摘要供后文使用，支持一次多版本择优<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-02-25 💤 · 🧩 应用 · 中文</sub><br><sub>💡 需 OpenAI 兼容 API；想用命令行加编辑器可搭配 t59688/novel-kit；仓库无许可证</sub>

- **[91Writing](https://github.com/ponysb/91Writing)** · ★ 1.6k<br>前端小说创作台：按类型模板建书，AI 生成大纲与章节、续写和分类润色，世界观模板化管理并做一致性检查，提示词库带变量可自定义<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2025-10-14 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 2025-10 后未更新，按 ≥100★ 保留；需自配 OpenAI 兼容 API，内置提示词仅为演示</sub>

- **[AI-Novel-Writer](https://github.com/EthanYoQ/AI-Novel-Writer)** · ★ 1.6k<br>桌面长篇写作软件：前提、角色、世界观、章节蓝图、草稿、审稿、修稿、定稿逐段推进，可按阶段绑定写作 Skill，支持本地与在线模型<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 提供 Windows/macOS 桌面版；仓库里另有 DeepSeek Harness 插件预览版，已冻结，作者说它的能力不到桌面版一成</sub>

- **[NovelForge](https://github.com/RhythmicWave/NovelForge)** · ★ 1.2k<br>卡片式长篇创作工具：按 JSON Schema 结构化生成设定、角色、大纲卡片，用 @DSL 注入上下文、知识图谱保一致，可编排代码式工作流（含拆书）<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文 · AGPL-3.0</sub>

- **[Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT)** · ★ 1.2k<br>长篇小说 Agent：章节→剧情→正文逐级扩写并多线程并行；可导入已有小说拆书得剧情纲要，按意见检索片段改写并同步更新纲要<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2025-11-05 💤 · 🧩 应用 · 中文</sub><br><sub>💡 2025-11 后未更新（1247★）；附天蚕土豆风格等提示词；Docker 部署</sub>

- **[OpenFic](https://github.com/syrizelink/OpenFic)** · ★ 1.2k<br>人机协同的小说写作工具：写作编辑器加可自定义的 Prompt/Agent/工作流，维护设定、角色与伏笔，向量检索百万字项目，支持 Docker/pip/桌面版<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 定位是协同写作，不做一键成书。README 里有 API 中转商的推广链接</sub>

- **[AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels)** · ★ 966<br>种子→根合同→里程碑链→逐章细纲→正文，每层发散 3 个候选由程序选优；评审须引原句证据、由程序扣分并自动返修，也能写短剧和影视剧本<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-14 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 带 Web UI 和守护进程长跑；内容类型由 packs 声明，可扩展；需配置至少一个模型网关</sub>

- **[novel-writer](https://github.com/wordflowlab/novel-writer)** · ★ 959<br>参照 Spec-Kit 的七步法：宪法→规格→澄清→计划→任务→写作→分析，以斜杠命令装进多种 AI 助手，配情节/时间线/关系/世界观追踪做一致性检查<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2025-10-26 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 npm 包 novel-writer-cn，novel init 生成项目和命令；插件含真实人声、风格模仿等</sub>

- **[denova](https://github.com/alfredxw/denova)** · ★ 929<br>小说写作与 AI 文字冒险一体平台：资料库按组给 Agent 供上下文，支持 SubAgent 协作和定时续写/审阅；游戏侧有剧情分支、角色世界状态与规则检定<br><sub>方法：规划 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · 8 个 skill · Apache-2.0</sub><br><sub>💡 发布版默认开启匿名使用统计（Umami，可关）；一键安装为 curl \| sh 脚本</sub>

- **[storyforge](https://github.com/yuanbw2025/storyforge)** · ★ 861<br>本地优先叙事工作台：长短篇小说、剧本、漫画/漫剧素材共用世界设定，按需检索上下文并限定字段写回，支持节点流程、插件，还能从作品派生跑团等互动体验<br><sub>方法：规划 · 设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 README 有九种语言，正文以中文为主；可经 Codex app-server 复用 ChatGPT 登录；含插件作者包 zip；漫剧部分只做到分镜交付包</sub>

- **[QMAI](https://github.com/Mochocyang/QMAI)** · ★ 817<br>总纲→卷纲→17 节章纲三级大纲；每章定稿后摄取摘要/人物状态/伏笔/图谱，写前按优先级组装上下文混合检索；拆文库提取文风与角色，六维审查<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 128 个 skill</sub><br><sub>💡 Tauri 桌面应用，官网 qmai.pro；许可证非标准声明（NOASSERTION）</sub>

- **[Ai-Novel](https://github.com/inliver233/Ai-Novel)** · ★ 790<br>自托管长篇写作平台：项目→大纲/细纲→章节，角色与世界观条目结构化存储，pgvector 检索故事记忆注入生成，可调试 Prompt 模板并批量生成<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-07-28 · 🧩 应用 · 中文</sub><br><sub>💡 README 对应 lite 分支；部署需 Docker Compose（PostgreSQL + pgvector、Redis）</sub>

- **[easy-writing](https://github.com/yilujian/easy-writing)** · ★ 716<br>本地网文写作桌面软件：工作流一键建书（灵感→大纲→设定→逐章自动生文，可断点续），配合续写、润色扩写和大纲/角色/时间线资料库<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-10-09 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 Tauri 桌面应用，BYOK；提示词为本地 md 可改；附竞品拆书与榜单爬虫；AGPL-3.0，另有商业授权</sub>

- **[show-me-the-story](https://github.com/Nigh/show-me-the-story)** · ★ 625<br>长篇小说本地应用：设定角色与世界观后分批生成大纲，逐章起草、审阅、定向修订；抽取带出处的事实、追踪伏笔、提出设定变更，最后全书校对<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 单个 Go 可执行文件，需 OpenAI 兼容 API；Release 提供预编译包，源码完整；支持导入已有作品续写</sub>

- **[kimi-writer](https://github.com/Doriandarko/kimi-writer)** · ★ 595<br>kimi-k2-thinking 自主写作 agent：模型自己规划并调用建项目、写文件工具逐章写小说或短篇集，接近上下文上限时自动压缩并存摘要以便断点恢复<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-29 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 需 Moonshot API；方法较轻，按影响力收录（595★）；2026-01 后无更新</sub>

- **[character-arc](https://github.com/uu201/character-arc)** · ★ 587<br>桌面小说工作台：设定、角色关系、分卷大纲绑定章节，初稿流程为写作备忘→初稿→审计→自动修复/去 AI 味，配创作记忆、拆书知识库与 Skill 路由<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · 29 个 skill · MIT</sub><br><sub>💡 Electron；内置 Distilled-Novel-Toolbox 等 Skill 包；支持 Codex CLI、OpenAI 兼容与 Anthropic 接口</sub>

- **[vela](https://github.com/heider-x/vela)** · ★ 582<br>本地优先的小说写作 IDE：世界观与人物档案→结构骨架→章节细纲→流式成章，再走重写→精修→审阅三级后处理，本地 RAG 召回设定<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 README 带 API 中转平台推广码；另提供 dmg/exe 安装包</sub>

- **[OmniSpace](https://github.com/Yzw202011/OmniSpace)** · ★ 531<br>本地 AI 创作工作站的写作台：灵感→卷/章大纲树，按章数与字数参数批量生成章节，伏笔烂尾预警，三档降 AI 味文风；剧本可直通漫画与漫剧<br><sub>方法：规划 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-09-20 · 🧩 应用 · 中文</sub><br><sub>💡 综合平台（对话/漫画/漫剧/写作/知识学习），写作只是其中一个模块；默认本地 GPU 推理，可接云端 API；无开源许可证，README 称最新进度暂未提交</sub>

- **[goink](https://github.com/sigpanic/goink)** · ★ 455<br>对话式 Agent 调 31 个工具自查自改，结构化追踪角色关系图、伏笔回收期、弧线节点、地点图和读者认知，写完强制维护；可从样文蒸馏仿写 Skill<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 Go + Wails 桌面应用，内置 BGE 本地语义检索和 Git 版本；Skill 分内置/用户/单书三层覆盖，可开审稿子 Agent</sub>

- **[tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer)** · ★ 448<br>每章正文须附 12 类变更声明，经引用、一致性、外貌描写、蓝图出场等六道门禁才落地，再回写 15 维事实快照供下章读取；大纲→分卷→章节→蓝图四层规划<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-04 · 🧩 应用 · 中文</sub><br><sub>💡 Windows WPF 桌面端，内置拆书爬虫；作者称部分新源码丢失、开源版有功能缺失并转向新项目，仓库混有 bin/Debug 编译产物；提示词版见 zy-zmc/tianming-skill</sub>

- **[AI_Gen_Novel](https://github.com/cjyyx/AI_Gen_Novel)** · ★ 427<br>按写作认知过程模型（计划-转换-审阅）组织多 agent 写网文，借鉴 RecurrentGPT 循环生成：把前文压缩成几句记忆，再迭代续写任意长度<br><sub>方法：规划 · 记忆 · 多智能体</sub><br><sub>更新于 2024-09-04 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 2024-09 后未更新（427★）；需要自己实现 LLM.py 的 chatLLM 接口；作者结论是当前 LLM 还写不好长篇网文</sub>

- **[WenShape](https://github.com/unitagain/WenShape)** · ★ 417<br>长篇小说智能体：卷章结构+人物/世界/文风卡，事实按章节距离衰减与 BM25 选择注入，Writer/Editor/Archivist 分工，可抓百科建同人设定<br><sub>方法：设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 中文</sub><br><sub>💡 原名 NOVIX；许可证为 NOASSERTION，商用前看清条款</sub>

- **[NovelClaw](https://github.com/iLearn-Lab/NovelClaw)** · ★ 378<br>以动态记忆为核心的长篇协作写作平台：会话、故事板、人物和世界面板、可编辑记忆库，逐章起草，每次运行的日志和稿件都可检查<br><sub>方法：规划 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 出自 HITSZ 团队（CoLong-Idea-Studio），有在线版；仓库根目录带一个 ISTask.dll（Inno Setup 插件），本地运行前留意</sub>

- **[MirrorNovel](https://github.com/Aerdelan/MirrorNovel)** · ★ 365<br>长篇平台：大纲确认后 AI 提阶段、支线、反转蓝图再写正文，持久化章节摘要、伏笔、角色状态和情绪曲线，每章专家团审稿修订，两遍去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文</sub><br><sub>💡 需 MongoDB；桌面版只是外壳，默认连作者服务器（可改成自己的）；内置番茄小说下载器需 SVIP 账号；拆书蒸馏功能暂时移除</sub>

- **[ReaDreamAI](https://github.com/NEKOparapa/ReaDreamAI)** · ★ 362<br>从一个创意出发由 AI 依次构建世界观、角色与情节写成长篇，再按场景为书生成插图并锁定角色形象，可一键转短剧视频或恋爱 AI 游戏<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 Flutter 全平台；重心偏插图/视频，需 DeepSeek、火山等接口或本地 ComfyUI；README 对写作流程着墨不多</sub>

- **[AIxiezuo](https://github.com/yefeng2renxing/AIxiezuo)** · ★ 356<br>按章节大纲生成正文，写完由 LLM 更新主角状态 JSON（境界、物品、关系、剧情摘要）和版本化世界设定，下一章自动注入；可多模型多版本对比<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2025-07-21 💤 · 🧩 应用 · 中文</sub><br><sub>💡 基于 LangChain 的 Web 工具；无 License；2025-07 后未更新</sub>

- **[novelwriter](https://github.com/Hurricane0698/novelwriter)** · ★ 293<br>长篇续写的世界模型引擎：从正文提取实体、关系、体系成结构化世界模型（作者审核），续写时只注入本章相关设定，多版本草稿由作者采纳<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-20 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 AGPL-3.0；有 Windows/macOS 桌面版和 Docker 自部署；需 OpenAI 兼容 API</sub>

- **[AI_novel](https://github.com/tyxben/AI_novel)** · ★ 280<br>长篇 5 agent：架构师出骨架，卷导演出细纲，章规划从伏笔/叙事债务账本组装章前简报，写手写章，审稿只标问题；7 维评估，伏笔兑现率设硬门禁<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-18 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 仓库同时是小说转短视频（推文）流水线；小说模块有 CLI、Web UI 和 MCP Server（README 写可由 Claude Code 调用）</sub>

- **[AIStoryWriter](https://github.com/datacrystals/AIStoryWriter)** · ★ 258<br>从一段提示词先生成全书大纲，再拆章节大纲，逐章分阶段写情节、人物、对白，每步经 LLM 评审反馈修订；大纲、章节、修订可各配不同模型<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-11-24 💤 · ⚙️ 框架 · 英文 · AGPL-3.0</sub><br><sub>💡 命令行工具，默认 Ollama 本地模型，也支持 Google / OpenRouter；附 Evaluate.py 评测脚本；2025-11 后未更新</sub>

- **[AI_Novel](https://github.com/kele-tao/AI_Novel)** · ★ 257<br>小说写作台：按题材模板生成大纲后实时逐章写，每章先写章节计划再动态更新世界观，滑动窗口固定上下文长度，可暂停改设定或单章重写<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-07-30 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 也能生成课程讲义（非虚构）；接任意 OpenAI 兼容接口，作者推荐 vLLM / LM Studio</sub>

- **[ai-novel-generator](https://github.com/yangqi1309134997-coder/ai-novel-generator)** · ★ 243<br>长篇生成平台：雪花法从核心创意分层展开大纲，按章节蓝图（情节节点、角色弧线、场景）逐章写，再做风格润色去 AI 味和跨章连贯性检测<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-04 💤 · 🧩 应用 · 中文</sub><br><sub>💡 分本地 Gradio 版和商业版（会员、卡密、支付）；README 声明公司版权，许可证却写 MIT</sub>

- **[ReNovel-AI](https://github.com/BiranSama/ReNovel-AI)** · ★ 240<br>导入现有小说分章入向量库，Writer 按指令与保留度/扩写度逐段改写扩写，独立 Reviewer 查 OOC 与逻辑漏洞并拦截，可全书批量精修续跑<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 定位是重写/扩写已有文本（含 NSFW 加料）；需 OpenAI 兼容接口；Windows 绿色版在 Releases</sub>

- **[EasyNovelAssistant](https://github.com/Zuntan03/EasyNovelAssistant)** · ★ 235<br>日语本地 LLM 小说助手：多标签提示词加引言提示词按章拼接（附 GoalSeek 分章写作样例），本地无限循环生成，从中挑好的段落累积成文<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2024-07-05 💤 · 🧩 应用 · 日文 · MIT</sub><br><sub>💡 基于 KoboldCpp 与本地模型，主打无审查、可生成成人内容；附 Style-Bert-VITS2 朗读；2024-07 后未更新，按 ≥100★ 收</sub>

- **[loom-novel](https://github.com/WadeZhao23/loom-novel)** · ★ 228<br>设定师→大纲师→写手→编辑→润色师五道工序读「外置大脑」写一章；从作者手改中蒸馏写作指纹，每章自动查跨章矛盾并记状态账本<br><sub>方法：记忆 · 多智能体 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Mac/Windows 桌面端；默认 DeepSeek，也可接其他国产模型或复用本机 Claude Code/Codex 登录；内置 38 个题材速查</sub>

- **[scriverse](https://github.com/musnows/scriverse)** · ★ 223<br>长篇小说本地工作台：设定库、组织、时间线看板、人物关系图、大纲与伏笔埋收提醒集中管理，AI 续写时引用章节行与角色设定，另有一致性分析<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 Node/Docker 部署，带 CLI；内置续写与润色 skill</sub>

- **[Writingway](https://github.com/a-omukai/Writingway)** · ★ 197<br>桌面小说写作工具：项目按章/场景组织，Compendium 设定库按提及动态注入上下文，配 POV 设置、场景摘要和可自定义提示词，在场景中生成与改写正文<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2026-07-25 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 类似 Novelcrafter 的开源替代（PyQt）；README 部分仍是占位文本，功能需看源码或 Discord</sub>

- **[NovelWriter_public](https://github.com/tuxiangxianzhe/NovelWriter_public)** · ★ 190<br>大纲/即兴双模式写小说：架构→目录（悬念节奏、伏笔）→逐章生成→定稿更新摘要和角色状态，另有文风仿写、叙事 DNA、作者参考库和多轮去 AI 痕迹<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-05-26 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 YILING0013/AI_NovelGenerator；带「XP 预设」（内容偏好），可能涉及成人向内容</sub>

- **[dramatica-flow](https://github.com/ydsgangge-ux/dramatica-flow)** · ★ 189<br>Dramatica 理论驱动的长篇引擎：建筑师→写手→硬规则校验→审计员→修订者五层管线，维护因果链、伏笔生命周期、角色信息边界和世界状态<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文</sub><br><sub>💡 带 Web UI 与 CLI；支持 DeepSeek / Ollama / OpenAI 兼容接口；仓库未声明许可证</sub>

- **[storycraftr](https://github.com/raestrada/storycraftr)** · ★ 174<br>命令行写书：建项目后分步生成世界观、人物与大纲、章节摘要，再逐章写作并迭代修订，用本地嵌入模型做 RAG 检索保持设定一致<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-03-06 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 支持 OpenAI / OpenRouter / Ollama；附 VS Code 扩展；最近更新 2026-03，按 ≥100★ 收</sub>

- **[GOAT-Storytelling-Agent](https://github.com/GOAT-AI-lab/GOAT-Storytelling-Agent)** · ★ 164<br>主题→书籍设定（类型/视角/人物/前提）→增强→分幕分章情节→增强→拆成场景→结合上一场景逐场写，可在任意层级介入<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-11-12 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 默认用自家 GOAT-70B-Storytelling 模型，可接 TGI/llama.cpp；HF 上附 20 部无人工干预生成的中篇</sub>

- **[NovelGenerator](https://github.com/KazKozDev/NovelGenerator)** · ★ 153<br>从一段前提生成整本小说：先建人物、世界规则、因果图和章节图并自审，逐场景写，事实抽取必须引用原段落，场景交接后重定下一场的因果计划<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-09 · 🧩 应用 · 英文</sub><br><sub>💡 writer 和 editor 双模型分工；支持 Gemini 和本地 Ollama；source-available 许可</sub>

- **[OrisonSpace](https://github.com/LumenStorm/OrisonSpace)** · ★ 144<br>小说 IDE：大纲、章节、人物/世界观资产卡同处一个工作区，AI 生成/续写/审阅以可回退 diff 落地，Story Sync 从正文抽设定补丁<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-17 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 Alpha；定位用户主导、AI 辅助；Agent 编排与 Auto Mode 为实验功能；Release 提供安装包，仓库源码完整</sub>

- **[novel-studio](https://github.com/Xiaoyangy/novel-studio)** · ★ 137<br>先冻结全书章位并整弧预演，重要角色以独立 agent 在至多 3 章窗口内决策、世界仲裁者裁决后果，封存章节合同后逐章渲染审核，验收正文才入正史台账<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-09-23 · ⚙️ 框架 · 中文 · 20 个 skill · Apache-2.0</sub><br><sub>💡 Go CLI + 只读 Dashboard；RAG（embedding + Qdrant）可选；仓库附 20 个 SKILL.md；建议审稿角色单独路由 DeepSeek</sub>

- **[xunlong](https://github.com/jaguarliuu/xunlong)** · ★ 135<br>LangGraph 多 agent 内容生成 CLI：小说模式按类型和章数先设计大纲再逐章创作并做人物一致性检查，可导入设定文档，支持局部/全局迭代修改<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-10-25 💤 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 同时做研究报告与 PPT，小说只是三种模式之一；2025-10 后未更新，但 ≥100★</sub>

- **[Fibb](https://github.com/Ckokoski/Fibb)** · ★ 127<br>研究→大纲→逐章写→修订的自主流水线；三层记忆加夜间整理，按实体库查矛盾，角色分身审自己台词，评判→修订→复评只留变好的版本<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-11 · 🧩 应用 · 英文 · 48 个 skill · MIT</sub><br><sub>💡 README 名为 AuthorAgent（克隆地址仍是 authoragent）；同时面向非虚构，另带选题调研、宣发模块；需自备模型 API key</sub>

- **[narralume](https://github.com/abligail/narralume)** · ★ 122<br>长篇写作环境：作者意图、大纲、实体、正典事实、时间线、伏笔共用一份故事圣经，AI 正文和设定变更都先作候选，审稿附证据，撞上锁定事实就暂停<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 不接模型也能纯手写；AI 长任务有检查点和运行记录；Docker 或脚本自部署，有托管 demo</sub>

- **[gptauthor](https://github.com/dylanhogg/gptauthor)** · ★ 116<br>人写故事提示（风格、人物）→AI 生成带各章摘要的梗概→人工审阅可重生成→按梗概加上一章逐章写出长篇<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2026-08-15 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 pip 可装的命令行工具，故事提示用 YAML 描述</sub>

- **[saga](https://github.com/Lanerra/saga)** · ★ 113<br>前提→大纲→逐场景草稿→导出：Neo4j 知识图谱追踪人物、事件与关系，嵌入检索补上下文，LangGraph 检查点可中断续跑，自动质量验收<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-15 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 需自备 OpenAI 兼容文本接口、Ollama 嵌入接口与 Neo4j；仅验证 Linux</sub>

- **[narracat-novel-agent](https://github.com/yannikzz/narracat-novel-agent)** · ★ 109<br>网文桌面应用：立项卡定题材和金手指→大纲→章纲→成稿，NovelMemory 长程记忆追踪伏笔，能力包从书中学写法，写作 agent/skill 提示词全开源<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 7 个 skill · AGPL-3.0</sub><br><sub>💡 自带 API Key；默认收集匿名使用统计（首次启动告知，可关闭）；AGPL-3.0</sub>

- **[Storydex](https://github.com/TensorHub-ORG/Storydex)** · ★ 102<br>本地长篇写作台：Agent 先查全文、章节摘要、相关旧文和 WIKI 再续写或修改，写入以 Diff 审阅、Git 记版本可回滚，内置连续性、悬疑、润色技能<br><sub>方法：记忆 · 修订</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · 6 个 skill</sub><br><sub>💡 许可证为 Apache-2.0 + Commons Clause（限制商用）；仓库自带 MinGit 的 exe/dll 和 Android bootstrap zip 等第三方二进制</sub>

- **[plotbunni](https://github.com/MangoLion/plotbunni)** · ★ 101<br>开源小说写作套件：幕→章→场景三级规划，场景链接设定概念库，AI 按大纲与关联概念生成梗概和场景正文，6 类任务提示词与模型可分别配置<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-19 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 可用 AI Horde 社区免费模型</sub>

- **[siming-ai](https://github.com/teangtang1122/siming-ai)** · ★ 95<br>长篇小说本地工作台：一句想法→卷纲与前 3 章细纲（场景节点）；写作时按预算选取角色当前状态、伏笔与时间线，写后更新叙事账本<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 Release 提供 Windows 安装包，源码完整；可导入 TXT 建档后续写；可把 Claude Code/Codex/OpenCode 当模型后端；有 Android 端</sub>

- **[obsidian-writing-buddy](https://github.com/xtenlab/obsidian-writing-buddy)** · ★ 92<br>Obsidian 长篇写作插件：Recanta 小说记忆追踪事件、状态、关系与角色所知，按写到的位置供上下文；续写、改写、一致性检查先出 diff 再采纳<br><sub>方法：记忆 · 修订 · 共创</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 原 onezeroooo/obsidian-writing-buddy，已转移到 xtenlab（API 重定向确认）；作者主写、AI 出候选为主；自带模型 Key</sub>

- **[novel_agent](https://github.com/blackzhanzhan/novel_agent)** · ★ 90<br>Git 原生的长篇网文工作台：导入小说蒸馏世界观、协作出大纲、生成续写草稿后审核归档，章节和剧情分支用 Git 管理，可回滚<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-05-27 · 🧩 应用 · 中文</sub><br><sub>💡 依赖 Dify 编排工作流；提供 Docker 和 Release 包部署</sub>

- **[InkAI-](https://github.com/yan2959088709/InkAI-)** · ★ 89<br>规划器先出全书蓝图和结构化章节卡（节拍、必现元素、伏笔编号、章末钩子），写作器按卡生成后硬校验、失败带反馈重写，跨章状态快照注入下一章<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-01 · ⚙️ 框架 · 中文</sub><br><sub>💡 题材规则包（文风、禁用语）贯穿规划与写作；默认阿里云百炼，可切 DeepSeek/OpenAI；有 Flask Web 界面；仓库无许可证</sub>

- **[ai-novel-writer](https://github.com/eliumusk/ai-novel-writer)** · ★ 88<br>PyQt 写作应用：Gemini 按全书大纲和章纲生成正文，SQLite 存角色、关系和章节摘要，自动摘要并追踪情节线与伏笔，支持文风模仿<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2025-01-09 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需 Gemini API</sub>

- **[AI_NovelCraft-](https://github.com/15673312611/AI_NovelCraft-)** · ★ 88<br>先生成含主线/支线/伏笔/角色弧线的超级大纲并拆卷、写章节细纲，按项目/卷/章管理上下文逐章流式生成，最后用消痕提示去 AI 味<br><sub>方法：规划 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-04-20 · 🧩 应用 · 中文</sub><br><sub>💡 Java + React 平台，作者另有在线版；License 未声明标准协议；同作者的 AnimaHub 是视频平台，未收</sub>

- **[Narraverse-Engine](https://github.com/wssyh339/Narraverse-Engine)** · ★ 86<br>长篇大纲与世界观推演工作室：LangGraph swarm 多 agent 回合制议事，维护正典库和关系图谱，推演世界规则、大纲、伏笔和正文，人工确认后入库<br><sub>方法：规划 · 设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-07-22 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 0.2.0 Alpha；Docker Compose 一键启动，数据存本地 SQLite</sub>

- **[NovelWriter](https://github.com/EdwardAThomson/NovelWriter)** · ★ 83<br>多类型小说写作 GUI：按类型套路生成宇宙设定、势力和人物，再做结构大纲、场景规划和逐章正文，多 agent 编排，多级审阅<br><sub>方法：规划 · 设定 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 英文</sub><br><sub>💡 Tkinter 界面；可走 API 或本地 codex/gemini/claude CLI；作者另有 EdwardAThomson/StoryDaemon</sub>

- **[StoryMoss](https://github.com/91zgaoge/StoryMoss)** · ★ 77<br>主创、管理、编辑审计三代理黑板协作，每章过加权质量门才交付；续写前检索前文原文，按书纲→卷纲→章纲规划，正文写完自动回流角色/设定/伏笔入库<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 37 个 skill</sub><br><sub>💡 Tauri+Rust 桌面应用，支持 OpenAI/Anthropic/Ollama；另有 StyleDNA 文风、拆书、按公版人类语料校准的 AI 腔检测；GitHub 未识别许可证（README 徽章写 ISC），仓库根目录混有构建日志等杂项</sub>

- **[AIStoryBuilders](https://github.com/AIStoryBuilders/AIStoryBuilders)** · ★ 73<br>把小说拆成时间线、地点、人物（按时间线分段描述）和章节段落的数据结构，写每段时按其时间线、地点和出场人物取对应设定作上下文<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-06-20 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 C# .NET MAUI 桌面应用，另有在线版和微软商店版；需 OpenAI / Azure OpenAI Key</sub>

- **[ProseForge](https://github.com/remacheybn408-boop/ProseForge)** · ★ 73<br>六席位 agent 流水线：分析→四路并行场景草稿择优→连续性/对抗/文风三审合议→定点改写；章节摘要金字塔+承诺台账+叙事 RAG 防失忆<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-08 · 🧩 应用 · 中文 · 87 个 skill · AGPL-3.0</sub><br><sub>💡 Docker 或原生安装包本地部署，模型走 OpenAI 兼容接口；packs/ 附 80 余个题材与技法 SKILL.md</sub>

- **[novel-engine](https://github.com/john-paul-ruf/novel-engine)** · ★ 70<br>七个 AI 编辑角色（故事教练、代笔、初读、发展编辑、校对等）走 15 步流程从 pitch 到出版稿，访谈作者建 Voice Profile 保持文风<br><sub>方法：规划 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-07-29 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 Electron 桌面应用，AGPL；使用 Claude、Codex 或 Ollama；作者称已用其出版 10 本 Amazon 书</sub>

- **[zenstory](https://github.com/zenstory-ai/zenstory)** · ★ 70<br>对话式小说工作台：路由按请求选五条流程，大纲规划师、爽点设计师、内容创作者、质量审稿人接力，超 500 字自动送审；每轮按预算注入 AI 记忆和相关文件<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 MIT 可自部署，另有官方在线版 app.zenstory.ai；外部 agent 通过 npx zenstory CLI 与 skill 接入</sub>

- **[StoryCrafter](https://github.com/FartyPants/StoryCrafter)** · ★ 66<br>text-generation-webui 扩展：按 beat 逐段提示生成，每段可存三个版本，Future Cues 指令作用于后续段落以保持连续<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2025-08-07 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 须装在 extensions/StoryCrafter；在作者旧扩展 BlockWriter 基础上扩展；仓库无许可证</sub>

- **[AI-Book-Generator](https://github.com/SimonWaldherr/AI-Book-Generator)** · ★ 64<br>浏览器端写书工具：先生成书名候选和概念（logline、前提、主题），再出带章节目的的大纲，带前文摘要逐章写作，可一键 Agent 模式跑完<br><sub>方法：规划</sub><br><sub>更新于 2026-03-16 💤 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 小说与非虚构通用；支持 OpenAI / Claude / Gemini，可生成封面</sub>

- **[mythpen](https://github.com/niyongsheng/mythpen)** · ★ 60<br>桌面写作应用：写作模式下 AI 按六步工作流读设定和前章，写含认知、情感、悬念等五维度的章纲，再成文、润色；另有协作共写模式<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-29 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 Tauri 桌面，数据存本地 SQLite；作者另有 Claude Code 工作流版 niyongsheng/clark-typer</sub>

- **[moshu](https://github.com/huihuijiangqiang/moshu)** · ★ 59<br>长篇网文工作台：卷纲、章纲和场景卡（POV、目标、阻力、转折、钩子）配 pgvector 设定库与时间线检索生成候选正文，再过一致性守卫和自然化审查<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 自部署需 PostgreSQL/pgvector、Redis、Celery；含积分计费和漫剧分镜管理模块；有在线体验站</sub>

- **[fictionforge](https://github.com/wanqili857-byte/fictionforge)** · ★ 56<br>每个角色是带记忆和信念的 agent，先演出事件；导演把多视角事件线合成章节 spec 再写，逐章过禁词/AI 腔门禁，不合格就返工<br><sub>方法：记忆 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 README 首屏是从门禁里抽出的 CanonBench 长篇一致性基准（零 LLM 判定器，三档 harness 消融）；换小说只换内容包</sub>

- **[nest-drama](https://github.com/63435212cwu-ops/nest-drama)** · ★ 55<br>从素材提炼世界观、必达/弹性剧情节点和角色三卡；角色是信息隔离的独立 agent 自主行动，舞台监督调度、监督者审人性，剧情经世界内因果收敛到节点<br><sub>方法：设定 · 人物 · 模拟 · 去 AI 味</sub><br><sub>更新于 2026-09-13 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 纯 Python 标准库本地网页应用，需 OpenAI 兼容 API；README 推荐下载 Release zip，但仓库含完整源码；中英双语 README</sub>

- **[Chevoink](https://github.com/Xcy8010/Chevoink)** · ★ 52<br>长篇小说平台：Agent 按两级路由加载 Skill，Story Compiler 按章程→承诺→场景任务→章节衔接编排写作，过连续性与人类感质量门<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文</sub><br><sub>💡 正文版本化可回滚；含书城阅读与社区；在线版按 Credits 计费，可自部署（React + PostgreSQL）</sub>

- **[Novel-OS](https://github.com/mrigankad/Novel-OS)** · ★ 51<br>架构→执笔→编辑→守卫→整理五角色流水线，结果并入持久 story_state，确定性连续性引擎先查断线与时间漂移再交 LLM 审校<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-09 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 浏览器写作工作室 + 无头 CLI；支持各家 OpenAI 兼容模型</sub>

- **[lightnovel-studio](https://github.com/mmlong818/lightnovel-studio)** · ★ 50<br>一句话概念依次生成世界观、角色群、章节大纲再逐章写正文，附续写、角色对话和一致性/读者体验推敲，内置中日轻小说题材<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-06-08 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 纯前端，作品存浏览器 localStorage；支持 Gemini/Claude/OpenAI/兼容接口</sub>

- **[novel-distiller](https://github.com/FutureFuzzy/novel-distiller)** · ★ 49<br>创世蓝图→为角色蒸馏思维 SKILL.md→蒸馏参考作者文风→多智能体推演场景→撰写→8 维锚定自检，YAML 数值状态层追踪暗线，叠加番茄/起点平台规则<br><sub>方法：人物 · 记忆 · 模拟 · 风格</sub><br><sub>更新于 2026-05-11 · ⚙️ 框架 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 Python CLI 负责组装 prompt，LLM 推理交给 Claude Code；剧情推演借用 MiroFish 多智能体模拟思路；demo 含孙悟空、刘慈欣蒸馏</sub>

- **[novel-master](https://github.com/bloodycrownD/novel-master)** · ★ 48<br>长篇写作 agent 工作台：世界观/人设/卷纲/章节放入虚拟文件树，目录级规则控制注入上下文的档位，只读分析/写作/资料整理多智能体分工，可派子代理<br><sub>方法：记忆 · 多智能体</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 中文 · 4 个 skill</sub><br><sub>💡 PolyForm Noncommercial 许可，禁止商用；桌面/安卓/CLI 三端；具体叙事方法需用户自建模板或导入 SKILL.md</sub>

- **[QianBi-Novel](https://github.com/GLFzr/QianBi-Novel)** · ★ 48<br>立项→设定→总纲→世界书与正则→细纲→正文六阶段共写；世界书按锚点注入，must 契约确定性复检，终审引证验真+三票投票，新设定回写<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-09-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Windows 桌面应用（PySide6），BYOK 全本地；内置 10 套题材预设，含同人设定集导入路径</sub>

- **[flutter-novel-main](https://github.com/xy9144/flutter-novel-main)** · ★ 47<br>按大纲→分卷规划→范围规划→章节规划→正文五级提示词逐章生成，用进度追踪文件支撑自动续写，可随机生成书名和题材<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-22 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Flutter 多端；支持 OpenRouter、Ollama 等自定义接口</sub>

- **[novel-writer](https://github.com/curvedinf/novel-writer)** · ★ 46<br>三段脚本写长篇：先依次生成梗概、人物、场景设定、情节和标题（每步可重做、可手改 JSON），再逐章起草，最后定稿<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2024-04-11 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 README 极简；API Key 写在 writer.py；作者建议用 Gemini 做设定、Claude/GPT-4 写正文</sub>

- **[novel-agent-studio](https://github.com/skuramatata/novel-agent-studio)** · ★ 45<br>设定作者声音后对话生成总纲、人物关系、双时间线与章纲，按场景起草，审稿回查原文核对时间/知情并局部修订，采纳正文才提取带出处的故事记忆<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-18 · 🧩 应用 · 中文</sub><br><sub>💡 Electron 桌面应用，仅验证 macOS Apple Silicon；接 GLM / MiniMax；附 desktop-app/runtime/skills/novel-workflow/SKILL.md</sub>

- **[LLM-book-generator](https://github.com/fangfufu/LLM-book-generator)** · ★ 44<br>命令行整书生成：从选题、书名到章节大纲、分节正文和前后附文，小说会生成人物表，草稿分两遍写，scratchpad 存人物和地点<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-11 · ⚙️ 框架 · 英文 · GPL-3.0</sub><br><sub>💡 通用书籍生成器，也写非虚构（含 LaTeX 公式渲染）；需本地 llama.cpp server；输出 DOCX</sub>

- **[AnySpark](https://github.com/Mikexujunrui/AnySpark)** · ★ 42<br>对话驱动的小说智能体：主循环按需调用图谱查证、伏笔、剧情计划、设定检索等工具，再用无历史的干净上下文写章；可拆书提炼技巧 skill，角色推演多探索选优<br><sub>方法：规划 · 记忆 · 模拟 · 风格</sub><br><sub>更新于 2026-09-01 · 🧩 应用 · 中文</sub><br><sub>💡 Python 后端 + React 创作台 + 对话 CLI；默认接 DeepSeek；License 未声明标准协议</sub>

- **[StoryDaemon](https://github.com/EdwardAThomson/StoryDaemon)** · ★ 41<br>不预先列大纲，agent 按 story tick 循环自主规划、写场景并更新人物/地点记忆，配张力评分、目标层级、从 21 部经典小说测得的场景骨架和矛盾检测<br><sub>方法：理论 · 记忆 · 修订</sub><br><sub>更新于 2026-09-24 · ⚙️ 框架 · 英文</sub><br><sub>💡 无开源许可证；默认走 Codex CLI，也可接各家 API；作者前作 EdwardAThomson/NovelWriter 是大纲先行路线</sub>

- **[wanxiangpu-loreweft](https://github.com/EXwhitewood/wanxiangpu-loreweft)** · ★ 41<br>长篇小说工程台：Story Plan→章节蓝图→按场景生成，世界规则/人物/伏笔/状态账本约束，并行校验+受控修订+提交门禁，15 个分工智能体<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-25 · 🧩 应用 · 中文 · 36 个 skill · AGPL-3.0</sub><br><sub>💡 主要面向 Windows 桌面（Tauri）；AGPL-3.0</sub>

- **[ai-book-writer](https://github.com/agruai/ai-book-writer)** · ★ 39<br>CrewAI 五角色流水线：概念→大纲→分章写作→编辑→连续性检查，小说模式导出角色圣经和时间线 JSON 供连续性校验，带流式输出和预算控制<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2025-10-13 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 也做非虚构书稿；需 OpenAI/Anthropic/Google Key，部署栈较重（PostgreSQL、Redis、K8s）；账号由 ai-joon 改名而来</sub>

- **[Morpheus](https://github.com/papysans/Morpheus)** · ★ 38<br>长篇小说工作台：多 agent 分担规划、设定、连续性、文风与裁决，L1/L2/L3 记忆加开放线程装配上下文，批量生成后按修改方向重做单章<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-22 💤 · 🧩 应用 · 中文</sub><br><sub>💡 默认 DeepSeek，支持 OpenAI 兼容接口；带知识图谱与轨迹回放；仓库无许可证</sub>

- **[Novelgen](https://github.com/kirinonakar/Novelgen)** · ★ 38<br>面向读者的小说生成器：输入种子生成分章情节，长篇分部生成和精修，靠分层上下文与滑动窗口记忆逐章写，可对照相邻章节自动出修改意见<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 Tauri 桌面应用；支持 LM Studio、Ollama 本地模型和 Gemini 等云端；输出韩/日/英</sub>

- **[inkflow](https://github.com/real-Elysia886/inkflow)** · ★ 37<br>战略→滚动 5 章大纲→上下文编排→写作→双层审计→事实提取→归档的多 agent 管线，7 类真相文件管人物、伏笔、资源、信息边界，可从样章蒸馏文风<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-21 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 架构和 Narcooo/inkos 高度相似（真相文件、资源账本、Plan→Compose→Write→Observe→Reflect），README 未注明来源；Python 重写，另加 Web 工作台和多书风格融合</sub>

- **[novelIDE](https://github.com/qq1375828505/novelIDE)** · ★ 37<br>安卓离线网文 IDE：主 Agent 调 40 多个工具读写角色、设定、伏笔资料库，委派大纲、角色、爽点检查、水文检测、去 AI 味等子 Agent 多轮推敲<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-07 · 🧩 应用 · 中文</sub><br><sub>💡 Flutter 源码在仓库里；仓库还夹带日志压缩包和改 hosts 的 .bat 工具脚本</sub>

- **[ai-novel-writer](https://github.com/KKKenChow/ai-novel-writer)** · ★ 35<br>全链路写长篇：世界观→人物→大纲→场景卡逐段写；按六阶段放宽大纲可见范围、过滤剧透防抢跑，章后更新伏笔台账和滚动摘要，五维评审后改写<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-09 · 🧩 应用 · 中文 · 4 个 skill · MIT</sub><br><sub>💡 默认火山方舟豆包 API，也可接 OpenAI 兼容接口；能把写作技巧文章蒸馏成 skill 包按步骤注入；数据存本地 JSON</sub>

- **[lore-weave](https://github.com/letuhao/lore-weave)** · ★ 35<br>长篇共写平台：每章自动抽取人物、地点、事件和关系进知识图谱，聊天、共写与翻译都以此为据，批评 agent 对照正史检查建议<br><sub>方法：设定 · 记忆 · 修订</sub><br><sub>更新于 2026-10-05 · 🧩 应用 · 英文 · 31 个 skill · AGPL-3.0</sub><br><sub>💡 多服务自托管、体量很大；写作合成引擎仍在开发（Phase 3）；另含术语一致的多语翻译和 MMO RPG 扩展；AGPL-3.0</sub>

- **[novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot)** · ★ 35<br>文件系统即记忆的写作 agent：自动生成人设、世界观、角色卡、大纲等 Markdown 文件，全局记忆加章节摘要双记忆，每章写完自动更新<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-02-16 💤 · ⚙️ 框架 · 多语言 · 4 个 skill · MIT</sub>

- **[OpenFicM](https://github.com/tioners/OpenFicM)** · ★ 33<br>安卓本地小说 Agent：读写章节、角色、世界书与三级笔记，可委派子智能体；参考书多轮蒸馏成文风约束，并对比 AI 原稿与作者定稿学习个人文风<br><sub>方法：规划 · 记忆 · 多智能体 · 风格</sub><br><sub>更新于 2026-10-08 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 基于 syrizelink/OpenFic 重构的 Android 版（非官方）；首次启动从 GitHub/Hugging Face 拉取 Agent/Skill 与本地检索模型</sub>

- **[hongyue-creation](https://github.com/chen647208/hongyue-creation)** · ★ 32<br>本地桌面写作室：灵感→世界→角色→大纲/细纲→按细纲单章或批量生成正文，黄金三章、雪花法、POV、伏笔回收、去 AI 味等写法技能以 SKILL.md 渐进注入<br><sub>方法：规划 · 理论 · 设定 · 去 AI 味</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · 10 个 skill · AGPL-3.0</sub><br><sub>💡 Electron 应用，AI 是可关闭的增强层，也能纯手写；Agent 改稿走建议/改写/直接三档审批；AGPL-3.0，另有商业授权</sub>

- **[novel_writer_agent](https://github.com/nonever2109/novel_writer_agent)** · ★ 32<br>本地长篇写作助手：选题→大纲和章节计划→每章经规划、生成、修订、连续性检查、体验评估、风险检查，写完更新角色、时间线、伏笔和主支线记忆<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-05-13 · 🧩 应用 · 中文</sub><br><sub>💡 Windows 本地运行；每章约跑 20 个流程，Token 消耗大</sub>

- **[bragi](https://github.com/wailers9/bragi)** · ★ 31<br>架空世界故事引擎：用数字路径管理时间树与空间树，当前节点保留全文、邻近节点只留摘要按需扩写，结合角色状态与事件记录续写剧情<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-05-17 · ⚙️ 框架 · 中文</sub><br><sub>💡 CLI + 本地 Web UI；支持 OpenAI / DeepSeek，附离线 Demo Agent</sub>

- **[Project-Wannabe](https://github.com/kawaii-justice/Project-Wannabe)** · ★ 30<br>配合小说微调模型 wanabi：先生成标题/梗概/设定/情节转入详情栏，再按「下一段展开指示」反复出候选卡片，人挑选插入正文<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2026-06-01 · 🧩 应用 · 日文</sub><br><sub>💡 需本地 KoboldCpp 加载 wanabi 系列 GGUF 小说模型（含 Gemma 4 31B 版）；Windows 桌面应用</sub>

- **[OpenNovel](https://github.com/Cppys/OpenNovel)** · ★ 29<br>LangGraph 多 agent：类型研究、故事架构、冲突设计出大纲，写作→编辑→审稿（含 AI 痕迹检测）不过即重写，ChromaDB 存章节摘要和角色状态<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-01 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 依赖 Claude Code CLI 登录；可用浏览器自动化发布到番茄小说</sub>

- **[waqupin](https://github.com/zhou491145-tech/waqupin)** · ★ 28<br>VS Code 网文插件：全局/项目/章节分层记忆检索注入，人物档案记录章前章后状态，伏笔埋收追踪，节奏评级，作家风格模板精修<br><sub>方法：人物 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-19 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 开源的是核心层升级前的旧版代码，含激活码校验</sub>

- **[1667](https://github.com/1667-ai/1667)** · ★ 27<br>终端/网页里写分支小说：每段保留多个生成版本组成故事树，Facts 按故事线锚定状态注入上下文，摘要节点压缩前文作为上下文重置<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 也可纯人工写；可接本地或云端模型，支持导入 SillyTavern 角色卡与 NovelAI 生成配置</sub>

- **[ElyHa](https://github.com/ShadowLoveElysia/ElyHa)** · ★ 27<br>图结构长篇写作：节点和边管理分支剧情，Planner→Writer→Reviewer→Synthesizer 写章并查设定一致性，AI 以幽灵节点提案、人工采纳<br><sub>方法：规划 · 多智能体 · 修订 · 共创</sub><br><sub>更新于 2026-04-02 💤 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 Web GUI + TUI，界面中英日；GitHub 识别为 AGPL-3.0（README 写 GPLv3）；仓库提交了 .venv-win 目录</sub>

- **[lshu-novel-generator](https://github.com/TSOFTP-afk/lshu-novel-generator)** · ★ 27<br>长篇小说工作台：规划→写手→审计→修订四 Agent 写章并查 OOC 和 AI 痕迹，Truth File+RAG 管设定，可从参考书提炼写作 Skills<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-22 · 🧩 应用 · 中文</sub><br><sub>💡 Truth File 机制与 InkOS 类似；与 XiaoJiuAI/lingshu 同叫「灵枢」，但不是同一项目</sub>

- **[open-skoob](https://github.com/OmMaBaMiHong/open-skoob)** · ★ 27<br>网文多智能体工作室：意图卡→世界观→大纲→卷→章六步开书，每章规划→编排→执笔→审校→修订→结算六师接力；八师逆向拆书建图谱，写前可多轮仿真推演<br><sub>方法：规划 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文</sub><br><sub>💡 README 引导去 gaotk.com 中转站建 Key，拆书/仿真/检测等引擎走官方云端 API；许可证 NOASSERTION，另附商业许可；含同人支线与互动影游模式</sub>

- **[xiami](https://github.com/zhangxunvvv/xiami)** · ★ 27<br>长篇逐章流水线：世界观/总纲/细纲/人物卡/伏笔库/剧情账本约束连续性，每章推演→主笔→门禁→定向修复→账本结算，另有情绪钩子排布与读者速读模型<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文</sub><br><sub>💡 Tauri 桌面应用，API Key 存 Windows 凭据管理器，主要面向 Windows；兼容任意 OpenAI 接口；仓库未声明许可证</sub>

- **[fiction-forge](https://github.com/geobond13/fiction-forge)** · ★ 26<br>Claude Code 通过 MCP 设定库按章节查人物已知信息；冷读协议带状态账本找连续性错误；按目标语料量化文风画像，扫描器防 AI 腔回潮<br><sub>方法：记忆 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-26 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 总结自作者写完约 29 万字小说的经验；另含 EPUB/PDF 发布和 DALL-E 插图脚本</sub>

- **[MortalAINovel-AIWritingSystem-ai-](https://github.com/hezhengtao/MortalAINovel-AIWritingSystem-ai-)** · ★ 26<br>本地桌面写作软件：按书/卷/章管理，AI 续写、润色和风格模仿；角色档案可一键生成关系图谱，拆书知识库分析范文「文笔DNA」供仿写<br><sub>方法：人物 · 风格</sub><br><sub>更新于 2025-12-29 💤 · 🧩 应用 · 中文</sub><br><sub>💡 Releases 提供 Windows exe，源码可用 Streamlit 直接运行</sub>

- **[novel_agent](https://github.com/Jackn0/novel_agent)** · ★ 26<br>Next.js 写作助手：小说预设→大纲→章纲→小节列表→正文五阶段，每阶段 AI 起稿用户审定，追踪人物状态和伏笔，五档记忆等级，可导入旧作续写<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-03-23 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 附多角色有声书制作（Edge TTS / 百度 TTS）；支持 Claude 和 OpenAI 兼容接口</sub>

- **[OpenNovelWriter](https://github.com/vibe-creator-art/OpenNovelWriter)** · ★ 23<br>类 Novelcrafter 的写作应用：章节、大纲、术语、摘要投影成文件交给 Codex 会话，靠 story-state 与上下文检索 skill 管上下文<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 中文 · 12 个 skill · AGPL-3.0</sub><br><sub>💡 依赖本机 Codex CLI；作者提示 Codex 有本地写权限、可能改删稿件，只建议自托管自用；AGPL-3.0</sub>

- **[write-chinese-long-screenplay](https://github.com/mudden2380078550-creator/write-chinese-long-screenplay)** · ★ 22<br>中文长篇小说/剧本状态 harness：人物、能力、资源与作者政策存为正典，每章先组装章纲与写前状态，候选正文附状态变更，过检查才落盘<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-12 · ⚙️ 框架 · 中文 · 2 个 skill · GPL-3.0</sub>

- **[Muses](https://github.com/zestor/Muses)** · ★ 21<br>GPT-3 长篇续写脚本：每场景依据上一场景、人物表、滚动摘要和随机情节队列生成，三选一取最长后补感官细节，再更新人物和摘要<br><sub>方法：人物 · 记忆 · 修订</sub><br><sub>更新于 2023-02-23 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 基于 GPT-3 / NLP Cloud 旧接口；可设定不会死亡的主角</sub>

- **[novel-studio](https://github.com/ldblckrs-258/novel-studio)** · ★ 21<br>越南语写作工作台：章节→全书→人物三阶段分析，六步自动写作（上下文→方向→大纲→写手→审稿→重写），另含中译越翻译、TTS 与爬虫导入<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-09-29 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 界面与提示词为越南语（lang 无对应项，暂填 multi）；数据存浏览器 IndexedDB；工具重心偏翻译</sub>

- **[NovelWritingAgent](https://github.com/xindaaW/NovelWritingAgent)** · ★ 21<br>多 agent 写小说：先生成并收敛设定 canon，章节写→审→改，评审团并行打分再由总评汇总，修订经 canon_patch 反写设定，长期记忆分级检索<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-02 💤 · ⚙️ 框架 · 中文 · 8 个 skill · MIT</sub><br><sub>💡 各 agent 提示词以 SKILL.md 形式放在包内；有不调模型的骨架调试模式</sub>

- **[WorldScript-Studio](https://github.com/qnbs/WorldScript-Studio)** · ★ 21<br>本地优先的小说/剧本写作工作室：大纲生成器可把结构化提纲写进稿件，配人物与世界档案、故事圣经、节拍表，AI 可续写、生成对白与梗概<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 以人写稿为主，AI 为可选能力（云端 BYOK、浏览器本地模型或 Ollama）；PWA + Tauri 桌面版</sub>

- **[ai-novel-generator](https://github.com/inyhow/ai-novel-generator)** · ★ 19<br>网文 Web 应用 + SKILL.md：5 问确认题材、主角缺陷、冲突、节奏和篇幅，出总纲与角色弧线，逐章写并补悬念钩子，每 5 章查连贯，最后去 AI 味<br><sub>方法：规划 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-17 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 根目录 SKILL.md 可单独当 skill 用；应用附番茄小说 CDP 自动发布和敏感词检测</sub>

- **[arcvellum](https://github.com/o-1717986918/arcvellum)** · ★ 19<br>本地长篇创作工作室：项目 Agent 接长期目标交后台推进；每个场景作为事务，主创定意图并向角色续演、描写器取候选，经审查修订后提交并写回人物与 Canon<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Windows 安装包 + 完整源码，Beta；也支持剧本与伪纪录体；作者自述多题材长篇稳定性仍待验证；需自配模型</sub>

- **[DAWO](https://github.com/dawo4/DAWO)** · ★ 19<br>长篇网文桌面软件：一句话建书→设定集→分卷大纲→逐章生文，按卷和出场裁剪注入大纲与角色卡，悬置伏笔作硬约束注入，配六维去 AI 味打分<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文</sub><br><sub>💡 仓库未附开源许可证（README 称暂未开源授权）；含 15 个提案制智能体、拆书与朱雀对抗手册；Windows 安装包未签名</sub>

- **[StoryForge](https://github.com/XZZKANY/StoryForge)** · ★ 19<br>长篇小说桌面 IDE：Agent 用只读工具跨文件取证，做多视角审稿并产出修订补丁，作者看 diff 决定写回；配 canon 防漂移、一致性扫描和逐章生成<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 作者自述仍在自用阶段，30 章长程生成人工通读未通过；本地需 Docker 起 Postgres/Redis/MinIO</sub>

- **[302_novel_writing](https://github.com/302ai/302_novel_writing)** · ★ 18<br>网页小说写作工具：填书名、作者和简介建书，AI 先生成章节剧情规划再写章节正文，可选现代/古风/奇幻等文风，也能全自动写完整本<br><sub>方法：规划 · 风格</sub><br><sub>更新于 2025-08-26 💤 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 302.AI 在线产品的开源版，需 302.AI API；界面中英日三语</sub>

- **[Closure](https://github.com/AoharuCat/Closure)** · ★ 18<br>小说 IDE：先在结构化叙事状态上操控信息差、情绪弧与角色欲望再落笔，每章抽取世界事件分「事实/读者所知」两本账，改设定沿依赖图追踪下游影响<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-11 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 LumenStorm/OrisonSpace 的派生版，叠加叙事状态机、混合检索、情绪闭环、风格卡与内嵌 llmlint 去 AI 味；接 OpenAI 兼容端点或经 Antigravity CLI 调 Gemini；AGPL-3.0</sub>

- **[Novel](https://github.com/DuckTraDo/Novel)** · ★ 18<br>一句话 idea 生成整章，故事圣经/角色知情与秘密/伏笔/时间线组成文件记忆库，章后连续性审查并更新记忆，可挂 LoRA 文风<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-03 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Tauri 桌面应用（Rust 引擎）；可接本地 OpenAI 兼容推理，或调用本机已登录的 Claude Code / Codex 订阅；LoRA 权重在 Hugging Face</sub>

- **[StoryCanvas](https://github.com/ydsgangge-ux/StoryCanvas)** · ★ 18<br>在画布上摆放 35 类叙事块（角色、伏笔、冲突、读者情绪曲线等）并用 8 种关系连线，选故事卡搭初始结构，由五层 agent 管线生成细纲和正文，12 维审计<br><sub>方法：规划 · 理论 · 设定 · 修订</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文</sub><br><sub>💡 无开源许可证；也有剧本类块；支持 DeepSeek/OpenAI/Claude/Gemini/Ollama</sub>

- **[ai-webnovel-workflow](https://github.com/sanshanjianke/ai-webnovel-workflow)** · ★ 17<br>四层网文框架：种子层定故事愿景，多专家会议编排卷纲章纲并标注读者效果，叙事层查表把效果映射成视角/节奏/话语模式，渲染层按约束扩写正文<br><sub>方法：规划 · 理论 · 记忆 · 多智能体</sub><br><sub>更新于 2026-05-20 · 🧩 应用 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 作者自述只完成约 30%；每层另有 .claude/skills 版本；用世界书、RAG 历史、RAG 技法三类数据支撑</sub>

- **[Book-Writing-AI-Agent](https://github.com/Aftabbs/Book-Writing-AI-Agent)** · ★ 17<br>CrewAI 顺序五 agent 写书示例：规划（大纲、人物、世界）→分章写作（每章千字以上）→编辑润色→事实核查→排版出稿<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-11-04 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 单个 Jupyter notebook；用 Groq 上的 LLaMA-3-70B</sub>

- **[knowrite](https://github.com/knoai/knowrite)** · ★ 17<br>小说写作后端：多 Agent 接力完成大纲、写章、审稿、去 AI 味和读者反馈，配时序事实库、作者指纹、RAG 记忆与提示词自动进化<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-09 · ⚙️ 框架 · 多语言 · AGPL-3.0</sub><br><sub>💡 Node.js 后端服务，图形界面需另装 knoai/knowrite-ui；AGPL-3.0；自配 OpenAI 兼容 API</sub>

- **[novel-generator](https://github.com/mushroomfk/novel-generator)** · ★ 16<br>本地长篇工作台：导入资料建 FTS5+embedding 检索，生成整书架构与章节蓝图，逐章经正文生成→小说专用去 AI 改稿→一致性复查→核验，作者确认后写回<br><sub>方法：记忆 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-06-14 · 🧩 应用 · 中文</sub><br><sub>💡 应用名「稿匣」，Tauri + Vue + FastAPI；可接入 Obsidian Vault、支持旧稿接管</sub>

- **[pulpgen](https://github.com/frobwick/pulpgen)** · ★ 16<br>CLI 写书 agent：Gemini 先生成标题、梗概、人物和逐章摘要，再按疏密策略分批写章，最后交互式 AI 编辑，XML 补丁记录状态可续跑<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2025-04-10 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需 Gemini API、Python 3.13+；可导出 HTML/EPUB</sub>

- **[ai-novel-studio-lingshumiaobi](https://github.com/hshenwl/ai-novel-studio-lingshumiaobi)** · ★ 15<br>网文工业化平台：总纲→卷纲→章纲后走七步 agent 流水线（约束规划→写作→读者视角→编辑视角→20 维审核→修订去 AI 味→定稿回写角色/伏笔/Hook）<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-12 · 🧩 应用 · 中文</sub><br><sub>💡 Windows 本地安装版（Go 启动器 + Inno Setup 打包脚本）；内置 645+ 篇写作知识库供规划阶段生成约束；同作者的 hshenwl/ai-novel-generator-genwenniu 是同源版本</sub>

- **[ApiSaverWriter](https://github.com/Vaxue/ApiSaverWriter)** · ★ 15<br>Tauri 多端网文工作台：世界观、总纲、章纲到正文，章节记忆按固定资料→历史摘要→最近对话组装上下文；可拆书、蒸馏文风绑定写作，并去 AI 味<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-11 · 🧩 应用 · 中文</sub><br><sub>💡 客户端默认接作者的 ApiSaver 中转站，需在该站注册 Key；安装包发在飞书；内置书籍搜索下载和番茄/起点/飞卢扫榜</sub>

- **[LoreSmith](https://github.com/G-Pegasus/LoreSmith)** · ★ 15<br>长篇网文 Agent 运行时：LangGraph 编排章节规划、草稿、一致性检查、提交、评审与重写，章后沉淀摘要/时间线/关系/伏笔供后续检索<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-17 · 🧩 应用 · 中文</sub><br><sub>💡 React 前端 + Spring Boot 平台层 + Python 运行时；另附一份 skill/SKILL.md</sub>

- **[Mo-Shen](https://github.com/wwxxzz666/Mo-Shen)** · ★ 15<br>AgentScope 编排策划、世界观、角色、大纲、写作、审校、总编 7 个 agent 接力写小说，先 200 字试写定风格，大纲确认后逐章生成<br><sub>方法：规划 · 设定 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Web 工作台 + 微信小程序 + CLI/HTTP API；旧 LangGraph 版保留在 v1 标签</sub>

- **[jarvis-write](https://github.com/ynnyh/jarvis-write)** · ★ 14<br>包在 LLM 外的长篇控制层：时序故事圣经按章节区间记事实，伏笔四态调度，改大纲自动分析下游并级联重生成，名家范文正向锚定加量化 AI 味门禁<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-05 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 定稿另做叙事结构指纹检查；附漫剧、宣传片等制片工坊（只出提示词）；桌面版和在线试用需进群领邀请码</sub>

- **[novel-workspace-mcp](https://github.com/LiZh132707/novel-workspace-mcp)** · ★ 14<br>长篇小说工作区：世界观、人物、章纲、时间线、事实和伏笔存成可审计的项目状态，经本地网页、MCP 工具或 Codex Skill 调模型起草和审校<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 默认接 LM Studio 本地模型，也可接 OpenAI 兼容 API；界面支持英/中/日三语</sub>

- **[MyAINovel](https://github.com/sEwhappend/MyAINovel)** · ★ 13<br>桌面长篇流水线：标签化生成初始方案，全书大纲确认后拆章→小节规划→场景导演→对白心理→正文→审稿→改写→定稿，资料库检索并回写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-02 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 PySide6 桌面程序，项目以 .json/.md 文件夹保存；AGPL-3.0</sub>

- **[novel-agent](https://github.com/Lin-A1/novel-agent)** · ★ 13<br>MetaGPT 多 agent 写小说：情节架构师出整体架构→评审打分→修订，章节规划拆章定目标，审阅者读前章给下章指导，写手逐章写<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-01-13 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 基于 MetaGPT；附生成样例 novel.txt；仓库无许可证</sub>

- **[novel-app](https://github.com/gelijunge22-code/novel-app)** · ★ 13<br>自托管写作台：出方案→挑刺→取料查证→写正文→复审改稿各为独立模型调用，可多角色分工；世界引擎存主体状态检测设定冲突，568 条规则查 AI 味<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-22 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 FastAPI 后端 + 网页 + 安卓壳，仓库附带 apk；世界引擎、讨论/计划/执行三模式等思路与 notnotype/neuro-book 相近，但为独立 Python 实现</sub>

- **[novel-multi-agents](https://github.com/QSPBU-LONG/novel-multi-agents)** · ★ 13<br>OpenAI Agents SDK 五 agent：大纲专家→角色开发专家深化人物弧线→章节撰写→编辑评估并给修改建议，由协调者串联<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2025-03-13 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 默认本地 Ollama qwen2.5:14b，也可接在线模型；仓库未声明许可证</sub>

- **[novelforge](https://github.com/LunaRime/novelforge)** · ★ 13<br>小说 IDE：AI 出大纲和细纲后逐章流式写，5 角色编辑部并行审阅加权评分，多稿择优，定稿后提取剧情、角色声音和伏笔并做三级摘要记忆<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 Electron 桌面应用，本地 RAG（SQLite + LanceDB）；界面中/英/俄三语</sub>

- **[autoNovel](https://github.com/youyouxia263/autoNovel)** · ★ 12<br>悬疑/言情长篇生成器：生成前提、世界观（地点、时间线）和人物卡，再出逐章大纲写章节、章后摘要，并做一致性、节奏和情节逻辑检查与修复<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-01-12 💤 · 🧩 应用 · 多语言</sub><br><sub>💡 界面中文、默认提示词英文；支持 Gemini、通义千问和 OpenAI 兼容接口</sub>

- **[Hi-Story](https://github.com/mofeifeifei/Hi-Story)** · ★ 12<br>本地长篇工作台：设定与题材约束→全书大纲和分卷→章节细纲→正文，生成后查衔接、因果、人设、重复并修订，定稿后抽章节记忆供后文用<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-08-23 · 🧩 应用 · 中文</sub><br><sub>💡 Python + React + SQLite，Windows 下用 bat 启动；支持 OpenAI 兼容和 Anthropic 协议，也有 CLI</sub>

- **[Moshu](https://github.com/HXSLtim/Moshu)** · ★ 12<br>作者主导的长篇工具：Story Bible 事实与事件账本按目标章取当时有效设定，LangGraph 三阶段续写配 Chroma RAG，AI 产出都需作者审核<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 中文</sub><br><sub>💡 与 huihuijiangqiang/moshu 同名但不是同一项目；六维章节审核后端已实现，独立入口待露出</sub>

- **[Novel-Claude](https://github.com/wzxsph/Novel-Claude)** · ★ 12<br>CLI 依次生成金手指→梗概→大纲→世界设定→蓝图，再分卷细纲、按章写作，ChromaDB RAG 检索记忆，审核与实体跟踪，skill 插件注入上下文<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-08-09 · ⚙️ 框架 · 中文 · GPL-3.0</sub><br><sub>💡 作者自称新手练手的实验项目；RAG 嵌入需智谱密钥，支持智谱 Batch API</sub>

- **[NovelForger](https://github.com/cedrusdang/NovelForger)** · ★ 12<br>LangGraph+Gemini notebook：按英雄之旅、三幕、七点结构定情节，人物贴合节拍生成，章节取结构化元数据和嵌入记忆，另一 agent 打分返工<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2025-04-21 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 Kaggle 上可运行的课程项目 notebook，需 Gemini API；人工把关可选；附越南语样例</sub>

- **[ai-novel](https://github.com/AI-Practical-Lab/ai-novel)** · ★ 11<br>网页长篇写作台：书架→分卷→章节三级结构，先定剧情路标并自动生成过渡细纲，再按细纲流式写正文，自动带入设定集、大纲和上一章<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-07 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 README 写后端是 Express，仓库实际以 Java 后端为主，文档与代码不一致；兼容 OpenAI/DeepSeek 接口；有在线体验站</sub>

- **[ai-novel](https://github.com/silly-zero/ai-novel)** · ★ 11<br>Go+Eino 多 agent 写长篇：架构师定大纲，人设/设定 agent 维护角色卡与世界观，主编拆场景卡，资料员规划 RAG 检索，审查员不合格打回重写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-01 · ⚙️ 框架 · 中文</sub><br><sub>💡 只有后端服务（REST/SSE），默认智谱 GLM 与 embedding-3，需 PostgreSQL；根目录有无扩展名的 main、server 文件（疑似编译产物）</sub>

- **[AI-StorySmith](https://github.com/takimdigital/AI-StorySmith)** · ★ 11<br>本地模型写书脚本：先按主角/目标/危机/独特点生成前提，再出标题、目录、每章内容类型并细化，最后逐章级联写作，中间结果落盘可续跑<br><sub>方法：规划</sub><br><sub>更新于 2025-10-23 💤 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 面向 LM Studio / Ollama 本地模型</sub>

- **[AI_NovelWriter](https://github.com/ATboy-web/AI_NovelWriter)** · ★ 11<br>情节、世界观、写手、审校、编辑五 Agent 流水线，审校意见回流修订到过质量阈值；每章检测决策点，可分出平行世界线与世代传承<br><sub>方法：人物 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-18 · 🧩 应用 · 中文</sub><br><sub>💡 Windows EXE / Android APK 在 Releases，仓库含完整 Python 源码；支持插件与 MCP</sub>

- **[huohuo-drama](https://github.com/appolloqin/huohuo-drama)** · ★ 11<br>数字作家批量写连载：brief→正文→一致性审校，章末强制写「触发→过程→结果」因果变更记录并注入后文，配四层记忆；小说可再改编成短剧出片<br><sub>方法：理论 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 多语言 · 40 个 skill</sub><br><sub>💡 含 100+ 个题材写作 skill、AI 检测与去味改写；同时是带多渠道支付的短剧/小说 SaaS；仓库无许可证</sub>

- **[Moyun](https://github.com/Not1a-del/Moyun)** · ★ 11<br>纯前端长篇写作台：大纲→细纲→正文，细纲按 ID 钉选本章活跃角色和世界资料作为生成上下文，角色资料分三档，AI 草案逐项审阅<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文</sub><br><sub>💡 CC BY-NC 4.0，禁止商用；可直接在 GitHub Pages 使用，数据存浏览器；兼容白鸟扩展和 MOD</sub>

- **[One-flower](https://github.com/sleepykino/One-flower)** · ★ 11<br>AI 小说工作台：摘要链+世界书 RAG+角色卡拼上下文续写，长文按节拍规划→逐拍生成→接缝自检，总纲、文风 Skill 包与 hook.md 校验三层约束<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-07 · 🧩 应用 · 中文 · 19 个 skill · Apache-2.0</sub><br><sub>💡 附 19 个文风 SKILL.md（金庸、老舍、海明威冰山等）；另含小说→剧本→分镜转化</sub>

- **[story](https://github.com/ATAIN000/story)** · ★ 11<br>长篇写作台：315 题材与 20 层世界观向导→宏观规划；每章先出决策卡再生成，抽取事件后经七步硬约束验证（含 Z3）自动修正，事件溯源可回滚<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-10-07 · 🧩 应用 · 中文</sub><br><sub>💡 单用户部署；首次启动为 Mock 演示模式</sub>

- **[Story-OS](https://github.com/tanao521/Story-OS)** · ★ 11<br>章节级滚动写长篇：先出故事蓝图和人物/世界/写作约束，逐章规划→草稿→修订，过人工审核闸门才进正史；摘要、Chroma 向量库和 Obsidian 做长期记忆<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-08-03 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 本地 FastAPI Web UI + CLI；支持 DeepSeek 与本地模型分工；另有实验性「模拟器模式」边玩边写</sub>

- **[BlockWriter](https://github.com/FartyPants/BlockWriter)** · ★ 10<br>text-generation-webui 扩展：按场景分块写作，每块写明该场景要发生什么再生成，可随时改任一块的指令或正文并重生成，全文随之动态拼接<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2024-01-13 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需放到 text-generation-webui 的 extensions/BlockWriter；实验性 WIP；无许可证</sub>

- **[novel-copilot](https://github.com/doctoroyy/novel-copilot)** · ★ 10<br>Story Bible→大纲→逐章/批量生成，滚动摘要+角色状态快照+伏笔依赖图+节奏控制注入上下文，多维 QC（一致性/节奏/目标）不过即进修复循环<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-26 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 部署在 Cloudflare Workers，含 Web 与 React Native App；另带动画/视频/TTS 模块；README 英文，章节提示词为中文</sub>

- **[novel-writing-agent](https://github.com/lianyichuan/novel-writing-agent)** · ★ 10<br>长篇写作管理系统：维护作者意愿、主线剧情脉络、人物关系和 Agent 执行手册等设定文档，剧情追踪面板看多条主线，调模型生成章纲和正文<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2025-07-25 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 默认接 Gemini API</sub>

- **[agent](https://github.com/sfxyn/agent)** · ★ 9<br>AI 先分析提示定类型、视角、结构等参数，再依次生成概念、角色、总纲和章纲，每章多轮生成凑足字数，可指定作家文风模仿，状态存档可续写<br><sub>方法：规划 · 人物 · 风格</sub><br><sub>更新于 2025-03-17 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 测试版；默认豆包/火山方舟接口；仓库未声明许可证；README 里的克隆地址是占位仓库名</sub>

- **[ai-novel](https://github.com/leehong0704/ai-novel)** · ★ 9<br>设定→章纲→正文，正文中插【标记】让 AI 只重写标记处；定稿时自动抽取人物变化同步角色卡，并增量更新全书梗概和近三章回顾<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-04-13 💤 · 🧩 应用 · 中文 · EPL-1.0</sub><br><sub>💡 Python 桌面应用，支持 DeepSeek/OpenAI/Gemini；仓库另附 Windows 打包 zip（release/ai-novel.zip），源码完整</sub>

- **[aiAIfiction](https://github.com/liaoma1993/aiAIfiction)** · ★ 9<br>从策划对话到世界观、角色势力、卷/弧/章节蓝图逐级生成正文；上传样本抽取写法 Skill 跨项目复用，按审计结果定位到句/段/整章局部修复<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-24 · 🧩 应用 · 中文</sub><br><sub>💡 FastAPI + React；默认管理员账号密码写在 README，部署需改；无 License</sub>

- **[NovelizeAI](https://github.com/paradroidlabs/NovelizeAI)** · ★ 9<br>Gemini 长篇写作应用：按类型、视角、语调等修饰项分三阶段出概念、人物设定和情节大纲，再逐章生成，根据评审反馈迭代<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-05-01 · 🧩 应用 · 英文</sub><br><sub>💡 源自作者早期的 Wordware 版 para-droid-ai/novella-xl-15；需 Gemini API</sub>

- **[AI_novelsTool_obsdian](https://github.com/Aurirlk/AI_novelsTool_obsdian)** · ★ 8<br>PyQt 桌面写作台：大纲师、码字工、督察、评论家等 12 个智能体分工，7 模块记忆追踪角色状态、钩子与大事记，配拆书分析和批评师审稿<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-09-08 · 🧩 应用 · 中文 · 57 个 skill</sub><br><sub>💡 内置约 49 个网文 skills（103 个 SKILL.md），据作者说明部分整合自 GitHub 其他项目；无 License；需自带 API</sub>

- **[LLMWriter](https://github.com/zhangwen-max/LLMWriter)** · ★ 8<br>RAG 长篇写作：世界观圣经、角色卡、阶段摘要、近三章记忆、上章结尾五层上下文，按写作计划多路检索 Qdrant，每章写完抽取事件/事实/关系/伏笔入库<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-22 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 默认 Qwen-Plus；未声明许可证</sub>

- **[Novel-factory](https://github.com/YonRen-code/Novel-factory)** · ★ 8<br>多智能体+确定性编排：卷→弧→段→章四层规划，角色/物品/势力三账本须附正文引证校验，伏笔排期状态机，异族模型候选盲评，禁泄扫描与 26 项批末体检<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-14 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 Java 17 / Spring AI；Qdrant 向量增强可选；ChatGPT 套餐授权通道为实验性功能</sub>

- **[Novel-IDE](https://github.com/KurohaneKaoruko/Novel-IDE)** · ★ 8<br>Tauri 长篇写作 IDE：AI 续写/改写/规划，Planner 拆任务执行，改稿默认先出审阅建议逐条采纳，自动维护角色状态与伏笔索引并可手工锁定<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-08 · 🧩 应用 · 中文 · GPL-3.0</sub>

- **[AI-Web-Novel-Assistant](https://github.com/XZQINSYSU/AI-Web-Novel-Assistant)** · ★ 7<br>PyQt6 网文桌面工具：全局梗概、人物卡、卷梗概、章细纲分层设定，按细纲加前文逐章写，挂机模式自动补全卷章写完全书，一键修复查人名错误和吃书<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-02-23 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 默认 DeepSeek-Reasoner，兼容 OpenAI 接口；example/ 附两部生成的示例小说（docx）</sub>

- **[AuctorForge](https://github.com/Te9ui1a/AuctorForge)** · ★ 7<br>本地文件型网文工作台，内置长篇技能包：可从零、带稿或拆样板书起步，设定→总纲/卷纲/章纲→逐章写作并更新角色快照与伏笔表→主编式质检<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-05-05 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 强调 AI 做可控助手、作者保留判断；流程由仓库内 skill-packs/novel-flow-kit 0.1.5 驱动</sub>

- **[AutoWrite](https://github.com/Linmoqian/AutoWrite)** · ★ 7<br>Rust/Tauri 桌面写作应用：先生成世界观、角色和章节大纲，再用三层提示词逐章写正文，可按内容配图并多格式导出<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文 · 2 个 skill</sub><br><sub>💡 README 很简略；需 DeepSeek API，配图用魔搭 Z-Image</sub>

- **[museflow](https://github.com/nhsprite/museflow)** · ★ 7<br>命令行工具：一句话梗概起步，LangGraph 编排世界观、角色、故事弧、章纲、起草、伏笔、一致性、修复等 10 类 agent 逐章写长篇，题材包可自定义<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-31 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 npm 全局安装；每章写完自动检查字数、连续性和伏笔，修不好时出报告请求整章重写</sub>

- **[novel-smith](https://github.com/huanweide/novel-smith)** · ★ 7<br>本地长篇工坊：探讨模式 11 步对话建世界观，章后自动抽取建角色卡/世界书，近章全文+摘要+远期压缩分层记忆，15 维拆书仿写，本地规则引擎检测 AI 味<br><sub>方法：设定 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Next.js + 本地 SQLite；去 AI 味检测可离线、无需 API Key</sub>

- **[novel-writer-master](https://github.com/qiuxinyuan321/novel-writer-master)** · ★ 7<br>小说伴写工具：Story Bible 管角色口癖、世界观硬规则和伏笔，章→场景分层大纲设必达检查点，生成时注入前文摘要，并做一致性检测和降 AI 率改写<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-10 💤 · 🧩 应用 · 中文</sub><br><sub>💡 降 AI 率对标朱雀检测（332 词黑名单、统计分析、定向改写）；可按任务路由不同模型</sub>

- **[novel_generator](https://github.com/2572873335/novel_generator)** · ★ 7<br>按 Anthropic 长时 agent 方案写小说：初始化 agent 建大纲和人物，管线经草稿、一致性检查、润色，Python 记情绪债账本，熔断防无限重写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-20 💤 · ⚙️ 框架 · 多语言 · 30 个 skill · MIT</sub><br><sub>💡 最后更新 2026-03，因情绪债账本和重写熔断的设计少见而收；带 PyQt6 界面</sub>

- **[Novelex](https://github.com/CayleyZ/Novelex)** · ★ 7<br>人审把关的长篇网文工作台：Plan 两轮出大纲，Write 先出多份细纲候选再写正文、审计、锁章，批准后回写事实账本、伏笔和角色状态<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-04-30 · 🧩 应用 · 中文</sub><br><sub>💡 PolyForm Noncommercial 许可；可绑定风格指纹、范文 RAG 和黄金开头库（建索引需智谱 embedding）</sub>

- **[RedQuill](https://github.com/UrmsOne/RedQuill)** · ★ 7<br>小说创作平台：按故事核心→世界观（修炼体系、社会结构）→角色档案→大纲→章节逐级生成，写章时自动注入前章摘要和正文，提示词模板可编辑<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2025-11-17 💤 · 🧩 应用 · 中文</sub><br><sub>💡 Go + Vue3 + MongoDB；接入 OpenAI、DeepSeek、豆包、千问等</sub>

- **[sopher.ai](https://github.com/cheesejaguar/sopher.ai)** · ★ 7<br>从作者简介到成书：多智能体依次做概念、大纲（可人工批准）、分批起草章节、编辑润色与连续性检查，配故事圣经和章节历史<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 英文 · 13 个 skill · MIT</sub><br><sub>💡 线上是付费 SaaS（预付 credits），源码 MIT 可自托管</sub>

- **[word-compiler](https://github.com/2389-research/word-compiler)** · ★ 7<br>长篇小说上下文编译器：设定圣经+场景计划按系统/章/场景三环组装并控 token 预算，逐块生成后人工审阅，审计禁用词与潜台词，从修改差异学规则<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-04-16 💤 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 需要 Anthropic API key</sub>

- **[ai-novel-generator](https://github.com/Cody8722/ai-novel-generator)** · ★ 6<br>命令行长篇生成器：先出大纲再逐章写，每章重建提示词并传入上一章结尾，配角色弧线强制器、冲突升级器和事件依赖图维持连贯<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-01-29 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 默认走硅基流动 API（GLM-4、DeepSeek R1 等）；README 侧重速度和成本，方法模块要看 core/ 代码</sub>

- **[autow](https://github.com/Alexsun1one/autow)** · ★ 6<br>长篇小说引擎库：规划→写作→审稿→修订→润色→校验→出版七阶段状态机，编辑部多角色分工，质量门打分决定返修，维护角色矩阵与伏笔板<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-26 · ⚙️ 框架 · 中文 · AGPL-3.0</sub><br><sub>💡 从商业产品「卷舍」抽出的引擎内核，附 CLI；需自备 OpenAI 兼容 API；AGPL-3.0</sub>

- **[kealin-AI-novels](https://github.com/XN-289/kealin-AI-novels)** · ★ 6<br>反 AI 味网文工作台：结构化角色卡、逐章场景控制（角色、节奏、情绪、目标）、分层记忆和五维一致性检查，生成时内置禁用词，生成后四阶段去味重写<br><sub>方法：人物 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-11 · 🧩 应用 · 中文</sub><br><sub>💡 README 自述借鉴 SillyTavern 角色卡和 Novelcrafter 场景控制；Windows 下用 bat 启动；仓库无许可证</sub>

- **[longform-ai](https://github.com/makieali/longform-ai)** · ★ 6<br>长文生成库：先生成并审批大纲再逐章写，滚动摘要和人物追踪保持连贯，字数不足自动扩写，检测拒答后重试；小说、剧本可用<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-02-13 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 npm 包，支持 8 家模型；通用长文引擎，也生成技术文档、课程等非虚构内容</sub>

- **[million-word-novel-ai-creator](https://github.com/kevinchcn/million-word-novel-ai-creator)** · ★ 6<br>LangChain + DeepSeek 长篇系统：由创意生成大纲、人物、世界观，章级/卷级分层摘要做长时记忆，按人物、情节、世界观规则查一致性，可批量写章<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2025-12-14 💤 · 🧩 应用 · 中文</sub><br><sub>💡 Streamlit 界面和命令行；未声明许可证</sub>

- **[novel-continuation](https://github.com/hsong6809-boop/novel-continuation)** · ★ 6<br>导入已有章节续写：总纲→分卷→章纲三层大纲约束，指定参考章节锚定文风，自动组装前文/角色/伏笔/世界观上下文，自动提取伏笔与时间线并续写自审<br><sub>方法：规划 · 记忆 · 风格</sub><br><sub>更新于 2026-05-11 · 🧩 应用 · 中文</sub><br><sub>💡 FastAPI + React 本地应用；面向续写作者已有长篇；受小米 MiMo 激励计划赞助</sub>

- **[Novel-Engine](https://github.com/Jackela/Novel-Engine)** · ★ 6<br>自托管长篇写作 IDE：章节挂接大纲节拍，Copilot 续写/重写以提案形式待作者采纳，按标题触发注入稳定状态的人物/世界词条，可按序整书生成<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 多语言 · 5 个 skill · MIT</sub><br><sub>💡 Node.js + SQLite，Docker 部署；界面中英双语；本地开发默认 mock provider，需自配 DashScope/DeepSeek 等</sub>

- **[Plotforge](https://github.com/1while1/Plotforge)** · ★ 6<br>本地 AI 长篇工坊：大纲节拍与节奏热力条，人物/世界观/事件账本由 AI 提案、人工采纳，本地向量检索章节，作家卡（人设+指纹+范文）管理文风<br><sub>方法：规划 · 记忆 · 风格</sub><br><sub>更新于 2026-10-11 · 🧩 应用 · 中文 · MIT</sub>

- **[Story-Creator](https://github.com/renfufei/Story-Creator)** · ★ 6<br>网文六步流程：世界观→角色卡→分卷与逐章大纲→带上下文逐章写作→润色→五项一致性校对自动修正，可全自动出书并断点续跑<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 中文</sub><br><sub>💡 Java 21 + Spring Boot；无开源许可证；另带 TTS、角色立绘等附加功能</sub>

- **[StoryBook-AI](https://github.com/ocedo-apps/StoryBook-AI)** · ★ 6<br>本地小说写作工具：Story Bible 作为设定事实源，写作模型起草正文、审阅模型复核，作者逐次决定取舍，附 Analyze 分析<br><sub>方法：记忆 · 修订 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 只连 Ollama / LM Studio 等本地 OpenAI 兼容服务，刻意屏蔽云端 API；界面支持英语、瑞典语、挪威语；姊妹项目 ocedo-apps/Sandbox-AI；2026-09 新建，星数少</sub>

- **[StoryClaw](https://github.com/leistung/StoryClaw)** · ★ 6<br>LangGraph 四角色写长篇：架构师规划本章→写手续写→连续性检查→编辑打分，不达标最多打回 3 次；用设定、伏笔、支线、情感弧等状态文件保持一致<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-28 · 🧩 应用 · 中文</sub><br><sub>💡 无开源许可证；状态文件命名（pending_hooks、subplot_board、emotional_arcs、character_matrix 等）与 InkOS 相同，疑似参考其设计，用 Python 重写</sub>

- **[xsun_novel_agent](https://github.com/xiaoSun1997/xsun_novel_agent)** · ★ 6<br>LangGraph 长篇流水线：Milvus 检索参考作品和写作理论出大纲待确认，逐章写后用 Neo4j 人物关系图谱查一致性，审稿不过重写，每 10 章总结<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-02-09 💤 · ⚙️ 框架 · 中文</sub>

- **[Cloud-Dream-Novel-Agent](https://github.com/XiongJL/Cloud-Dream-Novel-Agent)** · ★ 5<br>长篇小说桌面工作台：故事线/情节点/角色/世界观资料库配 RAG 检索，六种视角 Agent 先出计划再生成草稿，原文对照审核后事务性写回<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 Electron + LangGraph Python Runtime；可经 MCP 接入 Codex / Claude Code 等本地 CLI；Releases 提供安装包</sub>

- **[dodo](https://github.com/653390665/dodo)** · ★ 5<br>本地小说写作助手：开书向导生成设定/大纲/正文候选，编辑器实时命中人物道具做故事记忆，去 AI 味审稿给证据并出精修预览，确认后才写入 Canon<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 中文</sub><br><sub>💡 仓库名 dodo，产品名 InkFlow 墨影；未附开源许可证；需自配模型 API Key</sub>

- **[InkMind](https://github.com/jastfkjg/InkMind)** · ★ 5<br>长篇写作工作台：结合作品设定、人物、备忘和前文生成章节概要与正文，支持续写、选区扩写润色，生成后可自动质量评估并预览确认<br><sub>方法：人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 Web 与 macOS 桌面版；助手需 Anthropic 兼容连接；方法较常规</sub>

- **[novel-agent](https://github.com/HuangLeijiana/novel-agent)** · ★ 5<br>LangGraph 串起 12 个 agent：选题→世界观→人物→场景级章纲→两遍写作→编辑/连续性/读者模拟/对抗审稿→精修，记忆管理器追踪事实与伏笔<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-21 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 README 英文、提示词模板为中文；支持 ModelScope 免费额度、DeepSeek、Claude、Ollama 等</sub>

- **[novel-agent-workflow](https://github.com/realwindjpn/novel-agent-workflow)** · ★ 5<br>文件优先的关卡式流程：访谈→概念→故事圣经→总/卷/章纲逐级 PASS 锁定后发章，作者起草，编辑（去 AI）、读者、军事/科学顾问独立审，改稿重置关卡<br><sub>方法：规划 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-09 · ⚙️ 框架 · 多语言 · 5 个 skill · Apache-2.0</sub><br><sub>💡 Python CLI + 5 个 SKILL.md；面向长篇中文科幻网文；作者起草角色可由人或 AI agent 承担，工具中立</sub>

- **[novel-ai-agent](https://github.com/redmaplewww/novel-ai-agent)** · ★ 5<br>一句话简介→设定集/世界观（硬约束）→卷章大纲→分章写作，注入连续性约束与灵感库；写后审校偏离度、节奏曲线打分、文风指纹漂移检测、时间线校核<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-07-11 · ⚙️ 框架 · 中文</sub><br><sub>💡 CLI / Gradio WebUI / 飞书 Bot 三种入口；默认 DeepSeek，语义搜索用硅基流动 bge-m3</sub>

- **[novel-engine-template](https://github.com/ohh567/novel-engine-template)** · ★ 5<br>Director 章节设计→Writer 初稿→Critic 评审→不过则局部 patch 修订→质量门禁→Archivist 按证据段更新状态库的长篇模板<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-11 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 需自行填写 state_db 角色/世界规则/伏笔与分卷节拍；OpenAI 兼容接口</sub>

- **[novel-generator](https://github.com/ausdai-dev/novel-generator)** · ★ 5<br>PySide6 桌面小说生成器：按类型、文风、人物数生成书名和梗概，再出章节大纲并逐章扩写，可选翻译成其他语言<br><sub>方法：规划</sub><br><sub>更新于 2024-12-31 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需 OpenAI 兼容接口；仓库附两部生成样例</sub>

- **[novel-novel-generator](https://github.com/mike-cramblett/novel-novel-generator)** · ★ 5<br>一键长篇：先生成 story bible 并给主要角色注入语言指纹，规划师出逐章大纲，写手逐章写，连贯性编辑更新摘要并把新发现的 AI 套话加入禁用表<br><sub>方法：规划 · 人物 · 记忆 · 去 AI 味</sub><br><sub>更新于 2025-12-30 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需 Gemini API；API 密钥暴露在浏览器，只宜本地运行</sub>

- **[novelcraft-genre-weaver](https://github.com/SteakWrangler/novelcraft-genre-weaver)** · ★ 5<br>仿出版社分工的 23 个专职 agent：头脑风暴（类型预期、世界、人物、情节）→主题和章节场景大纲→五类写手分写→多维审稿后行编辑重写<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-08 · 🧩 应用 · 英文</sub><br><sub>💡 可混搭多种类型和套路；仓库附几部生成的样书</sub>

- **[novelops](https://github.com/a11003070312/novelops)** · ★ 5<br>网文框架：每章走上下文组装→情绪板→两稿制写作→脚本扫禁用词→人审→状态更新，创作指令极简、禁忌全交事后脚本，YAML 状态加向量检索<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-03-22 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 最后更新 2026-03，因「极简创作指令 + 事后脚本门控」的思路少见而收；有监督和自主段落两种模式</sub>

- **[novelos](https://github.com/ayermac/novelos)** · ★ 5<br>桌面长篇工作台：LangGraph 串起规划、编剧、执笔、润色、审核、记忆整理、发布 agent，用故事契约约束，按正文证据检查爽点兑现和数值继承<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文 · 11 个 skill · MIT</sub><br><sub>💡 Electron + 本地 FastAPI；目前只打包 macOS 版</sub>

- **[NovelWriter](https://github.com/KudoShusak/NovelWriter)** · ★ 5<br>Ollama 本地长篇流水线：情节（起中结）→人物卡和世界设定→章节/场景大纲→逐场景写作，状态存 JSON，手改场景后可重建一致性状态<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-30 💤 · ⚙️ 框架 · 日文 · MIT</sub><br><sub>💡 默认输出日语</sub>

- **[StoryMemory-Studio](https://github.com/Jackeyhate9/StoryMemory-Studio)** · ★ 5<br>SQLite 结构化记忆库存人物状态、伏笔、时间线和世界规则，长上下文编排逐章生成；写后做穿帮检测、伏笔管理、文风学习与 AI 腔治理，可转短剧/漫画改编<br><sub>方法：记忆 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-06 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 受 OpenHuman 长期记忆思想启发（自述非 fork、未复制代码）；Streamlit 本地应用，另提供 Windows exe；支持 DeepSeek/GLM/Ollama 等</sub>

- **[storyteller](https://github.com/johannhartmann/storyteller)** · ★ 5<br>自主生成多章故事：从英雄之旅、起承转合等 6 种叙事结构中选型并按章/场景分配篇幅，追踪情节线与每个角色的知情状态，可联网调研世界观，分场景/章/文风多级修订<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-01-26 💤 · ⚙️ 框架 · 多语言</sub><br><sub>💡 支持 Gemini/OpenAI/Anthropic，12 种语言模板，可模仿指定作者文风；可选 Tavily 调研与 Azure TTS 有声书；2026-01 后未更新</sub>

#### 研究代码（4）

- 🌟 **[RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT)** · ★ 999<br>用自然语言模拟 LSTM：每步写一段正文和下一段计划，改写短期记忆，段落摘要存入可语义检索的长期记忆；人可选改计划共写任意长度小说<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2024-05-15 💤 · 🎓 研究 · 英文 · GPL-3.0</sub><br><sub>💡 论文 arXiv 2305.13304；依赖 OpenAI API；也演示了互动小说用法；开源模型适配版见 jackaduma/Recurrent-LLM</sub>

- **[ReasoningNCP](https://github.com/Alex-Gurung/ReasoningNCP)** · ★ 78<br>论文代码：以 VR-CLI 奖励（计划能否提升下一章原文似然）做强化学习，训练模型先推理下一章计划再续写长篇，含数据构建、SFT/RL 与评测<br><sub>方法：规划</sub><br><sub>更新于 2025-04-19 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 Learning to Reason for Long-Form Story Generation（arXiv 2503.22828）；训练需 GPU</sub>

- **[Generating-Long-form-Story-Using-Dynamic-Hierarchical-Outlining-with-Memory-Enhancement](https://github.com/Qianyue-Wang/Generating-Long-form-Story-Using-Dynamic-Hierarchical-Outlining-with-Memory-Enhancement)** · ★ 19<br>论文 DOME 的代码：先出粗大纲，写作中动态细化分层大纲，用 neo4j 知识图谱记忆检测并消解前后矛盾，生成长篇故事<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2024-10-12 💤 · 🎓 研究 · 英文</sub><br><sub>💡 输入数据沿用 DOC/Re3；需自建 neo4j 和 OpenAI 兼容接口</sub>

- **[StoryBox](https://github.com/amcghm/StoryBox)** · ★ 19<br>沙盒中让多个角色 agent 自下而上互动产生事件，再结合自上而下的叙事规划把模拟结果组织成长篇故事（AAAI 2026 论文代码）<br><sub>方法：规划 · 多智能体 · 模拟</sub><br><sub>更新于 2026-03-27 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 需 OpenAI API；代码目录沿用 Generative Agents 的 reverie 沙盒结构</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# oh-story-claudecode
npx -y skills add zenstory-ai/oh-story-claudecode --agent claude-code
# webnovel-writer
npx skills add lingfengQAQ/webnovel-writer
# chinese-novelist-skill
npx skills add PenglongHuang/chinese-novelist-skill
# Chinese-WebNovel-Skill
npx skills add Tomsawyerhu/Chinese-WebNovel-Skill
# Openwrite
npx skills add LiPu-jpg/Openwrite
# awesome-novel-agent
npx skills add modoojunko/awesome-novel-agent
# novel-creator-skill
npx skills add leenbj/novel-creator-skill
# oh-story-dsh
npx skills add zenstory-ai/oh-story-dsh
# Novel-Control-Station-Skill
npx skills add jingtai123/Novel-Control-Station-Skill
# story-skills
npx skills add danjdewhurst/story-skills
# novel-writer-skills
npx skills add wordflowlab/novel-writer-skills
# Lorn.NovelWriteSkills
npx skills add lornshrimp/Lorn.NovelWriteSkills
# webnovel-writer-opencode
npx skills add lujih/webnovel-writer-opencode
# sumeru
npx skills add xindoo/sumeru
# Distilled-Novel-Toolbox
npx skills add dama-cyber/Distilled-Novel-Toolbox
# novel-kit
npx skills add t59688/novel-kit
# awesome-novel-studio
npx skills add MJbae/awesome-novel-studio
# tianming-skill
npx skills add zy-zmc/tianming-skill
# book-genesis-studio
npx skills add felipelobomotta-blip/book-genesis-studio
# novel-harness
npx skills add manhai934/novel-harness
# Claude-Book
npx skills add ThomasHoussin/Claude-Book
# ai-novel-writer
npx skills add Jieice/ai-novel-writer
# novel2agent-jp
npx skills add kgmkm/novel2agent-jp
# ani-book-skill
npx skills add ExplosiveCoderflome/ani-book-skill
# padwriter
npx skills add cheyann4399/padwriter
# dsh-novel-writer
npx skills add akira399/dsh-novel-writer
# long-novel-writer
npx skills add jiaw-Zh/long-novel-writer
# chinese-webnovel-skills
npx skills add tance-mang/chinese-webnovel-skills
# book-writer
npx skills add tobyilee/book-writer
# fanqie-novel-skill
npx skills add 304769384-png/fanqie-novel-skill
# DaisyWriter
npx skills add ricky-theseus/DaisyWriter
# dreampowers
npx skills add skyfiredao/dreampowers
# chinese-longnovel-skill
npx skills add xiaofeng-928/chinese-longnovel-skill
# book-os
npx skills add forsonny/book-os
# oh-story-claudecode
npx skills add qin1473692580-ux/oh-story-claudecode
# ai-fiction-writer
npx skills add Wooooooooood/ai-fiction-writer
# The-Crucible-Writing-System-For-Claude
npx skills add forsonny/The-Crucible-Writing-System-For-Claude
# ultimate-novel-creation-skill
npx skills add Fly143/ultimate-novel-creation-skill
# novel-writer
npx skills add AI-Practical-Lab/novel-writer
# craft-companion
npx skills add qcx1919788736-collab/craft-companion
# bmad-book-builder
npx skills add jblemee/bmad-book-builder
# novel-pro
npx skills add lgz-star/novel-pro
# mimoCode-story
npx skills add nihaoshi/mimoCode-story
# novel-writer
npx skills add sailoumili/novel-writer
# thriller
npx skills add pajama-studio/thriller
# novel-master
npx skills add bbroot/novel-master
# novelops-skill
npx skills add qiyan233/novelops-skill
# vibe-noveling
npx skills add TulanCN/vibe-noveling
# dsh-cuigengji-plugin
npx skills add mistnest/dsh-cuigengji-plugin
# dsh-novel-writer
npx skills add siweina/dsh-novel-writer
# openclaw-novel-writer-skill
npx skills add alever520/openclaw-novel-writer-skill
# speckit-preset-fiction-book-writing
npx skills add adaumann/speckit-preset-fiction-book-writing
# xt-webnovel-writing
npx skills add xiaotiewinner/xt-webnovel-writing
# book-writer-skill
npx skills add kshanxs/book-writer-skill
# webfiction-write
npx skills add qingyabailu-git/webfiction-write
# dsh-novel-forge
npx skills add huangziyuan-general/dsh-novel-forge
# novel-flow-one-by-one
npx skills add ZhangDongyang800/novel-flow-one-by-one
# hermes-novel-generator
npx skills add rwcrosk-arch/hermes-novel-generator
# long-novelist-skill
npx skills add tianshiemo7/long-novelist-skill
# novel-master
npx skills add dashenbibi/novel-master
# novel-skills
npx skills add PhosAQy/novel-skills
# writeAgent
npx skills add Ddhjx-code/writeAgent
# novel-writer-skills
npx skills add Shine8592/novel-writer-skills
# silver-novel-skills
npx skills add jialanhu0915/silver-novel-skills
# claude-novel-skill
npx skills add mane23-ai/claude-novel-skill
# novel-skill
npx skills add mave99a/novel-skill
# opencreator-novel
npx skills add xwcai999/opencreator-novel
# wangwen-writing-skill-kit
npx skills add hyi1233/wangwen-writing-skill-kit
# long-novel-generator
npx skills add jiaw-Zh/long-novel-generator
# novel-assistant-skill
npx skills add duiniwukenaihe/novel-assistant-skill
# plotrail
npx skills add waylean/plotrail
# webnovel-writer-hermes
npx skills add starMagic/webnovel-writer-hermes
# dsh-novel-solo
npx skills add Tkingxiao/dsh-novel-solo
# scriveno
npx skills add hannsxpeter/scriveno
# wangwenwrite-skill
npx skills add Thatgfsj-easyRep/wangwenwrite-skill
# DSH-Novelist
npx skills add KurohaneKaoruko/DSH-Novelist
# human-novel-writer
npx skills add huahuakandaima/human-novel-writer
# novel-writer-english
npx skills add JeroTan/novel-writer-english
# deepseek-harness-novel-studio
npx skills add qinpeizhan77/deepseek-harness-novel-studio
# human-like-novel-workbuddy-skill
npx skills add LittleLollipop/human-like-novel-workbuddy-skill
# novel-creation-skill
npx skills add skye-z/novel-creation-skill
# novel-skills
npx skills add vicalloy/novel-skills
# novel-writer-skill
npx skills add liuxiao20051106-prog/novel-writer-skill
# dsh-novel-craft
npx skills add shiyan688/dsh-novel-craft
# dsh-novel-writing
npx skills add peterwangze/dsh-novel-writing
# novel-creation-omnibus
npx skills add limingnanyue/novel-creation-omnibus
# snowflake-writer
npx skills add vagabondshun/snowflake-writer
# ty-xiaoshuo-skill
npx skills add danieltao118/ty-xiaoshuo-skill
# xiaoshuo-studio
npx skills add Zhao73/xiaoshuo-studio
# huxiuzhi-novel-agent
npx skills add huxiuzh-ops/huxiuzhi-novel-agent
# Novel-framework
npx skills add bafeite59/Novel-framework
# NovelGenerator
npx skills add Dylin-code/NovelGenerator
# agent-novel
npx skills add RTY798/agent-novel
# Claude-Code-Novel-Writing
npx skills add f43a9a/Claude-Code-Novel-Writing
# claude-novel-skills
npx skills add fnb666888/claude-novel-skills
# fanqie-novels-skills
npx skills add mhkz/fanqie-novels-skills
# inkcraft-writing-skills
npx skills add Fei2411/inkcraft-writing-skills
# novel-webfiction
npx skills add zlbigger/novel-webfiction
# novel-writer-workflow
npx skills add GonsonInter/novel-writer-workflow
# novelist
npx skills add comfuture/novelist
# novelist.skills
npx skills add Ink-dark/novelist.skills
# open-novel-fanqie
npx skills add kongxcer555/open-novel-fanqie
# web-novel-master
npx skills add tinylion1024/web-novel-master
# book-writer-mcp
npx skills add arupmaity1/book-writer-mcp
# chinese-novelist-skill
npx skills add lvyu-cmd/chinese-novelist-skill
# claude-novel-writer
npx skills add zhiliyouxian/claude-novel-writer
# dsh-novel
npx skills add ddedook/dsh-novel
# dsh-novel
npx skills add wbb316/dsh-novel
# fanqie-xiaoshuo-skill
npx skills add soultt/fanqie-xiaoshuo-skill
# general-novel-skill
npx skills add xiaoyuCR7/general-novel-skill
# light-novel-creator
npx skills add Nya-Nya-Hoshino/light-novel-creator
# novel-craft
npx skills add dongyanyuxuana/novel-craft
# novel-engine
npx skills add jiangying3222880/novel-engine
# novel-project-strategy
npx skills add wgwtest/novel-project-strategy
# novel-writer-agent
npx skills add ZBA-z/novel-writer-agent
# NovelClaw
npx skills add 7a-z/NovelClaw
# NovelFlow
npx skills add DongxUETAFFY/NovelFlow
# novelist-skill
npx skills add chanceline-max/novelist-skill
# Soundingboard
npx skills add richardelder2/Soundingboard
# story-foundry
npx skills add mmunro3318/story-foundry
# web-novel-writing-skill
npx skills add XINGANLIU/web-novel-writing-skill
# novel-craft
npx skills add chaserr/novel-craft
# Novelist-Skills
npx skills add KurohaneKaoruko/Novelist-Skills
# clark-typer
npx skills add niyongsheng/clark-typer
```

</details>

<a id="group-short"></a>
### 短篇 · 故事

短篇小说、短故事、微小说、儿童故事和睡前故事。

#### skill · 提示词（14）

- 🌟 **[lengdu](https://github.com/asass-11/lengdu)** · ★ 39<br>中文短篇创作与冷读：先写完正文，再由独立校准 Agent 和全新读者 Agent 首读，检验看懂、流畅、好看<br><sub>方法：多智能体 · 修订</sub><br><sub>更新于 2026-08-16 · 中文</sub><br><sub>💡 PolyForm Noncommercial 许可，禁止任何商业使用</sub>

- **[qiaomu-novel-generator](https://github.com/joeseesun/qiaomu-novel-generator)** · ★ 394<br>先拆成情绪承诺→高压关系→冲突场→经典桥段重构→升级节奏→结尾余味的可选剧情引擎，确认大纲后写完整短篇，再按钩子与去 AI 味清单自检<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-14 · 中文 · MIT</sub><br><sub>💡 可联网检索参考作品，只借桥段功能不搬原作；附 evaluate_story.py 质检脚本</sub>

- **[bookflow-skill](https://github.com/LanyXiaosheng/bookflow-skill)** · ★ 200<br>番茄短篇项目化生产：选题打分、对标拆解、人物、大纲到 beat 再写正文，每步定输入输出与人工确认点，写后 QA 与复盘<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-09-18 · 中文 · MIT</sub>

- **[salt-story](https://github.com/yfge/salt-story)** · ★ 85<br>对齐知乎盐选投稿标准写付费短篇：按官方篇幅与拒稿原因自检，规定每段 1-3 句、独句段≥30%、对白占 40-50%，参照爆款拆解设计反转<br><sub>方法：理论 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-03-13 💤 · 中文</sub><br><sub>💡 无 README，仅 SKILL.md 与 references；最后更新 2026-03，按平台化方法独特收录</sub>

- **[oh-my-folkstoryphoto](https://github.com/isLiuyx1/oh-my-folkstoryphoto)** · ★ 60<br>Codex 民间怪谈伪纪录图文技能：先定拍摄者与设备，写声音卡和八段式证据链故事，逐图字幕过连续三图测试与 AI 腔审计，再分镜生图并自审返修<br><sub>方法：理论 · 人物 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-08-25 · 中文 · MIT</sub><br><sub>💡 成品是 30–39 张 4:5 图文轮播，需要生图能力；字幕去公式化规则借鉴 op7418/Humanizer-zh</sub>

- **[storybook-generator-skill](https://github.com/weaiw/storybook-generator-skill)** · ★ 49<br>绘本生产 skill：先定故事节拍和逐页计划（每页叙事功能、翻页钩子、图文契约），再建角色/风格圣经，逐页写出图提示词，最后按排版规则和 QA 清单验收<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-07-06 · 多语言 · MIT</sub><br><sub>💡 支持中文、拼音、英文排版；附 KDP 上架验证的商业流程说明</sub>

- **[lofn](https://github.com/LocalSymmetry/lofn)** · ★ 24<br>多模态创作 skill 集里的故事管线：6 专家+1 唱反调小组辩论选概念，6 组不同叙事结构并行写节拍、成稿，艺术家⇄批评家修订后过 QA 关卡<br><sub>方法：规划 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-08-30 · 英文 · 24 个 skill</sub><br><sub>💡 主体是图像/音乐/视频/故事多模态系统，故事只是其中一条管线；需先跑 lofn 主 skill 生成编排包</sub>

- **[fanqie-hit-short-story](https://github.com/tianyayu6/fanqie-hit-short-story)** · ★ 16<br>番茄短篇 skill：核心梗拆解→8-10 章大纲（事件/情绪/反转/钩子）→标题导语→12000 字正文→短篇编辑审稿→整篇重写→去 AI 味一句一行终稿<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-17 · 中文 · MIT</sub>

- **[fanqie-short-story.skill](https://github.com/aby-aby111/fanqie-short-story.skill)** · ★ 15<br>番茄短故事创作：8 条赛道逐级选题、标题生成打分、5 段式结构与章末三层钩子、字数校验与手机排版<br><sub>方法：规划 · 理论 · 风格</sub><br><sub>更新于 2026-05-13 · 中文 · GPL-3.0</sub><br><sub>💡 README 未写安装步骤，目录示例为 CodeBuddy skills 路径；输出路径默认写死为 Windows D 盘</sub>

- **[short_novel_write](https://github.com/gyyxs88/short_novel_write)** · ★ 10<br>中文短篇流水线：类型×标签抽卡出创意→多套故事方案与写作简报→正文草稿→AI 腔/模板感诊断→按风格画像局部改写并复检，SQLite 归档<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-04-10 💤 · 中文 · Apache-2.0</sub><br><sub>💡 最后更新 2026-04-10，略早于时效线，因方法完整独特保留；需 OpenAI 兼容接口</sub>

- **[horror-weird-fiction-skill](https://github.com/EnderRomantice/horror-weird-fiction-skill)** · ★ 8<br>怪异恐怖短篇写作 skill：从日常场景放入单一异常，按同一方向升级 2 到 4 次，不解释来源收尾，避开鬼怪、血腥和惊吓桥段<br><sub>方法：理论</sub><br><sub>更新于 2026-06-26 · 中文</sub><br><sub>💡 附两篇示例；CC BY-SA 4.0</sub>

- **[human-story-writer](https://github.com/weistiger/human-story-writer)** · ★ 6<br>单个 SKILL.md：列出 AI 写作的典型毛病（套路开头、强行升华、扁平人物），要求开头直切、结尾开放、对话带潜台词、情感靠细节来写中文短篇<br><sub>方法：理论 · 去 AI 味</sub><br><sub>更新于 2026-03-19 💤 · 中文</sub>

- **[pingshu-skill](https://github.com/FerryCorleone/pingshu-skill)** · ★ 6<br>现代评书 skill：先核对素材来源与剧情细节，再按评书开场、节奏、停顿、醒木写成单人说书稿，附表演计划并用 TTS 合成交付音频<br><sub>方法：理论 · 风格</sub><br><sub>更新于 2026-07-05 · 中文 · MIT</sub><br><sub>💡 以改编已有作品/名场面为主，不鼓励凭空编；TTS 可用本地 VoxCPM2/Qwen3-TTS 或 API</sub>

- **[jiamama-bedtime-story-skill](https://github.com/leonluo2008-ops/jiamama-bedtime-story-skill)** · ★ 4<br>从 2101 篇儿童睡前故事语料双轨蒸馏出叙事人格：先承认情绪再化解、用具体动作表达爱、固定结尾公式等 11 条铁律和 12 条反模式<br><sub>方法：理论 · 风格</sub><br><sub>更新于 2026-06-15 · 中文</sub>

#### 框架 · 应用（19）

- **[Picture_book_production](https://github.com/whotto/Picture_book_production)** · ★ 58<br>批量绘本：按主题列表用含故事类型指南和结构要求的提示词生成 JSON 故事（标题、角色描述、段落），再做场景分析，用角色特征库保持形象一致并配图<br><sub>方法：理论 · 人物</sub><br><sub>更新于 2024-12-06 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 故事由单次结构化提示生成，方法重心偏插图一致性；需 OpenAI 和 Fal.ai Key；README 含第三方 API 中转推荐和推广链接；README 写 MIT 但未声明许可证</sub>

- **[StoryWriter](https://github.com/Avdpro/StoryWriter)** · ★ 58<br>AI2Apps 短篇写作 agent：先由 AI 生成背景设定，再按指示逐段写、每次给三个备选，可逐段 AI 改写和配插图，靠设定和内容提炼续写长文<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2023-12-25 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需在 AI2Apps 环境（在线或本地部署）运行；GPT-3.5/4；受 MidReal 启发</sub>

- **[AI_writing_novel](https://github.com/wyg5208/AI_writing_novel)** · ★ 46<br>本地 Ollama 循环：自动出写作要求→按目标字数写完整篇→多维度评分→生成修改建议并一键改写，可连续无人值守产出<br><sub>方法：修订</sub><br><sub>更新于 2025-12-16 💤 · 🧩 应用 · 中文</sub><br><sub>💡 单文件 Tkinter 应用；仓库里 Scripts/*.exe 是误提交的 Windows 虚拟环境，可忽略</sub>

- **[Agentic_Story_Book_Workflow](https://github.com/breakstring/Agentic_Story_Book_Workflow)** · ★ 31<br>基于 AutoGen 的儿童绘本多 agent 流程：接待员收集需求，故事、分镜、提示词编辑各配审稿 agent，不通过就打回重写，最后出图并合成视频/PPT<br><sub>方法：多智能体 · 修订</sub><br><sub>更新于 2025-03-15 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 推荐 Azure OpenAI GPT-4o；出图用 DALL-E 3 或 Replicate Flux，配音用 Azure Speech</sub>

- **[llm-storyteller](https://github.com/warc0s/llm-storyteller)** · ★ 17<br>Streamlit 故事生成器：三步提示链，先生成详细大纲，再写正文，最后润色语法与连贯性；可调风格、语言和长度<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-06-18 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 界面为西班牙语；用本地 OpenAI 兼容模型或 OpenRouter 免费模型</sub>

- **[spark-novel](https://github.com/xhongc/spark-novel)** · ★ 13<br>短篇写作工作台：素材库积累世界观与人物，技能库保存提示词与写作流程，故事工作区按设定→大纲→正文推进<br><sub>方法：规划 · 设定</sub><br><sub>更新于 2026-07-02 · 🧩 应用 · 中文</sub><br><sub>💡 无开源许可证；README 方法描述较少；含 Android 客户端</sub>

- **[semi-ai-chat-demo](https://github.com/YannLynn/semi-ai-chat-demo)** · ★ 12<br>Semi-UI AIChat 多 agent 演示：大纲 agent 调用背景要点工具写大纲，正文 agent 按大纲写成故事<br><sub>方法：规划 · 多智能体</sub><br><sub>更新于 2025-11-12 💤 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 主要是 UI 组件演示，流程很简单；支持 OpenAI、OpenRouter、Kimi、豆包、GLM</sub>

- **[storybloom](https://github.com/valleylmh/storybloom)** · ★ 12<br>一句话生成 8 页中英双语儿童绘本：按年龄段规则控制句式、冲突和情绪节奏，固定 8 页故事节拍和镜头规划，可先审大纲，Character Bible 锁定角色<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需自配 OpenAI 兼容文本模型和生图服务；视频导出依赖 Remotion，需另看其许可</sub>

- **[Storybook-Generator](https://github.com/naakaarafr/Storybook-Generator)** · ★ 11<br>CrewAI 绘本：大纲 agent 定故事结构、人物档案和五章大纲，写作 agent 每章约百字成文，再用 FLUX 配图排成 PDF，面向 4–8 岁<br><sub>方法：规划 · 人物 · 多智能体</sub><br><sub>更新于 2025-06-12 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需 Gemini 和 Hugging Face（FLUX.1-dev）Key</sub>

- **[YouTube-StoryVideo-Generator](https://github.com/Costa318/YouTube-StoryVideo-Generator)** · ★ 8<br>恐怖故事合集流水线：Claude 先定合集主题、生成带钩子的故事构想并评分排序，成稿后 TTS 配音，再按实测时长挑选组合凑满 3 小时<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2025-08-28 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 通过 Claude Code CLI 调用 Opus，配音依赖 Kokoro-FastAPI；目标是 YouTube 变现，画面和成片阶段未完成</sub>

- **[Emberglow-Story-Factory](https://github.com/abotic/Emberglow-Story-Factory)** · ★ 7<br>面向 YouTube 的长故事工厂：按种子题材生成 5–240 分钟旁白剧本，围绕人物转变和情感弧线展开，附标题排名、简介、缩略图和逐场画面提示词<br><sub>方法：理论 · 人物</sub><br><sub>更新于 2025-10-17 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需 OpenAI API；题材以灵异、恐怖、求生为主，也有历史纪录片类非虚构内容</sub>

- **[aiStories](https://github.com/TheApo/aiStories)** · ★ 6<br>儿童睡前故事应用：从主角、配角、世界、地点、物件五栏选元素，选五种故事类型并设年龄、长度、复杂度，由 GPT/Gemini 写成故事，可朗读<br><sub>方法：理论 · 共创</sub><br><sub>更新于 2026-04-27 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 方法偏轻（元素组合 + 类型模板 + 可编辑提示词）；另含 ElevenLabs 朗读、Suno 儿歌和 Tonie 上传</sub>

- **[mira](https://github.com/bagolzxz/mira)** · ★ 6<br>儿童睡前故事：输入孩子名字、年龄和兴趣，导演提示词先定四段式大纲，再由写手提示词成文，系统提示词禁止吓人内容，最后 TTS 朗读<br><sub>方法：规划</sub><br><sub>更新于 2026-05-20 · 🧩 应用 · 英文</sub><br><sub>💡 为小米 MiMo 激励计划而做，依赖 MiMo 推理、视觉、TTS 三个模型；无 key 时只能看种子故事并用浏览器朗读</sub>

- **[story-maker](https://github.com/FURUYAN1234/story-maker)** · ★ 6<br>把主题、类型、世界观、读者层、时代、结局、叙述视角、角色等多轴设定组装成生成契约，并随机化以避开套路；生成后 AI 编辑打分再润色，可选文风解析<br><sub>方法：理论 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 日文 · 13 个 skill</sub><br><sub>💡 纯前端静态网页，需自备 Gemini 或 OpenAI API Key；15 种输出模式含万字长篇；许可证为作者自定条款（NOASSERTION）</sub>

- **[storyforge-publishing](https://github.com/shilpamed/storyforge-publishing)** · ★ 6<br>4–8 岁插画故事书多 agent 工作室：Publisher 读需求后动态组建专家团队和任务图，并行写作，质量闸门打回定向修订，输出含插画说明的书稿<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-30 · 🧩 应用 · 英文</sub><br><sub>💡 无开源许可证；课程作业性质的 MVP；默认走 Fireworks API；不生成图片</sub>

- **[AI-fiction-generator](https://github.com/JackSuuu/AI-fiction-generator)** · ★ 5<br>DeepSeek 脚本：读入提示词文件和参考文本样例，先生成大纲和标题，再按大纲逐章写成一万多字的小说并模仿样例文风，导出 Word<br><sub>方法：规划 · 风格</sub><br><sub>更新于 2025-08-27 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 需 DeepSeek API；README 写 MIT 但仓库无许可证文件，文档里的脚本名与实际文件（main.py）不一致</sub>

- **[childbook-adk](https://github.com/MultiTales/childbook-adk)** · ★ 5<br>Google ADK 儿童故事流水线：写手结合随机抽取的人物/场景/冲突卡起稿，编辑润色，批评型和读者型两个审稿 agent 打分，循环三版后配图出 PDF<br><sub>方法：多智能体 · 修订</sub><br><sub>更新于 2025-06-23 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 黑客松项目；需 Gemini 和 Imagen（Google API 或 Vertex AI）</sub>

- **[futuring-machines](https://github.com/fidelthomet/futuring-machines)** · ★ 5<br>人机共写思辨小说的工具：用 JSON 定义静态/生成动作链做故事模板，选中文本或新起一行时触发提示，由 LLM 带全文上下文续写或改写<br><sub>方法：共创</sub><br><sub>更新于 2024-10-07 💤 · 🧩 应用 · 英文</sub><br><sub>💡 默认接本地 Ollama（mistral），也可换兼容 api/generate 的接口</sub>

- **[llm_novel_picture_writer](https://github.com/aigengen5-ship-it/llm_novel_picture_writer)** · ★ 5<br>轻小说分集生成脚本：用角色表、全局风格覆盖、分集剧情和背景四段设定驱动模型逐集写作，另有修订脚本，可同步生成插图提示词或调用 ComfyUI<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-04-11 💤 · ⚙️ 框架 · 韩文</sub><br><sub>💡 韩语说明；走 OpenAI 兼容接口，推荐本地 gemma-4-31b</sub>

#### 研究代码（3）

- **[SEED-Story](https://github.com/TencentARC/SEED-Story)** · ★ 885<br>多模态大模型生成图文交错长故事：给定开头图文逐段续写文本，同时生成角色与画风一致的配图，用注意力汇聚机制支撑长序列<br><sub>方法：人物 · 记忆</sub><br><sub>更新于 2024-10-11 💤 · 🎓 研究 · 英文</sub><br><sub>💡 基于 SEED-X 微调，需 GPU 与 HF 权重；同时发布 StoryStream 数据集（训练数据来自动画片）</sub>

- **[StoryReasoning](https://github.com/daniel3303/StoryReasoning)** · ★ 41<br>根据图片序列写故事：微调 Qwen2.5-VL 先用思维链列出人物、物体、场景与叙事结构表，再写出用标签绑定画面实体的故事，跨帧保持角色身份一致、减少指代幻觉<br><sub>方法：规划 · 人物</sub><br><sub>更新于 2025-05-16 💤 · 🎓 研究 · 英文</sub><br><sub>💡 论文配套代码，同时发布 StoryReasoning 数据集（4,178 个故事）与 QwenStoryteller 模型；需 GPU 运行 7B 视觉语言模型</sub>

- **[tinyfabulist](https://github.com/klusai/tinyfabulist)** · ★ 7<br>从动物角色、性格、场景、冲突、结局、寓意列表组合结构化提示词，批量让多种 LLM 写寓言，再由 LLM 评委按语法、创意、寓意清晰度打分<br><sub>方法：理论</sub><br><sub>更新于 2026-05-01 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 用于生成 HF 数据集 klusai/ds-tf1-en-3m（300 万篇英文寓言），偏合成训练数据</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# lengdu
npx skills add asass-11/lengdu
# qiaomu-novel-generator
npx skills add joeseesun/qiaomu-novel-generator
# bookflow-skill
npx skills add LanyXiaosheng/bookflow-skill
# salt-story
npx skills add yfge/salt-story
# oh-my-folkstoryphoto
npx skills add isLiuyx1/oh-my-folkstoryphoto
# storybook-generator-skill
npx skills add weaiw/storybook-generator-skill
# lofn
npx skills add LocalSymmetry/lofn
# fanqie-hit-short-story
npx skills add tianyayu6/fanqie-hit-short-story
# fanqie-short-story.skill
npx skills add aby-aby111/fanqie-short-story.skill
# short_novel_write
npx skills add gyyxs88/short_novel_write
# horror-weird-fiction-skill
npx skills add EnderRomantice/horror-weird-fiction-skill
# human-story-writer
npx skills add weistiger/human-story-writer
# pingshu-skill
npx skills add FerryCorleone/pingshu-skill
# jiamama-bedtime-story-skill
npx skills add leonluo2008-ops/jiamama-bedtime-story-skill
```

</details>

<a id="group-script"></a>
### 剧本 · 短剧 · 影视

影视剧本、短剧和漫剧的剧情写作。只做分镜和视频生成的不收，见 [awesome-short-drama-skills](https://github.com/UnderleveledBuilder/awesome-short-drama-skills)。

#### skill · 提示词（50）

- 🌟 **[screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)** · ★ 1.7k<br>从 47 本编剧书与 23 卷剧本蒸馏 26 个 skill：结构、Truby、场景、对白、剧集圣经、编剧室与改编，附中美日韩法剧作和戏曲案例<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-10-03 · 中文 · 26 个 skill · MIT</sub><br><sub>💡 skill 正文为中文，README 有五种语言</sub>

- 🌟 **[short-drama](https://github.com/0xsline/short-drama)** · ★ 1.4k<br>短剧编剧 skill：选题立项→故事骨架→角色与四层反派→分集目录（钩子、付费卡点）→逐集写剧本→五维评分审查→合规审核<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-04-17 💤 · 中文 · MIT</sub><br><sub>💡 13 种题材模板、节奏曲线与爽感矩阵；支持海外好莱坞格式（INT./EXT.）</sub>

- **[shuohao-skills](https://github.com/eternityspring/shuohao-skills)** · ★ 4.6k<br>小说改编短剧：先出改编说明、角色、节拍、分集梗概、资产表五件套大纲（14 道脚本门禁），再写动作与台词交替的节拍流剧本，前 3 拍设冷开场钩子<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-10-15 · 多语言 · 7 个 skill · Apache-2.0</sub>

- **[drama-skills](https://github.com/zenstory-ai/drama-skills)** · ★ 2.9k<br>短剧/漫剧全链路：先建故事引擎（压力、反制、代价、状态变化）和分集地图，再写分集剧本并审查；后段出连续性锁、分镜与图/视频提示词<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-10-15 · 中文 · 12 个 skill · MIT</sub>

- **[shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master)** · ★ 1.3k<br>按概念超短片、叙事短片、长片、多集剧集四种格式套三幕式/英雄之旅与类型框架，依次出人物小传、结构大纲、场景拆解和标准格式剧本<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-04-01 💤 · 中文 · MIT</sub><br><sub>💡 以 .skill 文件分发，不能用 npx skills 安装</sub>

- **[screen-creative-skills](https://github.com/VanGong1999/screen-creative-skills)** · ★ 458<br>31 个影视策划 skill：先评估小说/IP、拆情节点和人物小传，再出大纲，按「压弹簧/放弹簧」情绪节奏写竖屏短剧分集剧本，也做长剧改编<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-10-12 · 中文 · 31 个 skill · MIT</sub><br><sub>💡 31 个 skill 在仓库里有两份副本</sub>

- **[short-drama-factory](https://github.com/lixiaoxiao9888-create/short-drama-factory)** · ★ 370<br>抖音/红果短剧工业化编剧：一句创意或一部网文 → 60–100 集带付费卡点的剧本，配钩子、断章、反转公式和机检规则<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 中文 · MIT</sub>

- **[script-forging](https://github.com/zhlmi/script-forging)** · ★ 277<br>把现成故事改编成剧本：先判断长片/短片/短剧形态，写 13 字段剧本化提示包，再出分场大纲、剧本一二稿加自检报告，每步人工确认，可选分镜<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-06-05 · 中文</sub><br><sub>💡 与 zhlmi/narrative-to-screen-reader（叙事转译）配套；输入需是成型故事</sub>

- **[novel-to-script-team](https://github.com/Supreme-Ultimate/novel-to-script-team)** · ★ 178<br>小说改编短剧/漫剧的多 Agent 流水线：改编分析→情绪曲线→分集规划→逐集写剧本，经业务/合规/风格多层审核回改，连续性记录防跨集漂移<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-02 · 中文 · 26 个 skill · MIT</sub><br><sub>💡 写剧本时可从自备的授权剧本库检索爆款参考（仓库不带语料）；后段另有分镜和 Seedance/Sora 视频提示词，图片/视频脚本需自配 API</sub>

- **[manga-script-master](https://github.com/snailzsh/manga-script-master)** · ★ 77<br>漫剧编剧 skill：按爽文/甜宠/悬疑/搞笑四套节奏模型，先做带视觉锚点的角色卡，再写带时间码和景别的单集脚本，最后转成分镜提示词<br><sub>方法：理论 · 人物</sub><br><sub>更新于 2026-03-25 💤 · 中文 · MIT</sub><br><sub>💡 分镜提示词默认适配 Seedance 2.0</sub>

- **[ai-film-skills](https://github.com/62656456/ai-film-skills)** · ★ 71<br>21 个影视创作 skill，其中导演 agent 按人物目的、阻碍、行动、后果写剧本，用状态引擎核查因果和信息差，可冷读诊断，再交给分镜与提示词阶段<br><sub>方法：理论 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 多语言 · 21 个 skill · Apache-2.0</sub><br><sub>💡 剧本写作主要在 director-agent，其余多为视觉、分镜、视频制作技能；docs/research 下有几个 zip 冻结包（未打开）</sub>

- **[ai-short-drama](https://github.com/Hao0321/ai-short-drama)** · ★ 71<br>题材调研→八维评分立项→Bible 定角色、能力代价与反派阶梯→按 micro-arc 写单集（主转折、兑现、集尾钩子、状态增量），脚本校验连载契约<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-13 · 中文 · MIT</sub><br><sub>💡 README 为繁体中文</sub>

- **[story-systems-template](https://github.com/bybren-llc/story-systems-template)** · ★ 69<br>按编剧室分工设 11 个 agent（结构师、对白、场景、连续性编辑、场记等），结构师和场记有否决权，配 24 个技能和行业模式库，输出 Fountain 剧本<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-12 · 英文 · 24 个 skill · MIT</sub><br><sub>💡 模板仓库，可从上游同步更新；Claude Code / Gemini CLI 完整支持，Codex 只有文档；也覆盖小说</sub>

- **[su-ai-short-drama](https://github.com/doublesq97-ui/su-ai-short-drama)** · ★ 63<br>中文短剧 Skill，分女频/男频两套题材与情绪回报规则；总导演、编剧、选角、分镜等岗位共读写项目档案，先出候选再人工锁定，逐集写大纲与剧本<br><sub>方法：规划 · 理论 · 记忆 · 多智能体</sub><br><sub>更新于 2026-07-28 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 附离线 HTML 剧本参数生成器；选角/分镜/声音岗位面向后续 AI 视频制作；作者声明低维护</sub>

- **[drama-adapt-skill](https://github.com/rorojiao/drama-adapt-skill)** · ★ 62<br>网文改漫剧 skill：原著分析→人物小传→分集大纲（免费/付费卡点、爽点密度）→逐集剧本→三轮质检，设三个人工确认节点，可断点续跑<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-03-19 💤 · 中文 · MIT</sub><br><sub>💡 输入是已有网文，产出改编剧本；依赖 Superpowers skill 框架</sub>

- **[qianqianwriting](https://github.com/catyiqian/qianqianwriting)** · ★ 47<br>短剧/漫剧编剧七阶段：按 31 部爆款归纳的套路模板和开场模式定故事线，救猫咪节拍按 30-60 秒或 1-3 分钟时长分拍，每集埋情绪欠条，各阶段过合规检查<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-03-05 💤 · 中文</sub>

- **[short-drama-script](https://github.com/chengbenchao/short-drama-script)** · ★ 33<br>小说/IP 改短剧 8 步：提核心骨架→1+3+N 角色矩阵→裁剪重组情节→3-5-3 节奏→四级卡点→逐集写作→8 项量化自检，参考 22 部标杆剧本<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-05-06 · 中文</sub><br><sub>💡 references/database 附带 22 部短剧剧本原文件（docx/pdf）</sub>

- **[aliang-skills](https://github.com/aliang2052/aliang-skills)** · ★ 28<br>短剧技能按题材读爽点库与结构模板，脚本随机抽 8-12 个爽点写大纲，再扩成分集剧本（黄金 3 秒、集尾留扣），后接分镜、出图与图生视频<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-06-11 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 合集另含按年龄写儿童故事/有声绘本，以及电商图、播客、配音等非虚构技能；依赖阿里云百炼 bl CLI</sub>

- **[5min-drama-contest](https://github.com/SoloEnt-AI/5min-drama-contest)** · ★ 26<br>五分钟短剧剧本：一步一问锁定赛道、立意、结构原型和前 30 秒开场，四幕卡点大纲 → 正式剧本 → 分镜脚本<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-08-29 · 中文</sub><br><sub>💡 灵蟹创作（SoloEnt）出品，面向其五分钟短剧大赛</sub>

- **[douyin-tiktok-story-skill-agent](https://github.com/liujunxibaba/douyin-tiktok-story-skill-agent)** · ★ 26<br>抖音达人剧情脚本 skill：先在本地脚本库检索钩子/关系/反转机制，至少重组三类机制成稿，再按前三秒节奏检查并跑相似度防复刻<br><sub>方法：理论 · 修订 · 风格</sub><br><sub>更新于 2026-08-05 · 中文 · MIT</sub><br><sub>💡 脚本库在作者另一仓库 douyin-tiktok-story-database，需一起安装；安装脚本为 PowerShell；含品牌植入/种草剧情模式</sub>

- **[AI-Short-Drama-Agent-Skill](https://github.com/Coconah/AI-Short-Drama-Agent-Skill)** · ★ 20<br>短剧编剧 SOP skill：脑洞重构→3000 字以上四幕大纲→分集情绪走势与结尾钩子→单集分镜剧本初稿→剧本医生精修，每个卡点由用户拍板<br><sub>方法：规划 · 理论 · 修订 · 共创</sub><br><sub>更新于 2026-03-12 💤 · 中文</sub><br><sub>💡 仓库只有一个 SKILL.md；README 写 MIT 但无许可证文件</sub>

- **[chuanzhang-ai-shortdrama-skills](https://github.com/zhangxiansheng-888/chuanzhang-ai-shortdrama-skills)** · ★ 20<br>小说改编短剧 skill 集：改编大纲与分集爽点→角色→场景道具→场次剧本（动作节拍+台词）→分镜，各阶段脚本做质检并出评审报告<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-10-10 · 中文 · 6 个 skill</sub><br><sub>💡 后两步产出生图/视频提示词；README 含公众号推广</sub>

- **[ManjuForge](https://github.com/mengxiujie/ManjuForge)** · ★ 20<br>漫剧连载编剧：角色档案、伏笔表、故事圣经、关系图等 7 个记忆文件逐集更新，伏笔按埋设→发酵→回收追踪，22 项跨文件一致性检查，顺带出分镜和提示词<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-13 · 中文 · MIT-0</sub>

- **[aishiji-director](https://github.com/tjh-aoao/aishiji-director)** · ★ 19<br>成人科幻动画短片 skill：先定 hook、世界规则、角色欲望与主题伤口，按 6-10 beat 写剧本和导演注释，再出镜头表并查原创性与 IP 风险<br><sub>方法：理论 · 设定 · 人物</sub><br><sub>更新于 2026-07-12 · 中文 · MIT</sub><br><sub>💡 成人向黑色科幻/奇幻/恐怖题材；参照《爱死机》气质但要求原创；也输出关键帧和视频运动提示词</sub>

- **[how-to-make-script](https://github.com/XucroYuri/how-to-make-script)** · ★ 19<br>编剧知识基建：按意图×媒介×阶段×产出把请求路由到 29 个子技能，加载协议、评分量表和知识原子生成节拍表或剧本，按量表自检后回收反馈<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-08-24 · 多语言 · 30 个 skill · MIT</sub><br><sub>💡 也覆盖品牌广告脚本和互动分支脚本；中英双语文档</sub>

- **[aivideo-production-skills](https://github.com/RandomNest/aivideo-production-skills)** · ★ 15<br>AI 影视生产门禁式技能集：先出节拍表和场景表，经角色心理、叙事红队、观众模拟、连续性锁定等关卡把关，再做镜头规划和提示词打包<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-02-20 💤 · 英文 · 23 个 skill · MIT</sub><br><sub>💡 以 AI 视频生产为主，另含成本门禁、模型路由等非叙事 skill</sub>

- **[short-drama-scriptwriter](https://github.com/SumOneHK/short-drama-scriptwriter)** · ★ 13<br>AI 竖屏剧/漫剧编剧流程：立项选题→剧本圣经（世界观、人物、节拍、分集大纲）→分批写场次稿并做硬阈值质检→全剧复核后交付，状态文件门禁防跳步<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-05-08 · 中文 · MIT</sub><br><sub>💡 明确不做分镜、视频提示词和配音；区分抖音国内与 TikTok 出海市场</sub>

- **[cineflow-skill](https://github.com/1647371283/cineflow-skill)** · ★ 11<br>影视创作 skill：念头裂变出 3 个高概念方向，按 22 集波浪情绪曲线写人物档案、叙事大纲和逐集细纲，再接分镜与视频提示词<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-05-12 · 中文 · MIT</sub><br><sub>💡 12 条路径里多数是分镜/视频提示词，剧本相关是路径一、二</sub>

- **[tiktok-short-drama](https://github.com/SumOneHK/tiktok-short-drama)** · ★ 11<br>海外竖屏短剧 Skill：选题→设定→结构→分集大纲→分集剧本→分镜四层流程，8 道质检 P0 硬阻断，状态 JSON 支持中断续写，上下游改动双向触发复检<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-04-29 · 中文 · MIT</sub><br><sub>💡 可出中文策划+英文对白；含情绪曲线、悬念债务、付费卡点与合规检查</sub>

- **[ai-film-director-skill](https://github.com/HairuoLiu/ai-film-director-skill)** · ★ 10<br>两阶段影视创作 skill：先以编剧身份出大纲并迭代到剧本定稿，再分集、出分镜和 Seedance 2.0 时间轴提示词，每层停下等用户确认，可回退<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-06-02 · 中文</sub>

- **[400-duanju-shuangdian](https://github.com/icooldp/400-duanju-shuangdian)** · ★ 9<br>把《400个爆款短剧剧本爽点》蒸馏成 26 个桥段 skill，按身份反差/实力碾压/打脸/叙事手法生成桥段，元技能逐集打标校验爽点密度与雷区<br><sub>方法：理论 · 修订</sub><br><sub>更新于 2026-08-21 · 中文 · 26 个 skill · GPL-3.0</sub><br><sub>💡 套路来自圈内流传的同名汇编，用 cangjie-skill 流水线蒸馏；主装 DeepSeek Harness，也给了 Claude Code / Cursor 路径</sub>

- **[ai-comic-skills](https://github.com/jis60224/ai-comic-skills)** · ★ 9<br>AI 漫剧四件套 skill：引导式提问定题材、人设、大纲后写分集剧本，再拆分镜、出视频和生图提示词，每步附质检清单<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-08-12 · 中文 · 4 个 skill · MIT</sub><br><sub>💡 剧本部分在 ai-comic-script，其余三个技能是分镜、视频提示词和视觉资产</sub>

- **[claude-screenwriting](https://github.com/e06084/claude-screenwriting)** · ★ 9<br>编剧知识引擎：把 Vogler/McKee/救猫咪落成 Obsidian 故事 wiki，15-beat 节奏、三层角色卡、结构诊断<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-10-08 · 中文 · 8 个 skill · MIT</sub>

- **[ai-native-video-architect](https://github.com/wlxb625/ai-native-video-architect)** · ★ 8<br>AI 影视创作 Skill：从想法设计故事、人物与冲突并写成正式剧本，再出视觉圣经、镜头表和逐镜生图/生视频提示词，附连续性与可生成性检查<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-08-06 · 中文</sub><br><sub>💡 后半程侧重镜头表与生视频提示词包；有 CREATE / TRANSFORM / DIAGNOSE / ADAPT 四种模式；附 Windows 安装脚本和可选的契约校验脚本</sub>

- **[douyin-transcript-exporter](https://github.com/Taomitown/douyin-transcript-exporter)** · ★ 8<br>漫剧 skill 集：自写小说走原创策划→强冲突初稿→细节扩写→合规与爆点审核八阶段，再按模板改编分场剧本并精简、做连贯性审核<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-09-03 · 中文 · 8 个 skill · MIT</sub><br><sub>💡 仓库名是抖音逐字稿导出，实际主体是面向豆包工作台的漫剧技能集；另含分镜、三视图提示词、抖音采集等非写作 skill</sub>

- **[Hermes_Script_Cool](https://github.com/way928745-collab/Hermes_Script_Cool)** · ★ 8<br>先把爆款短剧剧本批量分类、评级、筛选并蒸馏成方法论素材库，再据此对话式生成带评分质检的短剧剧本，后接分镜、三视图、音色和视频提示词<br><sub>方法：理论 · 修订 · 风格</sub><br><sub>更新于 2026-09-08 · 中文 · 12 个 skill · MIT</sub><br><sub>💡 本仓库是冻结的基础版，进阶版在知识星球付费发布；后半段工位偏视频物料生产</sub>

- **[screenplay-generator-skill](https://github.com/mariozhaofan-pixel/screenplay-generator-skill)** · ★ 8<br>爆款编剧 skill：中文剧本分批续写（每批≤2 集）、人物与对白开发、定点修订、参考片研究，按需出分镜；内置方法卡与编剧书库转写按问题检索<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-10-15 · 中文 · 2 个 skill</sub><br><sub>💡 思路参考 Shanyin-ai/shanyin-screenwriting-master；附第三方书籍转写，LICENSE 限制再发布；可选飞书多维表协作</sub>

- **[super-ai-scriptwriter](https://github.com/Doing-Tai-JI/super-ai-scriptwriter)** · ★ 8<br>影视剧本 Skill：采编出故事方向，建人物欲望/恐惧与世界规则档案，按“目标-行动-反作用-代价-状态变化”排节拍写剧本，九维会诊分级改稿后出 Word 定稿<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-07-15 · 中文 · MIT</sub><br><sub>💡 附中文标准剧本 Word 模板；关键阶段设确认点，不擅自全稿重写</sub>

- **[ai-short-drama-from-zero](https://github.com/sanxsnr/ai-short-drama-from-zero)** · ★ 7<br>AI 短剧导演 Skill：判断进度后一次推进一关，把灵感或小说改编成分集可拍剧本并给对白读秒，再拆 10/15 秒分镜和资产，每轮自检并给 A/B/C 下一步<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-10-12 · 中文 · MIT</sub><br><sub>💡 后半程主要是分镜、资产和 Seedance 2.0 视频生成；技能调用名仍是 $ai-short-drama-director</sub>

- **[drama-script-writing](https://github.com/SSRYLJRSS/drama-script-writing)** · ★ 7<br>热点事件改编短剧剧本：S0-S7 流水线（多案例糅合人设→冲突提炼→序幕+四幕故事线→写稿自检），并从用户改稿中提炼经验写回规则<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-08-14 · 中文 · MIT</sub><br><sub>💡 题材取自真实社会事件，要求判决/数据不改；也支持 Hermes Agent 与网页版粘贴使用</sub>

- **[opencode-storyclaw](https://github.com/NINKCH/opencode-storyclaw)** · ★ 7<br>OpenCode 插件：把网文章节改编成短剧剧本，解析为结构化场景，再生成角色/场景/道具设定与逐 beat 分镜脚本，跨集共享设定、进度与全局风格文件<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-29 · 中文</sub><br><sub>💡 生图/生视频需自己拿提示词去即梦、可灵；无开源许可证</sub>

- **[Paperrolling-DIRcreative-SKILL](https://github.com/papperrollinggery/Paperrolling-DIRcreative-SKILL)** · ★ 7<br>Codex 影视前期 skill：从想法或参考片发展故事、剧本与对白，再出分镜、角色连续性约束和 Seedance 视频提示词，各阶段设共创确认门<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-09-09 · 英文 · 22 个 skill</sub><br><sub>💡 重心在分镜与视频提示词，剧本是前段；无开源许可证</sub>

- **[kitten-punch-screenwriting](https://github.com/YanKaFei/kitten-punch-screenwriting)** · ★ 6<br>中文编剧 skill：把故事状态当账本维护，每场先过 14 道证据式 QC 才提交，失败按来源层单调回修，长篇靠记忆快照续写<br><sub>方法：理论 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-13 · 中文 · MIT</sub><br><sub>💡 覆盖概念超短片、电影、剧集与竖屏短剧；README 称也可装进 DeepSeek Harness</sub>

- **[gushi-skill](https://github.com/pipivv/gushi-skill)** · ★ 5<br>蒸馏麦基《故事》：故事三角、节拍→场景→序列→幕层级、鸿沟原理、激励事件到结局五步设计、场景 7 项检查，附 AI 短剧适配<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-06-16 · 中文</sub>

- **[kunka-screenwriting-master](https://github.com/geslie1/kunka-screenwriting-master)** · ★ 5<br>13 个编剧 skill 按阶段调度：前提→因果结构→人物→场景与对白；改稿附文本证据并核对时间线和人物知情，story-bible 分记已定与暂定设定<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-09-10 · 中文 · 13 个 skill · MIT</sub>

- **[manju-full-pipeline](https://github.com/yangjiaxin2007123-dot/manju-full-pipeline)** · ★ 5<br>小说改竖屏漫剧：原著章节索引→改编契约→故事引擎与分集地图→单集剧本，再做资产图、九宫格和 MiniMax H3 视频提示词，独立审核后交付<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-08-22 · 中文</sub><br><sub>💡 后半段是资产图、分镜和视频提示词生产；附无第三方依赖的 Python 结构检查脚本</sub>

- **[write-screenplay-skill](https://github.com/egguy886/write-screenplay-skill)** · ★ 5<br>小说/设定改编短剧剧本：剥离心理描写、把情绪外化成可拍动作并拆成单动作节拍，过黄金三秒、集尾钩子等六项门禁，含英文对白出海模式<br><sub>方法：理论 · 修订</sub><br><sub>更新于 2026-09-06 · 中文 · MIT</sub>

- **[zhang-yimou-skill](https://github.com/Ye-Zayne/zhang-yimou-skill)** · ★ 5<br>短剧 skill：把张艺谋式色彩叙事、仪式化调度、空间权力、道具母题等原则转成写作规则，从一句灵感写出短剧剧本，再拆镜头表、故事版和 Seedance 提示词<br><sub>方法：规划 · 理论 · 风格</sub><br><sub>更新于 2026-06-10 · 中文</sub><br><sub>💡 不扮演张艺谋本人，只用公开可观察的导演原则；七步流程中后五步是分镜/视频/剪辑</sub>

- **[emma-screenwriting-skills](https://github.com/adoria111/emma-screenwriting-skills)** · ★ 1<br>八个短剧编剧方法：拆对标结构、迁移剧情引擎做改编、设计全剧期待与兑现链，按观众期待→戏剧机制→可拍呈现修集尾钩子，再扩集纲、诊断对白、删冗余<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-10-13 · 中文 · 10 个 skill · MIT</sub>

- **[hongguo-shortdrama-screenwriting](https://github.com/zhu5859243-free/hongguo-shortdrama-screenwriting)** · ★ 0<br>以 short-drama-factory 结构引擎为底，并入红果《短剧编剧第一课》的选题、黄金开场、钩子与情绪点方法，机检加查黄金三角与对白占比<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-09-22 · 中文 · MIT</sub><br><sub>💡 方法论来源为作者自述，未核实</sub>

#### 框架 · 应用（23）

- **[aid-studio](https://github.com/gzxx-2025/aid-studio)** · ★ 922<br>漫剧/短剧平台的剧本技能：分创作、续写、改写、规范化、修复五模式，按「行动→结果→下一动作」写场景，凭独立审核报告修硬伤，再接分镜和视频<br><sub>方法：理论 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 主体是 AI 漫剧/短剧视频生产平台，剧本 skill 在 aid-interface 资源目录（screenplay / screenplay-write / screenplay-review）；图像、视频模型需自付 API</sub>

- **[ZJT](https://github.com/jeffstric/ZJT)** · ★ 232<br>短剧平台：PM agent 调度编剧、人物、场景、情节分析（三幕式/悬念/节奏）、小说分集、合规等 8 个专家，ask_user 让用户选方向，再接分镜视频<br><sub>方法：规划 · 人物 · 多智能体</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · 24 个 skill</sub><br><sub>💡 自定义许可证（LICENSE_ZH）；含算力计费/微信支付等商业运营功能；Release 提供 exe 启动器，仓库有完整源码</sub>

- **[juben](https://github.com/VanGong1999/juben)** · ★ 162<br>40+ agent 的短剧策划、创作、评估平台：按情绪价值、黄金三秒钩子、期待-压抑-爆发三幕做策划，生成情节点、人物小传和剧本，再多维打分<br><sub>方法：理论 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-03 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 默认接智谱 AI 免费模型；作者另有剧本知识库 GongLingRui/skills 和 GongLingRui/screen-creative-skills</sub>

- **[huobao-drama-ai](https://github.com/dav-niu474/huobao-drama-ai)** · ★ 103<br>短剧平台的剧本工坊：章节原文→事件表→故事骨架（三幕、付费卡点、反转登记）→改编策略→剧本，再接分镜、出图、视频和配音<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-08-28 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 README 写明参考 chatfire-AI/huobao-drama 重写；CHANGELOG 称改编流水线受 Toonflow 启发；后半段是视频制作</sub>

- **[Creative-Writers-Toolkit](https://github.com/christiandarkin/Creative-Writers-Toolkit)** · ★ 92<br>GPT-3 脚本链：先生成人物，再出梗概，梗概逐层拆成场景列表和场景文件，最后把场景转成剧本，每一步都是可人工修改的文本<br><sub>方法：规划 · 人物</sub><br><sub>更新于 2022-10-26 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 基于已下线的 GPT-3 补全接口，需自行换接口；附大量 primer 示例</sub>

- **[mediago-drama](https://github.com/mediago-dev/mediago-drama)** · ★ 91<br>小说改漫剧的文档驱动 Agent 工作台：解析原文后用剧本、角色、场景、道具等 Skill 改写分场剧本并沉淀设定文档，再拆分镜出图出视频<br><sub>方法：设定 · 人物 · 记忆</sub><br><sub>更新于 2026-07-30 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 重心在图片和视频生成；仓库有 COMMERCIAL_FEATURES.md 列商业功能；开发环境需 Node 24 + Go 1.25</sub>

- **[toonflow](https://github.com/openfrees/toonflow)** · ★ 82<br>短剧创作平台：大纲故事线 Agent 下设规划师、故事师、导演、大纲师子 agent 拆解小说或创意，再生成分集剧本、分镜和角色/场景资产提示词<br><sub>方法：规划 · 多智能体</sub><br><sub>更新于 2026-04-10 💤 · 🧩 应用 · 中文</sub><br><sub>💡 README 只有部署说明，方法见 storyweaver-api/app/prompts；仅限非商业使用</sub>

- **[plotcat](https://github.com/mmlong818/plotcat)** · ★ 61<br>AI 编剧工作台：向导→意图锚点→故事圣经（角色/时间线/伏笔）→三幕/四幕剧情板→场景→剧本，再做一致性与弧光体检和 10 视角专家面板评审<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-10-09 · 🧩 应用 · 中文</sub><br><sub>💡 PolyForm Noncommercial 许可，禁止商用；默认智谱 GLM</sub>

- **[xiaomaque](https://github.com/mclwh/xiaomaque)** · ★ 23<br>短剧平台：LangChain agent 先把创意写成剧本摘要（集数、人物小传、梗概），再出分集大纲并逐集写影视格式剧本，后接分镜与生视频<br><sub>方法：规划</sub><br><sub>更新于 2026-06-29 · 🧩 应用 · 中文 · 21 个 skill · MIT</sub><br><sub>💡 仿字节「小云雀」；需 MySQL、七牛云存储与火山方舟 Key；后半段主要是资产库、分镜与视频生成</sub>

- **[storycine](https://github.com/ljy532126/storycine)** · ★ 19<br>短剧全流程平台，剧本段由 7 个 LangGraph agent 串联：标签解析→大纲→人物→剧情架构→撰写→校验，支持续写和小说转剧本，再接分镜与生图生视频<br><sub>方法：规划 · 人物 · 多智能体</sub><br><sub>更新于 2026-06-24 · 🧩 应用 · 中文</sub><br><sub>💡 无开源许可证；后半段依赖豆包 Seedream / Seedance 生图生视频</sub>

- **[script-to-storyboard](https://github.com/lookme2012/script-to-storyboard)** · ★ 14<br>短剧/微电影八步工作流：破题出 3 个方向→梗概→人物卡→背景→四幕结构→场次→正文→剧本医生诊断，每步生成后自检、通过或回滚<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-07-04 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Electron 桌面 + Web；剧本后接分镜流水线（即梦提示词）；支持 OpenAI/Anthropic/Gemini 接口格式</sub>

- **[Film-Production-Toolkit](https://github.com/slipknot0130/Film-Production-Toolkit)** · ★ 13<br>Showrunner 出大纲、节奏曲线和人物小传（Ghost/Lie/Flaw），编剧按集写，剧本医生审查、驳回并存记忆快照；按微短剧/长剧/电影切换审核标准<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-17 · 🧩 应用 · 中文</sub><br><sub>💡 另含预算审计、场景拆解、分镜提示词等制片模块；仓库无许可证</sub>

- **[narrative-core](https://github.com/Krishnaag23/narrative-core)** · ★ 13<br>多集剧本流水线：概念经 RAG 检索文化叙事库（五卷书、情味弧线），生成三幕式分集大纲和知识图谱，角色带向量记忆，分层摘要控上下文后成稿并质检<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2025-04-24 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 2025-04 后未更新，因注入印度文化叙事框架的思路少见而收；可输出 SSML 供音频制作</sub>

- **[ai-screenplay-writer](https://github.com/E-Asrar-Haghighi/ai-screenplay-writer)** · ★ 11<br>LangGraph 编剧室：先建世界圣经，每集按场景规划→大纲校验→逐场写作→组装，连续性检查不过就重写，状态存盘可续写多季<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-12 💤 · ⚙️ 框架 · 英文 · MIT</sub>

- **[MbhStoryboardScriptAssistant](https://github.com/SteenLuo/MbhStoryboardScriptAssistant)** · ★ 11<br>小说转 AI 漫剧剧本再转分镜的本地工作台：先判类型题材选规则，剧本和分镜各有生成、评审技能，从样例和修改意见提炼规则自我进化<br><sub>方法：规划 · 修订 · 风格</sub><br><sub>更新于 2026-10-08 · ⚙️ 框架 · 中文 · 9 个 skill</sub><br><sub>💡 偏 Windows（.bat/.ps1 启动与打包脚本），仓库附初始技能 zip 包；作者自述为 0.5 半成品版本</sub>

- **[script-weaver](https://github.com/KKenny0/script-weaver)** · ★ 10<br>编排器串联构思、结构、人物、场景、编剧、分镜等 9 个 agent，从 logline 出剧本和视频提示词；可插 Save the Cat 等方法，记忆改稿偏好<br><sub>方法：规划 · 理论 · 人物 · 多智能体</sub><br><sub>更新于 2026-09-29 · ⚙️ 框架 · 英文</sub><br><sub>💡 Web 工作台 + CLI；可加载 YAML/JSON/Claude Code .md 技能</sub>

- **[AI_Movie_Script_Generator](https://github.com/SakethramSathish/AI_Movie_Script_Generator)** · ★ 7<br>Story2Screen：把故事构想或帖子先做主题、人物、结构分析，再搭情节大纲、写标准格式电影剧本，最后抽取高光场景生成预告片文案<br><sub>方法：规划</sub><br><sub>更新于 2026-01-08 💤 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 Streamlit 应用，需 Gemini API；可导出 PDF</sub>

- **[AwesomeWriter](https://github.com/QuanLong427/AwesomeWriter)** · ★ 7<br>网文改编剧本的多 Agent 网页应用：调度器依次调用故事骨架、改编策略、剧本编写、监督审核四个 Agent，把小说转成剧本格式<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-05 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 输入是已有小说，产出改编剧本；需 MySQL</sub>

- **[Narr-Light](https://github.com/Shaun520/Narr-Light)** · ★ 6<br>剧本杀创作平台：分阶段生成大纲、人物、幕次、线索和时间线，带逻辑校验和插画生成，编辑器可逐项修改<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-08-07 · 🧩 应用 · 中文 · 3 个 skill</sub><br><sub>💡 需 Supabase；含定价、配额、支付、社区和运营后台；默认 mock 模式，真实生成需配 DeepSeek/Kimi 等 key</sub>

- **[Novel2Script_AI](https://github.com/LYGSYJ/Novel2Script_AI)** · ★ 6<br>小说转剧本：按章让 LLM 改写成场景化剧本，人物地点存 ChromaDB 长期记忆、章节摘要作短期记忆，可选 LangGraph 多 Agent 审稿<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-22 · 🧩 应用 · 中文</sub><br><sub>💡 需 OpenAI 兼容接口（默认 DeepSeek）；支持 EPUB 输入；README 叫「分镜脚本」，实际产出场景、动作、对白结构的剧本初稿</sub>

- **[StoryForge](https://github.com/zhiyuzi/StoryForge)** · ★ 6<br>短剧运行时：采访→梗概→评审自动修正→用户确认硬卡点→剧本或分镜，再由叙事/角色/逻辑/格式评审 agent 循环修正，附赛道与结构知识库<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-24 💤 · ⚙️ 框架 · 中文 · 3 个 skill</sub>

- **[MiaoMuse](https://github.com/15673312611/MiaoMuse)** · ★ 5<br>短剧剧本工作台：故事设定→角色小传→阶段大纲→分集大纲→分集正文逐级流式生成，另有剧本改写和网文改编入口，可导出 Word<br><sub>方法：规划 · 人物</sub><br><sub>更新于 2026-06-15 · 🧩 应用 · 中文</sub><br><sub>💡 Go 后端和 Vue 前端各只有一个源文件；需 MySQL；钱包、会员、充值界面仅作演示；作者留微信接定制开发</sub>

- **[screenplay-writer-agent](https://github.com/raahulrahl/screenplay-writer-agent)** · ★ 5<br>CrewAI 剧本 agent：分析素材→建人物、情节与分场→写剧本→严格格式化→质量评估五阶段，人物与对白专员分工，可接 Mem0 保持人物一致<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-11 💤 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 仓库由 Paraschamoli/screenplay-writer-agent 转移而来；基于 bindu 模板；需 OpenAI 或 OpenRouter</sub>

#### 研究代码（2）

- 🌟 **[dramatron](https://github.com/google-deepmind/dramatron)** · ★ 1.1k<br>从一句 logline 层级展开：先生成标题、人物、情节节拍和地点描述，再逐场生成对白，作者可在每一层编辑重写<br><sub>方法：规划 · 人物 · 共创</sub><br><sub>更新于 2024-07-16 💤 · 🎓 研究 · 英文 · Apache-2.0</sub><br><sub>💡 CHI 2023 论文配套 Colab；不内置模型，需自行实现 LLM 采样接口</sub>

- **[wr-AI-ter](https://github.com/Think-42/wr-AI-ter)** · ★ 7<br>iOS 编剧助手：按灵感冲击→追问→普遍情感→故事节拍结构→导出梗概四阶段推进，每步由 AI 给候选、作者挑选，研究保持作者归属感<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2024-10-16 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 IMX 2024 论文配套；产出到 treatment 梗概而非完整剧本；需在源码里填 OpenAI Key；作者另有网页版</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# screenwriting-skills
/plugin marketplace add jtydhr88/screenwriting-skills
# short-drama
npx skills add 0xsline/short-drama
# shuohao-skills
npx skills add eternityspring/shuohao-skills
# drama-skills
npx skills add zenstory-ai/drama-skills
# shanyin-screenwriting-master
# 下载仓库里的 .skill 文件，在 Claude App 的 Skills 中导入（另有通用 .md 版）
# screen-creative-skills
npx skills add VanGong1999/screen-creative-skills
# short-drama-factory
npx skills add lixiaoxiao9888-create/short-drama-factory
# script-forging
npx skills add zhlmi/script-forging
# novel-to-script-team
npx skills add Supreme-Ultimate/novel-to-script-team
# manga-script-master
npx skills add snailzsh/manga-script-master
# ai-film-skills
npx skills add 62656456/ai-film-skills
# ai-short-drama
npx skills add Hao0321/ai-short-drama
# story-systems-template
npx skills add bybren-llc/story-systems-template
# su-ai-short-drama
npx skills add doublesq97-ui/su-ai-short-drama
# drama-adapt-skill
npx skills add rorojiao/drama-adapt-skill
# qianqianwriting
npx skills add catyiqian/qianqianwriting
# short-drama-script
npx skills add chengbenchao/short-drama-script
# aliang-skills
npx skills add aliang2052/aliang-skills
# 5min-drama-contest
npx skills add SoloEnt-AI/5min-drama-contest
# douyin-tiktok-story-skill-agent
npx skills add liujunxibaba/douyin-tiktok-story-skill-agent
# AI-Short-Drama-Agent-Skill
npx skills add Coconah/AI-Short-Drama-Agent-Skill
# chuanzhang-ai-shortdrama-skills
npx skills add zhangxiansheng-888/chuanzhang-ai-shortdrama-skills
# ManjuForge
npx skills add mengxiujie/ManjuForge
# aishiji-director
npx skills add tjh-aoao/aishiji-director
# how-to-make-script
npx skills add XucroYuri/how-to-make-script
# aivideo-production-skills
npx skills add RandomNest/aivideo-production-skills
# short-drama-scriptwriter
npx skills add SumOneHK/short-drama-scriptwriter
# cineflow-skill
npx skills add 1647371283/cineflow-skill
# tiktok-short-drama
npx skills add SumOneHK/tiktok-short-drama
# ai-film-director-skill
npx skills add HairuoLiu/ai-film-director-skill
# 400-duanju-shuangdian
npx skills add icooldp/400-duanju-shuangdian
# ai-comic-skills
npx skills add jis60224/ai-comic-skills
# claude-screenwriting
npx skills add e06084/claude-screenwriting
# ai-native-video-architect
npx skills add wlxb625/ai-native-video-architect
# douyin-transcript-exporter
npx skills add Taomitown/douyin-transcript-exporter
# Hermes_Script_Cool
npx skills add way928745-collab/Hermes_Script_Cool
# screenplay-generator-skill
npx skills add mariozhaofan-pixel/screenplay-generator-skill
# super-ai-scriptwriter
npx skills add Doing-Tai-JI/super-ai-scriptwriter
# ai-short-drama-from-zero
npx skills add sanxsnr/ai-short-drama-from-zero
# drama-script-writing
npx skills add SSRYLJRSS/drama-script-writing
# opencode-storyclaw
npx skills add NINKCH/opencode-storyclaw
# Paperrolling-DIRcreative-SKILL
npx skills add papperrollinggery/Paperrolling-DIRcreative-SKILL
# kitten-punch-screenwriting
npx skills add YanKaFei/kitten-punch-screenwriting
# gushi-skill
npx skills add pipivv/gushi-skill
# kunka-screenwriting-master
npx skills add geslie1/kunka-screenwriting-master
# manju-full-pipeline
npx skills add yangjiaxin2007123-dot/manju-full-pipeline
# write-screenplay-skill
npx skills add egguy886/write-screenplay-skill
# zhang-yimou-skill
npx skills add Ye-Zayne/zhang-yimou-skill
# emma-screenwriting-skills
npx skills add adoria111/emma-screenwriting-skills
# hongguo-shortdrama-screenwriting
npx skills add zhu5859243-free/hongguo-shortdrama-screenwriting
```

</details>

<a id="group-interactive"></a>
### 互动叙事 · 游戏 · 角色扮演

AI 当叙事者或主持人，故事随玩家的选择展开：互动小说、文字冒险、跑团、视觉小说、角色扮演。

#### skill · 提示词（19）

- **[novel-to-game](https://github.com/zenstory-ai/novel-to-game)** · ★ 859<br>小说改编游戏：带原文出处的设计文档、网页游戏构建与基于证据的 QA，附三个可玩示例<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2026-10-15 · 多语言 · 7 个 skill · MIT</sub>

- **[dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern)** · ★ 175<br>DSH 长篇角色扮演：导入或对话共创酒馆角色卡，按需读世界书，关键词+语义混合检索长期记忆，多角色 Agent 独立推演，可分支世界线并导出小说<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-10-14 · 中文 · 4 个 skill · GPL-3.0</sub><br><sub>💡 DeepSeek Harness 插件，需 Node 24+ 与 DSH 宿主；Release 另提供 Windows/Linux 安装器</sub>

- **[ChatGPT-Adventure](https://github.com/capnmidnight/ChatGPT-Adventure)** · ★ 45<br>让 ChatGPT 扮演大型机文字冒险程序的初始提示词：规定房间双向连通、容器、钥匙锁门、搜索、背包和战斗指令，由模型即时生成世界<br><sub>方法：设定 · 共创</sub><br><sub>更新于 2022-12-08 💤 · 📝 提示词 · 英文</sub><br><sub>💡 只有提示词和游玩记录（另含让 ChatGPT 下国际象棋的提示词）；写于 2022-12</sub>

- **[interactive-fiction-skill](https://github.com/Treasure-hub-agent/interactive-fiction-skill)** · ★ 37<br>选项驱动互动小说：每轮写一段正文并给 A–E 五个选项，角色卡还原人设，自动存档记录好感与支线，设定核对和伏笔回收保长线一致<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-08 · 多语言 · MIT</sub>

- **[velvet-ascent-skill](https://github.com/ruijayfeng/velvet-ascent-skill)** · ★ 27<br>中文成人向后宫养成文字游戏 GM：角色分 6 阶段推进关系，NSFW 档位 0-4 可调，8 文件记忆世界、人物与伏笔，结束后可导出小说<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-07-13 · 中文 · MIT</sub><br><sub>💡 用 npx @ruizhefeng/velvet-ascent-skill 安装，默认装到 ~/.agents/skills/velvet-ascent，可用 --target 改路径；支持切换女性向剧情</sub>

- **[storytelling-guide](https://github.com/FailedSave/storytelling-guide)** · ★ 24<br>AI Dungeon 情色故事写作指南：把 Story 模式当协作写作，开场预设人物，用 pin 记忆固定人物动机与设定，不满意就编辑或重试，附示例故事<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2020-08-17 💤 · 📝 提示词 · 英文</sub><br><sub>💡 成人内容；针对 2020 年的 AI Dungeon（Dragon 模型），平台现已变化；无 README，正文在 Guide.md</sub>

- **[ace-os-v8](https://github.com/AgnosticArchitect/ace-os-v8)** · ★ 22<br>把 LLM 当确定性因果引擎跑角色扮演：角色 DNA、记忆印记、场域规则、JSON 状态表分开存，隐藏 CoT 比对实力数值判定行动成败后再叙述<br><sub>方法：人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-05-28 · 📝 提示词 · 英文 · MIT</sub><br><sub>💡 纯 Markdown/JSON 模板，需手动喂给模型；示例卡带是 Bleach 同人原创角色，模板本身通用</sub>

- **[character-card-skills](https://github.com/foreverse-app/character-card-skills)** · ★ 22<br>角色扮演卡写作 skill：四轴定位→47 类型套路→开场范式与 lorebook 写法，配确定性 AI 味检测器；另含以 2–3 部小说为语感锚点的仿写<br><sub>方法：理论 · 人物 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-26 · 多语言 · 4 个 skill</sub><br><sub>💡 卡片可导入 SillyTavern；附盲评实验（LLM 评审分辨人写/AI 写的准确率仅 12%）</sub>

- **[DUNGEON_ARCHITECT](https://github.com/gloria-yin/DUNGEON_ARCHITECT)** · ★ 17<br>酒馆无限流副本生成：按主题/评级/人数/PVE-PVP 参数生成表层与真相分离的副本大纲（机制、NPC、Boss、反转埋点），注入世界书供 AI 推剧情<br><sub>方法：规划 · 理论 · 设定</sub><br><sub>更新于 2026-04-30 · 📝 提示词 · 中文</sub><br><sub>💡 SillyTavern 酒馆助手脚本（导入 JSON）；作者推荐 Gemini 2.5/3.1 Pro；未声明许可证</sub>

- **[fanfic-roleplay-design](https://github.com/unknowlei/fanfic-roleplay-design)** · ★ 16<br>同人角色扮演设计：联网整理原作资料，生成或合并 SillyTavern 世界书，分还原模式与人物模式，可按主线阶段配置 MVU 变量<br><sub>方法：设定 · 人物 · 记忆</sub><br><sub>更新于 2026-10-06 · 英文</sub><br><sub>💡 产物是 SillyTavern 世界书 JSON；MVU/EJS 功能需预装 Tavern Helper 与 MVU</sub>

- **[delvewright](https://github.com/stellarfeline/delvewright)** · ★ 12<br>故事提示→Minecraft 冒险地图：agent 写世界/NPC/任务计划等 schema 文档，人确认设计后编译，静态遍历任务路径并让机器人通关验证<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2026-10-15 · 英文 · GPL-3.0</sub><br><sub>💡 产物是 Minecraft Java 原版数据包而非文本小说；需 Python 3.11+、Java 21+、Docker</sub>

- **[theatre](https://github.com/geekjourneyx/theatre)** · ★ 11<br>历史“见证引擎”：结局不可改，玩家只改变在场姿态（旁观→发问→联结→共鸣）四态状态机，姿态决定人物说什么，按条件注入史实彩蛋，剧本用 yaml 扩展<br><sub>方法：人物 · 共创</sub><br><sub>更新于 2026-04-14 💤 · 中文</sub><br><sub>💡 目前只有一个剧本（盛唐 744，李白杜甫）；2026-04-14 后未更新，因机制少见而收</sub>

- **[Cyber-Eros.skill](https://github.com/mlkgrnt/Cyber-Eros.skill)** · ★ 10<br>沉浸式角色扮演 skill 套件：从小说蒸馏设定与文风或由种子生成世界，导演引擎监测剧情停滞时注入变量，记忆归档折叠上下文并存读档<br><sub>方法：设定 · 记忆 · 风格 · 共创</sub><br><sub>更新于 2026-06-12 · 多语言 · 5 个 skill</sub><br><sub>💡 成人内容（NSFW 角色扮演）；一键安装是 curl \| bash / irm \| iex 远程脚本</sub>

- **[interactive-novel](https://github.com/din1919/interactive-novel)** · ★ 10<br>把小说片段变成可游玩的互动故事：提取世界状态和人物，用户扮演其中角色，系统接管 NPC 与世界反应，带分层记忆和存读档<br><sub>方法：人物 · 记忆 · 模拟 · 风格</sub><br><sub>更新于 2026-06-16 · 中文 · MIT</sub><br><sub>💡 skill 在 interactive-novel/ 子目录；附 state-helper.js（Node）做存读档和一致性检查；含 NSFW 协议</sub>

- **[speckit-preset-game-narrative-writing](https://github.com/adaumann/speckit-preset-game-narrative-writing)** · ★ 9<br>Spec Kit 游戏叙事预设：叙事简报→故事地图→对白与场景写作任务，支持分支、多结局、多视角与状态机，输出 Twine/Ink 并做校验<br><sub>方法：规划 · 理论 · 共创</sub><br><sub>更新于 2026-07-16 · 英文</sub><br><sub>💡 需 GitHub Spec Kit ≥0.5.0；与 fiction-book-writing 同一作者</sub>

- **[DeekSeek-V4-text-adventure-prompt-builder](https://github.com/EdenBush/DeekSeek-V4-text-adventure-prompt-builder)** · ★ 7<br>元提示词 skill：把世界观描述编译成文字冒险 DM 提示词，内嵌三幕蓝图、冲突预算与无聊度降阈、选择账本定期回调和每轮 think 自检<br><sub>方法：规划 · 理论 · 记忆 · 共创</sub><br><sub>更新于 2026-06-21 · 中文</sub><br><sub>💡 针对 DeepSeek V4 调优；含后宫、福利等成人向模块</sub>

- **[novel-rpg](https://github.com/kiki123124/novel-rpg)** · ★ 7<br>小说 RPG skill：导入 PDF 小说自动切章、抽角色、生成场景图，玩家扮演任一角色做选择，属性影响选项，偏离度记录与原著的分歧<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-04-02 💤 · 多语言 · MIT</sub><br><sub>💡 内置《呼啸山庄》《西游记》场景数据；支持存档续玩</sub>

- **[RPG-OS](https://github.com/croatianrdy2defend-create/RPG-OS)** · ★ 7<br>纯指令文件夹式单人跑团：AI 主持按 OS/AGENTS.md 运行游戏，世界、角色与战役状态写进可读文件跨对话续玩，附规则机制与主持契约文档<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-18 · 📝 提示词 · 英文 · CC-BY-4.0</sub><br><sub>💡 需能读写本地文件的 agent（README 以 Codex 桌面版为例）；游戏包是 Release 中约 320KB 的 Markdown 压缩包</sub>

- **[Frankkie](https://github.com/TaigaNoeru/Frankkie)** · ★ 6<br>SillyTavern 角色扮演预设：48 个可开关模块，含反套话规则、写前规划与连贯性检查、人物心理深度框架、文风预设、分题材思维链和长团一致性追踪<br><sub>方法：人物 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2025-12-30 💤 · 📝 提示词 · 英文</sub><br><sub>💡 原名 APEX v4.1；含成人内容开关</sub>

#### 框架 · 应用（162）

- 🌟 **[Marinara-Engine](https://github.com/Pasta-Devs/Marinara-Engine)** · ★ 712<br>角色扮演与游戏引擎：AI 游戏主持带队伍/任务/战斗，可按需安装叙事导演、连续性检查、世界状态与关系追踪、长期记忆、Lorebook 维护等代理<br><sub>方法：设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 AGPL-3.0，Beta；代理需从 Pasta-Devs/Marinara-Agents 下载；仓库附带 Windows 启动器 exe，但源码完整；可导入 SillyTavern 数据</sub>

- 🌟 **[OpenStory](https://github.com/ZJU-LLMs/OpenStory)** · ★ 430<br>多智能体故事世界推演框架：角色按感知→计划→执行→反思插件自主行动演出剧情，玩家可下指令、回溯分支；WorldKernel 一句话生成角色、地点与规则<br><sub>方法：设定 · 多智能体 · 模拟 · 共创</sub><br><sub>更新于 2026-08-19 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 基于 ZJU-LLMs/Agent-Kernel，需本地 Redis；内置红楼梦、西部世界示例；另有 DeepSeek Harness 插件</sub>

- 🌟 **[Sonder_Engine](https://github.com/N0819/Sonder_Engine)** · ★ 59<br>互动小说引擎：导演裁定客观因果，感知层决定每个角色能知道什么，角色代理只凭私有记忆行动，叙述者只写玩家可见部分，再统一提交状态<br><sub>方法：记忆 · 多智能体 · 模拟 · 共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 本地单人引擎；每回合多次模型调用，成本较高；每个阶段可重掷或手改</sub>

- **[SillyTavern](https://github.com/SillyTavern/SillyTavern)** · ★ 34.5k<br>LLM 角色扮演前端：World Info 世界书按关键词注入设定，配合角色卡、群聊、视觉小说模式和扩展生态支撑长篇互动叙事<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-02 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 基于 TavernAI 1.2.8 分叉后独立发展；通用 LLM 前端，叙事机制主要靠世界书与扩展；AGPL-3.0</sub>

- **[KoboldAI-Client](https://github.com/KoboldAI/KoboldAI-Client)** · ★ 4k<br>浏览器里的 AI 写作前端，最早把 Memory、Author's Note、World Info 做成一套，可在小说、文字冒险、聊天模式间切换<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 已停止维护，跑不了新模型，后继是 KoboldCpp 和 KoboldAI Lite</sub>

- **[TavernAI-v1](https://github.com/TavernAI/TavernAI-v1)** · ★ 2.7k<br>角色扮演/故事写作前端：角色卡、多角色群聊、故事模式，World Info 世界书注入设定，可接 KoboldAI、NovelAI、OpenAI 等后端<br><sub>方法：设定 · 人物 · 共创</sub><br><sub>更新于 2026-06-16 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 README 自称旧版仓库，新版为 TavernAI/TavernAI；SillyTavern 由其分叉而来</sub>

- **[Risuai](https://github.com/kwaroran/Risuai)** · ★ 1.7k<br>跨平台 LLM 角色扮演客户端：lorebook 按关键词注入设定，HypaMemory/SupaMemory 压缩长对话记忆，支持多角色群聊和条件变量提示词<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 主要定位角色扮演聊天前端；支持多家 API、插件与 TTS</sub>

- **[ChineseAiDungeonChatGPT](https://github.com/bupticybee/ChineseAiDungeonChatGPT)** · ★ 1.4k<br>早期中文 AI 地牢：玩家每回合输入行动，ChatGPT 按文字冒险设定续写剧情，支持存档读档与 GUI<br><sub>方法：共创</sub><br><sub>更新于 2023-03-27 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 2023 年项目，按影响力收录；依赖 revChatGPT 非官方接口，大概率已无法直接运行</sub>

- **[AI-Chat](https://github.com/HappyFox001/AI-Chat)** · ★ 818<br>Narratium 角色扮演与冒险平台：兼容 SillyTavern 角色卡和世界书，冒险模式由玩家选择推动剧情，用 React Flow 可视化会话记忆与分支<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-03-30 📦 · 🧩 应用 · 英文</sub><br><sub>💡 已归档、停止开发（2026-03 最后更新），按 ≥100★ 保留</sub>

- **[TenCyclesofFate](https://github.com/CassiopeiaCode/TenCyclesofFate)** · ★ 256<br>《浮生十梦》文字冒险：每天十次入梦轮回，AI 实时生成一世人生，关键行动请求 D100“天命判定”按成败改写走向，另有 AI 反作弊识别玩家的提示词注入<br><sub>方法：模拟 · 共创</sub><br><sub>更新于 2026-05-29 · 🧩 应用 · 中文</sub><br><sub>💡 需 OpenAI 兼容 API 与 Linux.do OAuth 登录；GitHub 未识别许可证</sub>

- **[open-dungeon](https://github.com/newideas99/open-dungeon)** · ★ 238<br>本地 AI 角色扮演/文字冒险：Do/Say/Story 三种输入推进叙事，旧段落滚动压缩成「前情提要」保长篇记忆，角色立绘同时喂给叙事模型与生图保持视觉连续<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-07-06 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 默认 Ollama + Gemma 4，可接任意 OpenAI 兼容端点；默认叙事提示词允许成人内容；Mac 版 DMG 在 Releases</sub>

- **[ai-novel-studio](https://github.com/weike-zhang/ai-novel-studio)** · ★ 225<br>互动小说引擎：冻结世界快照和已提交状态，玩家行动后模型只提出正文与状态补丁，服务端校验人物、场景不变量后再事务提交，防止设定漂移<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 公开版只含合成示例数据，不含线上站内容；完整运行需 MySQL、Redis、RabbitMQ；go run ./cmd/demo 可离线看校验演示</sub>

- **[Aventuras](https://github.com/AventurasTeam/Aventuras)** · ★ 212<br>AI 文字冒险/协作写作前端：按章自动摘要并检索前情，lorebook 按场景注入且有 agent 自动合并补全，逐回合追踪在场人物、地点与物品<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 有冒险与创意写作两种模式；提示词均为可编辑 Liquid 模板；提供桌面与 Android 安装包，也可源码构建</sub>

- **[lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)** · ★ 202<br>单 HTML 的 LLM 写作前端：故事/冒险/聊天/指令四种模式，支持 Memory、Author's Note、World Info 世界书和预设剧本库<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 随 KoboldCpp 捆绑，是旧版 KoboldAI 的继任前端；可接 KoboldCpp、AI Horde、OpenAI、Claude 等</sub>

- **[AI-Gamble](https://github.com/xiamuceer-j/AI-Gamble)** · ★ 196<br>互动小说游戏：开局先生成整篇故事结构图（Mermaid 可视化分支与多结局）和文风描述，再按玩家选择逐段生成情节<br><sub>方法：规划 · 风格 · 共创</sub><br><sub>更新于 2026-01-01 💤 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 2026-01 后未更新，按 ≥100★ 保留；用 OpenAI 接口</sub>

- **[WhatIf](https://github.com/ypcypc/WhatIf)** · ★ 189<br>把中文小说变成可玩世界：抽取事件、角色、地点、物品与实体状态变化，玩家进入原著自由行动、偏离主线，引擎保持叙事连贯<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-05-21 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Alpha 阶段；小说原文需自备</sub>

- **[app](https://github.com/LettuceAI/app)** · ★ 144<br>隐私优先的角色扮演客户端：自定义角色卡和结构化系统提示模板，长期记忆以上下文摘要加可编辑记忆条目实现，BYOK 接 20+ 模型含本地 llama.cpp<br><sub>方法：人物 · 记忆</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 偏角色聊天，也可作陪伴用途；叙事机制主要是长期记忆；Android / 桌面多端</sub>

- **[jubensha-ai](https://github.com/JianWang97/jubensha-ai)** · ★ 141<br>AI 先生成剧本杀（背景、角色秘密、证据、场景），可用自然语言改稿，再由 AI 扮演全部角色走自我介绍、搜证、讨论、投票、揭晓等 8 个阶段<br><sub>方法：人物 · 多智能体 · 模拟</sub><br><sub>更新于 2026-08-04 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 可选 TTS（MiniMax/CosyVoice）和文生图（ComfyUI/MiniMax）</sub>

- **[vellium](https://github.com/tg-prplx/vellium)** · ★ 138<br>本地桌面 RP 与写作工作台：多角色聊天带分支时间线、LoreBook、作者注与场景状态；写作按章节/场景组织，配 Character Forge 与 RAG<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-04 · 🧩 应用 · 英文 · MIT</sub>

- **[diceframe](https://github.com/diceframe/diceframe)** · ★ 123<br>自部署 AI 跑团引擎：GM 模型接收自然语言行动，系统自动判定检定并掷骰、更新 HP/理智/物品，世界书按关键词注入，长团压缩摘要加向量召回<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 支持 CoC 7e / D&D 5e 轻量规则与无骰叙事；可接 QQ 群聊 Bot（NapCat）；AGPL-3.0</sub>

- **[SillyTavern-Pathweaver](https://github.com/mattjaybe/SillyTavern-Pathweaver)** · ★ 119<br>ST 剧情导演扩展：读近期对话，按顺势、反转、新角色、类型风格生成最多 6 条走向供发给 AI；Surprise Me 提前埋入隐藏事件<br><sub>方法：理论 · 共创</sub><br><sub>更新于 2026-03-06 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 含可选 NSFW 建议类别；2026-03 后未更新，但 ≥100★</sub>

- **[Auto-Cards](https://github.com/LewdLeah/Auto-Cards)** · ★ 107<br>AI Dungeon 场景脚本：从剧情中识别命名实体，定期让 AI 自动写成故事卡，并为重要卡片做长期记忆更新和摘要，缓解剧情中的物体恒存问题<br><sub>方法：记忆</sub><br><sub>更新于 2026-01-20 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需装进 AI Dungeon 平台的场景脚本中使用；提供 API 供其他脚本作者调用</sub>

- **[NarrativeEngine-P](https://github.com/Sagesheep/NarrativeEngine-P)** · ★ 104<br>自托管 AI 跑团主持：导入世界设定和规则文件自动分块索引，长战役靠智能记忆、活 NPC、地点账本和世界自动管理推进，附多套现成世界<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 只需 Node 20+；另有 Android 客户端 NarrativeEngine-M；仓库含 mods/ability-compendium.7z 数据包和 .bat 启动/修复脚本</sub>

- **[sillytavern-DeepLore](https://github.com/pixelnull/sillytavern-DeepLore)** · ★ 89<br>ST 世界书检索引擎：设定存在 Obsidian 库，关键词+BM25 粗筛、AI 读摘要精选、按时代/地点/角色门控后注入；图书管理员代理补写缺失条目<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2026-07-04 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需 SillyTavern + Obsidian Local REST API 插件；AI 检索每轮多一次调用</sub>

- **[otaku](https://github.com/enclavum/otaku)** · ★ 87<br>LLM 创作/角色扮演前端：对话与小说两种模式，前 20 与后 150 条原文保文风，中段自动切场景换成摘要，识别角色并各记见闻日志，模型可留私密笔记<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 终端 TUI + Web；lorebook 尚在计划中</sub>

- **[Promised_Land_AI](https://github.com/HenryPotter0546/Promised_Land_AI)** · ★ 84<br>多人在线文字冒险：DeepSeek 按玩家属性、装备和阶段生成剧情，用 TF-IDF 检索剧情库做 RAG，AI 可直接读写玩家数据库，配迷雾 ASCII 地图<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2025-09-26 💤 · 🧩 应用 · 中文</sub><br><sub>💡 需 DeepSeek API</sub>

- **[aisandboxgame](https://github.com/hayowei/aisandboxgame)** · ★ 79<br>浏览器文字 RPG：设计模式访谈生成世界卡（设定/人物/地点/开场），游玩时模型推理并叙述，NPC 各自维护认知与关系状态，d20 检定裁定行动<br><sub>方法：设定 · 模拟 · 共创</sub><br><sub>更新于 2026-06-30 · 🧩 应用 · 多语言</sub><br><sub>💡 纯前端 PWA，BYOK；代码 AGPL-3.0，提示词 CC BY-NC-SA 4.0</sub>

- **[filmgame](https://github.com/mmlong818/filmgame)** · ★ 79<br>互动影游五阶段：世界锚点→规模方案→章/幕/节点分支结构→逐节点写对白（角色声纹卡）→全局结构校验和五位导演终审，可导出 ink<br><sub>方法：规划 · 人物 · 修订 · 共创</sub><br><sub>更新于 2026-09-16 · 🧩 应用 · 中文</sub><br><sub>💡 编剧主导、AI 协作；后端可用本地 Claude CLI 或 Anthropic/OpenAI/Gemini API；需 Postgres</sub>

- **[front-porch-AI](https://github.com/linux4life1/front-porch-AI)** · ★ 78<br>本地角色扮演桌面应用：Realism Engine 追踪角色情绪、信任、需求和记忆，随故事时钟变化；支持 lorebook、群像角色和故事工作室<br><sub>方法：人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · 4 个 skill · AGPL-3.0</sub><br><sub>💡 主打角色聊天，可导入 Backyard AI 的 .byaf；内置 TTS 和图像生成，支持本地 KoboldCpp</sub>

- **[Inner-Self](https://github.com/LewdLeah/Inner-Self)** · ★ 78<br>AI Dungeon 模组：给每个 NPC 独立的私有记忆、目标、秘密和计划，被提及时自我反思、整理思绪并驱动后续情节，可合并 Auto-Cards 建设定卡<br><sub>方法：人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-01-20 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需在 AI Dungeon 场景脚本里使用；2026-01 后无更新，NPC 自主心智的思路少见，按例外收录</sub>

- **[NeverEndingQuest](https://github.com/MoonlightByte/NeverEndingQuest)** · ★ 77<br>AI 地下城主跑 D&D 5e（SRD）战役：LLM 只负责叙事，独立规则引擎管骰子/背包/状态，配合冒险模块工具包与对话压缩保持长期战役记忆<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文</sub><br><sub>💡 基于 WOTC SRD 5.2.1 内容；默认 OpenAI GPT-5.x，可接 Gemini/本地模型；规则引擎 bin/nql-apply.exe 为编译二进制，Windows 安装用 .bat 脚本</sub>

- **[ludo-npc-ai](https://github.com/koronto11/ludo-npc-ai)** · ★ 76<br>游戏叙事与 NPC 工作台：世界设定→角色→场景→分支对白卡→审阅 AI 候选稿→试玩彩排，中英双语 Skills 和本地 MCP 让外部 AI 参与起草<br><sub>方法：设定 · 人物 · 共创</sub><br><sub>更新于 2026-10-11 · 🧩 应用 · 多语言 · 2 个 skill · MIT</sub><br><sub>💡 AI 只出候选稿，作者终审；0.1.0 预览版</sub>

- **[chasm_engine](https://github.com/atisharma/chasm_engine)** · ★ 70<br>生成式文字冒险服务器：几句话指定世界，边玩边生成地点和角色；地点、物品、背包、任务持久化，全局事件与角色对话记忆存向量库，NPC 会移动<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-05-09 📦 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 已停止维护（已归档），后继为重写版 atisharma/chasm；需配合客户端使用；Hy 语言，AGPL-3.0</sub>

- **[loreweaver](https://github.com/1A7432/loreweaver)** · ★ 66<br>AI 跑团主持引擎：AI KP 读模组、扮演全部 NPC、守线索，检定、伤害、理智都由代码掷骰结算；规则、设定、角色打包成可分享的文件包<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-10-11 · ⚙️ 框架 · 多语言 · 7 个 skill · MIT</sub><br><sub>💡 内置 CoC 7e 和 D&D 5e SRD，中英双语；可导入 SillyTavern 角色卡、配 AI 队友；桌面客户端在 1A7432/loreweaver-studio；安装脚本默认拉最新开发版</sub>

- **[Smart-Memory](https://github.com/senjinthedragon/Smart-Memory)** · ★ 64<br>ST 多层记忆扩展：自动抽取角色事实、关系史、各角色知道的信息与秘密、实体状态、场景史、故事弧和滚动摘要，按预算注入上下文<br><sub>方法：人物 · 记忆</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 英文 · AGPL-3.0</sub><br><sub>💡 需单独配置记忆用 LLM，可选 Ollama embeddings；群聊中每个角色有独立记忆</sub>

- **[hordestudio](https://github.com/ddkhan24/hordestudio)** · ★ 59<br>本地 AI 角色扮演工作室：角色卡与群聊房间、带地点和后果的持久世界、可选 RPG 规则与多人团，另有按日程、需求、关系推演生活的虚拟人<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 英文</sub><br><sub>💡 SillyTavern 式角色卡 + AI Dungeon 式世界；含虚拟人陪伴模块；仓库无许可证</sub>

- **[covel](https://github.com/ackness/covel)** · ★ 57<br>插件化 AI RPG 框架：叙事、NPC、设定、建卡各为插件 agent，世界包打包设定与规则，回合后投影共享事实层 WorldIR，隐藏事件按条件触发<br><sub>方法：设定 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-10-15 · ⚙️ 框架 · 多语言 · 4 个 skill · MIT</sub><br><sub>💡 早期版本，存档格式常有破坏性变更；另有视觉小说式舞台模式</sub>

- **[vina](https://github.com/vina-ai/vina)** · ★ 50<br>一句提示生成整部视觉小说：GPT 先出情节、带性格的人物和地点，再按场景写对白并配表情，SD 画背景，打包成可玩的 Ren'Py 工程<br><sub>方法：规划 · 人物</sub><br><sub>更新于 2023-06-28 💤 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 黑客松作品；需 OpenAI API、本地 SD WebUI 和 Ren'Py</sub>

- **[ai-murder-mystery](https://github.com/ScottishFold007/ai-murder-mystery)** · ★ 49<br>AI 剧本杀：每个角色是有人格、记忆和秘密的独立 agent，回复经生成→批评→修订防泄露；剧本编辑器支持 AI 辅助创作与质检，另有证物系统<br><sub>方法：多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-02-26 💤 · 🧩 应用 · 中文</sub><br><sub>💡 基于 ironman5366/ai-murder-mystery-hackathon（防泄露机制来自原版），新增自定义剧本编辑器、质检和证物系统；许可证 NOASSERTION；配图需火山引擎</sub>

- **[RPGraph](https://github.com/unrefined803/RPGraph)** · ★ 47<br>本地角色扮演工作室：节点工作流把每轮拆成翻译、扮演、说话人标注、故事时间、事件等独立 LLM 调用，Storybook 助手生成场景人物，带角色手机应用<br><sub>方法：设定 · 模拟 · 共创</sub><br><sub>更新于 2026-10-08 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 默认工作流按 Gemma 4 31B 调校，模型需稳定输出 JSON；含成人向社交应用；可选 ComfyUI 生图配音</sub>

- **[Project_Infinity](https://github.com/electronistu/Project_Infinity)** · ★ 45<br>5e 规则跑团：规则引擎掷骰结算并写机制面板，LLM 只写叙事；开局生成四王国政治世界或时间旅行设定，带角色锻造和战斗追踪<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 英文</sub><br><sub>💡 需 Ollama Cloud 或 Gemini；Gemini Key 解锁配图；基于 D&D SRD 5.1</sub>

- **[noras-tavern](https://github.com/LoveMaker-art/noras-tavern)** · ★ 41<br>基于 SillyTavern 的角色扮演应用：以世界组织角色、会话与世界书，剧情账本记长线进展，Nora agent 经 MCP 管理世界、角色与记忆<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 中文 · 5 个 skill</sub><br><sub>💡 基于 SillyTavern 二次开发，兼容角色卡/世界书生态；Nora 需 Hermes Agent 与 IM 平台，只装酒馆也可游玩；安装包未签名</sub>

- **[open-dungeon-master](https://github.com/Lebbitheplow/open-dungeon-master)** · ★ 41<br>AI 地下城主跑 D&D 5e：模型叙事并扮演 NPC，按隐藏故事主线（前提、赌注、反派）推进并随战役重生成，骰子与数值全由服务端规则引擎结算，支持多人<br><sub>方法：规划 · 模拟 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 基于 newideas99/open-dungeon 扩展而来；可用 Claude Code / Codex / opencode / Grok Build 订阅当叙事者</sub>

- **[project-lunar](https://github.com/horizonfps/project-lunar)** · ★ 41<br>AI 叙事 RPG 引擎：四层记忆每 4 回合结晶，NPC 各有私密情绪/目标/秘密计划且只知亲见之事，离屏世界随时间演化，自动生成宏观剧情弧与钩子<br><sub>方法：规划 · 人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-09-07 · 🧩 应用 · 多语言</sub><br><sub>💡 英语/巴西葡语；需 Docker 跑 Neo4j；附带把 Claude 订阅转 API 的代理；无开源许可证</sub>

- **[wrAIter](https://github.com/FontaineRiant/wrAIter)** · ★ 40<br>本地互动写故事：人机轮流写段落，或从 AI 给的 3 个行动中选、或语音输入；首段设定常驻上下文，配多角色 TTS 朗读与 SD 插图<br><sub>方法：共创</sub><br><sub>更新于 2026-08-23 · 🧩 应用 · 英文 · MPL-2.0</sub><br><sub>💡 用 Hugging Face 本地模型（默认 2.7B 故事微调模型，可换 Mistral 等），需 8GB+ 显存</sub>

- **[AnyWorld](https://github.com/iamarxs/AnyWorld)** · ★ 38<br>多人浏览器文字冒险：主持人设定场景、目标和私密引导，玩家按顺序用自然语言行动，一轮后 AI 统一叙述结果；可加隐藏的概率事件规则制造意外<br><sub>方法：共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 本地 llama.cpp 后端目前只输出英文叙述，OpenAI 后端跟随场景语言</sub>

- **[GameMasterAI](https://github.com/deckofdmthings/GameMasterAI)** · ★ 37<br>单人 TTRPG 网页应用：GPT 扮演地下城主叙事，另一个 AI 记录员整理游戏笔记供后续回合参考，存档存在 MongoDB<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2023-11-11 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 原为 YouTube 频道 Deck of DM Things 的 Patreon 项目，作者无力维护后开源；需 OpenAI Key 和 MongoDB Atlas</sub>

- **[storyforge-ai](https://github.com/Qiuerjun/storyforge-ai)** · ★ 37<br>小说/跑团对话式共创：每轮自动注入角色、世界状态和关键词触发的世界观词条，AI 从对话中抽取事实存入记忆并检索，追踪主线进度等变量，支持 KP 隐藏设定<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-07-04 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 兼容 OpenAI API 和本地 Ollama</sub>

- **[yikes](https://github.com/psema4/yikes)** · ★ 35<br>文字冒险上下文工程规范：状态分系统/角色/世界三层，LLM 按固定 JSON 返回叙事、效果和可选行动，效果校验后回写状态形成闭环，附 Node.js 实现<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2025-10-16 💤 · ⚙️ 框架 · 英文 · ISC</sub><br><sub>💡 参考实现需本地 Ollama</sub>

- **[ai-text-adventure](https://github.com/TomMannion/ai-text-adventure)** · ★ 34<br>选择式文字冒险：AI 先生成可选角色的特质和背景，每段剧情附 2–4 个带风险等级的选项，每段压成摘要（位置、物品、关系）供后文保持连贯<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2024-04-21 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需自备 OpenAI Key，DALL·E 配图；README 很简略，方法见 src/hooks 里的提示词</sub>

- **[ChatRPG](https://github.com/KarmaKamikaze/ChatRPG)** · ★ 34<br>C# Blazor 选择冒险游戏：叙事者、档案员、检查者、导航者、书记员等 ReAct agent 分工，LLM 当主持人推进战斗、NPC 与任务<br><sub>方法：记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-08-11 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需 PostgreSQL 与 OpenAI API</sub>

- **[ghostpad](https://github.com/ghostpad/ghostpad)** · ★ 33<br>KoboldAI 的移动优先改版：光标处续写故事，记忆、作者笔记和世界信息条目可存入库并拼装成场景与角色，支持语音输入输出和实时编辑<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2024-02-27 💤 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 基于 KoboldAI/KoboldAI-Client；跑本地模型（支持 Llama.cpp、AutoAWQ）；仓库带上游的安装脚本和 umamba.exe</sub>

- **[gpt-adventures](https://github.com/nferraz/gpt-adventures)** · ★ 33<br>文字冒险引擎：GPT 先生成含标题、情节、玩家、带出口的地点和物品的游戏结构，基础指令由引擎处理，其余行动交给模型当 GM 并改写游戏状态<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2023-05-17 💤 · 🧩 应用 · 英文</sub><br><sub>💡 单个 Python 脚本，默认 gpt-3.5-turbo</sub>

- **[VerseCraft](https://github.com/bei666qi-pan/VerseCraft)** · ★ 33<br>自由输入行动的互动小说引擎：回合路由先查世界知识与角色认知边界，模型生成叙事候选后经校验提交状态增量，后台世界导演推进 NPC 议程<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-09-03 · 🧩 应用 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 示例世界为中文悬疑恐怖；完整运行需 PostgreSQL 与 Redis</sub>

- **[ai-death-game](https://github.com/yami-inc/ai-death-game)** · ★ 31<br>5 个不同人设的 AI 代理在死亡游戏里辩论、投票互相淘汰，主持人播报流程，玩家以 GM 身份插话下指令、投票或强制淘汰来改变走向<br><sub>方法：多智能体 · 模拟 · 共创</sub><br><sub>更新于 2026-05-22 · 🧩 应用 · 日文 · MIT</sub><br><sub>💡 需自备 Gemini API key，浏览器直连；README 日英双语</sub>

- **[AIDscripts](https://github.com/Gnurro/AIDscripts)** · ★ 28<br>AI Dungeon 场景脚本合集：Encounters 按条件向故事注入动态事件，RPGmech 加入属性与技能检定，另有维持角色形态的上下文注释等工具<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2021-04-28 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 需在 AI Dungeon 场景脚本中使用；合集里也有改写文字风格的玩笑脚本；附带的 zip 是可直接导入的脚本包，同仓有 JS 源码</sub>

- **[gamentic](https://github.com/hec-ovi/gamentic)** · ★ 27<br>叙事者加每个角色一个 agent（人设、私聊记忆、秘密）；角色只能向叙事者申请改动世界状态，近期场景读原文，旧场景折叠成滚动摘要<br><sub>方法：人物 · 记忆 · 多智能体 · 模拟</sub><br><sub>更新于 2026-07-25 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 按 AMD Strix Halo 本地全栈调优（llama.cpp、FLUX、Maya1 TTS），docker-compose 部署</sub>

- **[DnD-AI](https://github.com/QuitoTactico/DnD-AI)** · ★ 25<br>Django 版 AI 跑团：按主题生成战役故事、八种地形地图、敌人、宝物和三个最终 Boss，玩家用自然语言下指令，关键场景配 AI 插图，支持多人<br><sub>方法：设定 · 共创</sub><br><sub>更新于 2024-11-12 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 EAFIT 课程项目；作者已转向后继 QuitoTactico/DnD-AI-2.0；需 OpenAI/Gemini 等 Key</sub>

- **[soul-killer](https://github.com/Xeonice/soul-killer)** · ★ 25<br>从任意人物的公开数字足迹提取身份、语言风格和行为模式，蒸馏成角色，再和世界观合成可游玩的 Galgame 剧本 skill<br><sub>方法：设定 · 人物 · 风格 · 共创</sub><br><sub>更新于 2026-04-15 💤 · ⚙️ 框架 · 多语言 · GPL-3.0</sub><br><sub>💡 CLI 工具（TypeScript 源码在仓库），导出的 .skill 档案在 Claude Code / OpenClaw 里游玩；官方安装脚本从作者的 Cloudflare 下载二进制，也可以从源码构建</sub>

- **[comic-book-generator](https://github.com/tfrere/comic-book-generator)** · ★ 24<br>互动漫画故事游戏：随机抽画风、类型、年代、麦高芬和主角生成世界，Mistral 逐段写剧情并给出选项，再为每段生成分格画面提示词和配音<br><sub>方法：设定 · 共创</sub><br><sub>更新于 2025-02-12 💤 · 🧩 应用 · 英文</sub><br><sub>💡 Mistral AI 游戏 Jam 作品；需 Mistral API 和 Hugging Face 图像端点；README 很简略</sub>

- **[gpt-interactive-novel](https://github.com/that-one-arab/gpt-interactive-novel)** · ★ 24<br>终端互动小说：玩家设定背景、主题、角色和篇幅，故事有明确开端和结局目标，可选选项式或自由输入推进<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2023-06-30 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 作者建议用 GPT-4，部分功能在 gpt-3.5 上不稳定</sub>

- **[ZRIC-AI-TRPG-Engine](https://github.com/zRICGao/ZRIC-AI-TRPG-Engine)** · ★ 24<br>DM 在环 AI 跑团引擎：每次行动生成 2–4 个带数值副作用的分支，三级记忆、RAG 世界书、NPC 情绪状态机、可生长地图、触发器与多时间线<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-05-13 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 早期开发阶段；需 DeepSeek 与硅基流动 Key（可选 Claude）；附带示例剧本不完整</sub>

- **[cyoa](https://github.com/essencevc/cyoa)** · ★ 23<br>选择冒险生成示例：先按用户提示生成标题、简介和封面描述，再用结构化输出递归生成二选一剧情树直到设定深度，每个节点配图<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2025-05-27 💤 · 🧩 应用 · 英文</sub><br><sub>💡 主要演示 restate 工作流编排；依赖 Gemini、Modal、S3 和 Turso</sub>

- **[Dungeon-master-OS-WFGY](https://github.com/djnightmare9909/Dungeon-master-OS-WFGY)** · ★ 23<br>Gemini 驱动的 D&D 长篇战役地下城主：持久化世界状态，玩家选择留下长期后果，程序化生成冒险；另提供可粘贴进任意聊天 AI 的 DM 内核提示词<br><sub>方法：记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-09-30 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需 Google AI Studio API Key；提示词基于 WFGY 语义推理引擎；线上版启用 Vercel Analytics</sub>

- **[AI-Novel](https://github.com/shuaihaoV/AI-Novel)** · ★ 22<br>按题材预设提示写一两千字开篇，之后每段生成三个走向不同的剧情选项，读者选定后带前文续写，逐步推进故事线<br><sub>方法：理论 · 共创</sub><br><sub>更新于 2025-06-26 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 参考 Linux.do 上 TQmyLady 的实现；需 OpenAI 兼容接口</sub>

- **[Omni-plane-Travels](https://github.com/xuegao1416/Omni-plane-Travels)** · ★ 22<br>AI 互动小说引擎：四阶段编织世界与角色，剧情导演写前指导、写后核对，NPC 幕后行动、被见闻后才更新认知，编译式记忆存长期事实；可把小说拆成世界书开局<br><sub>方法：规划 · 设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 BYOK；Web/PWA，Tauri 原生工程不在本版源码内；可选 Cloudflare 云存档与创意工坊</sub>

- **[rekallhalo](https://github.com/Idun/rekallhalo)** · ★ 22<br>Gemini 互动小说：开局选叙事结构与手法，分层记忆（核心/长期/剧情），导演模式预设事件由 AI 融入剧情，剧情蓝图按章字数与必触发事件推进<br><sub>方法：规划 · 理论 · 记忆 · 共创</sub><br><sub>更新于 2025-12-18 💤 · 🧩 应用 · 中文</sub><br><sub>💡 需 Gemini API Key；附实时配图与特效；最后更新 2025-12，按方法独特收录</sub>

- **[shadowrealms-ai](https://github.com/Somnius/shadowrealms-ai)** · ★ 21<br>自托管的《黑暗世界》跑团 AI 说书人：按角色卡掷骰池判定，本地模型配 RAG 检索规则书和剧情记忆，支持 oWoD 与 V5 规则<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub>

- **[taleweaver](https://github.com/jschm42/taleweaver)** · ★ 21<br>AI 全知主持人驱动的浏览器 RPG：生成世界、场景、NPC 与任务，NPC 有各自目标并可跨场景移动，后台按规则书管理战斗与物品，附冒险编辑器和 AI 校验<br><sub>方法：设定 · 模拟 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 自托管 Docker，beta 阶段；带 TTS 配音；部分素材为 CC BY-NC 4.0</sub>

- **[living-storybook](https://github.com/seehiong/living-storybook)** · ★ 20<br>多人共创分支故事：改写过去会触发因果矛盾检测，可分叉时间线或覆写正史；章节蓝图按节拍推进，角色跨时间线保留记忆<br><sub>方法：规划 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-02-08 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 Gemini 3 + LangGraph + Firestore；2026-02 后未更新，因时间线分叉思路少见保留</sub>

- **[InfinityWorlds](https://github.com/PatzEdi/InfinityWorlds)** · ★ 19<br>终端文字冒险：GPT 按玩家行动续写，flashback 机制回调前文的人名、地点与事件，可开行动回顾，主题和模型可配置<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2024-09-12 💤 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 需 OpenAI API</sub>

- **[LoomStudio](https://github.com/The-LoomStudio/LoomStudio)** · ★ 19<br>本地角色扮演与互动叙事工作台：时间线随时分支，角色卡和 Lore 设定共享，可查看提示词构建结果，Agent 用工具读写状态和剧情<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文</sub><br><sub>💡 Beta；官方扩展 STBridge 可导入 SillyTavern 卡/世界书，The World 扩展管理时间、天气和地点</sub>

- **[RPG-AI-Assistant](https://github.com/Guljaca/RPG-AI-Assistant)** · ★ 19<br>本地小模型跑文字 RPG：每轮拆成多阶段短提示，先取场上物件描述，再让每个 NPC 单独定意图后合成场景，按物件存取联想式长期记忆，加随机事件<br><sub>方法：记忆 · 模拟</sub><br><sub>更新于 2026-05-02 · 🧩 应用 · 多语言</sub><br><sub>💡 需 LM Studio 和支持 Tools/Thinking 的模型（Qwen 3.5 9B、Gemma-4 等）；支持 spec-v3 角色卡；俄/英双语</sub>

- **[Dungeo_ai_lan_play](https://github.com/Laszlobeer/Dungeo_ai_lan_play)** · ★ 18<br>本地 Ollama 多人回合制跑团：2–5 人建角选题材，AI 当 DM 叙事，世界追踪器记录 NPC、阵营和行动后果，世界状态永久变化并可存档<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-01-25 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需本地 Ollama，可选 AllTalk TTS 语音；仅局域网多人；同作者另有单人版 Laszlobeer/Dungeo_ai</sub>

- **[RyokanApp](https://github.com/Finn-Hecker/RyokanApp)** · ★ 16<br>Windows/Android 互动故事客户端：导入 V3 角色卡与关联 lorebook，可克隆分支对话、切换玩家身份，房主出模型、好友用浏览器加入多人共写<br><sub>方法：设定 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 本地模型或 API；多人房间端到端加密</sub>

- **[text-rpg-adventure](https://github.com/rhenry7/text-rpg-adventure)** · ★ 16<br>C# 控制台 D&D 文字冒险：创建角色后掷骰决定场景、敌人和目标，分四章调用 OpenAI 生成冒险，配背包、属性和战斗模拟<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2023-10-25 💤 · 🧩 应用 · 英文</sub><br><sub>💡 README 只有一句，方法要看代码；个人练习性质</sub>

- **[chasm](https://github.com/atisharma/chasm)** · ★ 15<br>生成式文字冒险：世界是一个 markdown 文件的 git 仓库，叙事者经 pi harness 读写地点、人物、事件状态，跨会话持久，可分发给他人续玩<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-06 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需支持工具调用的模型；作者旧版 chasm_client 已归档</sub>

- **[The-Endless-Tale](https://github.com/Jit-Roy/The-Endless-Tale)** · ★ 15<br>目标驱动的互动小说引擎：故事按 JSON 目标清单推进，评估玩家行动是否完成目标；每个角色独立思考并自行决定进出场景，世界状态随时间推移变化<br><sub>方法：人物 · 模拟 · 共创</sub><br><sub>更新于 2026-06-10 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需 Google Gemini API（建议两把 key 并行）；每轮约 40 秒</sub>

- **[world-walker](https://github.com/badhope/world-walker)** · ★ 15<br>互动小说规则核心+MCP：玩家行动交给 85+ 学术公式结算战斗/交易/社交/业力，Agent 只做文学转写；三层记忆撑长局，兼容酒馆角色卡与世界书<br><sub>方法：记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-10-15 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 示例设定为修仙世界</sub>

- **[chronicles-of-chaos](https://github.com/RedCliffScribe/chronicles-of-chaos)** · ★ 14<br>三国互动叙事 RPG：LLM 理解行动并叙事，本地结构化状态校验写回人物/势力/领地事实，NPC 分层记忆且离屏行动，战斗先规则结算再叙述<br><sub>方法：设定 · 记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-08-17 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 目前只有三国世界包；代码 AGPL，叙事素材 CC BY-NC-SA</sub>

- **[dungeongod-agi](https://github.com/benjcooley/dungeongod-agi)** · ★ 14<br>通用 AI 地下城主：用 YAML 定义规则、冒险模组、角色队伍和提示词，模型按规则主持并记住玩家，支持多套游戏<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2024-08-10 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 README 只有两句，方法要看 data/games 下的模组、规则和提示词文件；含微调脚本</sub>

- **[Infinite-RPG](https://github.com/Vekkul/Infinite-RPG)** · ★ 14<br>网页无限 RPG：Gemini 生成世界地图、地点描述、遭遇和社交场景，日志系统记录任务和隐藏叙事 flag，让之前的选择影响后续事件<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-04-11 💤 · 🧩 应用 · 英文</sub><br><sub>💡 vibe coding 作品，Google AI Studio 应用；需 Gemini API；含回合制战斗和像素头像生成</sub>

- **[taleweave-ai](https://github.com/ssube/taleweave-ai)** · ★ 14<br>文字冒险/MUD 引擎：一句话生成世界，LLM 角色按计划→行动轮次自主模拟，追踪情绪、饥渴、天气等状态，用行动摘要和笔记促成涌现剧情，可接 Discord<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2024-06-23 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 支持 Ollama 和 OpenAI 兼容接口；可选 ComfyUI 出图</sub>

- **[True-Auto-Stats-for-AIDungeon-RPG-Scenarios](https://github.com/Yi1i1i/True-Auto-Stats-for-AIDungeon-RPG-Scenarios)** · ★ 14<br>AI Dungeon 场景脚本：根据玩家输入和 AI 输出自动建立并更新属性、背包、技能、伤病、饥饿等状态，存进故事卡再转述给模型，限制玩家全能<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2025-08-23 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 粘贴到 AI Dungeon 脚本编辑器的四个钩子中使用</sub>

- **[DungeonGPT-JS](https://github.com/EdwardAThomson/DungeonGPT-JS)** · ★ 13<br>AI 地下城主网页 RPG：骰点、战斗和战役里程碑由确定性引擎裁决，AI 只负责叙述结果；程序生成世界与城镇，RAG 检索历史剧情保持记忆<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 基于同作者 Python 版 EdwardAThomson/DungeonGPT；线上版有会员分级</sub>

- **[living-story-world](https://github.com/jonmartin721/living-story-world)** · ★ 13<br>持续世界的配图章节生成：用知识图谱记住人物、地点和剧情线，玩家选择影响后续章节，文本与插图模型分别可换<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-21 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 默认本地 Ollama，可选 Gemini/Groq/OpenRouter 等；配图可接 ComfyUI/AI Horde</sub>

- **[Story-Arc-Engine](https://github.com/Yi1i1i/Story-Arc-Engine)** · ★ 13<br>AI Dungeon 脚本：每隔设定回合调用 AI 生成由关键事件组成的故事弧，写进作者笔记持续引导叙事，失败自动重试，故事弧可在故事卡里查看和修改<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-16 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 需在 AI Dungeon 平台作为场景脚本使用；作者标注 WIP；仓库未声明许可证</sub>

- **[TRPG-AI-DM](https://github.com/ACDD49967/TRPG-AI-DM)** · ★ 13<br>单人跑团 AI 主持：导入剧本后生成世界状态与知识图谱，主 DM 分派规则/战斗/记忆/图谱子 Agent，DM 与玩家信息隔离，后台定期推进剧情<br><sub>方法：设定 · 记忆 · 多智能体 · 模拟</sub><br><sub>更新于 2026-09-26 · 🧩 应用 · 中文 · 11 个 skill · MIT</sub><br><sub>💡 内置 D&D 5e/4e、COC 7e 规则；长期记忆带衰减与遗忘，可选 BGE-M3 / pgvector</sub>

- **[yumina-oss](https://github.com/lovetimo0421/yumina-oss)** · ★ 13<br>AI 原生互动小说引擎：世界文件声明世界书条目、类型化变量、规则与反应、空间/战斗/社交模拟系统，模型只发指令由引擎改状态，配会话记忆与分支回滚<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-09 · 🧩 应用 · 英文 · 10 个 skill · AGPL-3.0</sub><br><sub>💡 起源于 SillyTavern 分支，现为独立引擎；AGPL-3.0；托管版 yumina.io</sub>

- **[dmcp](https://github.com/shawnrushefsky/dmcp)** · ★ 12<br>AI 主持人用的 MCP 服务：170 个工具管理规则、世界、角色、任务、派系、秘密、时间和叙事日志，开局访谈后由 agent 设计规则并主持冒险<br><sub>方法：设定 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-01-06 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 内置 HTTP Web UI 看角色卡和地图；含图片存储与 NPC 语音描述，支持多 agent 协作</sub>

- **[freytag-forge](https://github.com/bcorfman/freytag-forge)** · ★ 12<br>作者用 Markdown 写有弧线的故事，引擎记录物件、位置和状态充当裁判，LLM 叙事者回应玩家任意行动；秘密要靠行动解锁，时钟持续推进<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 英文 · MIT</sub>

- **[Hashtag-DnD](https://github.com/raeleus/Hashtag-DnD)** · ★ 12<br>AI Dungeon 场景脚本：用 # 命令管理队伍角色属性与传记、背包、骰子检定、回合战斗、地点地图和不占上下文的笔记，可开 Auto-Cards 记忆卡<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2025-08-06 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 叙事由 AI Dungeon 平台模型完成；集成 LewdLeah 的 Auto-Cards；另含卡牌等小游戏</sub>

- **[openovel](https://github.com/Feed-Scription/openovel)** · ★ 12<br>互动小说双循环：前台叙事者只管流式出正文，后台 Showrunner、导演、世界、记忆等 agent 异步读回合，改写 Markdown/JSON 状态文件<br><sub>方法：记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-06-17 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 beta；不用向量库，故事状态全是普通文件；Electron 桌面版</sub>

- **[UnscriptedAdventures](https://github.com/dspencej/UnscriptedAdventures)** · ★ 12<br>5e 风格文字 RPG：先建角色（特质、职业、背景），LLM 主持人和 NPC 随玩家选择推进剧情，奖励系统评估玩家投入度并调整主持策略<br><sub>方法：人物 · 修订 · 共创</sub><br><sub>更新于 2024-12-11 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 作者标注 Alpha 阶段</sub>

- **[Dungeo-ai-new](https://github.com/Laszlobeer/Dungeo-ai-new)** · ★ 11<br>Ollama 终端文字冒险：选题材和角色后，DM 提示强制「行动→即时后果」，先分析玩家动作的动词和力度再注入题材规则续写，可存档和重抽<br><sub>方法：共创</sub><br><sub>更新于 2026-02-17 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 作者旧版为 Laszlobeer/-Dungeo_ai-otudated-</sub>

- **[InteractiveFilm-CharacterDailyAgent](https://github.com/OranDuanStudy/InteractiveFilm-CharacterDailyAgent)** · ★ 11<br>角色卡→Gemini 规划带精力和心情的全天日程→生成事件（R 级简单选择、SR 级多段分支）→导演分镜脚本→调用生图和视频模型演出<br><sub>方法：人物 · 模拟 · 共创</sub><br><sub>更新于 2026-03-23 💤 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 需 Gemini 和 nano_banana/seedream、sora2/kling 等图像视频 API；含亲密度养成，偏虚拟角色日常</sub>

- **[SceneIntruderMCP](https://github.com/Corphon/SceneIntruderMCP)** · ★ 11<br>故事工作台：把文本拆成场景、角色、物品和分支剧情供互动演绎，剧本模块生成初稿并逐章修订，场景还能转成漫画和视频<br><sub>方法：模拟 · 修订 · 共创</sub><br><sub>更新于 2026-04-01 💤 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 Go + React；漫画、视频工作台占很大比重；需配置 LLM、图像、视频提供方</sub>

- **[StatefulLore](https://github.com/cgstever/StatefulLore)** · ★ 11<br>ST 状态化世界书：用 JS lore 模块保存数值、状态、地点与机制，每轮生成权威状态快照注入提示，模型只管写作不管记忆<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2026-09-13 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 每个世界要写一个 JS 模块（附有让 AI 把现有世界书转成模块的指南）</sub>

- **[Story-Editor](https://github.com/izanagi771-stack/Story-Editor)** · ★ 11<br>ST 连续性审稿扩展：独立编辑模型只审新写内容，提出状态、设定、人物认知、剧情线变更与带引文的矛盾警告，作者批准后才写入记忆<br><sub>方法：记忆 · 修订</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 英文 · AGPL-3.0</sub><br><sub>💡 alpha 版，需 SillyTavern ≥1.19</sub>

- **[StoryWeaver-AI](https://github.com/1195214305/StoryWeaver-AI)** · ★ 11<br>无限流互动小说：按题材开局逐章生成 300–500 字并给选项，边缘函数注入文风指导、禁词过滤和上下文一致性校验，读者阅读时预生成后续分支<br><sub>方法：记忆 · 去 AI 味 · 共创</sub><br><sub>更新于 2025-12-23 💤 · 🧩 应用 · 中文</sub><br><sub>💡 阿里云 ESA 活动作品；依赖通义千问、通义万相和 ESA 边缘函数</sub>

- **[dnd-ai](https://github.com/chungs10/dnd-ai)** · ★ 10<br>本地 D&D 主持人实验：mem0 + ChromaDB 存角色与世界的长期记忆，掷骰、战斗等规则走确定性函数调用，提示模板维持人设和世界观<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2025-12-23 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 学生课程项目，多份实验脚本并存；需本地 Ollama（Qwen3:8B）；README 安装命令里的仓库名写错了</sub>

- **[GameMaster-GPT](https://github.com/dmkilday/GameMaster-GPT)** · ★ 10<br>命令行 AI 跑团 GM：读入角色卡文本，按角色生成冒险前提，玩家掷骰由程序结算后回报 GM，附对话压缩脚本控制上下文长度<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2023-07-17 💤 · 🧩 应用 · 英文 · GPL-3.0</sub>

- **[OpenCrawlEngine](https://github.com/savannah-i-g/OpenCrawlEngine)** · ★ 10<br>本地单人 RPG 引擎：LLM 主持人通过结构化工具调用叙事和驱动世界，属性、战斗、检定、势力、产业等由确定性规则引擎结算，战役存 SQLite<br><sub>方法：模拟 · 共创</sub><br><sub>更新于 2026-06-22 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 C++ / Dear ImGui 桌面程序；Releases 有 AppImage/deb，源码可自行构建</sub>

- **[tracyhill-rp](https://github.com/ArkAscendedAI/tracyhill-rp)** · ★ 10<br>自托管多人长篇 RP 客户端：按战役持久化会话，维护结构化世界状态，系统提示词做版本管理，对话中途可切换十家模型<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 可直接登录自己的 Claude / ChatGPT 订阅使用</sub>

- **[venger](https://github.com/murderteeth/venger)** · ★ 10<br>GPT 跑团式选择冒险：先按提示生成世界和角色，再按 d20 规则推进玩家行动，每步给出选项<br><sub>方法：设定 · 共创</sub><br><sub>更新于 2023-11-08 📦 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 已停止维护（仓库已归档）</sub>

- **[ai-dungeon-master](https://github.com/ITMO-Agentic-AI/ai-dungeon-master)** · ★ 9<br>LangGraph 八 agent 跑 D&D：故事架构师规划节拍，DM 叙述，世界引擎、规则裁判、动作结算、传说构建分工，共享一个 GameState<br><sub>方法：规划 · 设定 · 多智能体 · 模拟</sub><br><sub>更新于 2025-12-17 💤 · 🧩 应用 · 英文</sub><br><sub>💡 Chainlit 界面；支持任意 OpenAI 兼容接口；仓库未声明许可证</sub>

- **[AI-Game-From-Story](https://github.com/top777/AI-Game-From-Story)** · ★ 9<br>把任意小说 txt 抽取成世界书再转成 MUD 式互动游戏：状态层 JSON 记录世界真相，提示词由世界书、状态、滑动窗口和长期记忆组装<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-03 · 🧩 应用 · 中文</sub><br><sub>💡 自带示例游戏《剑起归墟》，可导出单文件 HTML5</sub>

- **[AI-TRPG-Demo](https://github.com/GA10d/AI-TRPG-Demo)** · ★ 9<br>DeepSeek 当跑团主持人：规则插件（COC/VHS 等）定义状态栏、技能判定和专属提示模板，状态管理跟踪玩家数值，附三套剧本和语音播报<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-02-13 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需要 DeepSeek API</sub>

- **[AiChatTrpg](https://github.com/Leehow/AiChatTrpg)** · ★ 9<br>导入规则书 PDF 和模组跑团：预处理→生成→后处理三段流水线，结构化 JSON 场景/NPC/剧情线加压缩叙事双记忆，预掷骰池使检定可审计<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-05-28 · 🧩 应用 · 多语言 · 4 个 skill · Apache-2.0</sub><br><sub>💡 Pre-alpha；需 PostgreSQL；仓库里的 .agents/skills 是开发流程用的，不是创作 skill</sub>

- **[dreamengine](https://github.com/onzag/dreamengine)** · ★ 9<br>LLM 角色扮演模拟引擎：维护物品位置、角色特质/隐藏状态/触发器、羁绊关系和世界规则，角色只知道亲历之事，上下文动态压缩<br><sub>方法：设定 · 人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 WIP，Electron 应用，面向 llama.cpp / vLLM 本地模型；支持条件化 NSFW 内容</sub>

- **[llm-dungeon](https://github.com/TJurijs/llm-dungeon)** · ★ 9<br>本地单人跑团：AI DM 维护持久世界记录和隐藏秘密，d100 由代码掷骰，可自写设定/剧本/角色或用冒险模板，英俄双语<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-07 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 Node.js 免安装依赖；默认 Gemini，可接 OpenRouter/OpenAI/Anthropic/DeepSeek/xAI</sub>

- **[MC-CIV](https://github.com/Pomilon/MC-CIV)** · ★ 9<br>Minecraft 服务器里的 AI 叙事：世界叙事者轮询服务器状态，触发天气、刷怪和剧情广播；LLM 驱动的 NPC 群体带三层记忆自主行动、与玩家对话<br><sub>方法：记忆 · 多智能体 · 模拟</sub><br><sub>更新于 2026-05-25 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 早期 alpha；需自建 Minecraft Java 服务器（RCON）和 Node.js Mineflayer；大部分代码是机器人行动能力，叙事者部分较轻</sub>

- **[thousand-lives](https://github.com/rockbenben/thousand-lives)** · ★ 9<br>AI 文字人生模拟器：10 个剧本各有属性、事件池与结局，属性值落入命名状态作为硬指令注入 AI，选项或自写行动由 AI 裁定，也可一句主题生成新剧本<br><sub>方法：模拟 · 共创</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 纯前端；免 Key 时用手写事件池，AI 模式自填 Key（24 家服务商预设）</sub>

- **[ai-jubensha](https://github.com/Zewang0217/ai-jubensha)** · ★ 8<br>AI 剧本杀：按主题生成完整剧本（角色背景、时间线、作案手法、线索网），DM/玩家/裁判/记录员多 Agent 主持搜证、讨论与投票，RAG 记忆<br><sub>方法：规划 · 记忆 · 多智能体 · 模拟</sub><br><sub>更新于 2026-06-22 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Spring Boot + LangChain4J + React</sub>

- **[loom-engine](https://github.com/Underline-1024/loom-engine)** · ★ 8<br>Rust 终端文字 RPG：玩家用自然语言行动，LLM 通过工具函数实时读写数值、标签特质和背包来推进叙事，建项目时写入世界设定<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-08-10 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 Releases 提供预编译二进制，仓库含源码；支持 OpenAI/Anthropic/Ollama</sub>

- **[ScrollWeaver](https://github.com/siruizou2005/ScrollWeaver)** · ★ 8<br>从小说/设定文档用 RAG 抽取世界观、地点与人物，Orchestrator 按事件链调度场景，Performer 角色代理带记忆自主行动，玩家入场改写剧情<br><sub>方法：设定 · 多智能体 · 模拟 · 共创</sub><br><sub>更新于 2026-08-19 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 2025 Soul AI Agent 大赛三等奖；内置三国、红楼梦等示例世界，另含狼人杀等社交推理玩法</sub>

- **[SillyStage](https://github.com/arkuna23/SillyStage)** · ★ 8<br>Rust 多 agent 互动叙事引擎：规划、架构、导演、演员、旁白、记录者分工，围绕故事图推进角色扮演剧情<br><sub>方法：规划 · 多智能体 · 模拟</sub><br><sub>更新于 2026-03-24 💤 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 README 只有构建说明，agent 分工见 AGENTS.md 和项目文档站</sub>

- **[story-collab-ai](https://github.com/jpinedaa/story-collab-ai)** · ★ 8<br>Storium 式协作写作应用：叙事者用地点、人物、障碍卡布置场景，各角色由 AI agent 或真人认领并打出故事卡推进剧情，可异步多人参与<br><sub>方法：多智能体 · 模拟 · 共创</sub><br><sub>更新于 2024-07-01 💤 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 Flutter + Python；需 NVIDIA NIM API；Release 提供 exe，仓库含源码</sub>

- **[WorldForge](https://github.com/EidzokuxS/WorldForge)** · ★ 8<br>LLM 主持的文字 RPG 沙盒：一句前提生成世界 DNA、势力与关键 NPC；状态变更先按规则结算留凭据，再由叙述者写正文，NPC 分层唤醒<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-08-31 · 🧩 应用 · 英文 · AGPL-3.0</sub>

- **[ai-dungeon-scripts](https://github.com/Lelallas3317024/ai-dungeon-scripts)** · ★ 7<br>AI Dungeon 脚本集：追踪时间推进、角色好感与记忆，隐藏任务分阶段触发加随机世界事件，SAE 模式把跑偏的剧情拉回当前任务阶段<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-04-14 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 粘贴进 AI Dungeon 的 Scripting 使用，叙事由平台模型完成；Auto Card 版会自动更新 Story Cards；隐藏任务模式作者标注仍在开发</sub>

- **[gemini-tales](https://github.com/vero-code/gemini-tales)** · ★ 7<br>儿童互动童话：Gemini Live 叙事者边讲边配水彩插图，孩子完成真实动作挑战才继续；Agent 模式下由研究员、评审、故事匠多 agent 先编排剧本<br><sub>方法：多智能体 · 修订 · 共创</sub><br><sub>更新于 2026-03-16 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 黑客松作品；依赖 Gemini Live、Veo 3.1、Google ADK 和 Cloud Run</sub>

- **[glyphkeeper](https://github.com/pineoncellar/glyphkeeper)** · ★ 7<br>COC7 AI 守密人：LangGraph 拆成意图→确定性规则裁定→叙事→状态固化节点，事件溯源做唯一事实源，LightRAG 加结构化库双脑记忆<br><sub>方法：记忆 · 多智能体 · 模拟</sub><br><sub>更新于 2026-08-11 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 作者已停止开发，自评规则仲裁过严、限制叙事，转做 OpenCOCKeeper；仓库不附规则书原文</sub>

- **[LivingCharacters](https://github.com/LivingNarratives/LivingCharacters)** · ★ 7<br>AI Dungeon 脚本：轮转调度关系卡、随机卡和世界事件，让 NPC 之间自发产生关系、冲突和支线，可选角色内心独白卡<br><sub>方法：人物 · 模拟</sub><br><sub>更新于 2026-07-30 · ⚙️ 框架 · 英文</sub><br><sub>💡 需装进 AI Dungeon 场景脚本；内心独白卡与 Optimized Context 不兼容</sub>

- **[LT](https://github.com/yangrunzhi345-blip/LT)** · ★ 7<br>本地互动叙事平台：从世界观、角色卡、NPC 快照开冒险，运行时状态中心追踪人物关系、地点、势力和时间线，按 token 预算组装上下文<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · 35 个 skill</sub><br><sub>💡 Flutter 全平台；资源生成走规划→蓝图→分段生成→校验；含本地神经 TTS</sub>

- **[ReputeX-Engine](https://github.com/MillennialJesus/ReputeX-Engine)** · ★ 7<br>AI Dungeon 脚本引擎：用正则词典判读玩家意图，维护派系与个人声望、世界时钟和日/月/年事件，把声望摘要和分视角地点设定注入上下文<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2025-11-02 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 叙事由 AI Dungeon 平台模型完成；示例是海拉鲁派系，需自行填派系和事件；仓库无许可证</sub>

- **[SillyTavern-CreativeStudio](https://github.com/rustyorb/SillyTavern-CreativeStudio)** · ★ 7<br>一句话生成整套 ST 角色扮演：前提→角色→角色卡→多个不同开场→能触发的世界书→预设与正则，每步结构化调用后自我批评修正<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-09-26 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 SillyTavern 扩展，需 ST ≥1.19；可选 ComfyUI 生成立绘与表情</sub>

- **[agentic-quest](https://github.com/intelc/agentic-quest)** · ★ 6<br>Claude Code/Codex 里的文字 RPG：从任意小说文本生成世界，谜题由 Python 校验函数判成败，同伴是真子 agent，按玩法偏好生成新区域<br><sub>方法：设定 · 多智能体 · 共创</sub><br><sub>更新于 2026-04-07 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 最后更新 2026-04-07，早于时效线；因谜题用代码校验、同伴派子 agent 的思路少见而保留</sub>

- **[ai-dungeon-master](https://github.com/samvoisin/ai-dungeon-master)** · ★ 6<br>Discord 跑团 GM 机器人：GPT-4 + LlamaIndex 按玩家行动即时推进剧情、扮演 NPC 对话并执行 TTRPG 规则，带存档目录<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-03-08 💤 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 需自备 OpenAI API 与 Discord 机器人令牌</sub>

- **[AIDND](https://github.com/Transcenduality/AIDND)** · ★ 6<br>单文件 Pygame 跑团引擎：LLM 当 DM 叙事，角色卡、物品、属性用结构化 JSON 维护，程序负责 d20 掷骰和数值，带存档与历史追踪<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-03-08 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 作者标注 WIP，只有一个 Python 文件；兼容 OpenAI 接口及 Ollama / LM Studio</sub>

- **[Aphelion](https://github.com/penpro/Aphelion)** · ★ 6<br>离线桌面 AI 的角色扮演模块：每轮回复后更新场景状态（服装、道具、地点）和 10 项角色数值并注入下一轮，限制用户替角色决定行为，配滚动摘要记忆<br><sub>方法：人物 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 通用本地 AI 助手（另有代码、文档、专家问答），角色扮演/写故事/对话树只是其中模块；基于 llama.cpp；角色数值含亲密与性唤起维度，涉成人内容</sub>

- **[cognee-dnd-game](https://github.com/harsh10tech/cognee-dnd-game)** · ★ 6<br>局域网多人 D&D：AI 地下城主讲述剧情，Cognee 把每次决策、NPC 和战役事件写进知识图谱与 Markdown 设定库，叙事时检索调用<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-08-14 · 🧩 应用 · 英文</sub><br><sub>💡 多人模式用 Groq API，单人模式用 Claude CLI；本质是 Cognee 图记忆的演示项目</sub>

- **[dnd_ai_dm](https://github.com/msadeqsirjani/dnd_ai_dm)** · ★ 6<br>控制台 D&D 主持：GPT 生成任务剧情并随玩家选择调整，NPC 管理器记录个性、关系、位置和所知信息，世界状态追踪地点、任务和时间天气<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2024-11-24 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 需 OpenAI API；按 D&D 5e 规则掷骰战斗</sub>

- **[faramita-worlds](https://github.com/Nobeta-Work/faramita-worlds)** · ★ 6<br>Electron 跑团世界引擎：运行时世界书（激活规则、注入位置、预算），多层记忆组装→结构化叙事输出→后置审查，世界状态按字段 delta 更新并检测冲突<br><sub>方法：设定 · 记忆 · 修订</sub><br><sub>更新于 2026-03-13 💤 · 🧩 应用 · 中文</sub><br><sub>💡 README 写 MIT 但仓库无许可证文件；可从 txt/md 导入设定</sub>

- **[llm-gamebook](https://github.com/buzz/llm-gamebook)** · ★ 6<br>图结构游戏书框架：用 YAML 定义故事弧、地点、角色节点与条件边，LLM 通过工具调用推进状态转移，沿预设路径生成叙事<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-08-30 · ⚙️ 框架 · 英文 · 11 个 skill · AGPL-3.0</sub><br><sub>💡 FastAPI + React；仓库里的 SKILL.md 是开发用 openspec 技能，不是写作 skill</sub>

- **[llmadventure](https://github.com/SoftwareApkDev/llmadventure)** · ★ 6<br>Gemini CLI 文字冒险：程序化生成世界、地点和 NPC 背景，任务随玩家选择调整，叠加战斗、成长和背包系统，插件可扩展机制<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2025-08-03 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需 Google AI API；可 pip 安装，另有可选 Web 界面</sub>

- **[Moodweaver](https://github.com/MLBott/Moodweaver)** · ★ 6<br>角色扮演叙事应用：性格引擎追踪角色动态特质与情绪事件，故事控制器按情节结构给角色布置目标，配会留下改变的可探索地图和摘要式长记忆<br><sub>方法：规划 · 人物 · 记忆 · 模拟</sub><br><sub>更新于 2025-09-18 💤 · 🧩 应用 · 英文</sub><br><sub>💡 支持 OpenAI、Anthropic、Ollama；主模型之外另用辅助模型做情绪分析</sub>

- **[Pliego-Lab](https://github.com/Gateton/Pliego-Lab)** · ★ 6<br>本地角色扮演工作台：世界书，NPC 追踪器给反复出场的配角建档，Memoria Viva 维护叙事连续与正典，Recast 多轮改写正文，自动配图<br><sub>方法：人物 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-09-20 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 早期版本；可导入 SillyTavern 角色卡；可选本地 ComfyUI 生图</sub>

- **[reveriesoil](https://github.com/reveriesoil/reveriesoil)** · ★ 6<br>一句提示生成可玩视觉小说：故事大纲→剧情校验→美术风格→完整台词→立绘/背景/CG→打包，交互深度五档可调，从观影式到高分支<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-05-14 · 🧩 应用 · 中文</sub><br><sub>💡 BYOK（DeepSeek/Kimi 等），图像与 TTS 可选；Windows/Android 安装包在 Releases</sub>

- **[WhisperQuest](https://github.com/maxcurrent420/WhisperQuest)** · ★ 6<br>语音选择冒险：Whisper 识别玩家口述的选择，LLM 按惊悚等预设或自定义题材逐回合讲故事，配场景图和多种 TTS、声音克隆朗读<br><sub>方法：共创</sub><br><sub>更新于 2025-05-07 💤 · 🧩 应用 · 英文</sub><br><sub>💡 支持本地 LLM 和 Groq；许可证是改版 CC BY-NC-SA，营收超 10 万美元需购买授权</sub>

- **[AaaliceTavern](https://github.com/WalkingMeatAxolotl/AaaliceTavern)** · ★ 5<br>规则引擎先结算行动条件、结果分支和 NPC 自主决策，再把结果、角色状态和世界书条目拼进提示词让 LLM 写旁白；内容按 addon 包组织<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-03-28 💤 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 自带可视化编辑器和创建实体的 AI 助手；AGPL-3.0</sub>

- **[ai-dungeon-game](https://github.com/prgrmcode/ai-dungeon-game)** · ★ 5<br>Gradio 文字地牢冒险：Llama 3.2 按玩家进度程序化生成多链任务并叙述回应，代码跟踪背包与世界状态，LLaMA Guard 逐条审核输出<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2025-12-15 💤 · 🧩 应用 · 英文</sub><br><sub>💡 本地跑 Llama-3.2-3B（8-bit 量化），需 Hugging Face Token</sub>

- **[AI-Dungeon-Master](https://github.com/ell-hosse/AI-Dungeon-Master)** · ★ 5<br>LLM 地下城主网页游戏：先生成冒险前提和主线/支线任务，按玩家行动更新背包、属性和任务状态，任务全部完成即通关<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2024-10-20 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需要 OpenRouter API</sub>

- **[ai-gamestudio](https://github.com/ackness/ai-gamestudio)** · ★ 5<br>双模型 RPG 引擎：Markdown 写世界观，主模型负责叙事，插件 agent 按统一规范管状态、事件、战斗、关系和记忆压缩，状态全部落库<br><sub>方法：设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-03-24 📦 · 🧩 应用 · 多语言</sub><br><sub>💡 已停止维护（仓库已归档）；LiteLLM 兼容模型；带剧情配图插件</sub>

- **[Corvus-Story-Core](https://github.com/JustLateNightAI/Corvus-Story-Core)** · ★ 5<br>本地文字 RPG 主持引擎：每回合叙述后由隐藏 GM 抽取数值/物品/NPC 态度增量写盘，NPC 卡自带记忆，旧对话自动压成章节摘要<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-06-18 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 任意 OpenAI 兼容端点；可选 ComfyUI 生图、Chatterbox TTS；设置里有全局越狱提示词选项</sub>

- **[Evermind](https://github.com/Phobetore/Evermind)** · ★ 5<br>自托管 AI 角色扮演：边玩边把承诺、旧伤、信任变化等剧情事实写进可编辑、可置顶的长期记忆并每轮注入，角色不讨好用户，附六个原创世界<br><sub>方法：人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 自带模型（本地或 OpenRouter 等）；无内容过滤，可生成成人内容；Docker 部署</sub>

- **[Fable-Friend](https://github.com/Shreemahor/Fable-Friend)** · ★ 5<br>LangGraph 互动冒险：状态记录类型、角色、张力和摘要，讲述者写剧情→配图→玩家行动→裁判改进者补细节并约束玩家，达成里程碑进入新章<br><sub>方法：记忆 · 多智能体 · 修订 · 共创</sub><br><sub>更新于 2026-03-12 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需 Groq API；配图走 Hugging Face FLUX 或 Pollinations</sub>

- **[gestaloka](https://github.com/KingYoSun/gestaloka)** · ★ 5<br>多人共享世界文字 MMO：世界包定义设定，玩家和 NPC 行动进入同一世界事件流，投影成图谱并向量检索记忆，AI GM 每回合给出局面和可选行动<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-06-25 · 🧩 应用 · 日文 · MIT</sub><br><sub>💡 README 英文，GM 规则和设计文档为日文；部署栈较重（Postgres、NebulaGraph、Keycloak、Langfuse）</sub>

- **[gpt-text-adventure](https://github.com/somacdivad/gpt-text-adventure)** · ★ 5<br>主题→标题与背景→6 个带目标和地点的剧情点，之后每回合把剧情点、玩家血量/体力/进度和上一选择以 JSON 交给模型生成叙述和选项<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2023-04-11 💤 · 🧩 应用 · 英文</sub><br><sub>💡 作者自述多数故事走不完</sub>

- **[InkRealm](https://github.com/xinxin2021110/InkRealm)** · ★ 5<br>网文 IP 角色共创：检索角色语录做沉浸对谈，或用 6 步向导建自定义角色后生成大纲和章节，章末给选项影响走向，仿 MetaGPT 的角色/动作/记忆抽象<br><sub>方法：人物 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-05-29 · 🧩 应用 · 中文</sub><br><sub>💡 附带《武动乾坤》《斗破苍穹》等网文角色语料 JSONL，可上传其他作品；课程项目性质，README 含作者本机路径；仓库无许可证</sub>

- **[koyoi](https://github.com/gucheng910/koyoi)** · ★ 5<br>上传 txt 小说后逐章抽取人物、时间线与文风建知识库，玩家魂穿入书；角色有情绪惯性和记忆闪回，NPC 自主互动，叙事导演每 5 轮调节奏<br><sub>方法：记忆 · 模拟 · 风格 · 共创</sub><br><sub>更新于 2026-09-19 · 🧩 应用 · 中文</sub><br><sub>💡 React Native 安卓 App（Releases 有 APK，源码在「源码/」目录）；主要适配 DeepSeek；同人穿越玩法</sub>

- **[LingMo-Engine](https://github.com/liyaonan/LingMo-Engine)** · ★ 5<br>文字游戏引擎：强模型负责叙事、快模型做结构化任务，9 个插件（战斗/背包/地图/修炼等）供 LLM 工具调用，三层记忆，YAML 定义世界<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-06-06 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 自带修仙示例世界「无极」和暗黑奇幻世界；接任意 OpenAI 兼容 API</sub>

- **[OpenArcana](https://github.com/krys64/OpenArcana)** · ★ 5<br>AI 地下城主网页/桌面应用：模型按结构化 JSON 返回叙事、场景、NPC、威胁与行动选项，自动更新背包/HP/经验，可注入本地世界设定文件（PDF/txt）<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-08-05 · 🧩 应用 · 多语言</sub><br><sub>💡 法语为主、附英文说明；默认 DeepSeek；无开源许可证</sub>

- **[realtime_ai_dungeon_master](https://github.com/ntanwir10/realtime_ai_dungeon_master)** · ★ 5<br>多人实时 AI 地下城主：玩家行动写入 Redis Streams 作叙事上下文，向量化的语义设定库检索 lore，叙事经 Pub/Sub 同步给所有玩家<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2025-08-09 💤 · 🧩 应用 · 英文</sub><br><sub>💡 Redis AI 挑战赛作品；需 OpenAI Key 和 Redis；仓库未声明许可证</sub>

- **[RePoG](https://github.com/tritonsan/RePoG)** · ★ 5<br>在 agent 工作区里跑单人跑团 GM 或 AI 伴侣：Markdown 记录战役连续性，限定角色已知信息，本地脚本管骰子与资源回滚，另产信件报纸等世界文书<br><sub>方法：设定 · 记忆 · 模拟</sub><br><sub>更新于 2026-10-07 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 不内置模型调用，直接用所在 agent 的模型；含 AI 伴侣模式</sub>

- **[StoryLoom](https://github.com/HHHHCHYK/StoryLoom)** · ★ 5<br>先填世界观、主角、势力、物品、场景，再逐步输入情节指令让 AI 续写；按行动/对白/思考模式生成，旧内容自动压缩为摘要，正文与摘要/建议用不同模型<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-05-08 · 🧩 应用 · 中文</sub><br><sub>💡 Windows 桌面（.NET 10 + Blazor Hybrid）；默认 DeepSeek；仓库混入编译产物 exe/dll</sub>

- **[Storyloom](https://github.com/SiriLee/Storyloom)** · ★ 5<br>实时视觉小说引擎：LLM 流式输出 XML 逐行解析，模型只提议状态写入、引擎类型校验后才落地并回馈拒绝；场景内选项与大纲级路线分叉两层分支，自动配立绘和背景<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-08-21 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 需 OpenAI 兼容 API；有 PyPI 包与独立二进制，立绘/背景素材包首次启动另行下载</sub>

- **[trinity](https://github.com/jorjiiie/trinity)** · ★ 5<br>HackMIT VR 原型：仿生成式智能体做小镇真人秀，角色按预设人格用 GPT 对话并摘要记忆，情感分析加概率分布决定反应，观众捐赠可推动恋爱、冲突剧情<br><sub>方法：人物 · 模拟</sub><br><sub>更新于 2023-09-17 💤 · 🧩 应用 · 英文</sub><br><sub>💡 2023 年黑客松原型，README 是作品介绍、没有安装说明；Unity VR 前端 + LangChain，语音用 ElevenLabs</sub>

- **[twine-mcp](https://github.com/Unveil-gg/twine-mcp)** · ★ 5<br>让编码 Agent 直接写 Twine 互动小说的 MCP：增改 .twee 段落，提供分支图、死胡同/孤立段落检测、结局汇总和叙事连续性检查<br><sub>方法：记忆 · 修订</sub><br><sub>更新于 2026-10-08 · ⚙️ 框架 · 英文 · MIT</sub>

- **[yinghui](https://github.com/Mrpora/yinghui)** · ★ 5<br>多 agent 世界演化沙盒：导演 agent 分回合调度角色自主行动与冲突，关键节点给分支供用户选择，演化记录再由写作+审查 agent 转成章节小说<br><sub>方法：记忆 · 多智能体 · 模拟 · 共创</sub><br><sub>更新于 2026-07-21 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 作者自称 Demo 项目；AGPL-3.0 + 商业许可双授权；另含带长期记忆的角色对话线</sub>

- **[DungeonGPT](https://github.com/EdwardAThomson/DungeonGPT)** · ★ 4<br>先建角色（属性/职业/种族）并组队，设定难度与叙事风格，再由 GPT-4o 扮演地下城主按会话历史推进冒险，可存读档<br><sub>方法：人物 · 共创</sub><br><sub>更新于 2026-02-18 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需 OpenAI API Key；无许可证</sub>

- **[OpenCOCKeeper](https://github.com/pineoncellar/OpenCOCKeeper)** · ★ 1<br>CoC 7 版 AI 守秘人：BM25 检索用户导入的模组原文和规则库，mem0/Qdrant 语义记忆，d100 检定与理智规则由纯函数经工具调用执行<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-09-26 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 开发中；不含规则书和模组，需自备；架构参考 Concordia 与 ChatRPG v2</sub>

- **[VySol](https://github.com/Vyce101/VySol)** · ★ 1<br>把按顺序排列的 TXT/EPUB 原著分块建向量库，在该世界的 Chronicle 会话里检索原著上下文进行角色扮演，目标是 GraphRAG 与实体消解<br><sub>方法：记忆</sub><br><sub>更新于 2026-09-29 · 🧩 应用 · 英文</sub><br><sub>💡 开发中：main 是新版基础，知识图谱/GraphRAG 尚未完成，早期原型在其他分支；Windows 启动</sub>

#### 研究代码（3）

- 🌟 **[AI4VisualNovel](https://github.com/ttsmallHot/AI4VisualNovel)** · ★ 102<br>视觉小说多 agent 框架：制片、编剧、演员、美术分工，先出大纲再生成拓扑排序的 DAG 分支剧情图，演员 agent 按人设演对白并审立绘，导出可玩游戏<br><sub>方法：规划 · 人物 · 多智能体 · 模拟</sub><br><sub>更新于 2026-10-14 · 🎓 研究 · 英文 · Apache-2.0</sub><br><sub>💡 论文尚未发布；需要文本和图像生成 API；可导出 Ren'Py 工程，支持自定义原创角色（OC）</sub>

- **[multiverse](https://github.com/motform/multiverse)** · ★ 15<br>生成文学原型：读者与 GPT-3 对话式续写并分叉，在交互式空间地图上浏览、回溯已探索的文本分支，是硕士论文和 IoT'20 论文的配套代码<br><sub>方法：共创</sub><br><sub>更新于 2024-10-06 💤 · 🎓 研究 · 英文 · GPL-3.0</sub><br><sub>💡 需 OpenAI key；旧版本地模型 client-server 版本见 README 指定的 commit</sub>

- **[payador](https://github.com/pln-fing-udelar/payador)** · ★ 9<br>ICCC 论文代码：把 LLM 落到结构化世界（物品、角色、地点）上，先预测玩家输入引起的世界状态变换，再据新状态生成叙事<br><sub>方法：记忆 · 模拟 · 共创</sub><br><sub>更新于 2026-08-19 · 🎓 研究 · 多语言 · GPL-3.0</sub><br><sub>💡 默认 Gemini API；预置英语/西语世界</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# novel-to-game
npx skills add zenstory-ai/novel-to-game
# dsh-nexttavern
npx skills add a86582751/dsh-nexttavern
# interactive-fiction-skill
npx skills add Treasure-hub-agent/interactive-fiction-skill
# velvet-ascent-skill
npx skills add ruijayfeng/velvet-ascent-skill
# character-card-skills
npx skills add foreverse-app/character-card-skills
# fanfic-roleplay-design
npx skills add unknowlei/fanfic-roleplay-design
# delvewright
npx skills add stellarfeline/delvewright
# theatre
npx skills add geekjourneyx/theatre
# Cyber-Eros.skill
npx skills add mlkgrnt/Cyber-Eros.skill
# interactive-novel
npx skills add din1919/interactive-novel
# speckit-preset-game-narrative-writing
npx skills add adaumann/speckit-preset-game-narrative-writing
# DeekSeek-V4-text-adventure-prompt-builder
npx skills add EdenBush/DeekSeek-V4-text-adventure-prompt-builder
# novel-rpg
npx skills add kiki123124/novel-rpg
```

</details>

<a id="group-imitation"></a>
### 仿写 · 同人 · 风格迁移

学一部作品或一位作者的写法再创作：拆书仿写、文风蒸馏、同人、续写。

#### skill · 提示词（11）

- 🌟 **[longzu.skillls](https://github.com/zuoyou12/longzu.skillls)** · ★ 11<br>江南、烽火戏诸侯文风蒸馏 skill：全文统计 1465 万字语料加等距精读，得出共享叙事骨架和可替换语言皮肤，支持风格杂交，附审计脚本和盲测<br><sub>方法：修订 · 风格</sub><br><sub>更新于 2026-07-28 · 中文 · 3 个 skill</sub><br><sub>💡 同人/仿写性质，仓库只有风格笔记、不含原文；盲测方法改造自 alchaincyf/nuwa-skill</sub>

- **[xin-skills](https://github.com/oscar-wang-xin/xin-skills)** · ★ 28<br>122 个文风锁定 skill：从番茄热门书和金庸、古龙等指定小说萃取十维风格规范，只仿文笔不抄剧情<br><sub>方法：风格</sub><br><sub>更新于 2026-09-25 · 中文 · 122 个 skill</sub><br><sub>💡 每个技能附对应原作的段落摘录作风格样本</sub>

- **[Skills-for-Long-Online-Novel-Authors](https://github.com/shuipingbai6/Skills-for-Long-Online-Novel-Authors)** · ★ 22<br>网文作者蒸馏 skill：导入作者小说、读者评论与社交内容，提取写作风格和作者人格，生成可调用的作者 skill，按其风格续写或开书<br><sub>方法：风格</sub><br><sub>更新于 2026-06-10 · 中文 · 2 个 skill · GPL-3.0</sub><br><sub>💡 没有 README.md，说明在 README_ZH.md；CLI 目录附带预编译 exe，建议用 Python 源码；需自备作者原文</sub>

- **[wenfeng-skill](https://github.com/XTmingyue/wenfeng-skill)** · ★ 21<br>给一部小说文本，提炼叙事模型、语言指纹、母题、人物与情节技法，生成可直接调用的仿写 SKILL.md<br><sub>方法：理论 · 人物 · 风格</sub><br><sub>更新于 2026-05-26 · 中文 · MIT</sub><br><sub>💡 仓库不含原作文本，需自备有权处理的小说文本</sub>

- **[stephen-chow-skill](https://github.com/chnjames/stephen-chow-skill)** · ★ 14<br>无厘头喜剧 skill：先定人物欲望、喜剧规则与地位关系，从 8 类喜剧机制选 2-3 个搭升级链再写台词，最后做原创性检查与可拍性评分迭代<br><sub>方法：理论 · 修订 · 风格</sub><br><sub>更新于 2026-06-15 · 中文 · MIT</sub><br><sub>💡 非周星驰官方；只抽象喜剧机制，不收录台词，内置近似文本检查</sub>

- **[AI-DaLiu](https://github.com/Wanludrame/AI-DaLiu)** · ★ 7<br>精读刘慈欣 26 部作品提炼构思与叙事方法来写科幻，三体同人遵守原作设定，并仿 Generative Agents 每天生成「大刘日记」积累生活质感<br><sub>方法：人物 · 模拟 · 风格</sub><br><sub>更新于 2026-09-09 · 中文 · 5 个 skill</sub><br><sub>💡 风格和同人技能绑定刘慈欣/三体；仓库含大量生成的作品与日记文本；另有短片制作技能</sub>

- **[novel-style-skills](https://github.com/xianzl/novel-style-skills)** · ★ 7<br>从小说样本蒸馏作者文风为 style.json，按声音/句法/对白分层融合多位作者，写前检查欲望-阻力-选择-代价故事引擎，写后评测风格漂移与 AI 味<br><sub>方法：修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-05-08 · 多语言 · 5 个 skill · MIT</sub><br><sub>💡 受 YIKUAIBANZI/forge-skill（人物蒸馏）启发，非其 fork；样本需用户自备</sub>

- **[works-dna-extractor](https://github.com/Shiaoming123/works-dna-extractor)** · ★ 7<br>把小说拆成 16 层「作品 DNA」（叙事引擎、POV、对话系统、情感算法、信息控制等），再按五步续写协议仿写/改写，用 8 维量表评估吻合度<br><sub>方法：修订 · 风格</sub><br><sub>更新于 2026-05-24 · 中文 · MIT</sub><br><sub>💡 也提供 Hermes Agent 入口</sub>

- **[author-style-extractor](https://github.com/alexsowake/author-style-extractor)** · ★ 6<br>仿写前置 skill：补查作者生平与文学渊源，分批通读原文累积提炼，按 references/作者名/ 写出作者信息、风格指南和作品参考供仿写调用<br><sub>方法：风格</sub><br><sub>更新于 2026-05-04 · 中文</sub><br><sub>💡 仓库只有一个 SKILL.md，无 README 与 License；配套的 author-imitation skill 不在本仓库</sub>

- **[xin-novel-style-builder](https://github.com/oscar-wang-xin/xin-novel-style-builder)** · ★ 6<br>文风 skill 生成器：清洗小说前 20 章正文，从视角、句式、对话、节奏、钩子等十个维度萃取文风，生成可安装的文风锁定 SKILL.md 供 AI 仿写<br><sub>方法：风格</sub><br><sub>更新于 2026-08-22 · 中文 · MIT</sub><br><sub>💡 只仿文笔不抄剧情；仓库附自身 skill 的 zip 打包，与目录内容一致</sub>

- **[character-card-fiction-workflow-skill](https://github.com/shigehaomingzi1/character-card-fiction-workflow-skill)** · ★ 5<br>从草稿、聊天记录或小说提炼带原文证据的角色设定；续写前先定六项风格参数、规划事件与优先级，再出正文和一致性清单，也能导出 SillyTavern 角色卡<br><sub>方法：规划 · 人物 · 风格</sub><br><sub>更新于 2026-06-18 · 中文 · GPL-3.0</sub>

#### 框架 · 应用（4）

- 🌟 **[harnessNovel](https://github.com/XTmingyue/harnessNovel)** · ★ 187<br>先对参考小说分三阶段拆书（结构、世界观、情节单元、文风），把情节抽象成叙事模式，再按核心玩法→舞台路线→章纲→正文仿写，章节级去 AI 味<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-23 · ⚙️ 框架 · 中文 · GPL-3.0</sub><br><sub>💡 pip 安装后有 CLI 和本地 Web 工作台；需 OpenAI 兼容 API，三组模型可分开配；系统文/领主文可开机制层管面板与资源；去 AI 味后处理基于 op7418/Humanizer-zh</sub>

- **[novel-writer-style-cn](https://github.com/lsg1103275794/novel-writer-style-cn)** · ★ 50<br>在七步规格驱动写作法上加风格学习：用分词、句长、情感等 NLP 指标量化分析样本作者，生成风格配置供 AI 仿写，并校验风格一致性<br><sub>方法：规划 · 记忆 · 风格</sub><br><sub>更新于 2026-08-20 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 基于 wordflowlab/novel-writer；另有开发中的 WebUI 版 lsg1103275794/novel-writer-style-cn-webui</sub>

- **[make-ur-Agent-writer](https://github.com/ARMANDSnow/make-ur-Agent-writer)** · ★ 20<br>导入原作切章，抽取人物、事件、关系并人工确认后选续写起点，经方向辩论、章节规划、5+1 审稿和文风漂移检测逐章续写，也支持原创<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-09-16 · ⚙️ 框架 · 中文 · 2 个 skill</sub><br><sub>💡 原作语料不入库；短剧实现单独放在 codex/short-drama 分支</sub>

- **[Novel-RAG](https://github.com/a-big-fish/Novel-RAG)** · ★ 5<br>为 AI 写作建「写作范本层」：小说切成 Scene，筛除垃圾、评估参考价值并结构化标注，四路向量召回+重排，按「试探感对白」等创作需求检索范本场景<br><sub>方法：风格</sub><br><sub>更新于 2026-10-11 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 本身不生成正文，是 novel-creator 写作系统的拆书/范本检索服务；需 PostgreSQL + Qdrant + Ollama</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# longzu.skillls
npx skills add zuoyou12/longzu.skillls
# xin-skills
npx skills add oscar-wang-xin/xin-skills
# Skills-for-Long-Online-Novel-Authors
npx skills add shuipingbai6/Skills-for-Long-Online-Novel-Authors
# wenfeng-skill
npx skills add XTmingyue/wenfeng-skill
# stephen-chow-skill
npx skills add chnjames/stephen-chow-skill
# AI-DaLiu
npx skills add Wanludrame/AI-DaLiu
# novel-style-skills
npx skills add xianzl/novel-style-skills
# works-dna-extractor
npx skills add Shiaoming123/works-dna-extractor
# author-style-extractor
npx skills add alexsowake/author-style-extractor
# xin-novel-style-builder
npx skills add oscar-wang-xin/xin-novel-style-builder
# character-card-fiction-workflow-skill
npx skills add shigehaomingzi1/character-card-fiction-workflow-skill
```

</details>

<a id="group-general"></a>
### 通用叙事方法

不限体裁的故事方法和原则：结构理论、人物、对白、视角，以及专门针对小说的去 AI 味。

#### skill · 提示词（24）

- 🌟 **[sepia](https://github.com/Nanako0129/sepia)** · ★ 3.2k<br>按 StoryScope 论文测出的 AI 小说结构特征分三遍修：先改叙事架构（不点题、松因果链、后置揭示），再改段落流和表层措辞<br><sub>方法：理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-15 · 英文 · 6 个 skill · MIT</sub>

- 🌟 **[creative-writing-skills](https://github.com/haowjy/creative-writing-skills)** · ★ 512<br>muse 主代理调度头脑风暴、角色模拟、大纲、写手、批评、编辑和读者模拟等子代理，从已有文字提炼文风文件，写后批评修订并同步知识库<br><sub>方法：记忆 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-10-15 · 英文 · 24 个 skill · Apache-2.0</sub>

- **[agent-skills](https://github.com/jwynia/agent-skills)** · ★ 172<br>叙事技能大全：故事教练、合写、大纲、人物弧光、对白、结局、反套路、闪小说，大量世界观构建体系<br><sub>方法：规划 · 理论 · 设定 · 人物</sub><br><sub>更新于 2026-02-24 💤 · 英文 · 119 个 skill</sub><br><sub>💡 也含营销等非虚构 skill，按需挑选安装</sub>

- **[novel-writing](https://github.com/wgwtest/novel-writing)** · ★ 49<br>小说写作基本功 skill：场景/章/卷的因果规划、视角与知情边界、有后果的对话、保留作者声音的修订与审稿<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-09-26 · 英文 · MIT</sub><br><sub>💡 skill 正文为英文，示例有中英两版</sub>

- **[chinese-erotic-fiction-writing](https://github.com/xWebt/chinese-erotic-fiction-writing)** · ★ 45<br>中文成人向（H）小说写作 skill：动笔前勘察偏好，按写作规范写作、扩写、重写，可学习本地书库文风，会话记忆逐步收敛口味<br><sub>方法：理论 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-08-04 · 中文</sub><br><sub>💡 本地 CLI 需 Python ≥3.10（pip install -e .），可把本地 txt 书库建成 SQLite 索引，统计技法密度；用户偏好存在 sessions/，不进 git</sub>

- **[writers-room-story-engine](https://github.com/jackterror/writers-room-story-engine)** · ★ 42<br>故事开发 skill：按前提→故事核→主角→Story Spine→因果节拍→世界压力→场景→修订推进，融合皮克斯 22 条、英雄之旅与「所以/但是」因果<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-07-07 · 英文 · MIT</sub>

- **[storywriting.skill](https://github.com/changlizhi569/storywriting.skill)** · ★ 25<br>把《查理编剧课》整理成 skill：用八要素检查人物与冲突，按类型片十类定型、十序列/四幕式排节拍，再设计场景起承转合、对白潜台词和悬念反转<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2026-08-02 · 中文</sub><br><sub>💡 基于查理编剧课笔记；适用小说/剧本/电视剧；SKILL.md 引用的 references/ 路径与实际文件位置（根目录）不符</sub>

- **[novel-humanize](https://github.com/qi531416/novel-humanize)** · ★ 20<br>中文小说去 AI 味 skill：对话改「」、破折号清零、调整标点节奏、打散骨架逐句细改，保剧情不 OOC 注入人味，配 L1–L4 分层自检<br><sub>方法：去 AI 味</sub><br><sub>更新于 2026-08-06 · 中文</sub><br><sub>💡 主打过朱雀检测；整合 laoguo2025/huoren-write 与 KKKKhazix/human-writing 的规则（后两者细则需去原仓库查看）</sub>

- **[mckee-story](https://github.com/song776/mckee-story)** · ★ 19<br>把麦基《故事》做成 Claude Code 知识库 skill：核心框架速览、术语表、可复用故事模式和分章原文，按话题或章节加载供写作时调用<br><sub>方法：理论</sub><br><sub>更新于 2026-08-11 · 中文</sub><br><sub>💡 内容是原书的提炼与摘录；README 带作者自媒体账号推广</sub>

- **[BMad-Expansion-Pack-Creative-Writing](https://github.com/DrBalls/BMad-Expansion-Pack-Creative-Writing)** · ★ 16<br>BMad-Method 创意写作扩展包：情节架构、人物心理、世界构建、编辑、试读等 10 个 agent，配小说/剧本/短篇/系列 8 套流程和 27 份清单<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2025-08-09 💤 · 英文</sub><br><sub>💡 需先安装 BMad-Method；也含封面设计、KDP 出版等周边 agent 与清单</sub>

- **[ai-story-forge](https://github.com/nwiizo/ai-story-forge)** · ★ 11<br>日文小说模板集：人物按不变核心/准稳定/可变三层设定，故事分骨架→关键场景→场景细化三阶段构建，五轴质检，附 Claude Code 斜杠命令<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2025-06-29 💤 · 📝 提示词 · 日文 · MIT</sub>

- **[fiction-humanizer-zh](https://github.com/deedeekong07-alt/fiction-humanizer-zh)** · ★ 11<br>中文小说去 AI 味：修复梗概感、情绪标签、对白汇报腔、冲突无代价，按铺垫-过程-余波重写，强化前 300 字和章末钩子<br><sub>方法：理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-01 · 中文 · MIT</sub>

- **[gpt3-cyoa](https://github.com/scottleibrand/gpt3-cyoa)** · ★ 10<br>2020 年 GPT-3 方案：把文本逐级摘要成场景→章节→全书的层级大纲作外部记忆，再按摘要重新展开，设想用来生成分支冒险，附《汤姆·索亚》摘要/展开实验<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2020-08-15 💤 · 📝 提示词 · 英文 · Apache-2.0</sub><br><sub>💡 只有构想文档和提示词实验输出，分支冒险生成器本身没有实现；API 脚本取自 minimaxir/gpt-3-experiments</sub>

- **[Johnsons-Narrative-Spittoon-Inversion](https://github.com/MushroomFleet/Johnsons-Narrative-Spittoon-Inversion)** · ★ 9<br>提示词框架：先填世界、人物、说话风格模板，从结局页倒推写到开头，用隐性因果替代显式转折，再用评分/审读/编辑/弱点四种导师模式修订<br><sub>方法：规划 · 人物 · 修订 · 风格</sub><br><sub>更新于 2026-04-07 💤 · 📝 提示词 · 英文</sub><br><sub>💡 需 VSCode + Cline；附 10/20/30/40 页故事模板和 CYOA 版；2026-04-07 后无更新，倒序写作思路少见，按例外收录；仓库无许可证</sub>

- **[chinese-webnovel-editor](https://github.com/fanjack510-ctrl/chinese-webnovel-editor)** · ★ 8<br>网文去 AI 味精修 skill：先冻结剧情事实、人物证据与世界规则，再处理报告腔、剧本式对话、段落碎裂和章尾不兑现，分四种审改模式<br><sub>方法：修订 · 去 AI 味</sub><br><sub>更新于 2026-07-15 · 中文 · Apache-2.0</sub><br><sub>💡 beta；README 中作者名和仓库地址仍是占位符</sub>

- **[vibe-writing](https://github.com/pakholeung37/vibe-writing)** · ★ 8<br>wiki 式 AI 协作写小说：人物、地点、概念各一页用 [[双链]] 互连，先写大纲和时间线，红链记待补设定，CLAUDE.md 要求 AI 先查条目保一致<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-01-17 💤 · 📝 提示词 · 英文</sub><br><sub>💡 仓库本身是一部示例推理小说项目，使用时需替换成自己的项目；未声明许可证</sub>

- **[worldbuilding-skill](https://github.com/tahini2007/worldbuilding-skill)** · ★ 7<br>十三步世界观设计 Skill：核心偏离不超过 3 条，每条推七层后果链，再做兼容性、神秘预算、语气与叙事接口审计，另有诊断与轻量模式<br><sub>方法：理论 · 设定 · 修订</sub><br><sub>更新于 2026-08-12 · 中文 · MIT</sub>

- **[advanced-writer](https://github.com/angrysky56/advanced-writer)** · ★ 6<br>MCP 服务加 Skill：先选结构范式，按情绪理论和荣格原型建人物，场景用「神经化学」节奏曲线和病理评分诊断后批量修订，设定存向量库与图库<br><sub>方法：理论 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-17 · 英文 · GPL-3.0</sub><br><sub>💡 需要 ChromaDB 和 Neo4j，模型走 OpenRouter 或 Ollama；另带 Next.js 写作工作台</sub>

- **[fictional-erotica](https://github.com/rs-skills-lab/fictional-erotica)** · ★ 6<br>中英双语成人情色场景写作与修订：可调明确度、语域、对白密度和场景重心，保持人物声口和身体动作连续，支持原创与同人<br><sub>方法：理论 · 人物 · 修订</sub><br><sub>更新于 2026-08-27 · 多语言 · MIT</sub><br><sub>💡 仅限 18+；skill 在 fictional-erotica/ 子目录，tests/ 附测试提示词和评分表</sub>

- **[huoren-write](https://github.com/laoguo2025/huoren-write)** · ★ 6<br>网文与短剧文本的去 AI 味打磨：清理模板腔、假精确、万能安抚腔和强行升华，保留剧情事实与人物声口，附检查脚本<br><sub>方法：人物 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-25 · 中文</sub><br><sub>💡 同时覆盖短剧剧本</sub>

- **[AutoWriter](https://github.com/sinfiny/AutoWriter)** · ★ 5<br>34 个英文写作 skill：Sanderson 方法论套件、网连载谋略与悬念公平性、潜台词、叙述密度、因果世界观，外加自主写作循环<br><sub>方法：规划 · 理论 · 设定 · 人物</sub><br><sub>更新于 2026-04-30 · 英文 · 34 个 skill</sub><br><sub>💡 主 README 只介绍未完成的 Elixir 循环，skill 说明见 skills/README.md；另含若干非虚构和营销类 skill</sub>

- **[Creative-writing-skill](https://github.com/xbraindance/Creative-writing-skill)** · ★ 5<br>用 Verbalized Sampling 一次给出多版点子、开头、大纲和人物，草稿自动归档进项目 wiki，带卡文诊断和批评命令<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-04-28 · 英文 · MIT</sub><br><sub>💡 通用创意写作（含诗歌），非长篇专用；仓库附 12MB 论文 PDF</sub>

- **[reliquery](https://github.com/the-essential/reliquery)** · ★ 5<br>Claude 插件：把手稿/跑团日志拆成按角色、地点、势力存放的 relic 文件，建本地语义索引和时间知识图谱，共写时按问题检索所需设定<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2026-05-21 · 英文 · 6 个 skill · MIT</sub><br><sub>💡 依赖 MemPalace 本地语义检索；.plugin / .claude-plugin 格式；架构也可用于非虚构项目</sub>

- **[novel-to-webnovel](https://github.com/aimerfeng/novel-to-webnovel)** · ★ 1<br>把日轻译稿、机翻稿的翻译腔改成中文网文口感：分三档程度，格式清理、风格定调、样例确认、分块并行改写、QA 脚本<br><sub>方法：修订 · 风格</sub><br><sub>更新于 2026-07-03 · 中文 · MIT</sub><br><sub>💡 需要 perl。默认另存新文件；重度档会把人名和背景改成中国本土</sub>

#### 框架 · 应用（8）

- **[arrows](https://github.com/p-e-w/arrows)** · ★ 172<br>补全式写作前端：每次按段落生成两个续写候选，用方向键选取、重生成或撤回，无任何界面元素，靠作者逐段挑选推进正文<br><sub>方法：共创</sub><br><sub>更新于 2024-07-15 💤 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 需 OpenAI 兼容的 text completion 接口（推荐 llama.cpp server 并行生成）；2024-07 后未更新</sub>

- **[LLooM](https://github.com/the-crypt-keeper/LLooM)** · ★ 127<br>人在环中的续写界面：读取模型 logits 同时展开多条候选 beam，作者逐段挑选或改写后再继续，一点点织出故事<br><sub>方法：共创</sub><br><sub>更新于 2024-12-14 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 2024-12 后未更新（127★）；需本地 vLLM/llama.cpp 提供 logits，OpenAI 模式写死 gpt-3.5-turbo</sub>

- **[WalkingShadows](https://github.com/ofey404/WalkingShadows)** · ★ 28<br>故事原型工具：参考生成式智能体论文，分阶段提示先描绘设定、搭故事主干、按故事动力写大纲、提炼主题，再摘要设定，全栈 monorepo<br><sub>方法：规划 · 设定</sub><br><sub>更新于 2023-06-13 💤 · 🧩 应用 · 英文 · GPL-2.0</sub><br><sub>💡 2023 年早期原型，README 说明有限，提示词迭代记录在 experiments/；Bazel 构建</sub>

- **[Serendipity-Engine](https://github.com/IsaiahN/Serendipity-Engine)** · ★ 14<br>八阶段工作台：作者画像→叙述者（视角/时态/可靠性）→世界→人物→关系→大纲→写前结构审计→逐章写作，正文带入作者声音与人物声纹<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-06-29 · 🧩 应用 · 英文</sub><br><sub>💡 自带 API key；main 分支是纯 Markdown 理论与模板，可脱离应用手动使用；作者主导，AI 按请求生成正文；仓库内的 zip 是 Chrome 扩展打包</sub>

- **[clawloom](https://github.com/Aaron-ou/clawloom)** · ★ 9<br>世界推演平台：人设规则、播种角色，AI 角色按 tick 自主决策和互动，事件写入时间线，再从事件中提取叙事导出为小说或剧本<br><sub>方法：设定 · 人物 · 模拟</sub><br><sub>更新于 2026-03-08 💤 · 🧩 应用 · 中文</sub><br><sub>💡 外部 AI 通过 API Key 接入来建世界、推进模拟</sub>

- **[deep-narrative-engine](https://github.com/2540581291/deep-narrative-engine)** · ★ 9<br>成人向虚构创作桌面工具：以角色卡为核心（AI 生成或从小说提取），配世界观、文风分析与语料库，生成小说章节、互动分支故事等多种文体<br><sub>方法：设定 · 人物 · 风格 · 共创</sub><br><sub>更新于 2026-10-05 · 🧩 应用 · 中文</sub><br><sub>💡 成人内容；作者自述约一半模块是凑数；无开源许可证；大语料文件走 Git LFS</sub>

- **[worldbuilder](https://github.com/gofastercloud/worldbuilder)** · ★ 7<br>文件化世界观与写书系统：11 类实体用 Markdown+YAML 互引，图校验关系与时间线一致性，CLI 向导出提示词交 Claude Code 写设定与正文<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-06-23 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 插画与角色配音生成需 Apple Silicon</sub>

- **[ai_writers_workshop](https://github.com/angrysky56/ai_writers_workshop)** · ★ 6<br>MCP 服务器：给 AI 助手提供原型人物、英雄之旅等叙事模式和情节线库，按项目管理人物、场景、大纲与象征，知识图谱存实体关系后汇编成稿<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2025-05-15 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 附 Ollama modelfile（qwen3）</sub>

#### 研究代码（8）

- 🌟 **[WriteHERE](https://github.com/principia-ai/WriteHERE)** · ★ 976<br>异构递归规划：把写作任务动态拆成检索、推理、撰写三类子任务，边分解边执行并按上下文调整，小说与长报告共用一套引擎<br><sub>方法：规划</sub><br><sub>更新于 2026-09-03 · 🎓 研究 · 英文</sub><br><sub>💡 EMNLP 2025 oral 论文代码；同时做技术报告（报告模式需 SerpAPI）；需 OpenAI/Anthropic Key；README 标 MIT 但 GitHub 未识别许可证</sub>

- 🌟 **[doc-story-generation](https://github.com/yangkevin2/doc-story-generation)** · ★ 161<br>DOC：先生成前提和多层细纲（重排器挑大纲顺序、检测人物），再按细纲逐段写正文并用控制器保持贴合大纲，产出 3500+ 词长故事<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2023-10-27 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 ACL 2023，Re3 的后续；需 GPT-3 API 和 GPU 跑控制器；更新版见 facebookresearch/doc-storygen-v2</sub>

- **[emnlp22-re3-story-generation](https://github.com/yangkevin2/emnlp22-re3-story-generation)** · ★ 257<br>Re3：先生成前提、设定、人物和大纲（Plan），逐段起草（Draft），用相关性/连贯性重排器挑候选（Rewrite），再检测修正前后矛盾（Edit）<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2022-12-21 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 EMNLP 2022 论文代码，调用 GPT-3 旧接口；作者推荐后续版本 yangkevin2/doc-story-generation</sub>

- **[doc-storygen-v2](https://github.com/facebookresearch/doc-storygen-v2)** · ★ 93<br>DOC 官方重写版：前提→层级大纲→正文三步，每步用开源或聊天大模型生成并按 logprob 重排挑选，前提与大纲存 JSON 供人工修改<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2026-05-13 · 🎓 研究 · 英文</sub><br><sub>💡 原作者对 yangkevin2/doc-story-generation 的重写；默认用 vLLM 部署 LLaMA-2 等，需改一行 vLLM 代码；附 7000 对情节人工偏好标注</sub>

- **[MoPS](https://github.com/GAIR-NLP/MoPS)** · ★ 47<br>ACL 2024：把故事前提拆成主题、背景、人物等模块，先归纳各模块候选成嵌套字典，抽一条路径再让 LLM 合成前提，供扩写成小说或剧本<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2024-07-19 💤 · 🎓 研究 · 英文</sub><br><sub>💡 附 HuggingFace 数据集 ManTle/mops（前提及扩写故事）；扩写用 Dramatron 和 RecurrentGPT；默认 gpt-3.5</sub>

- **[Pacing](https://github.com/YichenZW/Pacing)** · ★ 18<br>EMNLP 2023 长篇故事规划：训练具体度评估器，在层级大纲扩展时对齐同层节点详略、控制节奏，再用 ChatGPT 版 DOC 逐条生成正文<br><sub>方法：规划</sub><br><sub>更新于 2024-11-19 💤 · 🎓 研究 · 英文</sub><br><sub>💡 基于 yangkevin2/doc-story-generation；评估器模型与 GPT-BookSum 数据集在 Hugging Face</sub>

- **[CoDi](https://github.com/Speeditidious/CoDi)** · ★ 16<br>导演-演员框架：planner 设定世界人物并可按四段式结构规划，director 调度角色 agent 逐轮演出达成故事目标，editor 整理成剧本或小说<br><sub>方法：规划 · 理论 · 多智能体 · 模拟</sub><br><sub>更新于 2025-11-19 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 AIIDE 2025 论文代码；默认 GPT-4o + Gemini，需 OpenAI / Google API Key</sub>

- **[Collective-Critics-for-Creative-Story-Generation](https://github.com/EMNLP-2024-CritiCS/Collective-Critics-for-Creative-Story-Generation)** · ★ 14<br>在 DOC 长故事流水线上加集体评审：多位带人设的 LLM 评论家按新颖性等创意标准批评故事计划与正文表达，领导者汇总后迭代修订<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-01-10 💤 · 🎓 研究 · 英文 · MIT</sub><br><sub>💡 EMNLP 2024 论文代码，基于 yangkevin2/doc-story-generation；Streamlit 查看生成结果</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# sepia
npx skills add Nanako0129/sepia
# creative-writing-skills
npx skills add haowjy/creative-writing-skills
# agent-skills
npx skills add jwynia/agent-skills
# novel-writing
npx skills add wgwtest/novel-writing
# chinese-erotic-fiction-writing
npx skills add xWebt/chinese-erotic-fiction-writing
# writers-room-story-engine
npx skills add jackterror/writers-room-story-engine
# storywriting.skill
npx skills add changlizhi569/storywriting.skill
# novel-humanize
npx skills add qi531416/novel-humanize
# mckee-story
npx skills add song776/mckee-story
# BMad-Expansion-Pack-Creative-Writing
npx skills add DrBalls/BMad-Expansion-Pack-Creative-Writing
# fiction-humanizer-zh
npx skills add deedeekong07-alt/fiction-humanizer-zh
# chinese-webnovel-editor
npx skills add fanjack510-ctrl/chinese-webnovel-editor
# worldbuilding-skill
npx skills add tahini2007/worldbuilding-skill
# advanced-writer
npx skills add angrysky56/advanced-writer
# fictional-erotica
npx skills add rs-skills-lab/fictional-erotica
# huoren-write
npx skills add laoguo2025/huoren-write
# AutoWriter
npx skills add sinfiny/AutoWriter
# Creative-writing-skill
npx skills add xbraindance/Creative-writing-skill
# reliquery
npx skills add the-essential/reliquery
# novel-to-webnovel
npx skills add aimerfeng/novel-to-webnovel
```

</details>

<a id="by-method"></a>
## 按创作方法查找

同一种方法在不同项目里怎么落地，完整索引见 [METHODS.md](METHODS.md)：

- [规划先行：层级大纲、分解写作](METHODS.md#method-planning)（425）
- [叙事理论注入：结构模型、类型套路、写作原则](METHODS.md#method-theory)（137）
- [设定 · 世界观构建](METHODS.md#method-worldbuilding)（138）
- [人物塑造 · 角色档案](METHODS.md#method-character)（168）
- [长篇记忆 · 一致性：状态库、设定库、检索](METHODS.md#method-memory)（423）
- [多智能体分工：作者、编辑、审稿、读者](METHODS.md#method-multiagent)（134）
- [角色模拟 · 世界推演：让角色演出情节](METHODS.md#method-simulation)（71）
- [审稿 · 自我批评 · 迭代修订](METHODS.md#method-revision)（341）
- [风格学习 · 仿写：范文、文风蒸馏、拆书](METHODS.md#method-style)（112）
- [去 AI 味 · 文笔打磨](METHODS.md#method-deai)（87）
- [交互共创：读者选择、人机协作](METHODS.md#method-interactive)（176）

<a id="resources"></a>
## 相关资源

- [yingpengma/Awesome-Story-Generation](https://github.com/yingpengma/Awesome-Story-Generation)、[Picrew/awesome-llm-story-generation](https://github.com/Picrew/awesome-llm-story-generation)：故事生成方向的论文列表，没有开源代码的研究看这两个
- 评测：[lechmazur/writing](https://github.com/lechmazur/writing)（给定 10 个必备元素写短篇，比较各家模型）、[EQ-bench/creative-writing-bench](https://github.com/EQ-bench/creative-writing-bench)（创意写作评测）、[jenna-russell/storyscope](https://github.com/jenna-russell/storyscope)（统计 AI 小说在叙事结构上的特征，[sepia](https://github.com/Nanako0129/sepia) 的去 AI 味方法就来自它）
- [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)：让模型一次给出多个带概率的候选来缓解千篇一律，不限于小说，但常被用在故事点子和开头上
- [awesome-novel-skills](https://github.com/UnderleveledBuilder/awesome-novel-skills)：网文作者的工具箱，除了写作还收下载、书源、翻译、发布
- [awesome-short-drama-skills](https://github.com/UnderleveledBuilder/awesome-short-drama-skills)：AI 短剧 · 漫剧 skill，包括分镜和视频提示词
- [anthropics/skills](https://github.com/anthropics/skills)：官方 Agent Skills 仓库，想自己写 skill 可以从这里看起

## 参与贡献

推荐项目可以[提交 issue](../../issues/new?template=submit-skill.yml)，也可以直接改 `data/skills.toml` 发 PR，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。自己做的故事生成项目也欢迎自荐。

<a id="badge"></a>
## 收录徽章

项目已被收录的作者，可以在自己的 README 里加上这个徽章：

[![收录于 Awesome LLM Storytelling](https://img.shields.io/badge/%E6%94%B6%E5%BD%95%E4%BA%8E-Awesome_LLM_Storytelling-1f6feb)](https://github.com/UnderleveledBuilder/awesome-llm-storytelling)

```markdown
[![收录于 Awesome LLM Storytelling](https://img.shields.io/badge/%E6%94%B6%E5%BD%95%E4%BA%8E-Awesome_LLM_Storytelling-1f6feb)](https://github.com/UnderleveledBuilder/awesome-llm-storytelling)
```

## 许可

[CC0 1.0](LICENSE)

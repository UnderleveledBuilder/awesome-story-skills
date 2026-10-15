**解决什么问题**：让一个模型在同一段上下文里规划、写作、自查，规划材料会挤占写作空间，自己审自己的稿也难发现问题。拆成多个角色后，每次调用只看该看的材料，写和审分开，审不过可以打回。

**常见做法**

1. **工序接力**：按编辑部或编剧室分岗，策划、设定、写手、编辑、润色各有一段提示词，按固定顺序传递文件。长篇网文和整书生成里最常见，有的项目还给特定岗位否决权。代表：[loom-novel](https://github.com/WadeZhao23/loom-novel)、[Novel-OS](https://github.com/mrigankad/Novel-OS)、[story-systems-template](https://github.com/bybren-llc/story-systems-template)、[Book-Writing-AI-Agent](https://github.com/Aftabbs/Book-Writing-AI-Agent)
2. **总控按状态派单**：调度者读项目状态，决定下一步派谁；子 agent 各有独立上下文，只通过落盘的工件交流。ainovel-cli 把调度写成确定性代码，只在少数需要判断的节点单次调用 Arbiter，每步写 checkpoint；在 Claude Code 类宿主里，常见形态是主会话只组 brief、派子代理、写文件。代表：[ainovel-cli](https://github.com/voocel/ainovel-cli)、[Novel-factory](https://github.com/YonRen-code/Novel-factory)、[awesome-novel-agent](https://github.com/modoojunko/awesome-novel-agent)、[NovelGenerator](https://github.com/Dylin-code/NovelGenerator)
3. **写审分离与评审团**：生成和评审交给不同 agent，评审可多路并行，再由裁定者汇总；不过就打回，并限定轮数。ProseForge 四路并行写草稿后择优，再由连续性、对抗、文风三评审合议；CritiCS 让多位带人设的评论家批评计划和正文，领导者汇总后修订；Fibb 只保留复评后可测地变好的版本。代表：[Claude-Book](https://github.com/ThomasHoussin/Claude-Book)、[ProseForge](https://github.com/remacheybn408-boop/ProseForge)、[CritiCS](https://github.com/EMNLP-2024-CritiCS/Collective-Critics-for-Creative-Story-Generation)、[Fibb](https://github.com/Ckokoski/Fibb)
4. **冷读者**：另起一个不继承作者上下文的 agent，按普通读者的顺序读成稿，只报告看不看得懂、读不读得下去。lengdu 把作者侧校准和读者首读拆成两个全新 agent，改稿后必须换一个新 Reader 复核；novel-agent-workflow 要求编辑和读者的身份不能与作者相同。代表：[lengdu](https://github.com/asass-11/lengdu)、[novel-agent-workflow](https://github.com/realwindjpn/novel-agent-workflow)、[book-genesis-studio](https://github.com/felipelobomotta-blip/book-genesis-studio)
5. **角色演出，导演收束**：每个角色一个 agent，按感知、计划、行动、反思自主行动，事件先在沙盒里演出来，再由导演或叙述者按故事目标整理成章节或剧本。Sonder_Engine 把客观因果、各角色感知、角色决策、叙述拆成独立调用，只有提交步骤能写入状态。互动叙事、剧本杀和群像故事里常见。代表：[OpenStory](https://github.com/ZJU-LLMs/OpenStory)、[StoryBox](https://github.com/amcghm/StoryBox)、[CoDi](https://github.com/Speeditidious/CoDi)、[Sonder_Engine](https://github.com/N0819/Sonder_Engine)、[fictionforge](https://github.com/wanqili857-byte/fictionforge)

**取舍和坑**

- **调用数随岗位增长**：Sonder_Engine 每回合多次调用模型，成本较高。也有项目在往回收：novel_generator 在 v4.0 把每章 8–12 次调用合成 1 次；AI_novel 把 agent 从 9 个并到 5 个；ainovel-cli 写明"越简单越稳定，拒绝复杂编排"。
- **同一个模型评自己**：Novel-factory 让写手和评审分属两个模型族做候选盲评，专门对抗自评偏好；NovelGenerator 的写手和修订者走本地模型，评论家用 Claude。
- **返工要有上限和出口**：Claude-Book 的三审循环不超过 3 轮，StoryClaw 最多打回 3 次，novel_generator 用熔断防止无限重写，NovelGenerator 把两轮仍未收敛的章节记进 issues.md。
- **信息泄漏会让分工失效**：lengdu 不许向 Reader 透露作者意图和校准报告；hermes-novel-generator 让角色 agent 互不可见地规划场景；Novel-factory 给写手的视图去掉元信息，并逐字扫描谜底关键词。
- **自由演出不等于有故事**：StoryBox 和 CoDi 都在角色互动之上加了自上而下的规划或导演。互动场景还要顾及延迟：openovel 让前台叙述者只管流式出正文，导演、记忆等后台 agent 异步改状态文件。

**从哪里开始**：

- [ainovel-cli](https://github.com/voocel/ainovel-cli)：适合想搭自己流水线的开发者，README 把确定性引擎、自主 worker、按需裁定三层分工讲得清楚，可在 TUI 里看着写，也能 headless 跑。
- [Claude-Book](https://github.com/ThomasHoussin/Claude-Book)：适合用 Claude Code 写书的人，bible 只读、state 按章版本化、三审限轮，目录简单好改。
- [lengdu](https://github.com/asass-11/lengdu)：适合已有成稿、只想加一道独立读者检查的人，流程短，核心是一个 SKILL.md 和几份角色档案。

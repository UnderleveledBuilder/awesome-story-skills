**解决什么问题**：模型一次写成的稿子常有它自己察觉不到的毛病：前后设定打架，角色提前知情，节奏塌，套话多；章数一多，错误还会累积。审稿和修订把「写」和「挑错」拆开：用独立的评审、打分或脚本找问题，定点改，改完再复检。

**常见做法**

1. **写后门禁，不过就返修**：每章固定走「写→审→改→回写状态」，评审按维度出问题清单，不过就打回，设轮次上限。Claude-Book 跑文风、人物、连续性三道审，最多循环 3 轮；ainovel-cli 的 Editor 按七个维度评审，每一项都要引原文举证。长篇 harness 多用这种结构。代表：[inkos](https://github.com/Narcooo/inkos)、[webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)、[Claude-Book](https://github.com/ThomasHoussin/Claude-Book)、[ainovel-cli](https://github.com/voocel/ainovel-cli)
2. **打分择优，只留变好的**：一次出几个候选，或改完重打分，按分数决定留弃。autonovel 照搬 autoresearch 的「改—评—留弃」循环，各阶段分数过阈值才往下走；Fibb 只保留「可测地变好」的修订稿；AI-automatically-generates-novels 每层发 3 个候选，评审只报带原句证据的问题，分数由程序按扣分表算。代表：[autonovel](https://github.com/NousResearch/autonovel)、[Fibb](https://github.com/Ckokoski/Fibb)、[AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels)、[Re3](https://github.com/yangkevin2/emnlp22-re3-story-generation)
3. **多视角评审团**：几个带人设的评论家各看一面，再由主持人汇总成修改意见。CritiCS 让多位评论家按新颖性等创意标准批评计划和正文；ProseForge 的连续性、对抗性、文风三位评审互相看不到，最后合议；Fibb 让每个主要角色审自己的台词。代表：[CritiCS](https://github.com/EMNLP-2024-CritiCS/Collective-Critics-for-Creative-Story-Generation)、[ProseForge](https://github.com/remacheybn408-boop/ProseForge)、[novel2agent-jp](https://github.com/kgmkm/novel2agent-jp)、[novelforge](https://github.com/LunaRime/novelforge)
4. **冷读**：评审不继承作者上下文，只读正文，报告看不看得懂、想不想读下去。lengdu 改稿后必须换一个新读者复核，校准报告和作者意图都不许透露给读者；book-genesis-studio 在写完第一章时就请盲读读者，修订稿只有读者更喜欢才保留。代表：[lengdu](https://github.com/asass-11/lengdu)、[book-genesis-studio](https://github.com/felipelobomotta-blip/book-genesis-studio)、[fiction-forge](https://github.com/geobond13/fiction-forge)
5. **确定性检查，作者采纳**：能机械判定的交给脚本，模型只提修订补丁，作者看 diff 决定收不收。story-skills 把人物生死、伏笔、知情状态写进 frontmatter，CLI 像编译器报类型错误一样报「死人复出」「兑现早于铺垫」；Story-Editor 让独立编辑模型只审新写的内容，带引文提出记忆变更，批准后才入库。代表：[story-skills](https://github.com/danjdewhurst/story-skills)、[StoryForge](https://github.com/XZZKANY/StoryForge)、[Story-Editor](https://github.com/izanagi771-stack/Story-Editor)

**取舍和坑**

- 自己评自己会偏心。Novel-factory 让写手和评审分属两个模型族做盲评，专门对抗自偏好；AI-automatically-generates-novels 把评审温度压到 0.3，理由是尺子自己飘了，章与章的分数就不可比。
- 循环要有出口。autonovel 在分数进入平台期时停，初稿阶段「进度优先于完美」；book-genesis-studio 每道关最多三轮；novel_generator 设熔断，超阈值强制挂起，防止无限重写。
- 候选重排可能比事后编辑更要紧。Re3 的 README 写明：关掉 Edit 模块会快不少、损失不大；把候选数设为 1、关掉重排，效果明显变差。
- 脚本抓不到累积型错误。fiction-forge 写完约 29 万字后，一次带状态账本的通读找出 191 个五轮自动编辑漏掉的问题，如时间线漂移、道具同时出现在两处。扫描器适合防回潮，不适合找问题。
- 改稿会越改越散。kitten-punch-screenwriting 要求按问题来源回修对应层，禁止为修局部问题重写整体或引入新设定；dsh-novel-craft 的批注只改被标的段落。

**从哪里开始**：[Claude-Book](https://github.com/ThomasHoussin/Claude-Book) 适合在 Claude Code 里给现有流程加审稿：bible 只读、状态按章存档、三审最多三轮，目录结构可照搬。[autonovel](https://github.com/NousResearch/autonovel) 适合想做全自动长篇的开发者，从设定打分到全书修订都有独立脚本，循环怎么停写得清楚。[lengdu](https://github.com/asass-11/lengdu) 适合写中文短篇、在意读感的作者，核心只有「独立校准＋新读者首读」两步。

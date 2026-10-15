**解决什么问题**：整本书装不进上下文，模型也不会自己记账。写到几十章，死去的人物又出场，伏笔埋了没收，角色知道了还没发生的事。这个方法把"记住"交给文件、数据库和检索，不靠模型回忆。

**常见做法**

1. **关键词触发的设定条目**：每条人物、地点、规则配几个触发词，近期文本里出现就注入上下文，KoboldAI 的 World Info、SillyTavern 的世界书都是这样；Auto-Cards 还会从剧情里识别命名实体，自动写成新卡。互动叙事和角色扮演里最常见。代表：[KoboldAI-Client](https://github.com/KoboldAI/KoboldAI-Client)、[SillyTavern](https://github.com/SillyTavern/SillyTavern)、[Writingway](https://github.com/a-omukai/Writingway)、[Auto-Cards](https://github.com/LewdLeah/Auto-Cards)
2. **近文原文，远文摘要**：最近的内容保留原文，更早的逐级压成摘要。otaku 固定发送前 20 条和后 150 条原文以保文风，中段换成场景摘要；word-compiler 把上下文分成项目、章、场景三环，超预算时按优先级压缩，场景环至少占 60%。代表：[RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT)、[otaku](https://github.com/enclavum/otaku)、[NovelFlow](https://github.com/DongxUETAFFY/NovelFlow)、[word-compiler](https://github.com/2389-research/word-compiler)
3. **状态账本与写后结算**：人物状态、伏笔、时间线存成结构化文件或库；每章写完，模型提交变更，程序校验后才落盘。tianming-novel-ai-writer 要求正文附 JSON 变更声明，过六道门禁才落地；ai-novel-studio 只接受状态补丁，服务端校验后事务提交，模型改不了已登场角色的名字。代表：[inkos](https://github.com/Narcooo/inkos)、[tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer)、[agent-novel](https://github.com/RTY798/agent-novel)、[ai-novel-studio](https://github.com/weike-zhang/ai-novel-studio)
4. **检索：关键词、向量与图谱**：给事实、摘要和原文建索引，写前按当前章节取相关片段。WenShape 用 BM25 加实体增强挑事实，再按与当前章的距离衰减权重；saga 用 Neo4j 知识图谱追踪人物、事件和关系，DOME 在写作中用知识图谱检测并消解前后矛盾。代表：[WenShape](https://github.com/unitagain/WenShape)、[saga](https://github.com/Lanerra/saga)、[DOME](https://github.com/Qianyue-Wang/Generating-Long-form-Story-Using-Dynamic-Hierarchical-Outlining-with-Memory-Enhancement)、[Ai-Novel](https://github.com/inliver233/Ai-Novel)
5. **按时间和视角分账**：同一条事实在不同章节真假不同，角色、作者、读者知道的也不同。neuro-book 用时间线切面做事件溯源，任意时刻的世界状态由此前切面推算；jarvis-write 给每条事实绑生效章节区间；oh-story-claudecode 和 Closure 分开记作者真相与读者已知，Smart-Memory 给每个角色单独记它知道的事。代表：[neuro-book](https://github.com/notnotype/neuro-book)、[jarvis-write](https://github.com/ynnyh/jarvis-write)、[oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)、[Closure](https://github.com/AoharuCat/Closure)、[Smart-Memory](https://github.com/senjinthedragon/Smart-Memory)

**取舍和坑**

- **关键词触发有规模上限**：DeepLore 的 README 说，世界书关键词匹配在 80–100 条左右开始失灵，正文没打出那个词，相关条目就不触发。它加了一步让模型读条目摘要精选，代价是每轮多一次调用。
- **写回要有闸门**：自动抽取会把错误写成正典。Story-Editor 让编辑模型只提议、作者批准才入账；novel-agent-studio 只从作者采纳的正文提取记忆；Novel-factory 要求账本条目附正文引证，对不上不入账。
- **记忆要有预算和权威源**：oh-story-claudecode 的状态卡上限 12 KiB，主会话只把本章相关部分交给写手；ProseForge 按真实窗口的 65% 给每个席位设预算；inkos 以原始文件为权威，检索索引可以重建。
- **约束太硬会伤叙事**：glyphkeeper 停更时说明，事件溯源加物理仲裁"过度限制了 LLM 的叙事灵活性"，还拖慢响应。agent-novel 只对事实错误严格拦截，文风规则只作观察项。
- **收益因模型而异**：fictionforge 的 CanonBench 首期结果里，裸写违反较多的两个模型注入上下文后明显改善，裸写违反最少的那个几乎不变；作者还订正过一次，一项"模型差异"大半来自判定器误报和被截断的残章。上线前用自己的模型实测。

**从哪里开始**：

- [oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)：适合用编程 Agent 写网文的作者，记忆就是项目里的文件，demo 有真实的续写状态卡可对照。
- [RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT)：适合想弄懂"短期记忆 + 长期记忆"最小结构的开发者，代码少，配论文。
- [sillytavern-DeepLore](https://github.com/pixelnull/sillytavern-DeepLore)：适合已在用 SillyTavern 世界书、条目多到关键词不够用的人。

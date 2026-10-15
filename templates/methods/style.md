**解决什么问题**：只在提示里写「模仿某某的风格」，模型学到的是表面印象：堆几个标志性的词，套一种腔调，句式、节奏和对白还是它自己的平均写法；写长了文风还会漂。风格学习把「像谁」落成能执行、能检查的东西：从样本提炼的规则档案、可检索的范文、或一组可测量的指标。写时注入，写完比对。

**常见做法**

1. **蒸馏成文风档案**：读样本，按固定维度（视角、句式、对白、节奏、钩子、禁忌等）提炼成可安装的 SKILL.md 或 style.json，写作时加载。xin-novel-style-builder 先清洗出前 20 章正文，再做十维萃取；works-dna-extractor 拆 16 层「作品 DNA」，附 8 维吻合度量表。代表：[xin-novel-style-builder](https://github.com/oscar-wang-xin/xin-novel-style-builder)、[works-dna-extractor](https://github.com/Shiaoming123/works-dna-extractor)、[novel-style-skills](https://github.com/xianzl/novel-style-skills)、[author-style-extractor](https://github.com/alexsowake/author-style-extractor)
2. **量化指纹，写后比对**：用分词、句长、标点密度、TTR 等统计给作者画像，成稿再对照语料区间。longzu.skillls 逐字统计了 1465 万字原著，加 45 个等距精读点；审计脚本超出区间给警告，对话动词用错直接判 FAIL，可以挂进 CI。代表：[longzu.skillls](https://github.com/zuoyou12/longzu.skillls)、[novel-writer-style-cn](https://github.com/lsg1103275794/novel-writer-style-cn)、[bmad-book-builder](https://github.com/jblemee/bmad-book-builder)
3. **范文检索**：不压成规则，把语料切成片段或场景建索引，写前按需求取几段放进上下文。Novel-RAG 先筛掉没有参考价值的场景，再支持「对白带试探感」这类需求检索；character-card-skills 选 2–3 部互补的小说当语感锚点。代表：[Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill)、[Novel-RAG](https://github.com/a-big-fish/Novel-RAG)、[character-card-skills](https://github.com/foreverse-app/character-card-skills)、[jarvis-write](https://github.com/ynnyh/jarvis-write)
4. **从作者自己的修改里学**：不读名家，读作者对 AI 稿的改动或评价，总结成个人偏好。loom-novel 把作者手改蒸馏进「写作指纹」；OpenFicM 对比 AI 原稿和作者定稿；dsh-novel-craft 让作者逐段点赞点踩，模型总结成几百字节的偏好档案；word-compiler 分析修改 diff，生成规则提案。代表：[loom-novel](https://github.com/WadeZhao23/loom-novel)、[OpenFicM](https://github.com/tioners/OpenFicM)、[dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft)、[word-compiler](https://github.com/2389-research/word-compiler)
5. **拆书学结构**：学的不只是文笔，而是参考作品的结构、情节单元、节奏和套路，先抽象成叙事模式再套到新故事上。网文和短剧最常见。harnessNovel 先拆书再仿写；open-novel-fanqie 拆一本对标书出套路 JSON，再「换壳」给出切入方案。代表：[harnessNovel](https://github.com/XTmingyue/harnessNovel)、[open-novel-fanqie](https://github.com/kongxcer555/open-novel-fanqie)、[AnySpark](https://github.com/Mikexujunrui/AnySpark)、[Hermes_Script_Cool](https://github.com/way928745-collab/Hermes_Script_Cool)

**取舍和坑**

- 只喂语料不够。character-card-skills 人工复核后改了结论：只给语料、不加禁用规则，净效果为负；套话靠禁用纪律压下去，语料只在词汇、物件、语域上起作用。
- 档案存规律，不存原文。dsh-novel-craft 的理由：原文几千字，带两轮上下文就满；规律几百字节，每轮都带得动，学到的是「怎么写」而不是可抄的句子。loom-novel 只学作者的改动，绝不学 AI 自己的输出。
- 多位作者不能取平均。novel-style-skills 先逐位蒸馏，再按叙述声音、句法、对白分层组合；longzu.skillls 把两位作者共享的叙事骨架和互斥的语言皮肤分开，杂交时皮肤成套使用。
- 文风对了，故事可能是死的。novel-style-skills 写明风格评估只看语言，一稿可能通过评估却没有欲望、阻力、选择和代价；harnessNovel 先把参考情节抽象成叙事模式，避免直接换名搬运。
- 保真度要标边界、要盲测。longzu.skillls 注明规则只覆盖采样过的那几部书，并请禁用本地资源的独立 agent 盲判归属；第一轮因评审偷看了 skill 被作废。

**从哪里开始**：[longzu.skillls](https://github.com/zuoyou12/longzu.skillls) 适合想蒸馏一位作者的人，统计、精读、盲测三层证据都公开，审计脚本零依赖。[dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft) 适合想让 AI 越写越像自己、又说不清自己要什么的作者，只需点赞点踩，但依赖 DeepSeek Harness。[harnessNovel](https://github.com/XTmingyue/harnessNovel) 适合写网文、想学对标书结构的人，拆书和仿写分阶段，有本地 Web 工作台。

**解决什么问题**：模型写小说有固定指纹：套话、「不是 X 是 Y」、情绪直接贴标签、对白像汇报、段落节奏均匀；结构上爱点题，因果过分整齐，结尾靠主角成长收束。读者几行就能认出来。去 AI 味就是把这些痕迹找出来改掉，或在下笔前避开。

**常见做法**

1. **写后规则扫描**：把套话、句式、标点写成规则或脚本，正文落盘后扫一遍，命中就改。neuro-book 的 llmlint 有 360 条规则，静态规则扫全稿，LLM 规则判语境；novel-novel-generator 把每章新查出的套话加进后续章节的禁用表。代表：[neuro-book](https://github.com/notnotype/neuro-book)、[novelops](https://github.com/a11003070312/novelops)、[oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)、[novel-novel-generator](https://github.com/mike-cramblett/novel-novel-generator)
2. **分层诊断改写**：先改叙事结构，再改段落，最后改措辞。sepia 按 StoryScope 论文分三遍（不点题、松因果链、后置揭示 → 段落流 → 表层用词）；fiction-humanizer-zh 把梗概式情节按「铺垫、过程、余波」重写。代表：[sepia](https://github.com/Nanako0129/sepia)、[fiction-humanizer-zh](https://github.com/deedeekong07-alt/fiction-humanizer-zh)、[chinese-webnovel-editor](https://github.com/fanjack510-ctrl/chinese-webnovel-editor)
3. **门禁加退回重写**：去 AI 味是章节流水线上的一道关，计数或打分不过就退回。xt-webnovel-writing 命中「回滚级硬门」整章退回；jarvis-write 用套话规则加句长、段落统计打分，超标定向重写再复测，改坏了回退旧版；autonovel 机械打分加 LLM 评审，再让模型找出可删的 500 字。代表：[xt-webnovel-writing](https://github.com/xiaotiewinner/xt-webnovel-writing)、[jarvis-write](https://github.com/ynnyh/jarvis-write)、[autonovel](https://github.com/NousResearch/autonovel)、[awesome-novel-agent](https://github.com/modoojunko/awesome-novel-agent)
4. **正向锚定**：给模型一个具体的人去学，而不只是禁词。human-like-novel-workbuddy-skill 写章节计划时注入人常用、模型少用的词、句式和修辞；loom-novel 只从作者手改中蒸馏写作指纹；novel-style-skills 从样本蒸馏 style.json，写后查风格漂移。代表：[human-like-novel-workbuddy-skill](https://github.com/LittleLollipop/human-like-novel-workbuddy-skill)、[loom-novel](https://github.com/WadeZhao23/loom-novel)、[novel-style-skills](https://github.com/xianzl/novel-style-skills)、[Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill)
5. **按统计指标改写**：用指标定位要改的句子。Claude-Book 用本地 8B 模型算困惑度，改写低困惑度句子；novel-writer-master 用 332 词黑名单加统计分析定向改写，以朱雀检测为对标。代表：[Claude-Book](https://github.com/ThomasHoussin/Claude-Book)、[novel-writer-master](https://github.com/qiuxinyuan321/novel-writer-master)、[novel-humanize](https://github.com/qi531416/novel-humanize)

**取舍和坑**

- 禁词表会养出新套路。human-like-novel-workbuddy-skill 认为禁词只是让模型改用第二、第三顺位的词，久了是另一种 AI 味。novelops 称实测写作指令越短文笔越好，于是写作指令只留三条，禁忌全交给写后脚本。
- 只改措辞不够。sepia 引用的 StoryScope 研究中，人工编辑改写表层文风后，检出率只从 95.5% 降到 93.9%。
- 通用规则可能偏离目标文风。fiction-forge 发现「删副词、删比喻」让案例稿离目标作者更远，改为先按目标语料测每千字画像。它也只把扫描器当防回潮的围栏：一次带状态账本的通读，找出五轮自动编辑漏掉的 191 个问题。
- 别让 LLM 判断像不像人。character-card-skills 的盲评中，LLM 评审分辨人写与 AI 写的准确率只有 12%。
- 改写会伤剧情和声口。chinese-webnovel-editor 先冻结剧情事实、人物证据和世界规则再动笔；huoren-write 不新增剧情事实，保留各角色声口。两者都写明不以绕过检测为目标。

**从哪里开始**：[sepia](https://github.com/Nanako0129/sepia) 适合已有稿子、想从结构层改的人，可以先只跑诊断。[huoren-write](https://github.com/laoguo2025/huoren-write) 适合中文网文和短剧，只改表达层、不碰剧情，附检查脚本。[fiction-forge](https://github.com/geobond13/fiction-forge) 适合长篇作者，把扫描器、文风测量和通读校对配起来用。

**解决什么问题**：不做规划，模型只能逐段续写：主线越写越散，节奏前松后赶，伏笔埋了不收。整本书又放不进上下文，后面的章节会推翻前面的设定。规划把"写什么"和"怎么写"分开，先定骨架，再让模型按骨架填正文。

**常见做法**

1. **逐层展开**：一句话前提→人物与设定→分幕或分卷情节→场景→正文，每层的输出是下一层的输入，作者可以在任一层改完再往下生成。不少项目用雪花法组织这些层级。代表：[Dramatron](https://github.com/google-deepmind/dramatron)、[GOAT-Storytelling-Agent](https://github.com/GOAT-AI-lab/GOAT-Storytelling-Agent)、[AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator)
2. **规划层多候选择优**：大纲阶段一次生成几个候选，用模型自评、训练好的重排器或程序判据挑一个；Pacing 用具体度评估器让同一层节点的详略对齐。代表：[gpt-author](https://github.com/mshumer/gpt-author)、[doc-story-generation](https://github.com/yangkevin2/doc-story-generation)、[AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels)、[Pacing](https://github.com/YichenZW/Pacing)
3. **滚动规划**：只细化眼前几章，远处保持粗纲，写到了再展开，展开时参考已写部分的摘要和角色状态。RecurrentGPT 把粒度压到段落：每步写一段正文，再写下一段的计划。代表：[RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT)、[ainovel-cli](https://github.com/voocel/ainovel-cli)、[DOME](https://github.com/Qianyue-Wang/Generating-Long-form-Story-Using-Dynamic-Hierarchical-Outlining-with-Memory-Enhancement)、[long-novel-generator](https://github.com/jiaw-Zh/long-novel-generator)
4. **章节合同**：每章写前生成结构化卡片，列目标、阻力、节拍、必现元素、伏笔编号、章末钩子和禁止项；写完由程序对照卡片检查，不过就带着反馈重写。短剧里同样的东西叫分集目录，逐集标钩子类型和付费卡点。代表：[InkAI](https://github.com/yan2959088709/InkAI-)、[agent-novel](https://github.com/RTY798/agent-novel)、[dsh-novel-forge](https://github.com/huangziyuan-general/dsh-novel-forge)、[short-drama](https://github.com/0xsline/short-drama)
5. **阶段门禁**：把流程切成固定阶段，每段有明确产物，前置产物缺失或未确认就不进下一段，有的由脚本或状态文件判定。不少项目照搬 Spec Kit 的"宪法→规格→澄清→计划→任务→写作→分析"七步。代表：[novel-writer](https://github.com/wordflowlab/novel-writer)、[speckit-preset-fiction-book-writing](https://github.com/adaumann/speckit-preset-fiction-book-writing)、[short-drama-scriptwriter](https://github.com/SumOneHK/short-drama-scriptwriter)

**取舍和坑**

- **大纲给多了会抢跑**。模型知道结局，就急着往结局写。[ai-novel-writer](https://github.com/KKKenChow/ai-novel-writer) 按全书进度分六个阶段逐步放开大纲可见范围，生成后再查是否提到了后续章节的关键词；dsh-novel-forge 把悬念人物的档案整份移出上下文。
- **写在提示词里的门禁会被跳过**。dsh-novel-forge 的原则是"代码强制 > 提示词自觉"，细纲没批准，写章工具直接拒绝。只靠提示词管流程的项目要看宿主配合，[ultimate-novel-creation-skill](https://github.com/Fly143/ultimate-novel-creation-skill) 就要求先把它的 system_prompt.md 配成宿主的系统提示词。
- **大纲迟早要改**。[jarvis-write](https://github.com/ynnyh/jarvis-write) 改任一章大纲会分析下游影响，由作者勾选级联重生成，并把已写正文标为失配；ainovel-cli 允许写作中途插入意见，评估影响范围后重写受影响章节。
- **层级越细，正文越像填空**。Dramatron 的用户研究里，编剧觉得输出偏公式化，更愿意拿它找点子和搭世界观；README 也承认自上而下的层级生成不对应每个人的写法。agent-novel 在关键分歧处先给三个方案让作者挑，避免模型总走最顺的路。
- **候选和步骤都要花钱**。每层发散多个候选、每章跑十几步，token 成倍增长；[novel_writer_agent](https://github.com/nonever2109/novel_writer_agent) 每章约跑 20 个流程。

**从哪里开始**：[GOAT-Storytelling-Agent](https://github.com/GOAT-AI-lab/GOAT-Storytelling-Agent) 适合先看懂层级规划的骨架，README 里一段代码就串起了从书籍设定到逐场写作的全流程。[agent-novel](https://github.com/RTY798/agent-novel) 适合在 Claude Code、Codex 里人机共写长篇，章节卡加作者确认关键选择，流程轻。[ainovel-cli](https://github.com/voocel/ainovel-cli) 适合想全自动跑长篇的人，重点看它的卷弧滚动规划和步骤级断点恢复。

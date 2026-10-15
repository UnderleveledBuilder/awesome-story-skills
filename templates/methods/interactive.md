**解决什么问题**：一键生成的故事，作者插不上手，读者只能看。模型自己定走向时容易平淡、跑偏，篇幅一长还会忘设定、乱改数值。交互共创把决定权分出去：作者在关键处挑选和拍板，读者或玩家用选择和行动推动剧情。

**常见做法**

1. **逐段候选，作者挑**：模型一次给两条以上续写，作者选一条、重生成或撤回。arrows 每次生成两段，用方向键选；LLooM 读模型 logits 同时展开多条候选；1667 每段保留多个版本，组成故事树。dsh-novel-craft 让作者对候选段点赞点踩，模型总结成几百字节的偏好档案带进下一轮。代表：[arrows](https://github.com/p-e-w/arrows)、[LLooM](https://github.com/the-crypt-keeper/LLooM)、[1667](https://github.com/1667-ai/1667)、[dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft)
2. **分层提案，作者拍板**：从一句 logline 或几轮问答出发，逐层生成人物、节拍、场景和正文，每层作者改完再往下，AI 产出采纳后才算数。RecurrentGPT 每步给几个下一段计划，人可选可自己写；ElyHa 的提案以「幽灵节点」出现，人工采纳。代表：[dramatron](https://github.com/google-deepmind/dramatron)、[RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT)、[wr-AI-ter](https://github.com/Think-42/wr-AI-ter)、[narralume](https://github.com/abligail/narralume)、[ElyHa](https://github.com/ShadowLoveElysia/ElyHa)
3. **读者选项分支**：每段正文后给 2–5 个选项，读者选完再续写。interactive-fiction-skill 每轮给 A–E 五个选项，也收自由输入；AI-Gamble 开局先生成整张故事结构图和多结局，再按选择逐段写；StoryWeaver-AI 在读者阅读时预生成后续分支。代表：[interactive-fiction-skill](https://github.com/Treasure-hub-agent/interactive-fiction-skill)、[AI-Gamble](https://github.com/xiamuceer-j/AI-Gamble)、[StoryWeaver-AI](https://github.com/1195214305/StoryWeaver-AI)、[cyoa](https://github.com/essencevc/cyoa)
4. **自由行动，代码裁定**：玩家用自然语言行动，模型只管叙述，骰子、数值、背包由规则引擎结算；模型要改状态，先过校验。ai-novel-studio 让模型只提交正文和状态补丁，服务端校验人物和场景的不变量后才提交。多见于 AI 跑团和文字冒险。代表：[NeverEndingQuest](https://github.com/MoonlightByte/NeverEndingQuest)、[loreweaver](https://github.com/1A7432/loreweaver)、[ai-novel-studio](https://github.com/weike-zhang/ai-novel-studio)、[yikes](https://github.com/psema4/yikes)
5. **轮流续写，手动注入**：用户和模型轮流写，作者用 Memory、Author's Note 和按关键词触发的世界书决定模型每轮看到什么。KoboldAI-Client 最早把三者做成一套，角色扮演前端大多沿用；Pathweaver 扩展读近期对话，给出最多 6 条走向供选。代表：[KoboldAI-Client](https://github.com/KoboldAI/KoboldAI-Client)、[SillyTavern](https://github.com/SillyTavern/SillyTavern)、[lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)、[SillyTavern-Pathweaver](https://github.com/mattjaybe/SillyTavern-Pathweaver)

**取舍和坑**

- 即时生成的分支容易走不到结局。gpt-text-adventure 开局先列 6 个剧情点，作者仍写明多数故事走不完。对策是给故事设终点：gpt-interactive-novel 定结局目标，The-Endless-Tale 按目标清单评估玩家行动。
- 判定交给模型，就没有真骰子。NeverEndingQuest 把骰子、背包、状态和时钟交给独立规则引擎；loreweaver 也说明，确定性部分有测试兜底，AI 主持人的表现是另一回事。
- 层级流程不合所有人。dramatron 团队承认自上而下的结构不符合每个作者的写法；研究中的剧作家嫌输出公式化，更愿意拿它搭世界、试换情节，而不是写完整剧本。
- 成本和延迟。多 agent 推演每回合要调用多次模型：Sonder_Engine 每个阶段单独调用，The-Endless-Tale 每轮约 40 秒。逐段候选也要多倍生成，arrows 靠 llama.cpp 并行批量生成抵消。

**从哪里开始**：[narralume](https://github.com/abligail/narralume) 适合写长篇的作者：AI 建议不因为生成了就进书，都先当候选；不接模型也能手写。[interactive-fiction-skill](https://github.com/Treasure-hub-agent/interactive-fiction-skill) 适合做中文选项式互动小说，装进 AI 助手即用，不用部署。[loreweaver](https://github.com/1A7432/loreweaver) 适合做跑团和文字冒险的开发者，规则、设定、角色都是可分享的文件，判定由代码完成。

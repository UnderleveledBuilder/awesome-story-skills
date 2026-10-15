**解决什么问题**：一个模型同时当作者和所有角色，角色就会提前知道秘密、为推剧情突然降智；配角需要时才出现，下场就不存在，世界像一块布景。角色模拟把「写」拆成「先演、后写」：每个角色单独决策，世界状态单独结算，最后才成文。

**常见做法**

1. **角色先演，导演再写**：每个角色一个 agent，带人设、记忆和信念，先各自给出行动或场景策略；导演或叙事者把多条视角线合成章节 spec，再交写手成文。novel-studio 让重要角色在至多 3 章的窗口内决策，世界仲裁者只裁决后果，不能改角色意图。代表：[hermes-novel-generator](https://github.com/rwcrosk-arch/hermes-novel-generator)、[fictionforge](https://github.com/wanqili857-byte/fictionforge)、[novel-studio](https://github.com/Xiaoyangy/novel-studio)、[CoDi](https://github.com/Speeditidious/CoDi)
2. **自下而上的世界沙盒**：沿用 Generative Agents 的思路，角色按「感知→计划→执行→反思」或按 tick 自主行动，系统只记事件，事后再从时间线里提取故事。多见于名著同人推演（红楼梦、西部世界）。代表：[OpenStory](https://github.com/ZJU-LLMs/OpenStory)、[StoryBox](https://github.com/amcghm/StoryBox)、[clawloom](https://github.com/Aaron-ou/clawloom)、[taleweave-ai](https://github.com/ssube/taleweave-ai)
3. **信息隔离**：客观事实、各角色感知、记忆和叙述分层存放，每个阶段单独调用模型。角色只拿到它合理能看到的信息，叙述者只写玩家可见的部分。gamentic 的角色不能直接改世界，只能向叙事者提出主张，由叙事者当轮裁定。代表：[Sonder_Engine](https://github.com/N0819/Sonder_Engine)、[project-lunar](https://github.com/horizonfps/project-lunar)、[gamentic](https://github.com/hec-ovi/gamentic)、[ai-murder-mystery](https://github.com/ScottishFold007/ai-murder-mystery)
4. **状态先结算，模型后叙述**：世界状态是唯一事实源，角色和玩家的行动都先变成状态变更、按规则结算，模型再把结果写成正文。payador 先让模型预测玩家输入引起的世界状态变换，再据新状态写叙事；world-walker 规定 Agent 只把引擎输出的 JSON 转成文字，不得编造数值。代表：[payador](https://github.com/pln-fing-udelar/payador)、[world-walker](https://github.com/badhope/world-walker)、[WorldForge](https://github.com/EidzokuxS/WorldForge)、[AaaliceTavern](https://github.com/WalkingMeatAxolotl/AaaliceTavern)
5. **写前局部推演**：不跑整个世界，只在关键场景前让角色演几轮或多路探索，挑合理的走向再写。代表：[creative-writing-skills](https://github.com/haowjy/creative-writing-skills)（规划阶段的角色模拟子代理）、[AnySpark](https://github.com/Mikexujunrui/AnySpark)（低成本多探索后判别选优）、[novel-distiller](https://github.com/FutureFuzzy/novel-distiller)（先为角色蒸馏思维 SKILL.md 再推演）、[open-skoob](https://github.com/OmMaBaMiHong/open-skoob)

**取舍和坑**

- 纯涌现容易散。没有目标的沙盒会原地打转，所以常再加一层自上而下的约束：ScrollWeaver 用事件链控制宏观走向；nest-drama 设必达和弹性剧情节点，要求经由世界内的因果抵达；StoryBox 把模拟结果交给叙事规划再组织成长篇。
- 成本随角色数上涨。WorldForge 认为每回合给每个人跑完整决策又慢又吵又贵，于是把 NPC 分成关键、常驻、临时三层，只让关键 NPC 完整决策；novel-studio 按事件激活角色，并限制每阶段的上下文。
- 规则锁太死会伤叙事。glyphkeeper 停更时作者自评：多 Agent 链路加事件溯源和物理仲裁「过度限制了 LLM 的叙事灵活性」，延迟也高。WorldForge 的折中是给叙述者一小份描写预算，只许加无害的表面细节。
- 隔离要落到上下文结构上。Sonder_Engine 规定真相、感知、记忆、信念和叙述不能合进同一个上下文；ai-murder-mystery 在角色回复后再加一道批评和修订，专防泄露秘密。
- 演出记录不是小说。逐轮记录是流水账，要再加工：fictionforge 合成章节 spec 时标出反转落点，CoDi 由 editor 改写成剧本或小说格式。

**从哪里开始**：[hermes-novel-generator](https://github.com/rwcrosk-arch/hermes-novel-generator) 适合先看懂流程：一个 SKILL.md 加五份 agent 提示词，角色互不可见地出策略，叙事者编织成文，角色再查声口。[novel-studio](https://github.com/Xiaoyangy/novel-studio) 是同一思路的完整长篇工程，带窗口推演、仲裁和台账。[Sonder_Engine](https://github.com/N0819/Sonder_Engine) 适合做互动小说的开发者，导演、感知、角色、叙述、提交各自独立，每一步都可重掷或手改。

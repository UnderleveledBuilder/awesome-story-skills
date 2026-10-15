**解决什么问题**：模型记不住自己编过的设定。写到后面，体系规则前后矛盾，人名地名漂移，已经写好的设定被它重新编一遍，还编错。全部设定塞进提示词又放不下。世界观方法把设定存在模型之外，用时按需取回；对状态要求严格的场景，干脆交给程序管。

**常见做法**

1. **关键词触发的世界书**：设定拆成条目，每条配触发词，近期对话或正文里出现触发词，才把条目插进上下文。这是角色扮演前端的基础设施，后来很多工具都能导入它的格式。代表：[SillyTavern](https://github.com/SillyTavern/SillyTavern)、[KoboldAI-Client](https://github.com/KoboldAI/KoboldAI-Client)、[Risuai](https://github.com/kwaroran/Risuai)、[Writingway](https://github.com/a-omukai/Writingway)（设定库按提及注入）
2. **结构化实体库，按场景取用**：人物、地点、势力、体系各存成带字段的文件或卡片，互相引用；写一段时按这段的时间线、地点和出场人物取对应条目。代表：[AIStoryBuilders](https://github.com/AIStoryBuilders/AIStoryBuilders)、[worldbuilder](https://github.com/gofastercloud/worldbuilder)（11 类实体用 Markdown+YAML 互引，图校验双向关系和时间线）、[NovelForge](https://github.com/RhythmicWave/NovelForge)、[vibe-writing](https://github.com/pakholeung37/vibe-writing)（双链 wiki，红链记待补设定）
3. **从正文反抽设定**：每章写完，让模型抽出新出现的人物、地点、关系和规则变化，写回设定库或知识图谱，下一章再取用。代表：[novelwriter](https://github.com/Hurricane0698/novelwriter)、[lore-weave](https://github.com/letuhao/lore-weave)、[AIxiezuo](https://github.com/yefeng2renxing/AIxiezuo)（主角境界、物品、关系存成逐章状态 JSON）、[novel-smith](https://github.com/huanweide/novel-smith)
4. **状态归引擎，模型只提议**：数值、物品、位置、人物身份这类硬事实由代码持有；模型输出指令或状态补丁，引擎校验通过才落地，每轮再把权威状态注入提示。互动小说和跑团里最常见。代表：[ai-novel-studio](https://github.com/weike-zhang/ai-novel-studio)（改角色名的补丁会被拒）、[StatefulLore](https://github.com/cgstever/StatefulLore)、[yumina-oss](https://github.com/lovetimo0421/yumina-oss)、[faramita-worlds](https://github.com/Nobeta-Work/faramita-worlds)（字段级增量和冲突检测）
5. **先定规则再展开**：从少数核心设定推后果，而不是先写百科。代表：[worldbuilding-skill](https://github.com/tahini2007/worldbuilding-skill)（核心偏离不超过 3 条，每条推七层后果链，再审叙事接口和"神秘预算"）、[DUNGEON_ARCHITECT](https://github.com/gloria-yin/DUNGEON_ARCHITECT)（副本表层与真相分开设计、预埋反转，再注入世界书）、[Narraverse-Engine](https://github.com/wssyh339/Narraverse-Engine)（多 agent 回合制议事推演世界规则，人工确认后入库）

**取舍和坑**

- **关键词匹配规模一大就漏**。[sillytavern-DeepLore](https://github.com/pixelnull/sillytavern-DeepLore) 的 README 说世界书在 80–100 条左右开始失灵：场景写的是背誓的后果，没人打出条目名，条目就不触发，模型转而自己编。它改成关键词加 BM25 粗筛、模型读条目摘要精选、再按时代地点角色门控，代价是每轮多一次模型调用。
- **设定越多越挤上下文**。注入要有预算。faramita-worlds 给每张世界书卡设激活规则、注入位置和预算；[bragi](https://github.com/wailers9/bragi) 只让当前时空节点保留全文，邻近节点留摘要；[WenShape](https://github.com/unitagain/WenShape) 按章节距离衰减事实。
- **自动抽取会把错的写进正史**。novelwriter 的抽取结果先当草稿，作者审核才入库；[Aventuras](https://github.com/AventurasTeam/Aventuras) 另用一个 agent 合并重复条目、补空缺。不审核，误读就会成为后文的依据。
- **设定会随时间变**。只存一份当前状态，回忆和倒叙容易穿帮。AIStoryBuilders 让人物和地点的描述按时间线分段，写哪段取哪段的版本。
- **不必先造百科**。worldbuilding-skill 把核心偏离限在 3 条以内；vibe-writing 用红链把没想好的设定先空着，写到再补。

**从哪里开始**：[novelwriter](https://github.com/Hurricane0698/novelwriter) 适合写长篇或续写已有作品，从正文抽设定、作者审核、按章注入，链条完整。[SillyTavern](https://github.com/SillyTavern/SillyTavern) 适合做角色扮演或互动故事，先学它的世界书，很多同类工具都能导入这种格式。[worldbuilding-skill](https://github.com/tahini2007/worldbuilding-skill) 适合动笔前把世界设计扎实，也能诊断现有设定为什么越写越难收束。

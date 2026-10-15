**解决什么问题**：不给人物建档，模型每章都在临场捏人：性格跟着剧情需要摇摆，几个角色的说话方式越写越像，角色还会用上自己不可能知道的信息。篇幅一长，这些小偏差会累积成 OOC 和人物趋同。

**常见做法**

1. **写前动机档案**：开写前用固定字段写清人物要什么、缺什么、怕什么，再拿去排大纲和节拍。字段多取自编剧理论，如 want/need 与致命缺陷、欲望/恐惧、Vogler 原型；短剧项目还会单独设计逐级升级的反派。代表：[NovelGenerator](https://github.com/Dylin-code/NovelGenerator)、[super-ai-scriptwriter](https://github.com/Doing-Tai-JI/super-ai-scriptwriter)、[claude-screenwriting](https://github.com/e06084/claude-screenwriting)、[short-drama](https://github.com/0xsline/short-drama)
2. **固定层与可变层分开**：人物卡分成只读的核心（价值观、外貌、口癖、创伤）和每章更新的状态（身份、能力、关系、资产）。写前读卡，写后只改可变层并与时间线互相校验，审稿时按核心层查 OOC。代表：[light-novel-creator](https://github.com/Nya-Nya-Hoshino/light-novel-creator)、[ai-story-forge](https://github.com/nwiizo/ai-story-forge)、[web-novel-writing-skill](https://github.com/XINGANLIU/web-novel-writing-skill)
3. **声口卡**：单独记录每个角色怎么说话：语气、句尾、用词习惯、受压时的防御方式、非语言动作。写对白时注入，每章审稿再逐个角色对照。代表：[awesome-novel-studio](https://github.com/MJbae/awesome-novel-studio)、[filmgame](https://github.com/mmlong818/filmgame)、[novel-novel-generator](https://github.com/mike-cramblett/novel-novel-generator)、[Serendipity-Engine](https://github.com/IsaiahN/Serendipity-Engine)
4. **角色即 agent**：每个重要角色是一次独立调用，只拿到自己看见、记得的信息，先决定自己要做什么，再由叙事者或导演合成正文。互动叙事和角色扮演里最常见。代表：[nest-drama](https://github.com/63435212cwu-ops/nest-drama)、[gamentic](https://github.com/hec-ovi/gamentic)、[Inner-Self](https://github.com/LewdLeah/Inner-Self)、[AI4VisualNovel](https://github.com/ttsmallHot/AI4VisualNovel)
5. **从文本反推人物**：输入小说、草稿、聊天记录或公开资料，抽取人设、口吻和行为模式，生成角色卡或角色专用的 SKILL.md，同人和续写里常用。抽取时保留原文出处，方便作者逐条核对。代表：[character-card-fiction-workflow-skill](https://github.com/shigehaomingzi1/character-card-fiction-workflow-skill)、[novel-distiller](https://github.com/FutureFuzzy/novel-distiller)、[soul-killer](https://github.com/Xeonice/soul-killer)

**取舍和坑**

- **先定好锁多少**：核心层全锁，人物没有弧光；什么都能改，人设就会漂。light-novel-creator 只开放 8 个动态字段每章更新，其余只读；ai-story-forge 在不变核心和可变层之间多设一个"准稳定层"，允许在一定范围内变化。
- **声口会随篇幅趋同**：awesome-novel-studio 把"人物深度塌缩"列为长篇的三堵墙之一，对策是设计期写语气表、每集按 VOICE 轴复查。开篇写一次人设不够。
- **"谁知道什么"要单独记**：角色提前知道答案，是和性格无关的另一类穿帮。kunka-screenwriting-master 有专门核对人物知情的技能，Smart-Memory 给群聊里每个角色存独立的记忆和秘密，project-lunar 的 NPC 只知道亲眼见过的事。
- **角色自主不等于成戏**：nest-drama 把必达和弹性剧情节点当作引力场，让剧情经世界内的因果收敛，另设监督者判断"一个人会不会这么做"；gamentic 只允许角色向叙事者申请改动世界状态。
- **别让模型单独评人设**：character-card-skills 的盲评实验里，LLM 评审彼此一致率 86%，分辨人写和 AI 写的正确率只有 12%，它们把细节密度和状态栏当成人写的证据。卡写得好不好，要靠真人读，或靠写成规则的检查。

**从哪里开始**：

- [awesome-novel-studio](https://github.com/MJbae/awesome-novel-studio)：适合写连载长篇的作者，角色卡带语气表，每集写前自动汇总前两集的时间线、伏笔和角色状态，装成 Claude Code 插件即可用。
- [nest-drama](https://github.com/63435212cwu-ops/nest-drama)：适合想试"让角色自己演"的人，纯 Python 标准库本地运行，导入已有设定就能看到角色三卡和信息隔离怎么工作。
- [character-card-skills](https://github.com/foreverse-app/character-card-skills)：适合写角色扮演卡的人，含开场范式、lorebook 写法和确定性 AI 味检测器，产出的卡可导入 SillyTavern。

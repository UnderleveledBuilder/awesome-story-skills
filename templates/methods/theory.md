**解决什么问题**：模型读过大量写作术语，但默认写出的是"平均故事"：冲突没有代价，场景不转折，结尾靠主角成长和释怀收束。让它"写得像某种类型"，往往只得到堆砌的口头禅和似曾相识的桥段。理论注入把编剧书、类型套路和平台规则拆成模型能照做的步骤、能逐条核对的标准。

**常见做法**

1. **结构模型当骨架**：先选一种结构（三幕、英雄之旅、救猫咪、起承转合、七点），把篇幅分到各节拍（Crucible 按全书百分比分六个乐章），再按节拍写章或场景。代表：[storyteller](https://github.com/johannhartmann/storyteller)（六种结构自动选型）、[The-Crucible-Writing-System-For-Claude](https://github.com/forsonny/The-Crucible-Writing-System-For-Claude)（自创 36 拍、三线交织）、[NovelForger](https://github.com/cedrusdang/NovelForger)、[shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master)
2. **编剧书蒸馏成按需加载的知识库**：把一本或几十本书拆成主题 skill 或知识条目，按请求的意图、媒介、阶段只加载相关部分，不让整套理论挤占上下文。代表：[screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)（47 本编剧书加 23 卷剧本）、[how-to-make-script](https://github.com/XucroYuri/how-to-make-script)、[gushi-skill](https://github.com/pipivv/gushi-skill)、[story-foundry](https://github.com/mmunro3318/story-foundry)
3. **类型套路参数化**：网文和短剧最常见。按题材、频道、平台加载模板，把爽点、钩子、付费卡点写成配比和位置要求，写完逐集打标统计密度。代表：[short-drama](https://github.com/0xsline/short-drama)（13 种题材模板、五种钩子、10–15% 的集数设付费卡点）、[400-duanju-shuangdian](https://github.com/icooldp/400-duanju-shuangdian)、[chinese-webnovel-skills](https://github.com/tance-mang/chinese-webnovel-skills)、[salt-story](https://github.com/yfge/salt-story)
4. **因果单元做写作原语**：不论整体用什么结构，每个事件或节拍都按固定格式填，比如"因→事→果→决""目标→行动→反作用→代价→状态变化""所以/但是"，写作时把这条链注入上下文。代表：[dramatica-flow](https://github.com/ydsgangge-ux/dramatica-flow)、[super-ai-scriptwriter](https://github.com/Doing-Tai-JI/super-ai-scriptwriter)、[writers-room-story-engine](https://github.com/jackterror/writers-room-story-engine)、[stephen-chow-skill](https://github.com/chnjames/stephen-chow-skill)（喜剧拆成欲望、规则、地位和升级链）
5. **理论做诊断量表**：写完用理论派生的清单审稿，先定位问题再定点修。代表：[claude-screenwriting](https://github.com/e06084/claude-screenwriting)（结构诊断）、[thriller](https://github.com/pajama-studio/thriller)（线索公平性、诺克斯检查）、[sepia](https://github.com/Nanako0129/sepia)（按 StoryScope 论文测出的 AI 小说结构特征分三遍修）

**取舍和坑**

- **套路叠满就是公式**。大家用同一套节拍表和爽点表，产出会撞车。[ty-xiaoshuo-skill](https://github.com/danieltao118/ty-xiaoshuo-skill) 规定连续两章同一情节类型，第三章必须换；[story-maker](https://github.com/FURUYAN1234/story-maker) 对主题、类型、结局等多个轴随机组合来避开俗套。
- **因果太整齐反而像 AI**。sepia 引用的研究把单线、因果工整、主题由叙述者点明、结局靠主角成长收束列为 AI 小说的结构特征，它第一遍就是松开因果链、把揭示后置。这和"每个事件必须有因有果"的做法有张力：因果链防散，写完还要查是不是工整到只剩一条线。
- **套路库容易滑向复刻**。[douyin-tiktok-story-skill-agent](https://github.com/liujunxibaba/douyin-tiktok-story-skill-agent) 要求至少重组三类机制并跑相似度检查；stephen-chow-skill 只抽象机制、不收台词，成稿前做近似文本检查。
- **小说理论不能直接套剧本**。[write-screenplay-skill](https://github.com/egguy886/write-screenplay-skill) 先剥掉心理描写，把情绪外化成可拍的动作；[qianqianwriting](https://github.com/catyiqian/qianqianwriting) 按 30–60 秒或 1–3 分钟的单集时长重新分配救猫咪节拍。
- **来源要自己核对**。不少知识库蒸馏自单本书、课程笔记或圈内流传的汇编，[hongguo-shortdrama-screenwriting](https://github.com/zhu5859243-free/hongguo-shortdrama-screenwriting) 的方法论来源只有作者自述。模块多不等于有效，最好拿同一章做加载前后的对比。

**从哪里开始**：[screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) 适合写电影或剧集，素材覆盖中美英日韩剧作，按任务自动触发对应 skill。[how-to-make-script](https://github.com/XucroYuri/how-to-make-script) 适合想自己搭理论知识库的开发者，看它怎样按请求路由、限量加载、按量表自检。[short-drama](https://github.com/0xsline/short-drama) 适合写竖屏短剧，题材、钩子、节奏曲线、付费卡点都已参数化，上手直接。

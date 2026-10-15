**解决什么问题**：把新闻、访谈、字幕或论文交给模型讲成故事，它会顺手补上材料里没有的引语、数字和因果。"写得像小说"要场景、对白、感官细节和人物内心，真实材料里很少有，模型就用看起来合理的内容去填，读者分不出哪句是真的。事实约束把"讲得好"和"讲得对"分开：先定哪些内容能用，再定怎么讲，写完逐条对回原材料。

**常见做法**

1. **先建账，再定结构**：动笔前把材料拆成带出处的条目，叙事方向在账本之后才定，正文只用账本里的条目。aletheia 的 evidence-ledger.json 把主张、引文、人物和原声逐项绑定来源；startup-llm-content-pipeline 先让 Gemini 抽成结构化 JSON，Claude 只按它写，缺的写 Not mentioned。代表：[aletheia](https://github.com/mycyg/aletheia)、[daily-bookcast](https://github.com/GODGOD126/daily-bookcast)、[lawyer-short-video-skill](https://github.com/axing0916/lawyer-short-video-skill)、[startup-llm-content-pipeline](https://github.com/biswajyoti-nath/startup-llm-content-pipeline)
2. **从证据里找冲突**：张力从材料的矛盾和缺口里挖，不靠编。XinZhongZhiCheng-skills 从人物自述与行动对不上的地方立题，每个解释要两条证据、一条反证和一个替代解释；doodle-explainer-video 要求选题同时有可核实的反常事实、错误的直觉解释和真实机制，缺一样结尾就立不住。代表：[good-story](https://github.com/Rimagination/good-story)、[XinZhongZhiCheng-skills](https://github.com/startuo/XinZhongZhiCheng-skills)、[doodle-explainer-video](https://github.com/sadekxD/doodle-explainer-video)、[simon-skills](https://github.com/trustfuture/simon-skills)
3. **事实分级**：材料按可信度分层，推断要归属或标明不确定。cinematic-confessional-writing 分已知事实、当事人陈述、第三方说法和未核实信息；yang-jiang-restrained-narrative-skill 分亲见、转述、推测；yingxue-writing 先选事实模式，来源约束、个人回忆、明示虚构三种规则不同。代表：[cinematic-confessional-writing](https://github.com/5ysy/cinematic-confessional-writing)、[yang-jiang-restrained-narrative-skill](https://github.com/constantin2088/yang-jiang-restrained-narrative-skill)、[xigua-msvideo-skill](https://github.com/124zhe/xigua-msvideo-skill)、[yingxue-writing](https://github.com/Jujie-YANG/yingxue-writing)
4. **逐句溯源，写完对源**：句子和数字带出处，写完由脚本或独立审稿对回原材料。data2story-skill 生成 viewer.html，点任意一句能看到背后的数据、代码或引文；AutoYY 的写手只能交 candidate 稿，过了素材直接引用数、数字有据、锚点覆盖率等闸门才转正；ai-director-video-commentary 把解说对 ASR 时间戳校验，推断标低置信待审。代表：[data2story-skill](https://github.com/QinghongLin/data2story-skill)、[AutoYY](https://github.com/DaBaoAgent/AutoYY)、[ai-director-video-commentary](https://github.com/fqyy360t/ai-director-video-commentary)、[voice-film](https://github.com/artkruglov/voice-film)
5. **访谈取材，本人确认**：人生故事先采访，事实由本人认定。lifetrace 把候选记忆的原话、时间、来源和私密范围给本人看，确认后才写入 JSON 档案，草稿引用条目 ID；memoir-product 只做去赘词、顺语序、断句三层整理，AI 补的内容标「[AI补充]」；Writingbook-AgenticWorkflow 做 12 轮访谈后写故事圣经，审稿时做 CoVe 事实核查。代表：[lifetrace](https://github.com/wudixiaoshuaibi/lifetrace)、[memoir-product](https://github.com/VelVet8418/memoir-product)、[Writingbook-AgenticWorkflow](https://github.com/idoforgod/Writingbook-AgenticWorkflow)、[wedding-video-guided-wizard](https://github.com/aaronyi97/wedding-video-guided-wizard)

**取舍和坑**

- **故事越圆，越容易挑证据**。good-story 引 Nature Methods：追求完美叙事会诱导挑证据、藏起不确定性，所以它选最强但不越界的讲法，不选最戏剧化的。lawyer-short-video-skill 规定没有真实结果就不造逆转。
- **文风技法会索要材料里没有的东西**。孙学一类写法讲数字精确、旁观者证词。[justin-sun-skill](https://github.com/Leon-Drq/justin-sun-skill) 信息不全时保留模糊或追问，不为文风补造数字和旁观者；[jingtian-style](https://github.com/anhao/jingtian-style) 素材不够就写短帖："合租就写合租，不要为了像而发明五千万。"
- **能虚构多少，各家划线不同**。[agent-saga](https://github.com/bbismm/agent-saga) 事件全真，只放开叙述者的内心和事件里的小质感；[persona-story-skill](https://github.com/Dragocytus/persona-story-skill) 只禁编核心冲突，允许补行业常识细节；wedding-video-guided-wizard 许演绎、不许虚构经历，还防着把示例剧情套给每对新人。这条线要先写明。
- **润色会把错带回来**。AutoYY 先去 AI 味再核事实，并记录稿件哈希，稿子一变就重过闸门；[deepwrite](https://github.com/willyzengg-pixel/deepwrite) 只要修正过内容就重审。
- **访谈也会改写记忆**。memoir-product 把"AI 追问可能植入暗示，让老人混淆 AI 提示与自己的记忆"列为核心风险，对策是只追问已说过的内容，说法有出入不替本人裁定。

**从哪里开始**：[aletheia](https://github.com/mycyg/aletheia) 适合把文章、论文做成纪录片，examples 里的最小工程能直接看证据账本怎么写。[data2story-skill](https://github.com/QinghongLin/data2story-skill) 适合从数据集出发的开发者，七个角色的流水线和逐句证据查看器有论文配套。[lifetrace](https://github.com/wudixiaoshuaibi/lifetrace) 适合做回忆录和传记，流程就是访谈、本人确认、入档、按条目写作。

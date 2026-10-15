# 参与贡献

## 收录标准

满足以下全部条件：

1. **用大模型讲故事**：故事的主体由大模型生成，项目提供的是创作方法、原则或流程。小说、网文、短篇、剧本、短剧、互动小说、跑团、视觉小说、角色扮演、同人、仿写，各种类型都收。只服务写作周边的工具不收，比如下载、书源、发布、翻译、通用润色、分镜和视频生成、阅读器。
   - **非虚构叙事也收**：把给定的真实素材（新闻、事件、科研、历史人物、产品经历）写成故事，包括特稿、事件复盘、科普、传记、口播和解说文案、品牌故事。要求两点：有讲故事的方法（结构、场景、悬念、人物），并且约束模型只用给定的事实、不编造。只套标题公式、营销模板，或者通用改写润色的不收。
2. **有方法**：能看出设计了创作方法，比如大纲先行、分章写作、设定库和记忆、角色档案、多 agent 分工、审稿循环、文风学习。只把一句话丢给模型返回一篇故事的套壳不收。
3. **形态不限**：标准 `SKILL.md`、agent 插件、提示词 / 方法文档、agent 框架、命令行工具、桌面或网页应用、论文配套代码都收，没有星数门槛。只有论文、没有代码的不收，见[相关资源](README.md#resources)里的论文列表。
4. **有说明**：README 写清楚做什么；标准 SKILL.md 目录结构视为可以直接安装。
5. **能复用**：只为某一个人或某一部作品写死、换个题材就用不上的不收。
6. **有源码**：只给 exe / 安装包、仓库里没有源码的不收；照搬别人项目再塞安装包的不收。

不要求近期更新：这个列表想收齐所有探索，停更的老项目也收，超过 180 天没有更新的会标 💤。

fork 和改名换皮的不收。在原版基础上加了新的方法、模块或功能的派生版可以收，条目说明里会注明上游。

## 怎么提交

**不想动代码**：[提交 issue](../../issues/new?template=submit-skill.yml)，填仓库地址和推荐理由即可。

**直接发 PR**：

1. 在 `data/skills.toml` 对应类型的分组下追加一条（字段见下文）。
2. 本地运行（需要 Python 3.11+，无第三方依赖）：

   ```bash
   python3 scripts/refresh.py --only owner/repo   # 抓取星数、许可证等元数据
   python3 scripts/build.py                       # 重新生成 README.md
   ```

   跳过这一步也可以，合并后 GitHub Actions 会自动刷新并生成。
3. 提交 PR。CI 会校验数据格式。

## 字段说明

```toml
[[skills]]
repo    = "owner/repo"                 # 必填，GitHub 仓库
desc    = "一句话说清做什么、怎么做"        # 必填，≤ 80 字，写具体方法，少用形容词
group   = "novel"                      # 必填，故事类型，取值见 data/taxonomy.toml [groups]
methods = ["planning", "memory"]       # 必填，用到的创作方法，见 [methods]
format  = "skill"                      # 必填，skill / prompts / harness / app / research
lang    = "zh"                         # 必填，zh / en / ja / multi（项目正文的语言）
agents  = ["claude-code"]              # 可选，仓库明确说明支持的 agent，见 [agents]
install = "npx skills add ..."         # 可选，skill 默认生成 npx skills add owner/repo
name    = "显示名"                      # 可选，默认取仓库名
tier    = "featured"                   # 可选，精选；默认 listed
note    = "需要注意的地方"                # 可选，显示在简介下方
checked = 2026-10-15                   # 可选，人工核对日期（TOML 日期，不加引号）
```

`agents` 只填仓库里明确写了的，不要推测。星数、许可证、最近更新时间、skill 数量由 `scripts/refresh.py` 自动抓取，不用手填。

## 收录徽章

项目被收录后，可以在自己的 README 里加上收录徽章，代码见 [README 的「收录徽章」一节](README.md#badge)。

## 不收录的项目

看过但决定不收的项目记在 `data/ignore.toml`，并写明原因，这样 `discover.py` 不会再把它们列为候选。

## 维护者工作流

| 脚本 | 作用 |
|---|---|
| `scripts/refresh.py` | 刷新元数据，报告改名、失效、归档、久未更新的仓库 |
| `scripts/build.py` | 生成 README.md；`--check` 检查是否最新，`--validate` 只校验数据 |
| `scripts/discover.py` | 按 taxonomy.toml 里的关键词搜候选项目，输出待审清单 |

GitHub Actions 每周一自动刷新元数据、重新生成 README，并把新候选开成 issue。

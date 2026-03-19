# AGENTS.md

## Mission
使用 Codex 驱动公开数据获取、仿真、分析与 SCI 论文草稿生成的半自动流程。
优先级顺序：可追溯 > 可复现 > 审慎解释 > 产出速度。
宁可结论更弱，也不要证据不足。

## Non-negotiable rules
1. 仅使用许可清晰的公开数据。记录来源 URL、访问日期、版本、许可与校验值。
2. `02_public_data/raw/` 禁止修改、覆盖或删除。原始数据只进不改。
3. 所有清洗、分析、仿真、作图、制表必须脚本化；禁止手工改 Excel、截图改图或仅靠 GUI 操作。
4. 每个结果都必须能回溯到：输入快照、脚本、配置、随机种子、依赖环境与 commit hash。
5. 禁止伪造或补写：数据、文献、DOI、实验设置、结果、显著性或任何超出证据的表述。
6. 必须明确区分：观测结果、仿真结果、假设、解释与猜测。
7. 影响解释的失败运行、空结果、排除规则与敏感性失败必须保留并报告。
8. 证据不足时，降级表述或停止；不得“写过头”。

## Directory responsibilities
| 路径 | 职责 |
| --- | --- |
| `00_scope/` | 研究问题、假设、数据计划、仿真计划、分析计划、允许声明与风险登记 |
| `01_literature/` | 文献管理：`notes/` 阅读笔记、`screening/` 筛选记录、`novelty_map/` 新颖性映射 |
| `02_public_data/raw/` | 外部公开原始数据与元数据；只读，禁止修改、覆盖或删除 |
| `02_public_data/processed/` | 脚本生成的分析输入；不得手工编辑 |
| `02_public_data/provenance/` | 数据来源追溯信息（URL、访问日期、版本、许可、校验值） |
| `02_public_data/licenses/` | 数据集许可文件存档 |
| `03_simulation/configs/` | 仿真配置；包含种子、参数、阈值 |
| `03_simulation/src/` | 仿真可复用代码；不放临时结果 |
| `03_simulation/runs/` | 仿真运行输出与运行清单 |
| `03_simulation/sensitivity/` | 敏感性分析与参数扫描结果 |
| `03_simulation/verification/` | 仿真验证报告与校验记录 |
| `04_analysis/notebooks/` | 分析用 Notebook |
| `04_analysis/figures/` | 脚本生成的图；不存手工改图 |
| `04_analysis/tables/` | 脚本生成的表；不存手工结论 |
| `05_manuscript/` | 论文正文（`main.md`）、大纲（`outline.md`）、参考文献（`refs/`）、投稿信（`cover_letter/`） |
| `06_review/` | 自审报告：致命问题（`fatal_issues.md`）、期刊匹配（`journal_fit.md`）、可复现性（`reproducibility.md`） |
| `99_archive/` | 已废弃或归档的历史文件 |

## Allowed vs forbidden claims
**Allowed**
- “在数据集 X、筛选规则 Y 下，观察到 A 与 B 存在相关/差异。”
- “在假设 H、参数范围 P、种子集合 S 下，仿真显示方法 M 在指标 K 上优于基线 B。”
- “该结果仅适用于当前数据、当前假设与当前评估协议。”
- “该结论对某些种子、参数或子样本敏感。”

**Forbidden**
- “证明了”“因果成立”“普适有效”“真实世界一定有效”。
- 未经完整基准比较就声称 “state-of-the-art”“最优”“领先”。
- 未给出检验方法、阈值与多重比较处理就声称“显著”。
- 未经外部验证就声称“可部署”“可临床/政策使用”“具备工程落地价值”。
- 未经可核查文献检索就声称“首次”“首个”“填补空白”。

## Required workflow order
1. 先写明研究问题、主要指标、比较对象与结论上限。
2. 登记数据源、许可、纳入/排除规则；下载到 `02_public_data/raw/`，许可存入 `02_public_data/licenses/`，来源信息存入 `02_public_data/provenance/`。
3. 固定环境、依赖、配置与随机种子。
4. 由脚本生成 `02_public_data/processed/`，并输出数据血缘信息。
5. 先跑基础统计与 sanity checks，再进入正式分析。
6. 实现并运行仿真；显式记录假设、参数范围与终止条件。
7. 进行重复种子、敏感性、消融或基线对照验证。
8. 由脚本生成 `04_analysis/figures/`、`04_analysis/tables/` 中的表图与摘要指标。
9. 先写 `05_manuscript/claim_map.md`，再写论文正文（`05_manuscript/main.md`）；正文只引用已验证结果。
10. 人工复核通过后，才允许合并或投稿。

## Validation and reporting requirements
1. 每次运行都必须输出 `03_simulation/runs/<run_id>/manifest.json`，至少包含：命令、commit hash、配置文件、种子、环境锁定文件、输入校验值与输出文件列表。
2. 关键结果必须能在干净环境中用单条命令复现。
3. 每个表和图都必须标注来源脚本、输入版本与结果 ID。
4. 正文中的每个数字都必须能在 `03_simulation/runs/` 或 `04_analysis/` 中定位到对应源文件与结果 ID。
5. 报告必须包含：样本量、排除规则、缺失情况、指标定义、基线、运行次数/种子数、不确定性区间，以及结果属于观测还是仿真。
6. 必须单独写明 limitations、threats to validity 与未解决不确定性。
7. 校验失败时必须产出失败报告；禁止静默重跑后仅保留“最好看”的结果。

## Stop conditions
出现以下任一情况时，立即停止新增结论与正文扩写，只记录 blocker：
- 数据许可、来源或版本不清晰。
- 原始数据缺少校验值，或处理结果无法回溯到原始输入。
- 基础 sanity checks 失败，存在泄漏、污染、重复计数或明显异常。
- 仿真不收敛，或结果对合理的种子/参数扰动高度不稳定。
- 关键结果无法在干净环境中复现。
- 结论需要依赖未验证文献、未生成结果或人工补写数字。
- 有人要求隐藏负结果、弱化限制或强化未经支持的表述。

触发停止条件后，在 `06_review/` 中记录原因、影响范围与建议下一步；不得自动继续推进。

## Required context files
Before any implementation, read:
- 00_factory/CLAIM_BOUNDARY.md
- 00_factory/REVIEW_CHECKLIST.md
- 00_scope/RESEARCH_QUESTION.md
- 00_scope/HYPOTHESIS.md
- 00_scope/DATA_PLAN.md
- 00_scope/SIMULATION_PLAN.md
- 00_scope/ANALYSIS_PLAN.md
- 00_scope/CLAIMS_ALLOWED.md

Use these files as the source of truth for:
- evidence boundaries
- allowed claims
- workflow order
- review criteria

Use 00_factory/JOURNAL_MAP.yaml only for journal selection and manuscript-targeting tasks.
Use 00_factory/TOPIC_SCORECARD.md only when evaluating new topic ideas or scope changes.
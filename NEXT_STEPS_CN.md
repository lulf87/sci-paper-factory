# 推进清单：主控 / 单篇， 本地 / GPT 网页端

本文将推进工作拆成四条线：

- 本地 — 主控
- GPT 网页端 — 主控项目 `SCI_Paper_Factory_Control`
- 本地 — 单篇项目
- GPT 网页端 — 单篇项目 `2026_Paper_01_PublicData_Simulation`

## 总原则

**主控层只负责门禁、审查、收窄和派单。  
单篇层只负责这一篇论文的具体执行。**

这与你仓库里的总控职责一致：先筛选方向，再立项，再冻结协议，再允许编码与写作；并且不混稿，先完成一篇样板 paper。  
单篇项目的执行顺序也已经在 `AGENTS.md` 中固定：研究问题与终点 → provenance → processed data → sanity checks → simulation → sensitivity → figures/tables → `claim_map` → manuscript。

---

# 1）本地 — 主控

## 角色

本地主控只维护工厂级规则和阶段状态。  
不要进入单篇论文的具体研究结论。

## 本周清单

### P0：把主控变成真正的 gate 系统
- [ ] 建一个**总控状态看板**
  - active paper
  - 当前阶段
  - blocker
  - 是否允许进入下一阶段
  - 下一步最小任务
- [ ] 建一个**阶段门禁表**
  - scope frozen
  - data frozen
  - simulation frozen
  - verification passed
  - first formal run finished
  - claim review passed
  - manuscript review passed
- [ ] 建一个**风险关闭表**
  - 风险编号
  - 当前状态
  - 关闭证据
  - 关闭日期
- [ ] 建一个**claim ledger 模板**
  - claim_id
  - 章节
  - 原句
  - 类型（E/I/H/X）
  - 证据路径
  - 动作

### P1：把工厂文档串起来
- [ ] 在 `00_factory/` 下增加一个**主控入口说明**
  - 各文件作用
  - 何时使用
  - 哪些只给主控看
  - 哪些只给单篇项目看
- [ ] 补一个**根目录 README**
  - 仓库结构
  - 主控与单篇项目的关系
  - 推荐推进顺序
- [ ] 固定一套**命名规则**
  - 论文目录命名
  - run_id 命名
  - figure/table 命名
  - 审查文件命名

## 完成标志
你打开本地仓库，不看聊天，也知道：
- 现在哪篇在推进
- 推到了哪一关
- 哪些风险没关
- 下一步只该做什么

## 现在不要做
- [ ] 再扩工厂新概念
- [ ] 再开第二篇样板 paper
- [ ] 先做投稿格式细修

---

# 2）GPT 网页端 — 主控项目 `SCI_Paper_Factory_Control`

## 角色

这个项目只做四件事：

1. 阶段门禁
2. 风险复核
3. claim 审查
4. 任务派发

不要在这里沉淀单篇论文的具体研究细节。

## 项目内清单

### P0：把主控项目收紧成 gatekeeper
- [ ] 把项目说明固定为：
  - 不混稿
  - 不补故事
  - 只做 gate / review / tasking
  - 先样板，后复制
- [ ] 不再把单篇项目的大量原始上下文长期堆在这里
- [ ] 每次只输入：
  - 当前阶段
  - 已产出物
  - blocker
  - 风险项
  - 候选下一步

### P0：固定 4 个长期线程
- [ ] `线程1：阶段门禁`
- [ ] `线程2：风险复核`
- [ ] `线程3：claim 边界审查`
- [ ] `线程4：任务拆解与派单`

### P1：固定每次提问模板

```text
当前项目：
当前阶段：
Inputs Used：
Artifacts Produced：
Open Risks：
Blockers：
Candidate Next Actions：
请只输出：
1. 是否允许进入下一阶段
2. 必须先关闭的 blocker
3. 下一步最小任务单
```

## 主控项目的使用方式

### 该让它做
- [ ] 判断单篇项目是否可以过 gate
- [ ] 检查输出有没有越界
- [ ] 把下一步压缩成最小任务单
- [ ] 审核某一轮结果是否足以开始写正文
- [ ] 审核某一版摘要/结论是否越界

### 不该让它做
- [ ] 帮你补没跑出来的结果
- [ ] 帮你“把故事讲完整”
- [ ] 代替单篇项目保存研究上下文
- [ ] 同时混入两篇论文的具体内容

## 完成标志
你把一轮产物丢给它，它只会回答：
- 过 / 不过
- 先修什么
- 下一步干什么

---

# 3）本地 — 单篇项目

这条线最重要。

本地单篇项目的执行，严格按 `AGENTS.md` 的目录和顺序推进：
- `02_public_data/raw/`
- `provenance/`
- `licenses/`
- `03_simulation/configs/`
- `runs/`
- `verification/`
- `04_analysis/figures/`
- `tables/`
- `05_manuscript/`
- `06_review/`

## A. 数据与环境冻结

### 本周必须完成
- [ ] 把 KiTS23 放进 `02_public_data/raw/`
- [ ] 在 `02_public_data/provenance/` 记录：
  - 数据来源
  - 下载日期
  - 版本信息
  - 校验信息
- [ ] 在 `02_public_data/licenses/` 保存许可文件
- [ ] 固定环境文件
  - `requirements.txt` / `environment.yml`
  - Python 版本
  - 关键依赖版本
- [ ] 固定随机种子与基础配置
- [ ] 建一个**单命令入口**
  - 例如 `make first-formal-run`
  - 或 `bash run_first_formal.sh`

### 完成标志
任何人拿到项目，都知道：
- 数据从哪来
- 用的是什么版本
- 环境怎么装
- 从哪条命令开始跑

---

## B. 预处理闭环

### 必须完成
- [ ] 读取 KiTS23 原始影像和 truth masks
- [ ] 做空间一致性检查
- [ ] 做 mask 完整性检查
- [ ] 做 3D 连通域拆分
- [ ] 固定 `d_max` 算法
- [ ] 固定纳入 / 排除逻辑
- [ ] 固定 `cystic_interference` 规则
- [ ] 输出这些表：
  - `planning_instance_table`
  - `exclusion_log`
  - `subgroup_labels`
  - `roi_metadata`

### 完成标志
你已经能稳定回答：
- 有多少 eligible planning instances
- 哪些被排除
- 为什么被排除
- 哪些进 `≤3 cm`
- 哪些进 `3–4 cm`

---

## C. 仿真冻结

### 必须完成
- [ ] 冻结 surrogate library 的**numeric parameter table**
- [ ] 冻结搜索分辨率
- [ ] 冻结 ROI 边界 / 裁剪规则
- [ ] 冻结 primary solution 的 tie-break 规则
- [ ] 冻结 formal run 配置文件
- [ ] 把这些记录到 `03_simulation/configs/`

### 完成标志
你不会在看完结果后再改 library、分辨率或边界

---

## D. 验证闭环

### 必须完成
- [ ] geometry unit tests
  - volume calculation
  - boolean ops
  - involved fraction
  - signed margin
- [ ] synthetic sanity checks
  - sphere / ellipsoid
  - coverage 判定
  - margin 正负
  - objective 优化方向
- [ ] KiTS23 可视化抽检
  - 随机抽若干 case
  - 看 surrogate 是否覆盖 tumor
  - 看 involved parenchyma 是否合理
- [ ] deterministic rerun
  - 同配置重复跑
  - 输出一致

### 产物位置
- [ ] `03_simulation/verification/`
- [ ] `tests/`
- [ ] 抽检截图或审查记录

### 完成标志
你能明确说：不是“跑出来了”，而是“计算逻辑被验证过了”

---

## E. 第一轮 formal run

### 只做 prespecified 内容
- [ ] feasible complete-coverage rate
- [ ] `primary_involved_fraction`
- [ ] `best_signed_margin / margin deficit`
- [ ] `≤3 cm` vs `3–4 cm` subgroup comparison

### 本轮必须输出
- [ ] `03_simulation/runs/<run_id>/manifest.json`
- [ ] 主结果表
- [ ] 主结果图
- [ ] 失败 / 空结果记录
- [ ] 运行日志

### 完成标志
你已经有第一轮正式结果  
但还没有开始扩写摘要和结论

---

## F. 最小稳健性检查

### 必须完成
- [ ] 分辨率轻扰动
- [ ] surrogate library 轻扰动
- [ ] ROI 边界轻扰动

### 目的
只回答一个问题：

> 主结论会不会因为轻微数值细节变化而翻转？

### 完成标志
你知道哪些结果稳，哪些结果只能降级表述

---

## G. 写作绑定

### 在结果后做
- [ ] 建 `05_manuscript/claim_map.md`
- [ ] 先写 `outline.md`
- [ ] 再写 `main.md`
- [ ] 写 `06_review/fatal_issues.md`
- [ ] 写 `06_review/reproducibility.md`
- [ ] 写 `06_review/journal_fit.md`

### 顺序
- [ ] 先 claim ledger
- [ ] 再 outline
- [ ] 再正文
- [ ] 最后期刊适配

### 完成标志
正文中的每个关键数字，都能追溯到 run 或 analysis 产物

---

## 本地单篇项目现在不要做
- [ ] 多针、多次 pull-back
- [ ] 真实器械品牌映射
- [ ] 真实功率 / 时间推荐
- [ ] 真实肾功能获益叙事
- [ ] 提前做目标期刊的格式修饰

---

# 4）GPT 网页端 — 单篇项目 `2026_Paper_01_PublicData_Simulation`

## 角色

这个项目只服务**这一篇**论文。

它的作用是：
- 协议内审
- 产物审查
- claim ledger
- manuscript drafting
- review support

不要把别的论文内容放进来。

## 项目内清单

### P0：固定项目边界
- [ ] 项目说明只保留这一篇的：
  - research question
  - hypothesis
  - data plan
  - simulation plan
  - analysis plan
  - claims allowed
- [ ] 明确写：
  - 不得补数
  - 不得补文献
  - 不得混入别的 paper context
  - 不得越界到真实临床结论

---

## 固定 5 个线程
- [ ] `线程1：00_scope 与 protocol freeze`
- [ ] `线程2：preprocessing 与 exclusion audit`
- [ ] `线程3：simulation + verification`
- [ ] `线程4：results + claim ledger`
- [ ] `线程5：manuscript + review`

---

## 每轮你应该往这个项目里喂什么

### A. 预处理阶段
喂：
- [ ] planning instance table 摘要
- [ ] exclusion log 摘要
- [ ] subgroup 数量
- [ ] 异常项列表

让它做：
- [ ] 检查纳排是否一致
- [ ] 检查 scope 是否被改了
- [ ] 识别后验排除风险

### B. 仿真冻结阶段
喂：
- [ ] surrogate parameter table
- [ ] formal run config
- [ ] 搜索分辨率
- [ ] ROI 规则

让它做：
- [ ] 检查有没有 post-hoc 调参风险
- [ ] 检查 formal run 是否可以开始

### C. formal run 后
喂：
- [ ] 主结果表
- [ ] 主结果图
- [ ] 失败 run 摘要
- [ ] 敏感性检查摘要

让它做：
- [ ] 生成 claim ledger
- [ ] 区分 E / I / H / X
- [ ] 帮你写 results wording
- [ ] 帮你写 limitations wording

### D. 写作阶段
喂：
- [ ] figure/table 编号
- [ ] 每条 claim 对应的 artifact path
- [ ] 当前 target journal 倾向
- [ ] 当前 fatal issues 列表

让它做：
- [ ] 先写 outline
- [ ] 再写 main text
- [ ] 再做 review checklist 对照审查

---

## 这个项目该让它做什么
- [ ] 审核你本地产物是否符合 scope
- [ ] 检查 claim 是否越界
- [ ] 把表图转成 results 文字
- [ ] 帮你写 discussion 的受限推断
- [ ] 帮你起草 limitations
- [ ] 帮你做投稿前自审

## 不该让它做什么
- [ ] “猜一个可能结果然后先写”
- [ ] “帮我把故事补完整”
- [ ] “没跑敏感性，先假装稳健”
- [ ] “帮我补 DOI / 补 citation / 补 benchmark”
- [ ] 混入第二篇论文内容

---

# 推荐日常循环

## 每日循环
1. **本地单篇项目**产生产物
2. **网页单篇项目**审查这一轮产物
3. **网页主控项目**判断是否过 gate
4. **本地主控**更新总控状态看板
5. 再回到**本地单篇项目**执行下一轮最小任务

---

# 接下来 7 天就按这个排

## Day 1–2
- 本地单篇：KiTS23 provenance、license、环境锁定
- 网页单篇：审查 data plan 是否已可执行
- 网页主控：确认是否允许进入 preprocessing

## Day 3–4
- 本地单篇：连通域、`d_max`、exclusion log、subgroup labels
- 网页单篇：审查纳排与后验排除风险
- 网页主控：确认是否允许冻结主队列

## Day 5
- 本地单篇：冻结 surrogate parameter table、formal config
- 网页单篇：审查 simulation freeze
- 网页主控：确认是否允许 formal run

## Day 6
- 本地单篇：geometry tests、sanity checks、deterministic rerun
- 网页单篇：审查 verification 是否足够
- 网页主控：决定是否准许 first formal run

## Day 7
- 本地单篇：first formal run
- 网页单篇：results + claim ledger 初审
- 本地主控：更新总控状态

---

# 你现在最该盯住的完成标志

## 主控线完成标志
- 你已经有明确 gate
- 知道何时停线
- 知道谁负责审查什么

## 单篇线完成标志
- 你已经从“冻结题目”走到“可正式首跑”

---

## 立即执行的两件事

1. **先在本地补总控状态看板**
2. **再在单篇项目里补 KiTS23 provenance + preprocessing 首轮脚本**

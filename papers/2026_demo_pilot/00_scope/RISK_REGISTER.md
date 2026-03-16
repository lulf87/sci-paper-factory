# RISK_REGISTER.md

## 0. 文件角色

本文件登记当前稿件从 `00_scope` 到投稿前的关键风险，并给出停线规则。  
本题的高风险集中在三处：

1. **proxy 过度解释**
2. **single-applicator generic surrogate 的后验调参**
3. **把 simulated geometric findings 写成 clinical guidance**

---

## 1. 风险等级定义

| 等级 | 含义 | 动作 |
|---|---|---|
| L | 低风险，可监控 | 记录并复核 |
| M | 中风险，可能影响稳健性或叙事 | 必须缓解 |
| H | 高风险，可能推翻主分析或主张边界 | 进入 `HOLD` |
| K | Kill risk，一票否决 | `DO NOT SUBMIT` |

---

## 2. 风险登记表

| risk_id | 类别 | 风险描述 | 等级 | 触发条件 | 后果 | 缓解措施 | 停线条件 | 状态 |
|---|---|---|---|---|---|---|---|---|
| D01 | Data | KiTS23 provenance 记录不完整 | H | 官方来源、下载日期、版本/哈希缺失 | 数据可追溯性不足 | 补齐 provenance record | 正式分析前仍无法补齐 | open |
| D02 | Data | `d_max ≤ 4 cm` 的 small renal mass 定义执行不一致 | H | 不同脚本/版本得到不同 `d_max` 或边界判定 | 主队列不稳定 | 固定 `d_max` 算法与单位 | 主队列无法稳定重现 | open |
| D03 | Data | 囊肿明显干扰 planning 的筛选存在后验性 | H | 看到结果后再决定是否排除 | 主分析偏倚 | 先筛查后跑数；保留 exclusion log | 主队列依赖后验排除 | open |
| D04 | Data | 多连通域/多病灶处理不一致 | M | 同病例在不同运行中被拆分方式不同 | planning instance 不稳定 | 固定连通域规则并日志化 | 主结果依赖不稳定拆分 | open |
| D05 | Data | kidney \ tumor 被过度解释为真实功能肾实质 | K | 文稿出现真实肾功能/肾单位获益暗示 | 直接越界 | 全文替换为 proxy 术语；claim 审查 | 终稿仍出现功能获益主张 | open |
| S01 | Simulation | surrogate library 未在正式运行前冻结 | H | 先跑结果后再补 library | feasibility 与 primary endpoint 均不可信 | 运行前冻结 parameter table | 主结果依赖未冻结 library | open |
| S02 | Simulation | 为了提高 feasibility 后验扩大 surrogate library | K | 结果不理想后增加更大热区 | 主结论失真 | versioned parameter table；禁止 post hoc enlargement | 主结果建立在后验扩大的 library 上 | open |
| S03 | Simulation | surrogate 被错误解释为真实器械/真实参数 | K | 文稿把 generic library 映射到品牌/针型/功率/时间 | 直接越界 | 强制使用 device-agnostic 话术 | 终稿仍有品牌/参数推荐 | open |
| S04 | Simulation | 几何实现错误（coverage、margin、volume 计算错误） | K | 单元测试或 sanity check 失败 | 全部结果无效 | 修复并重跑全部结果 | 核心几何测试未通过 | open |
| S05 | Simulation | feasibility 接近 100% 仅因 surrogate 过大或约束过弱 | H | surrogate family 事实上失去区分度 | feasible rate 失去意义 | 收紧到冻结 finite library；解释边界 | feasible rate 主要由约束错误造成 | open |
| S06 | Simulation | feasibility 接近 0 使 primary endpoint 样本过少 | H | feasible subset 极少 | 主终点叙事崩塌 | 如实承认并降级叙事 | 主摘要仍回避这一点 | open |
| S07 | Simulation | 结果高度依赖搜索分辨率或 ROI 边界 | H | 轻微数值设置变化导致主结论翻转 | 主结论不稳 | 最小敏感性分析；如实降级 | 主结论对数值细节极端敏感 | open |
| A01 | Analysis | primary endpoint 被替换或重定义 | K | 结果后切换到其他 endpoint | p-hacking | 锁定唯一主终点 | 正式分析后主终点变化 | open |
| A02 | Analysis | 次要终点越界扩张 | H | 新增未冻结 secondary endpoints | scope 漂移 | 仅允许 4 类 secondary endpoints | 摘要/结论依赖未冻结 endpoint | open |
| A03 | Analysis | 子组界值后验修改 | K | `≤3 cm` / `3–4 cm` 被改动 | 主分析失真 | 固定界值写入脚本 | 子组阈值被后验修改 | open |
| A04 | Analysis | 多病灶同病例的聚类问题被忽略 | M | 置信区间明显过窄 | 不确定性被低估 | case-level bootstrap 或敏感性分析 | 关键不确定性估计明显失真 | open |
| C01 | Claim | simulated geometric trade-off 被写成真实肾功能获益 | K | 出现 renal function / nephron benefit 等表述 | 直接越界 | claim ledger 全文审查 | 终稿仍保留此类语句 | open |
| C02 | Claim | 子组差异被写成器械或治疗建议 | K | 出现 should / recommend / select 等话术 | 直接越界 | 改写为 subgroup-specific simulated differences | 摘要/结论仍含建议性语言 | open |
| C03 | Claim | 结果被写成可直接用于临床部署 | K | 出现 deployable / clinical workflow ready 等 | 直接越界 | 删除并重写 | 终稿仍含部署暗示 | open |
| C04 | Claim | exploratory 结果冒充 prespecified | H | 连续趋势、形状异质性等被写成主结论 | 主叙事失真 | 显式标记 exploratory | 摘要/结论依赖 exploratory | open |
| P01 | Practical | 本地 MacBook Pro 16GB 无法重跑主结果 | H | 内存、耗时或存储超出主流程能力 | 复现链断裂 | 压缩 ROI、控制 library、减少冗余输出 | 主结果不能本地重跑 | open |
| P02 | Practical | 代码/图表无法由单一入口重建 | H | 手工改数或图表无脚本 | 可追溯性不足 | 建立单一运行入口与 artifact ledger | 关键图表不能脚本重现 | open |
| J01 | Journal | 选刊时隐性要求真实验证/湿实验 | H | 目标期刊不接受当前证据强度 | 高拒稿风险 | 投稿前做官方 scope 核验 | 未核验即投稿 | open |

---

## 3. 必须优先关闭的风险

在写摘要前，以下风险必须关闭或降级：

- D01
- D03
- D05
- S01
- S02
- S03
- S04
- A01
- A03
- C01
- C02
- C03
- P01
- P02

---

## 4. 最小验证链对应风险关闭

### 4.1 数据侧
要关闭 D01–D04，至少需要：

- provenance record
- exclusion log
- 连通域与 `d_max` 输出表
- `cystic_interference` 筛查记录

### 4.2 仿真侧
要关闭 S01–S07，至少需要：

- versioned parameter table
- geometry unit tests
- synthetic sanity checks
- deterministic rerun log
- sensitivity report

### 4.3 主张侧
要关闭 C01–C04，至少需要：

- claim ledger
- 摘要/结果/结论逐句边界审查
- proxy / clinical / deployment 词表清洗

---

## 5. 停线规则

### 5.1 进入 HOLD

出现以下任一情况，稿件进入 `HOLD`：

1. surrogate library 未冻结
2. `cystic_interference` 排除规则无法稳定执行
3. feasible subset 太小，主终点无法支撑主叙事
4. 主结论对分辨率/library 轻微变化即翻转
5. 主结果不能在本地 16GB 资源重跑
6. 关键图表无脚本来源

### 5.2 进入 DO NOT SUBMIT

出现以下任一情况，稿件进入 `DO NOT SUBMIT`：

1. 终稿把 proxy 写成真实肾功能获益
2. 终稿出现器械/参数推荐
3. 终稿暗示可直接临床部署
4. 几何计算单元测试未通过
5. 主终点、子组或主队列存在后验修改
6. 结果无法追溯到真实脚本输出

---

## 6. 风险复核节奏

建议在以下节点固定复核：

1. 数据冻结后
2. surrogate library 冻结后
3. 主结果首次跑完后
4. 摘要初稿后
5. 投稿前终审

---

## 7. 一句话原则

**任何让论文“看起来更临床、更强、更可用”的改写，只要证据链没有同步变强，都应先被登记为风险。**

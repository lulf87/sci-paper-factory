# RESEARCH_QUESTION.md

## 0. 文件角色

本文件用于冻结当前稿件的 **00_scope 研究问题边界**。  
适用对象为 **公开数据 + 本地几何仿真**；当前稿件不包含湿实验、动物实验、私有临床数据、自动分割方法创新或 HPC 依赖。

**当前状态：** `FORMALLY_FROZEN`  
**修改规则：** 只能收窄，不能扩张。

---

## 1. 稿件身份冻结

### 1.1 冻结题目

**中文题目**  
《基于 KiTS23 的小肾肿瘤单针通用热消融几何 surrogate 下覆盖—肾实质保留权衡研究》

**英文题目**  
Coverage–Renal Parenchyma Preservation Trade-offs for Small Renal Masses on KiTS23 Under a Single-Applicator Generic Thermal Ablation Surrogate

### 1.2 研究类型

本研究被固定为以下类型：

- `retrospective public-data analysis`
- `local geometric simulation study`
- `device-agnostic single-applicator planning surrogate study`

本研究**不是**：

- 临床试验
- 前瞻性验证
- 自动分割方法论文
- 器械品牌对比研究
- 真实热传导/热损伤参数推荐研究
- 临床部署研究
- 肾功能获益研究
- 因果识别研究

### 1.3 数据与仿真对象

- 公开数据：`KiTS23`
- 分割来源：**直接使用 KiTS23 真值分割**
- 仿真对象：**single-applicator generic thermal ablation geometric surrogate**
- 研究对象：**small renal masses，最大径 ≤ 4 cm**
- 主队列：**排除囊肿明显干扰 planning 的病例/病灶**
- 预设子组：
  - `SG1: ≤ 3 cm`
  - `SG2: > 3 cm 且 ≤ 4 cm`

---

## 2. 一句话主研究问题（Prespecified）

> 在 KiTS23 中、使用真值肾/肿瘤分割并排除囊肿明显干扰 planning 的 small renal masses（最大径 ≤ 4 cm）后，  
> 在 **固定的 single-applicator generic thermal ablation geometric surrogate** 假设下，  
> 能否以**完整覆盖肿瘤**为约束，得到每个病例/病灶的 **最小非肿瘤肾实质受累比例**，  
> 以及该 simulated geometric trade-off 在 `≤ 3 cm` 与 `3–4 cm` 子组之间如何不同？

### 2.1 这句话允许回答什么

1. 在当前几何 surrogate 假设下，哪些病例/病灶可达到 complete coverage
2. 在 complete coverage 条件下，最小非肿瘤肾实质受累比例的分布如何
3. minimum margin / margin deficit 如何分布
4. `≤ 3 cm` 与 `3–4 cm` 子组的 simulated geometric trade-off 是否不同
5. 这些结果对预设求解分辨率、surrogate library、筛选规则是否稳定

### 2.2 这句话不允许被扩写为什么

- 真实肾功能是否改善
- 哪个真实器械品牌/针型更优
- 应使用何种真实功率、时间或临床参数
- 可直接指导临床部署或术中决策
- 已证明真实机制、真实疗效或真实安全性

---

## 3. 研究单元与术语冻结

### 3.1 分析单元（Prespecified）

主分析单元固定为 **eligible planning instance**。

操作化定义：

- 从 KiTS23 肿瘤真值 mask 出发，按连通域定义候选病灶
- 对每个候选病灶计算分割导出的最大三维径（`d_max`）
- 满足 `d_max ≤ 4 cm` 且通过主队列筛选者，形成一个 eligible planning instance

### 3.2 small renal mass 的本研究定义

在本研究中，small renal mass 仅指：

- **分割导出的三维最大径 `d_max ≤ 4 cm` 的目标病灶**

这是一条**几何纳入规则**，不是对真实临床分期、病理性质或治疗指征的直接替代。

### 3.3 preserved renal parenchyma 的本研究定义

本稿中所谓 “renal parenchyma preservation” 仅通过几何/体积 proxy 表达：

- `non-tumor renal parenchyma proxy = kidney mask \ tumor mask`
- `preserved fraction = 1 - involved fraction`

该 proxy **不得**解释为：

- 真实肾功能保留
- nephron-sparing 的临床获益
- eGFR、CKD 风险或术后功能结局改善

---

## 4. Prespecified 研究问题

### RQ1（Primary）

对每个 eligible planning instance，若存在至少一个 single-applicator generic surrogate 方案可实现 complete coverage，则：

- 其 **最小非肿瘤肾实质受累比例** 是多少？

这是本稿唯一的 **primary endpoint question**。

### RQ2（Secondary）

在主队列中，**feasible complete-coverage rate** 为多少？

### RQ3（Secondary）

在主队列中，**minimum margin / margin deficit** 的分布如何？

### RQ4（Secondary）

在实现 complete coverage 的方案中，**non-tumor renal parenchyma involved volume/fraction** 的分布如何？

### RQ5（Secondary）

上述 primary / secondary endpoints 在 `≤ 3 cm` 与 `3–4 cm` 两个预设子组之间有何差异？

---

## 5. Exploratory 研究问题

以下问题允许研究，但必须显式标记为 `exploratory`，不得替代主问题：

### EQ1
连续肿瘤大小、肿瘤形状复杂度或位置特征，是否与 simulated geometric trade-off 呈现额外模式？

### EQ2
对主队列排除项（尤其囊肿明显干扰 planning 的病例/病灶）单独描述时，结果是否系统性偏离主队列？

### EQ3
在不改变 single-applicator、generic、device-agnostic 前提下，替代 surrogate library 或搜索分辨率是否改变结论强度？

### EQ4
多发/形态复杂病灶的处理规则改变后，结果是否有方向性变化？

**Exploratory 规则：**

1. 只能在结果出现后标记为 exploratory
2. 不得回填为 prespecified
3. 不得成为标题、摘要或结论的核心承诺
4. 若与 prespecified 结果冲突，必须如实报告冲突

---

## 6. 主队列纳入、排除与子组规则

### 6.1 Prespecified 纳入

eligible planning instance 必须同时满足：

1. 来源于 KiTS23 且原始影像与真值分割可读取
2. 存在可识别的肾 mask 与目标肿瘤 mask
3. 分割导出的目标病灶最大三维径 `d_max ≤ 4 cm`
4. 可在不引入自动分割新方法的前提下直接使用真值分割进入几何计算

### 6.2 Prespecified 排除

以下任一条件满足则排除出主队列：

1. 缺失、损坏或不可读取的影像/真值分割
2. 目标病灶 `d_max > 4 cm`
3. 囊肿明显干扰 planning，使得单针几何目标区无法由 KiTS23 肿瘤真值稳定定义
4. 病灶目标定义在连通域层面存在不可消解歧义，无法形成单一 eligible planning instance
5. 运行前即确定无法在本地固定流程内完成几何计算的异常数据

### 6.3 囊肿明显干扰 planning 的操作化定义

以下任一条满足，则标记为 `cystic_interference = yes`，排除出主队列：

- 目标区存在显著囊性成分或邻近大型囊肿，导致“应覆盖的实体肿瘤边界”无法由 KiTS23 肿瘤真值稳定代表
- 囊性结构与目标病灶在几何上造成单针 planning 明显歧义
- 若不额外引入人工临床判断，无法仅凭 frozen 规则确定单针 generic surrogate 的覆盖目标

该筛查必须在任何 endpoint 计算前完成，并记录在 exclusion log 中。

### 6.4 预设子组

- `SG1: d_max ≤ 3.0 cm`
- `SG2: 3.0 cm < d_max ≤ 4.0 cm`

子组界值在 00_scope 后固定，不得根据结果更改。

---

## 7. 非研究边界（Out of Scope）

本稿明确**不回答**以下问题：

- 自动分割性能或自动分割创新
- 多针、多次 pull-back、组合治疗或真实操作流程
- 器械品牌、针型、能量模式的优劣排序
- 临床功率/时间/温度参数推荐
- 真实肾功能、并发症、肿瘤控制率、生存结局
- 术中导航、机器人部署或临床工作流集成
- 普遍适用于全部肾肿瘤或全部数据集的外推结论

---

## 8. 最小验证链（Minimum Validation Chain）

本稿允许形成主结论，至少需要以下证据链全部成立：

1. **数据可追溯**  
   KiTS23 下载记录、版本记录、真值分割读取日志完整

2. **纳排可追溯**  
   `d_max ≤ 4 cm`、囊肿干扰排除、连通域处理均有脚本/日志

3. **几何计算正确性**  
   surrogate 体积、覆盖判定、margin 计算、肾实质受累体积计算通过单元测试与合成几何 sanity check

4. **主结果可重跑**  
   同一配置下可在本地 MacBook Pro 16GB 级资源重复得到相同结果

5. **主结论不越界**  
   结论仅停留在 simulated geometric trade-off，不延伸到肾功能、器械选择或临床部署

缺一项，则摘要/结论不得写强主张。

---

## 9. 进入正文时允许的最强表述

在本文件边界下，正文最多只能得到以下层级的结论：

### 9.1 Evidence
- “在 KiTS23 小肾肿瘤主队列中，complete-coverage feasible rate 为……”
- “在可完整覆盖病例/病灶中，最小非肿瘤肾实质受累比例的分布为……”
- “`≤ 3 cm` 与 `3–4 cm` 子组在上述 simulated geometric endpoints 上存在/不存在差异。”

### 9.2 受限 Inference
- “这些结果提示，在当前 generic single-applicator 几何假设下，存在 coverage–parenchyma involvement trade-off。”
- “这一模式与较大病灶几何难度增加相一致。”

### 9.3 明确禁止
- “改善真实肾功能”
- “可直接指导临床参数或器械选择”
- “可直接用于临床部署”
- “证明真实热消融机制/疗效/安全性”

---

## 10. 一句话冻结原则

**本稿回答的是 KiTS23 small renal masses 在固定单针通用热消融几何 surrogate 下的 simulated geometric trade-off，而不是现实临床已被证明了什么。**

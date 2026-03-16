# HYPOTHESIS.md

## 0. 文件角色

本文件冻结当前稿件的 **可检验命题**，并明确区分：

- `prespecified hypotheses`
- `exploratory hypotheses`

本文件**不预写结论**。  
所有假设都必须服从以下硬边界：

- 只能支持几何/体积层面的 simulated evidence
- 不能支持真实肾功能、真实器械优劣、真实参数推荐或临床部署主张

---

## 1. 总体原则

1. 假设与已冻结研究问题一一对应
2. primary endpoint 优先级高于全部 secondary / exploratory endpoints
3. “preserved renal parenchyma” 仅为几何/体积 proxy
4. 任一机制性、临床性或部署性解释都不是 prespecified evidence
5. 假设即使被支持，也只能形成符合 `CLAIM_BOUNDARY` 的窄结论

---

## 2. Prespecified 假设

### H1-P（Primary endpoint hypothesis）

在主队列中，存在至少一部分 eligible planning instances 能在 **single-applicator generic thermal ablation geometric surrogate** 下实现 complete coverage；  
对于这些 feasible instances，能够计算出 **在 complete coverage 条件下的最小非肿瘤肾实质受累比例**。

**若被支持，允许写为：**
- “Among complete-coverage feasible instances, the minimum non-tumor renal parenchyma involved fraction was …”
- “The primary endpoint was computable in the feasible subset under the frozen surrogate setting.”

**不得写为：**
- “The approach preserves renal function.”
- “The method is nephron-sparing in clinical practice.”

---

### H2-P（Feasibility hypothesis）

在主队列中，feasible complete-coverage rate **既不是预设为 0，也不是预设为 100%**；  
即在固定 generic single-applicator surrogate library 下，complete coverage 是一个需要被测量的几何可行性问题，而非先验成立。

**若被支持，允许写为：**
- “The complete-coverage feasible rate under the frozen surrogate library was …”

**不得写为：**
- “Single-applicator ablation is clinically feasible for these tumors.”
- “These tumors should be treated with a single applicator.”

---

### H3-P（Margin hypothesis）

best achievable minimum margin / margin deficit 在主队列中存在可报告分布，并能区分：

- 可完整覆盖病例/病灶
- 不可完整覆盖病例/病灶

**若被支持，允许写为：**
- “Best signed margin values were higher in feasible than infeasible instances.”
- “Margin deficit remained in instances without complete coverage under the frozen surrogate library.”

**不得写为：**
- “Margin results validate clinical safety.”
- “Margin results establish treatment adequacy in practice.”

---

### H4-P（Subgroup hypothesis）

在当前几何 surrogate 假设下，`≤ 3 cm` 与 `3–4 cm` 两个预设子组的 simulated geometric trade-off 可能不同；  
差异体现在以下 prespecified endpoints 之一或数项上：

- feasible complete-coverage rate
- 最小非肿瘤肾实质受累比例
- minimum margin / margin deficit
- non-tumor renal parenchyma involved volume/fraction

**若被支持，允许写为：**
- “Subgroup differences were observed between the `≤ 3 cm` and `3–4 cm` groups under the simulated geometric setting.”

**不得写为：**
- “Tumors >3 cm should not undergo single-applicator ablation.”
- “The size threshold directly guides clinical selection.”

---

### H5-P（Proxy-bound interpretation hypothesis）

即使 simulated geometric trade-off 被观察到，本研究中的 renal parenchyma preservation 也只允许解释为：

- 非肿瘤肾区几何受累较少/较多
- 一种 volume-based proxy

**不得**提升为：

- 真实功能保护
- 真实肾单位保护
- 长期肾结局改善

这一条不是结果假设，而是**结果解释假设的上限**；它对全文均有约束力。

---

## 3. Exploratory 假设

以下内容允许研究，但必须标记为 `exploratory`，且不得替代 prespecified 结论。

### H6-E（连续大小趋势）
除预设两子组外，连续 `d_max` 或肿瘤体积与 simulated geometric endpoints 之间可能存在额外梯度关系。

### H7-E（形状/位置异质性）
肿瘤形状复杂度、外生/内生程度、近肾门程度等几何特征，可能与 complete-coverage feasibility 或 parenchyma involvement 呈现异质性模式。

### H8-E（排除队列偏移）
囊肿明显干扰 planning 的排除病例/病灶，可能与主队列表现出系统性不同的几何特征。

### H9-E（Surrogate-library sensitivity）
在不改变 “single-applicator + generic + device-agnostic” 边界下，替代 surrogate library 或搜索分辨率可能改变结果幅度。

**Exploratory 结果允许写为：**
- “Exploratory analysis suggested …”
- “A possible geometric interpretation is …”
- “This warrants further evaluation under separate validation.”

**禁止写为：**
- “We confirmed …”
- “We validated …”
- “This should guide practice …”

---

## 4. 假设失败时的处理规则

### 4.1 Prespecified 假设未被支持时

允许：

- 如实报告 “未观察到”“不可行”“对该假设不支持”
- 将解释收窄到 current surrogate assumptions
- 将额外发现降级为 exploratory

不允许：

- 改 primary endpoint
- 改子组阈值
- 删除不利病例/病灶以制造支持
- 把 exploratory 结果改写成 prespecified 成功

### 4.2 Exploratory 假设看起来“很好”时

不允许升级为：

- prespecified 假设
- 摘要主结论
- 题目核心承诺
- 临床建议

---

## 5. 假设与章节的对应关系

| 假设编号 | 类型 | 可进入 Results | 可进入 Abstract | 可进入 Conclusion | 限制 |
|---|---|---:|---:|---:|---|
| H1-P | Prespecified | 是 | 是 | 是 | 仅限几何/体积 evidence |
| H2-P | Prespecified | 是 | 是 | 是 | 仅限 simulated feasibility |
| H3-P | Prespecified | 是 | 是 | 是 | 不得外推为安全/疗效 |
| H4-P | Prespecified | 是 | 审慎 | 审慎 | 仅限子组内 simulated differences |
| H5-P | Prespecified boundary | 是 | 是 | 是 | 约束解释上限，不是疗效证据 |
| H6-E | Exploratory | 可 | 否 | 否 | 只能作为补充讨论 |
| H7-E | Exploratory | 可 | 否 | 否 | 同上 |
| H8-E | Exploratory | 可 | 否 | 否 | 同上 |
| H9-E | Exploratory | 可 | 否 | 否 | 同上 |

---

## 6. 最小验证链（与假设对应）

每条 prespecified 假设要进入正文，至少需要以下证据支撑：

- `H1-P`：可重跑的 feasible-set 搜索结果 + primary endpoint 计算日志
- `H2-P`：全体主队列 feasibility 统计 + exclusion flow
- `H3-P`：margin 计算单元测试 + 主队列 signed margin 分布
- `H4-P`：冻结子组标签 + 子组比较输出
- `H5-P`：全文 claim 审查，确保未把 proxy 写成功能结局

---

## 7. 一句话原则

**本研究的假设最多只能检验“在冻结几何 surrogate 下能否观察到何种 coverage–parenchyma trade-off”，不能检验“真实临床是否获益”。**

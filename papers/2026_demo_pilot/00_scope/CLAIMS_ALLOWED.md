# CLAIMS_ALLOWED.md

## 0. 文件角色

本文件是当前稿件的 **claim firewall**。  
它将 `CLAIM_BOUNDARY.md` 落到本题，并直接规定：

- 能写什么
- 不能写什么
- prespecified 与 exploratory 如何分流
- 哪些句子即使“听起来合理”也必须删除

---

## 1. 本稿允许的主张等级

### E（Evidence）
可追溯到 KiTS23 真值分割、固定几何 surrogate 输出或可重跑脚本结果的陈述。

### I（Inference）
只能建立在 E 之上，并且必须用保守措辞。

### H（Hypothesis）
未被当前研究直接证明的解释，只能放在 Discussion / Limitations / Future work。

### X（Prohibited）
当前研究设计绝对不能支撑的说法，必须删除。

---

## 2. 本稿允许写的内容

### 2.1 关于数据与研究对象

允许写：

- “本研究基于 KiTS23，直接使用真值分割。”
- “研究对象限定为分割导出的最大径 ≤4 cm 的 small renal masses。”
- “主队列排除了囊肿明显干扰 planning 的病例/病灶。”
- “预设子组为 `≤3 cm` 与 `3–4 cm`。”

### 2.2 关于 primary endpoint

允许写：

- “在 complete coverage 条件下，最小非肿瘤肾实质受累比例为……”
- “该主终点仅在 complete-coverage feasible instances 中定义。”
- “主终点反映的是几何/体积 proxy。”

### 2.3 关于次要终点

允许写：

- “在冻结 surrogate library 下，complete-coverage feasible rate 为……”
- “best signed margin / margin deficit 的分布为……”
- “非肿瘤肾实质受累体积/比例为……”
- “`≤3 cm` 与 `3–4 cm` 子组在 simulated geometric endpoints 上存在/不存在差异。”

### 2.4 关于仿真边界

允许写：

- “本研究采用 device-agnostic 的 single-applicator generic thermal ablation geometric surrogate。”
- “结果成立于当前 surrogate 假设、搜索分辨率与纳排规则之内。”
- “这些发现描述的是 simulated geometric trade-off。”

### 2.5 关于 proxy 解释

允许写：

- “preserved renal parenchyma 在本文中仅以几何/体积 proxy 表达。”
- “该 proxy 不应被解释为真实肾功能获益。”

---

## 3. 本稿可以写，但必须显式标记为 exploratory 的内容

以下内容只能写成 `exploratory`：

- 连续大小趋势
- 形状/位置异质性
- 囊肿干扰排除队列的补充描述
- 替代 surrogate library
- 更密搜索与其他数值实验
- 可能的几何机制解释

**允许话术：**
- “Exploratory analysis suggested …”
- “A possible geometric explanation is …”
- “This warrants separate validation …”

**禁止话术：**
- “We demonstrated …”
- “We established …”
- “This should guide practice …”

---

## 4. 本稿明确禁止写的内容

### 4.1 肾功能类（X）
- “improves renal function”
- “preserves nephron function”
- “reduces CKD risk”
- “supports functional nephron-sparing benefit”

### 4.2 临床参数/器械推荐类（X）
- “supports device selection”
- “identifies the best applicator”
- “recommends power/time settings”
- “guides clinical parameter choice”

### 4.3 临床部署类（X）
- “clinically deployable”
- “ready for intraoperative planning”
- “ready for clinical use”
- “decision-support ready”

### 4.4 验证/疗效类（X）
- “validated”
- “clinically effective”
- “experimentally confirmed”
- “proves treatment adequacy”
- “demonstrates oncologic control”

### 4.5 因果/机制确认类（X）
- “proves the true mechanism”
- “confirms causality”
- “establishes why … in real patients”
- “demonstrates real biologic effect”

---

## 5. 分章节写作边界

### 5.1 Title
允许：

- KiTS23
- small renal masses
- single-applicator generic thermal ablation surrogate
- coverage–parenchyma preservation trade-off

禁止：

- prove / confirm / validated / clinically useful / deployment-ready

### 5.2 Abstract
允许：

- 已完成的数据筛选
- 已完成的几何 surrogate 分析
- primary/secondary endpoint 数值
- 受限到 simulated geometric trade-off 的结论

禁止：

- renal function benefit
- device or parameter recommendation
- clinical deployment promise
- exploratory 结果冒充主结论

### 5.3 Results
只允许：

- E（Evidence）

不得出现：

- 机制解释
- 临床意义拔高
- 临床建议
- 功能获益暗示

### 5.4 Discussion
允许：

- E + I + H

但必须显式区分：

- 哪些是观察结果
- 哪些是受限解释
- 哪些是待验证假设

### 5.5 Conclusion
允许：

- “simulated geometric trade-off was observed / not observed”
- “subgroup differences were / were not observed”
- “the findings remain proxy-based and hypothesis-generating”

禁止：

- “improves renal function”
- “guides clinical device/parameter selection”
- “ready for deployment”

---

## 6. 可直接复用的安全措辞

### 6.1 优先使用
- observed
- feasible under the frozen surrogate setting
- under simulated geometric conditions
- proxy-based
- device-agnostic
- associated with
- differed between prespecified subgroups
- consistent with

### 6.2 谨慎使用（必须有对应证据）
- robust
- stable
- interpretable
- plausible
- hypothesis-generating

### 6.3 原则上删除
- prove
- confirm
- validate
- clinically useful
- deployment-ready
- nephron-sparing benefit
- treatment recommendation

---

## 7. Prespecified 与 Exploratory 的话术分流

| 类型 | 可进入 Abstract | 可进入 Results | 可进入 Conclusion | 话术要求 |
|---|---:|---:|---:|---|
| Prespecified E | 是 | 是 | 是 | 直接数值 + 条件边界 |
| Prespecified I | 审慎 | 否 | 审慎 | `suggest / consistent with` |
| Exploratory E/I | 否 | 可，但需明确标记 | 否 | 必须写 `exploratory` |
| H | 否 | 否 | 否/极审慎 | 仅 Discussion / Future work |
| X | 否 | 否 | 否 | 删除 |

---

## 8. 本题特有的高风险越界与改写模板

| 高风险原句 | 问题 | 可接受改写 |
|---|---|---|
| The method preserves renal function. | 把 volume proxy 写成真实功能 | The method reduced non-tumor renal parenchyma proxy involvement under the frozen simulated setting. |
| The findings guide device selection. | 无品牌比较、无真实器械数据 | The findings describe geometric trade-offs under a device-agnostic generic surrogate only. |
| The model can be used clinically. | 无真实部署验证 | The framework may be useful for future evaluation, but was not clinically validated or deployed here. |
| Tumors >3 cm should not receive single-applicator ablation. | 把子组差异写成临床建议 | The `3–4 cm` subgroup showed a less favorable simulated geometric profile under the current assumptions. |
| Parenchyma preservation implies nephron-sparing benefit. | 直接越界到功能获益 | In this study, parenchyma preservation is a geometric/volume proxy only. |

---

## 9. Claim Ledger 强制绑定

进入摘要、结果、结论的每条核心句都必须登记：

| claim_id | 章节 | 原句 | 类型(E/I/H/X) | 证据路径 | 动作 |
|---|---|---|---|---|---|
| C001 | Results |  |  |  |  |
| C002 | Results |  |  |  |  |
| C003 | Conclusion |  |  |  |  |
| C004 | Discussion |  |  |  |  |

未登记，不得入稿。

---

## 10. 一句话原则

**本稿允许声明 simulated geometric trade-off；不允许把它写成真实肾功能获益、器械推荐或临床部署能力。**

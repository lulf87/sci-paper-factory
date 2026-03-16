# CLAIM_BOUNDARY.md

## 0. 目的

本文件用于定义论文中的主张边界，防止以下问题：

- 观察结果被写成因果结论
- 仿真现象被写成现实验证
- 局部发现被写成普遍规律
- 讨论性解释被写成已证实事实
- 未来工作被写成已完成工作

适用对象：

- 公开数据分析
- 本地仿真
- 二者耦合形成的 SCI 稿件

---

## 1. 四类主张定义

所有关键句必须先归类，再决定能否进入正文。

### 1.1 EVIDENCE（证据陈述）

定义：  
可被**直接证据**支撑的陈述。

可接受证据包括：

- 公开数据集原始记录
- 可复现脚本输出
- 已核验文献的准确内容
- 仿真日志与参数文件中实际生成的结果

允许写法示例：

- “In dataset D, variable X was associated with Y.”
- “Model M achieved AUROC = 0.81 under split S.”
- “Under the calibrated simulation setting, outcome Z increased by 12%.”

要求：

1. 句子必须可追溯到具体证据
2. 数值必须可回溯到产物文件
3. 若存在条件，必须写条件
4. 不得超出实验设置范围

### 1.2 INFERENCE（受限推断）

定义：  
在证据基础上进行的**有限解释**，但不是直接观察事实。

允许写法示例：

- “These findings suggest…”
- “This pattern is consistent with…”
- “One interpretation is…”
- “The results may indicate…”

要求：

1. 必须建立在 EVIDENCE 之上
2. 必须使用保守措辞
3. 必须说明适用范围
4. 不得包装成已证实机制或普遍规律

### 1.3 HYPOTHESIS（假设）

定义：  
尚未被当前研究直接证明、但可检验的机制解释或未来方向。

允许写法示例：

- “A possible explanation is…”
- “We hypothesize that…”
- “This warrants future validation…”
- “Future experiments are needed to test whether…”

要求：

1. 必须明确其未被验证
2. 不得在摘要结果段中写成事实
3. 不得作为论文主结论核心支柱
4. 必须与未来工作/局限性绑定

### 1.4 PROHIBITED（禁止性主张）

定义：  
当前研究设计、数据、仿真、文献均不足以支撑的说法。

典型形式：

- 把关联写成因果
- 把仿真写成现实证明
- 把内部测试写成临床/工业有效
- 把局部数据写成普遍结论
- 把猜测写成事实
- 把未做验证写成已验证

一旦识别，必须删除或改写，不得保留。

---

## 2. 主张判定流程

对每条关键句，按以下顺序判断：

### Step 1：是否有直接证据？
- 若无 → 不得写为 EVIDENCE

### Step 2：证据是否来自当前研究实际产物或已核验文献？
- 若无 → 不得进入正文事实陈述

### Step 3：句子是否超出数据/仿真假设边界？
- 若是 → 改写为更窄的 INFERENCE，或删除

### Step 4：句子是否暗示因果、机制已证实、真实部署有效？
- 若是 → 通常为 PROHIBITED，除非研究设计足以支撑

### Step 5：句子是否只是解释性猜测？
- 若是 → 只能写为 HYPOTHESIS

---

## 3. 章节级边界规则

### 3.1 Title（标题）

允许：

- 问题
- 方法
- 数据来源
- 受限范围的结果

禁止：

- “proves”
- “confirms”
- “causal”
- “clinical utility” （若无真实临床验证）
- “real-world deployment” （若无真实部署）

### 3.2 Abstract（摘要）

允许：

- 已完成工作
- 已核验方法
- 已观察结果
- 受限结论

禁止：

- 机制已证实
- 广泛推广
- 临床/工业可用性承诺
- 未做验证却写“validated”

摘要原则上只允许：

- `EVIDENCE`
- 非核心、极保守的 `INFERENCE`

摘要中应尽量避免：

- `HYPOTHESIS`

### 3.3 Introduction（引言）

允许：

- 背景
- 问题缺口
- 本研究目标
- 贡献陈述（需真实）

禁止：

- 夸大研究意义
- 虚构“尚无研究”
- 未核验地声称“普遍共识”

### 3.4 Results（结果）

只允许：

- `EVIDENCE`

结果节不得出现：

- 机制解释
- 价值拔高
- 因果断言
- 临床/工业承诺

### 3.5 Discussion（讨论）

允许：

- `EVIDENCE`
- `INFERENCE`
- `HYPOTHESIS`

但必须显式区分三者，不能混写。

### 3.6 Conclusion（结论）

允许：

- 对当前研究问题的窄结论
- 明确边界内的总结
- 局限性下的谨慎意义

禁止：

- 超范围推广
- 现实落地承诺
- 未验证机制结论化
- 将 future work 写成 current evidence

---

## 4. 不同证据来源的边界

### 4.1 公开观察性数据

允许：

- 描述分布、差异、关联、预测表现

禁止：

- 因果证明
- 干预有效性证明
- 机制被确认
- 临床获益被证实

安全表达：

- “associated with”
- “correlated with”
- “predictive of”
- “observed in this dataset”

危险表达：

- “caused”
- “led to”
- “resulted in”
- “demonstrated efficacy”

### 4.2 本地仿真

允许：

- 在假设下的系统行为
- 参数变化下的趋势
- 机制探索
- 可行性评估

禁止：

- 现实世界有效性证明
- 真机/临床/现场行为确认
- 安全性、可靠性、可部署性承诺

安全表达：

- “under simulated conditions”
- “within modeled assumptions”
- “in the calibrated regime”

危险表达：

- “will improve real-world outcomes”
- “is deployment-ready”
- “confirms practical effectiveness”

### 4.3 公开数据 + 本地仿真耦合

允许：

- 数据观察与仿真趋势一致
- 仿真可解释部分观测现象
- 数据约束下的机制探索

禁止：

- 声称“仿真已证明真实机制”
- 声称“已完成外部验证”
- 声称“已证实真实系统因果过程”

安全表达：

- “The simulation reproduces part of the observed trend.”
- “The findings are consistent with the modeled mechanism.”
- “This provides a hypothesis-generating explanation.”

危险表达：

- “The simulation confirms the true mechanism.”
- “This validates the real system.”
- “This proves causality.”

---

## 5. 常见越界类型与改写模板

| 越界写法 | 问题 | 可接受改写 |
|---|---|---|
| X causes Y | 观察性数据通常不能证明因果 | X was associated with Y in dataset D |
| Our simulation proves the mechanism | 仿真不能单独证明真实机制 | Our simulation is consistent with one possible mechanism |
| The method is clinically effective | 无临床验证 | The method showed promising predictive performance in retrospective public data |
| The framework is ready for deployment | 无真实部署验证 | The framework may serve as a candidate for future deployment-oriented evaluation |
| This model generalizes to all settings | 外推过度 | This model performed well in the evaluated datasets/settings |
| We validated the approach | 若仅内部测试，不应泛称 validated | We evaluated the approach using internal experiments and sensitivity checks |
| The intervention improves outcomes | 若无干预研究，不可写 | The intervention was associated with improved simulated outcomes under modeled assumptions |
| The observed difference is significant | 若无统计检验，不可写 | The observed difference was numerically larger under setting A |
| Literature has established… | 若未核验，不可写 | Prior studies have reported…, subject to the cited settings |
| This explains why… | 解释被写成事实 | One possible explanation is… |

---

## 6. 允许与禁止用语清单

### 6.1 优先使用

- observed
- associated with
- suggests
- may indicate
- is consistent with
- under the current setting
- within the current dataset
- under simulated conditions
- hypothesis-generating

### 6.2 谨慎使用（必须有对应支持）

- robust
- generalizable
- validated
- effective
- reliable
- interpretable
- mechanism

### 6.3 原则上禁止

- proves
- confirms causality
- establishes efficacy
- deployment-ready
- clinically useful
- universally applicable
- definitively demonstrates
- real-world validated

---

## 7. 主张登记表（Claim Ledger）

每条核心主张必须在内部登记，不登记不得进入摘要/结果/结论。

| claim_id | 章节 | 原句 | 类型(E/I/H/X) | 证据来源 | artifact_path / citation | 风险 | 处理动作 |
|---|---|---|---|---|---|---|---|
| C001 | Results |  |  |  |  |  |  |
| C002 | Discussion |  |  |  |  |  |  |
| C003 | Conclusion |  |  |  |  |  |  |

### 处理动作取值

- `KEEP`
- `NARROW`
- `MOVE_TO_DISCUSSION`
- `REWRITE_AS_HYPOTHESIS`
- `DELETE`

---

## 8. 强制删除条件

若某句满足以下任一条件，必须删除或重写：

1. 找不到证据路径
2. 证据仅来自记忆或猜测
3. 结论范围大于数据范围
4. 仿真被写成现实证明
5. 观察关联被写成因果
6. 统计支持不存在却声称显著
7. 外部验证不存在却写“validated”
8. 把未来工作写成已完成贡献

---

## 9. 最终执行规则

投稿前必须满足：

1. 摘要中无 `X`
2. 结果节中无 `I/H/X`
3. 结论节中无 `X`
4. 所有核心句均有 `claim_id`
5. 所有数值句均可回溯到具体产物
6. 所有“解释性句子”均使用保守措辞
7. 所有“落地价值”都被限定在证据范围内

---

## 10. 一句话边界原则

**证据说到哪里，文字就停在哪里。**
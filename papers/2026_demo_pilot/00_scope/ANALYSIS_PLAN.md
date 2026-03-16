# ANALYSIS_PLAN.md

## 0. 文件角色

本文件冻结当前稿件的 **分析路径、指标定义、统计与判读规则**。  
目标是防止：

- 结果出来后改主问题
- 把 exploratory 发现伪装成 prespecified
- 把 proxy 指标解释成真实临床获益
- 把数值更优直接写成临床建议

---

## 1. 分析总原则

1. primary endpoint 唯一且固定
2. secondary endpoints 仅限已冻结的四类
3. results 节只允许 `EVIDENCE`
4. discussion 节才允许受限推断
5. 未经支持，不得使用 `significant / validated / clinically useful / deployment-ready`
6. 若主结论对数值实现细节高度敏感，必须降级表述
7. 所有主结果必须可在本地 MacBook Pro 16GB 级环境重跑

---

## 2. Endpoint 与判读规则冻结

### 2.1 Primary endpoint（唯一主终点）

对每个 feasible planning instance：

```text
primary_involved_fraction
= min over complete-coverage plans of
  volume(surrogate ∩ non_tumor_renal_parenchyma_proxy)
  / volume(non_tumor_renal_parenchyma_proxy)
```

**主判读规则：**

- 主终点只在 `complete_coverage_feasible = 1` 的 instances 中定义
- 主结论优先围绕主终点分布与子组差异
- 若 feasibility 太低导致主终点样本极少，必须在摘要与结论中如实承认

### 2.2 Secondary endpoints（仅限以下）

1. `feasible complete-coverage rate`
2. `minimum margin / margin deficit`
3. `non-tumor renal parenchyma involved volume/fraction`
4. `subgroup differences`

### 2.3 明确不作为 endpoint 的内容

以下均不得升级为主/次终点：

- preserved fraction 的功能性解释
- 任意真实临床参数建议
- 任意真实器械排序
- 任意自动分割表现
- 任意术后功能/肿瘤学结局

---

## 3. 主分析队列与子组

### 3.1 主队列
- KiTS23 eligible planning instances
- `d_max ≤ 4 cm`
- 排除囊肿明显干扰 planning
- 排除目标定义不稳定者

### 3.2 子组
- `SG1: d_max ≤ 3.0 cm`
- `SG2: 3.0 cm < d_max ≤ 4.0 cm`

### 3.3 补充队列
- 被排除的囊肿明显干扰 planning 病例/病灶
- 仅用于 exploratory exclusion audit
- 不进入主结论

---

## 4. Prespecified 分析顺序

### A1：数据审计与样本流程
输出：

- 数据 provenance 记录
- 纳排流程图
- exclusion log
- 主队列样本量
- 两个子组样本量

### A2：主队列描述性分析
输出：

- `d_max`、tumor volume、proxy kidney volume 的分布
- feasibility 分布
- primary / secondary endpoints 的总体分布

### A3：Primary endpoint 主分析
在主队列 feasible subset 中报告：

- `primary_involved_fraction` 的中位数、IQR、均值、SD
- 适当的区间估计（优先 bootstrap CI）
- 个体级分布图

### A4：Secondary endpoint 分析
报告：

- feasible complete-coverage rate
- best signed margin 分布
- primary involved volume / fraction 分布

### A5：预设子组比较
比较 `SG1` 与 `SG2`：

- feasible complete-coverage rate
- primary_involved_fraction
- best signed margin
- primary involved volume / fraction

### A6：最小稳健性分析
至少包括：

- 搜索分辨率变动
- surrogate library 轻度扰动
- ROI 裁剪边界变化
- 连通域/排除规则的有限敏感性检查

---

## 5. 统计与不确定性规则

### 5.1 统计策略

本稿以**描述性 + 区间估计**为主。  
若进行正式组间比较，优先使用与数据分布相匹配的非参数或重抽样方法，并在脚本中预先固定。

### 5.2 推荐最小输出

- 中位数 `[IQR]`
- 均值 `± SD`（如适合）
- bootstrap 95% CI
- 比例的 exact 或 bootstrap CI

### 5.3 若使用显著性检验

必须预先固定：

- 检验方法
- 双侧阈值
- 多重比较处理策略

若未执行正式检验，只能写：

- `numerically higher/lower`
- `observed difference`
- `directionally different`

不得写：

- `significant`
- `superior`
- `validated`

### 5.4 若存在多病灶同病例

主分析单位仍为 planning instance；  
但区间估计与重抽样优先按 **case-level clustering** 处理，以避免同病例多病灶造成过度乐观不确定性估计。

---

## 6. 关键公式与选择规则

### 6.1 Feasibility

```text
feasible_i = 1 if ∃ plan such that tumor_i ⊆ surrogate_i(plan)
```

### 6.2 Primary solution

若 `feasible_i = 1`，则从全部 feasible plans 中选取：

```text
argmin volume(surrogate_i(plan) ∩ non_tumor_renal_parenchyma_proxy_i)
/ volume(non_tumor_renal_parenchyma_proxy_i)
```

如有并列，按以下顺序打破平局：

1. 更大的 minimum margin
2. 更小的 involved volume
3. 预设的确定性排序规则（写入代码）

### 6.3 Signed margin

```text
best_signed_margin_i = max over all evaluated plans of minimum signed distance
```

解释：

- `>= 0`：可完整覆盖且有非负 margin
- `< 0`：margin deficit；数值越负，覆盖缺口越大

---

## 7. Results 与 Discussion 的话术分流

### 7.1 Results 只允许写
- feasible/infeasible 的数量与比例
- primary endpoint 数值
- margin / deficit 数值
- 子组差异的数值
- 稳健性检查中是否方向翻转

### 7.2 Discussion 才允许写
- 这些模式与肿瘤几何复杂度相一致
- 这些结果提示较大病灶可能有更差的 simulated trade-off
- proxy 指标的局限性
- surrogate library 作为几何假设的限制

### 7.3 全稿禁止写
- 改善真实肾功能
- 应采用某品牌/针型/参数
- 可直接用于临床部署
- 已验证临床有效性

---

## 8. 最小验证链（分析侧）

主分析要成立，至少需要以下链条：

1. **Cohort correctness**  
   纳排、子组、排除日志无冲突

2. **Geometry correctness**  
   coverage、margin、involved volume/fraction 的计算经单元测试验证

3. **Primary traceability**  
   每个 primary endpoint 值都能追溯到具体 planning instance 与具体 primary solution

4. **Deterministic reproducibility**  
   同配置重复运行结果一致

5. **Numerical robustness**  
   主结论不会因轻微分辨率/library 扰动而完全翻转；若翻转则必须降级

6. **Claim compliance**  
   结论仅停留在 simulated geometric trade-off

---

## 9. Exploratory 分析（必须单独标记）

允许但不得替代主分析：

- 连续大小趋势拟合
- 形状/位置异质性分析
- exclusion cohort 描述
- 替代 surrogate library
- 更密搜索或其他数值实验

规则：

1. 只能标记为 `exploratory`
2. 不得进入摘要主结论
3. 不得改变主终点、主队列或子组阈值
4. 若与主分析冲突，必须如实报告冲突

---

## 10. 停线条件

出现以下任一情况，稿件进入 `HOLD` 或降级：

1. 主终点无法稳定计算
2. feasibility 接近 0 且不足以支撑 primary endpoint 叙事
3. 子组标签或排除规则存在后验调整
4. 结果高度依赖未冻结 library
5. proxy 被写成真实功能结局
6. 本地环境无法重跑主结果

---

## 11. 一句话原则

**主分析只回答“在冻结 generic 单针几何 surrogate 下可观察到何种 coverage–parenchyma trade-off”，不回答“现实临床该怎么做”。**

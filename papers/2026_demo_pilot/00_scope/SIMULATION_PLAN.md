# SIMULATION_PLAN.md

## 0. 文件角色

本文件冻结当前稿件的 **本地几何仿真计划**。  
仿真目的不是替代真实验证，而是用可在本地 MacBook Pro 16GB 级资源上运行的 **single-applicator generic thermal ablation geometric surrogate**，评估 KiTS23 small renal masses 的 simulated geometric trade-off。

---

## 1. 仿真角色与禁区

### 1.1 本研究中仿真的合法角色

1. 在固定几何假设下评估 complete coverage 的可行性
2. 在 feasible complete coverage 条件下，最小化非肿瘤肾实质 proxy 受累
3. 计算 minimum margin / margin deficit
4. 比较 `≤3 cm` 与 `3–4 cm` 子组的 simulated geometric endpoints
5. 做本地可承受的分辨率、surrogate-library、筛选规则敏感性检查

### 1.2 本研究中仿真的非法角色

仿真结果不得被写成：

- 真实热生物学已被验证
- 真实器械品牌/针型已被比较
- 真实功率/时间/温度参数已被推荐
- 临床疗效或安全性已被证明
- 可直接用于临床部署

---

## 2. 模型对象冻结

| 项目 | 冻结内容 |
|---|---|
| 仿真对象 | KiTS23 主队列 small renal masses 的单针几何覆盖规划 |
| 模型类型 | 3D 局部 ROI 几何 surrogate；不做全三维热传导 PDE |
| Surrogate family | **fixed, finite, device-agnostic single-applicator generic thermal zone library** |
| 几何表示 | 单个 3D 连通、凸性近似、轴向可定向的热区 surrogate；默认实现为轴对称椭球族或其等价参数化 |
| 规划自由度 | surrogate library 成员选择 + 单针方向 + 空间位置 |
| 输入 | kidney truth mask、tumor truth mask、ROI 几何元数据 |
| 输出 | feasibility、primary involved fraction、involved volume、best signed margin |
| 计算约束 | 本地 MacBook Pro 16GB；允许多核 CPU，但不依赖 HPC |
| 明确不做 | 多针、pull-back、多次叠加、品牌映射、真实功率/时间拟合 |

### 2.1 关于 surrogate family 的边界

本稿只冻结 surrogate family 的 **结构边界**：

- single-applicator
- generic
- device-agnostic
- finite library
- same library for all cases
- no case-specific post hoc enlargement outside the frozen library

**exact numeric library values** 必须在正式运行前写入 `parameter_table` 并冻结；  
若未冻结，不得开始正式分析。  
这些数值即使被冻结，也只能作为 **几何假设**，不得反向解释为真实品牌或真实参数。

---

## 3. 规划问题的形式化定义

对每个 eligible planning instance `i`，记：

- `K_i`：kidney mask
- `T_i`：tumor mask
- `P_i = K_i \ T_i`
- `L`：冻结的 surrogate library
- `plan = (ℓ, x, θ)`，其中  
  - `ℓ ∈ L`：某一 surrogate library 成员  
  - `x`：空间位置参数  
  - `θ`：单针方向参数  
- `A_i(ℓ, x, θ)`：对应的 surrogate 几何区

### 3.1 Feasibility 判定

```text
feasible_i = 1 if there exists (ℓ, x, θ) such that T_i ⊆ A_i(ℓ, x, θ)
           = 0 otherwise
```

### 3.2 Primary objective（在 feasible 条件下）

```text
minimize volume(A_i(ℓ, x, θ) ∩ P_i) / volume(P_i)
subject to T_i ⊆ A_i(ℓ, x, θ)
```

### 3.3 Signed margin / deficit

定义：

```text
m_i(ℓ, x, θ) = minimum signed distance from tumor surface to surrogate boundary
```

则：

- `m_i ≥ 0` 表示 complete coverage 下的最小 margin
- `m_i < 0` 表示 margin deficit

best signed margin 定义为：

```text
M_i = max over all evaluated plans of m_i(ℓ, x, θ)
```

---

## 4. 参数分层管理

### P1：直接由公开数据确定
- kidney / tumor masks
- ROI 尺寸
- `d_max`
- tumor volume
- non-tumor renal parenchyma proxy volume

### P2：实现参数
- voxel spacing / resampling rule
- signed-distance 计算规则
- ROI cropping margin
- 搜索分辨率

### P3：冻结几何 library 参数
- surrogate library 的离散尺寸/形状参数
- 方向采样密度
- 位置采样/优化边界

### P4：敏感性/探索参数
- 替代 library
- 替代搜索分辨率
- 替代 ROI 扩边
- 替代连通域处理细节

**规则：**

- P1–P3 为主分析固定项
- P4 只能进入 sensitivity / exploratory
- 不得根据结果“好不好看”修改 P3

---

## 5. Prespecified 仿真任务

### S1-P：ROI 构建
基于 KiTS23 真值分割生成每个 planning instance 的局部 ROI，记录坐标、spacing、mask statistics。

### S2-P：冻结 library 下的单针搜索
在统一 surrogate library、统一方向/位置搜索规则下，对每个 planning instance 搜索 candidate plans。

### S3-P：Feasibility 与 primary solution 提取
- 先判定是否存在 complete-coverage plan
- 若存在，则从 feasible set 中选择 **非肿瘤肾实质受累比例最小** 的 plan 作为 primary solution

### S4-P：Secondary endpoint 计算
对每个 planning instance 计算：

- feasible complete-coverage flag
- best signed margin
- primary involved volume
- primary involved fraction

### S5-P：子组比较
对 `≤3 cm` 与 `3–4 cm` 子组分别汇总主终点和次要终点。

### S6-P：最小敏感性检查
至少检查：

- 搜索分辨率变化
- surrogate library 的轻度扰动
- ROI 裁剪边界变化

这些检查用于确认主结论是否依赖数值实现细节。

---

## 6. Exploratory 仿真任务

以下允许进行，但必须标记为 `exploratory`：

1. 替代 surrogate family 但仍保持 single-applicator + generic + device-agnostic
2. 更密的方向/位置搜索
3. 更复杂的形状/位置异质性分析
4. 对主队列排除项单独跑数
5. 其他不改变主 endpoint、但改变数值实现细节的补充实验

**禁止：**

- 将 exploratory library 结果回填成主结果
- 将后验调参写成预设设计
- 因结果不佳而扩大 surrogate library 直至几乎所有病例都可覆盖

---

## 7. 本地算力约束下的 MVP 设计

本稿主方案必须满足本地可运行：

- 仅做局部 ROI 几何计算
- 不做全器官/全时程热传导与热损伤耦合
- 不依赖 GPU / HPC
- 不做超大规模参数扫描
- 优先使用确定性、可中断、可重跑的搜索流程
- 需要时采用 coarse-to-fine 搜索，但 coarse 与 fine 规则须预先冻结

若主结果不能在本地 16GB 资源上重跑，则稿件进入 `HOLD`。

---

## 8. 最小验证链（仿真侧）

仿真侧至少需要以下验证全部通过：

### V1：几何单元测试
- surrogate 体积计算与解析值一致
- mask 布尔运算正确
- involved volume / fraction 计算正确

### V2：合成几何 sanity check
在球体、椭球体或规则几何体上验证：

- complete coverage 判定正确
- signed margin 正负号正确
- primary objective 优化方向正确

### V3：KiTS23 可视化抽检
对随机抽取的 planning instances，人工查看：

- surrogate 是否覆盖 tumor mask
- involved kidney proxy 是否符合几何直觉
- 明显异常是否被发现并记录

### V4：确定性重跑
同一配置下重复运行，输出一致。

### V5：数值实现稳健性
主结论在预设分辨率 / library 轻度变化下不出现完全翻转；  
若翻转，则必须如实降级主张。

---

## 9. 仿真层允许与禁止主张

### 9.1 允许
- “Under the frozen generic single-applicator surrogate library, complete coverage was feasible in …”
- “Among feasible instances, the minimum non-tumor renal parenchyma involved fraction was …”
- “The result was sensitive / insensitive to prespecified numerical settings.”

### 9.2 禁止
- “This identifies the best clinical device.”
- “This recommends clinical power or time settings.”
- “This demonstrates real renal function preservation.”
- “This is ready for clinical use.”

---

## 10. 失败时的处理规则

若仿真未给出期望模式，只允许：

- 如实报告 infeasible cases 或不利结果
- 检查实现错误、library 冻结、搜索分辨率与 exclusion log
- 将额外解释降级为 exploratory

不允许：

- 临时扩大 library 直至得到更好结果
- 用未登记的参数改动覆盖原结果
- 只展示最好看的个别案例

---

## 11. 一句话原则

**本稿中的仿真是 device-agnostic 的单针几何 surrogate 评估，不是现实热消融治疗效果验证。**

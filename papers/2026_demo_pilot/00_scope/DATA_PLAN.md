# DATA_PLAN.md

## 0. 文件角色

本文件冻结当前稿件的 **公开数据计划**。  
目标是保证：

- 数据真实、公开、可追溯
- 纳入/排除、子组、终点定义在分析前固定
- 不引入自动分割 novelty
- 所有 volume / fraction 指标均明确为几何 proxy

---

## 1. 数据使用总原则

1. 仅使用公开数据；本稿主数据固定为 `KiTS23`
2. 直接使用 KiTS23 真值分割；**不做自动分割方法创新**
3. 不使用私有临床数据、机构内影像或闭源标签
4. 不使用湿实验、动物实验或新增体外/离体验证
5. 不将 kidney/tumor 几何量写成真实肾功能或真实临床获益
6. 所有纳排、连通域处理、几何派生都必须脚本化并保留日志

---

## 2. 数据清单（冻结）

| dataset_id | 数据名称 | 角色 | 本稿用途 | 备注 |
|---|---|---|---|---|
| D1 | KiTS23 | 主数据 | 影像 + 真值肾/肿瘤分割，用于几何 ROI 构建、病例筛选、endpoint 计算 | 官方下载路径、版本、下载日期、哈希值写入 provenance 记录，不在本文件伪造填写 |

**说明：**

- 本文件冻结研究范围，不伪造未核验的 URL、版本号或许可细节
- 在正式跑数前，必须补齐 `data provenance record`
- 若 provenance 无法补齐，则稿件进入 `HOLD`

---

## 3. 分析单元与派生对象

### 3.1 主分析单元

主分析单元固定为 **eligible planning instance**，定义为：

- 从 KiTS23 肿瘤真值 mask 经过预设连通域处理得到的单个目标病灶
- 满足 `d_max ≤ 4 cm`
- 通过全部主队列排除规则
- 可直接进入单针 generic thermal surrogate 几何求解

### 3.2 连通域处理规则（Prespecified）

对 KiTS23 肿瘤真值 mask 执行 3D 连通域分解：

- 每个连通域先独立计算 `d_max`
- 仅保留 `d_max ≤ 4 cm` 的目标病灶作为候选 planning instance
- 若同一病例存在多个候选连通域，则每个连通域分别登记
- 若连通域之间无法在 frozen 规则下形成独立单针 planning target，则排除并记录原因

### 3.3 肾实质 proxy 定义

由于 KiTS23 不直接提供功能性肾单位标签，本稿中：

```text
non_tumor_renal_parenchyma_proxy = kidney_truth_mask \ tumor_truth_mask
```

所有以下量均指 proxy，而非真实功能组织：

- non-tumor renal parenchyma involved volume
- non-tumor renal parenchyma involved fraction
- preserved fraction = 1 - involved fraction

---

## 4. Prespecified 纳入与排除

### 4.1 纳入标准（Prespecified）

eligible planning instance 必须同时满足：

1. 来源于 KiTS23
2. 原始影像、肾真值分割、肿瘤真值分割均可读取
3. 目标病灶 `d_max ≤ 4 cm`
4. 在不引入自动分割新算法的前提下可直接构建几何 ROI
5. 满足单针 generic thermal surrogate 的目标定义要求

### 4.2 排除标准（Prespecified）

以下任一项满足则排除出主队列：

1. 影像或真值分割缺失、损坏或坐标不一致
2. 目标病灶 `d_max > 4 cm`
3. 囊肿明显干扰 planning
4. 目标病灶定义不稳定，无法按 frozen 规则形成单一 planning instance
5. 数据异常导致无法完成固定几何求解流程

### 4.3 囊肿明显干扰 planning 的筛选规则（Prespecified）

在任何 endpoint 计算前，对每个候选 planning instance 做固定筛查并记录 `cystic_interference`：

标记为 `yes` 的条件包括：

- 显著囊性成分或邻近大型囊肿使“应被覆盖的实体肿瘤边界”无法仅由 KiTS23 tumor mask 稳定代表
- 囊性结构导致单针几何目标区存在明显 planning 歧义
- 若不额外引入人工临床解释，就无法确定单针 generic surrogate 的目标覆盖区

标记为 `yes` 的病例/病灶：

- **排除出主队列**
- 可在后续作为 exploratory exclusion audit 单独描述
- 不得混入主结果

### 4.4 预设子组（Prespecified）

按 `d_max` 划分：

- `SG1: ≤ 3.0 cm`
- `SG2: 3.0 cm < d_max ≤ 4.0 cm`

---

## 5. 变量冻结表

| variable_name | 角色 | 来源 | 类型 | prespecified/exploratory | 操作化定义 |
|---|---|---|---|---|---|
| `kidney_mask` | 基础输入 | KiTS23 真值分割 | binary mask | prespecified | 肾 truth segmentation |
| `tumor_mask` | 基础输入 | KiTS23 真值分割 | binary mask | prespecified | 肿瘤 truth segmentation |
| `d_max` | 纳入/子组变量 | script from tumor mask | geometric | prespecified | 肿瘤分割导出的最大三维径 |
| `tumor_volume` | 描述变量 | script | geometric | prespecified | tumor mask 体积 |
| `non_tumor_parenchyma_proxy_volume` | 分母变量 | script | geometric | prespecified | `volume(kidney_mask \ tumor_mask)` |
| `complete_coverage_feasible` | 次要终点 | simulation output | binary | prespecified | 存在至少一个 complete-coverage 方案 |
| `primary_involved_fraction` | 主终点 | simulation output | fraction | prespecified | 见第 6 节公式定义 |
| `best_signed_margin` | 次要终点 | simulation output | distance | prespecified | 可为正（margin）或负（deficit） |
| `primary_involved_volume` | 次要终点 | simulation output | volume | prespecified | 主终点对应方案的 involved volume |
| `size_subgroup` | 子组变量 | script | categorical | prespecified | `≤3 cm` vs `3–4 cm` |
| `shape/location descriptors` | 描述/异质性变量 | script | derived | exploratory | 仅用于补充几何异质性分析 |

---

## 6. Endpoint 冻结定义

### 6.1 Primary endpoint（唯一主终点）

对每个 eligible planning instance `i`，记：

- `K_i`：kidney truth mask
- `T_i`：tumor truth mask
- `P_i = K_i \ T_i`：non-tumor renal parenchyma proxy
- `A_i(plan)`：某一 single-applicator generic surrogate 方案对应的 3D 几何区

complete coverage 条件定义为：

```text
T_i ⊆ A_i(plan)
```

则 primary endpoint 定义为：

```text
y_i = min over complete-coverage plans of
      volume(A_i(plan) ∩ P_i) / volume(P_i)
```

即：

**在 complete coverage 条件下的最小非肿瘤肾实质受累比例。**

若不存在 complete-coverage plan，则 `y_i = NA`，该 instance 仍计入 feasibility 分析，但不进入 primary endpoint 分布。

### 6.2 Secondary endpoints（仅限以下四类）

1. `feasible complete-coverage rate`
2. `minimum margin / margin deficit`
3. `non-tumor renal parenchyma involved volume/fraction`
4. `subgroup differences`

本稿**不得新增** primary/secondary endpoints。

---

## 7. 预处理与审计流程（Prespecified）

1. 读取 KiTS23 原始影像与真值分割
2. 执行坐标一致性检查与 mask 完整性检查
3. 执行肿瘤 3D 连通域分解
4. 对每个候选病灶计算 `d_max`
5. 执行 `d_max ≤ 4 cm` 筛选
6. 执行 `cystic_interference` 筛查
7. 生成：
   - analysis-ready planning instance table
   - exclusion log
   - subgroup label table
   - ROI metadata

任何结果分析不得绕过这一路径。

---

## 8. 最小验证链（数据侧）

数据侧至少需要以下验证：

1. **provenance 完整**：下载日期、版本、官方来源记录齐全
2. **mask 可读且一致**：影像与分割空间一致性检查通过
3. **连通域可追溯**：每个 planning instance 能追溯到原病例与原连通域
4. **纳排可重现**：`d_max`、`cystic_interference`、异常排除在重复运行下结果一致
5. **主终点分母稳定**：`volume(P_i)` 计算脚本固定，未被后验修改

---

## 9. 明确禁止的解释

以下表述不从本文件获得授权：

- “preserved renal parenchyma implies preserved renal function”
- “the dataset supports direct treatment recommendation”
- “ground-truth masks validate a clinical planning tool”
- “the findings can be directly deployed”

---

## 10. 一句话原则

**本稿的数据层只支持 KiTS23 真值分割上的几何 planning proxy，不支持真实功能或临床效益主张。**

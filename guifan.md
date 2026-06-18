---
title: "自定义 C/C++ 编程规范——代码审核知识库（最佳实践版）"
document_type: "coding-standard-knowledge-base"
kb_schema: "coding-standard/v2"
language: "zh-CN"
target_languages: ["C", "C++"]
authority: "custom-project-policy"
source_file: "guifan.txt"
source_sha256: "cffcc4d638985d179945c8cfe1d61ccb9d86f80fcdc886c4708084b1b955b59d"
generated_on: "2026-06-18"
chunk_unit: "one-rule-per-chunk"
---

# 自定义 C/C++ 编程规范——代码审核知识库（最佳实践版）

> 本文档面向 RAG、AI 代码审核、静态检查规则建设和人工 Code Review。它忠实保留原始规范，同时把“原规范要求”“自动审核策略”和“最佳实践质量提示”分层，避免把历史写法、破损示例或项目特定偏好误当成通用语言规则。

## 1. 权威性与使用边界

- 规范权威来源：`guifan.txt`。
- 原文从第 3 章开始；缺失的第 1、2 章未补造。
- 本文对原规则编号保持稳定，规则 ID 格式为 `CSTD-x.y`。
- 一个原规则包含多项要求时，拆分为原子检查项 `CSTD-x.y-nn`，审核意见优先引用检查项 ID。
- “最佳实践校验”不会静默修改原规范，只负责提示过时、歧义、示例缺陷或技术冲突。
- `需项目确认` 的规则在项目未明确启用前，默认输出 `needs_review`，不得自动判违规。
- `需修订原规范` 的规则在修订前不得自动执行。

## 2. 质量审计结论

- 一级章节：12 个。
- 原始规则：107 条。
- 原子检查项：170 项。
- 有效规则：71 条。
- 有效但示例有缺陷：10 条。
- 需项目确认：23 条。
- 需修订原规范：3 条。
- 已修复上一版中“强制级别与人工审核方式混用”“关键词误判风险等级”“示例代码混入审查断言”等问题。
- 已删除一处明显文档处理残留：`正文件切分`。

### 2.1 规则状态

| 状态 | 含义 | 默认审核行为 |
|---|---|---|
| 有效 | 原要求未发现明显技术冲突 | 按 MUST/SHOULD 和证据判定 |
| 有效，但示例有缺陷 | 规则意图可用，但原示例不可作为标准答案 | 审核规则；引用示例时附警告 |
| 需项目确认 | 属于历史、平台、语言版本或团队偏好政策 | 未确认时输出 `needs_review` |
| 需修订原规范 | 原文包含明显冲突或不可靠结论 | 修订前不自动执行 |

### 2.2 规范强度

| 强度 | 含义 | 建议处理 |
|---|---|---|
| MUST | 必须满足的项目规则 | 有明确证据时可判违规 |
| SHOULD | 推荐或设计性要求 | 输出改进建议，通常不阻断 |

## 3. AI 代码审核协议

1. 先检查规则状态，再检查适用范围和语言版本。
2. 只对当前变更可证明的问题给出 `violation`；跨文件、运行时或设计背景不足时给出 `needs_review`。
3. `需项目确认` 和 `需修订原规范` 不得在未知项目配置下自动判违规。
4. 示例仅用于解释目标规则。示例中与目标规则无关的其他写法，不应被模型模仿或据此扩大规则。
5. 同一位置命中多个检查项时可合并描述，但必须列出全部检查项 ID。
6. 每个问题必须提供文件、行号、最小证据、原因、修复建议和置信度。
7. 不得用注释数量、代码风格等低风险问题掩盖内存安全、未定义行为或数据竞争问题。

### 3.1 审核结果建议格式

```json
{
  "rule_id": "CSTD-11.2",
  "check_id": "CSTD-11.2-01",
  "policy_status": "active",
  "result": "violation | advisory | needs_review | not_applicable | pass",
  "risk": "critical | high | medium | low",
  "file": "src/example.c",
  "line": 42,
  "evidence": "free(p); ... p = p->next",
  "reason": "释放 p 后再次读取 p->next。",
  "suggestion": "释放前保存 next 指针。",
  "confidence": 0.98
}
```

## 4. 规则索引

| 规则 ID | 名称 | 强度 | 状态 | 风险 | 审核方式 | 证据范围 |
|---|---|---|---|---|---|---|
| CSTD-3.1 | 缩进排版 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.2 | 对齐方法 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.3 | 添加空行 | MUST | 有效 | medium | hybrid | `line/file` |
| CSTD-3.4 | 代码行长度 | MUST | 需项目确认 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.5 | 单条语句 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.6 | 逻辑控制语句排版 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.7 | 程序块的分界符 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.8 | 操作符前后格式 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-3.9 | 文件末尾 | MUST | 有效 | medium | automatic-or-hybrid | `line/file` |
| CSTD-4.1 | 注释量 | MUST | 需项目确认 | medium | automatic-or-hybrid | `line/function/file` |
| CSTD-4.2 | 注释语言 | MUST | 需项目确认 | medium | automatic-or-hybrid | `line/function/file` |
| CSTD-4.3 | 注释格式 | MUST | 需修订原规范 | medium | automatic-or-hybrid | `line/function/file` |
| CSTD-4.4 | 文件的注释 | MUST | 有效，但示例有缺陷 | medium | hybrid | `line/function/file` |
| CSTD-4.5 | 函数的注释 | MUST | 有效，但示例有缺陷 | medium | hybrid | `line/function/file` |
| CSTD-4.6 | 代码注释内容要求 | MUST | 有效 | medium | manual | `line/function/file` |
| CSTD-4.7 | 注释缩写 | SHOULD | 有效 | low | manual | `line/function/file` |
| CSTD-4.8 | 注释位置 | MUST | 有效 | medium | automatic-or-hybrid | `line/function/file` |
| CSTD-4.9 | 变量及常量的注释 | MUST | 有效 | medium | manual | `line/function/file` |
| CSTD-4.10 | 数据结构的注释 | MUST | 有效 | medium | manual | `line/function/file` |
| CSTD-4.11 | 全局变量的注释 | SHOULD | 有效 | low | manual | `line/function/file` |
| CSTD-4.12 | 注释的排版 | MUST | 有效 | medium | hybrid | `line/function/file` |
| CSTD-4.13 | 逻辑控制语句的注释 | MUST | 需项目确认 | medium | hybrid | `line/function/file` |
| CSTD-4.14 | 代码屏蔽 | MUST | 有效 | medium | hybrid | `line/function/file` |
| CSTD-5.1 | 标识符的命名基本要求 | SHOULD | 有效 | low | manual | `identifier/file/project` |
| CSTD-5.2 | 命名中的注释 | MUST | 有效 | medium | manual | `identifier/file/project` |
| CSTD-5.3 | 命名风格的前后一致性 | MUST | 有效 | medium | manual | `identifier/file/project` |
| CSTD-5.4 | 命名风格的系统一致性 | MUST | 有效 | medium | manual | `identifier/file/project` |
| CSTD-5.5 | 禁用数字或奇怪的字符命名 | MUST | 有效 | medium | hybrid | `identifier/file/project` |
| CSTD-5.6 | 接口部分标示符命名 | MUST | 有效 | medium | manual | `identifier/file/project` |
| CSTD-5.7 | 函数的命名 | SHOULD | 有效 | low | manual | `identifier/file/project` |
| CSTD-5.8 | 下划线开始和结尾的定义 | SHOULD | 有效 | low | automatic-or-hybrid | `identifier/file/project` |
| CSTD-5.9 | 标识符长度 | MUST | 需项目确认 | medium | automatic-or-hybrid | `identifier/file/project` |
| CSTD-6.1 | 运算符的优先级 | MUST | 有效 | medium | hybrid | `expression/function` |
| CSTD-6.2 | 有意义标识的使用 | MUST | 有效 | medium | manual | `expression/function` |
| CSTD-6.3 | 关系紧密的代码位置 | SHOULD | 有效 | low | manual | `expression/function` |
| CSTD-6.4 | 语句的技巧性和易读性 | MUST | 有效 | medium | manual | `expression/function` |
| CSTD-6.5 | 逗号操作符 | MUST | 有效 | medium | automatic-or-hybrid | `expression/function` |
| CSTD-6.6 | 嵌套 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function` |
| CSTD-7.1 | 没有必要的公共变量 | SHOULD | 有效 | low | manual | `declaration/function/module` |
| CSTD-7.2 | 公共变量耦合度 | MUST | 有效 | medium | manual | `declaration/function/module` |
| CSTD-7.3 | 公共变量的数据传递 | MUST | 有效 | medium | manual | `declaration/function/module` |
| CSTD-7.4 | 局部变量与全局变量同名 | MUST | 有效 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.5 | 自动变量赋值 | MUST | 有效 | medium | hybrid | `declaration/function/module` |
| CSTD-7.6 | 数据类型的使用 | MUST | 有效，但示例有缺陷 | medium | hybrid | `declaration/function/module` |
| CSTD-7.7 | 八进制的使用 | MUST | 有效 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.8 | 结构体功能单一 | SHOULD | 有效 | low | manual | `declaration/function/module` |
| CSTD-7.9 | 结构体与结构体之间 | SHOULD | 有效 | low | manual | `declaration/function/module` |
| CSTD-7.10 | 结构体中元素的个数 | SHOULD | 有效 | low | manual | `declaration/function/module` |
| CSTD-7.11 | 结构体元素的布局及排列 | SHOULD | 有效 | low | manual | `declaration/function/module` |
| CSTD-7.12 | 数据类型转换 | MUST | 有效 | high | hybrid | `declaration/function/module` |
| CSTD-7.13 | 函数指针的类型转换 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.14 | 指针属性 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.15 | 常量 | MUST | 有效 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.16 | 重复定义类型 | MUST | 有效 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.17 | 对位域的定义 | MUST | 需项目确认 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.18 | 二进制的使用 | MUST | 需项目确认 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.19 | 十六进制转义字符、非标准转义字符、特殊字符 | MUST | 需项目确认 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.20 | 结构体初始化 | MUST | 有效 | medium | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.21 | 运算符左值右值取值范围 | MUST | 有效 | high | hybrid | `declaration/function/module` |
| CSTD-7.22 | 有符号数赋值 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.23 | 使用合适的存储期声明目标 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.24 | 使用正确语法声明柔性数组成员 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-7.25 | 越过可信边界传递结构体时应避免信息泄露 | MUST | 有效 | critical | hybrid | `declaration/function/module` |
| CSTD-7.26 | 不要将指针强制转换为对其要求更加严格的指针类型 | MUST | 有效 | high | automatic-or-hybrid | `declaration/function/module` |
| CSTD-8.1 | 数组大小 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function` |
| CSTD-8.2 | 数组初始化 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function` |
| CSTD-8.3 | 没有指向同一个数组的2个指针之间不能相减和比较 | MUST | 有效，但示例有缺陷 | high | automatic-or-hybrid | `expression/function` |
| CSTD-8.4 | 不要对指向非数组目标的指针进行加减 | MUST | 需项目确认 | high | automatic-or-hybrid | `expression/function` |
| CSTD-9.1 | 函数参数检查 | MUST | 有效 | medium | hybrid | `function/module` |
| CSTD-9.2 | 函数的参数处理 | MUST | 有效 | medium | hybrid | `function/module` |
| CSTD-9.3 | 函数的规模 | SHOULD | 有效 | low | manual | `function/module` |
| CSTD-9.4 | 为重复实现的功能编写函数 | SHOULD | 有效，但示例有缺陷 | low | manual | `function/module` |
| CSTD-9.5 | 函数功能的可预测性 | MUST | 有效 | medium | manual | `function/module` |
| CSTD-9.6 | 减少函数参数 | SHOULD | 有效 | low | hybrid | `function/module` |
| CSTD-9.7 | 函数形参 | MUST | 需项目确认 | medium | automatic-or-hybrid | `function/module` |
| CSTD-9.8 | 非调度函数的参数 | SHOULD | 有效 | low | manual | `function/module` |
| CSTD-9.9 | 函数参数输入与非参数输入的有效性 | MUST | 有效 | high | hybrid | `function/module` |
| CSTD-9.10 | 函数返回值 | MUST | 有效 | medium | hybrid | `function/module` |
| CSTD-9.11 | 函数的调用 | MUST | 需项目确认 | medium | hybrid | `function/module` |
| CSTD-9.12 | 禁止随机内聚 | MUST | 有效 | medium | manual | `function/module` |
| CSTD-9.13 | 高扇入、合理扇出的函数 | MUST | 需项目确认 | medium | manual | `function/module` |
| CSTD-9.14 | 递归函数 | MUST | 需项目确认 | medium | automatic-or-hybrid | `function/module` |
| CSTD-9.15 | 函数返回值的引用 | MUST | 需项目确认 | medium | hybrid | `function/module` |
| CSTD-9.16 | 函数出口唯一性 | MUST | 需项目确认 | medium | automatic-or-hybrid | `function/module` |
| CSTD-9.17 | 函数原型声明 | MUST | 有效 | medium | automatic-or-hybrid | `function/module` |
| CSTD-9.18 | 外部对象声明唯一性 | MUST | 有效 | medium | automatic-or-hybrid | `function/module` |
| CSTD-10.1 | 空间效率 | SHOULD | 有效 | low | manual | `function/module/runtime` |
| CSTD-10.2 | 循环体内工作量最小化 | SHOULD | 有效 | low | manual | `function/module/runtime` |
| CSTD-10.3 | 提高效率的其他方法 | MUST | 需修订原规范 | medium | manual | `function/module/runtime` |
| CSTD-11.1 | 防止内存操作越界 | MUST | 有效，但示例有缺陷 | critical | hybrid | `expression/function/module` |
| CSTD-11.2 | 禁止访问已经释放的内存空间 | MUST | 有效 | critical | hybrid | `expression/function/module` |
| CSTD-11.3 | 动态分配的内存已不再使用时应被及时释放 | MUST | 有效 | high | hybrid | `expression/function/module` |
| CSTD-11.4 | 模块的设置和配置更改权限 | MUST | 有效 | medium | manual | `expression/function/module` |
| CSTD-11.5 | 选择语句的分支语句 | MUST | 需修订原规范 | medium | automatic-or-hybrid | `expression/function/module` |
| CSTD-11.6 | 禁止使用goto语句 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function/module` |
| CSTD-11.7 | 汇编语句使用 | SHOULD | 有效 | low | manual | `expression/function/module` |
| CSTD-11.8 | 有符号数位操作 | MUST | 需项目确认 | high | automatic-or-hybrid | `expression/function/module` |
| CSTD-11.9 | 判断条件中的赋值语句 | MUST | 有效 | high | automatic-or-hybrid | `expression/function/module` |
| CSTD-11.10 | 判断条件 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function/module` |
| CSTD-11.11 | Continue语句 | MUST | 需项目确认 | medium | automatic-or-hybrid | `expression/function/module` |
| CSTD-12.1 | 函数宏 | MUST | 有效，但示例有缺陷 | medium | automatic-or-hybrid | `macro/file` |
| CSTD-12.2 | 宏参数 | MUST | 有效 | high | automatic-or-hybrid | `macro/file` |
| CSTD-12.3 | 宏内容 | MUST | 有效，但示例有缺陷 | high | automatic-or-hybrid | `macro/file` |
| CSTD-13.1 | 头文件内容 | MUST | 需项目确认 | medium | automatic-or-hybrid | `file/project` |
| CSTD-13.2 | 头文件要求 | MUST | 有效，但示例有缺陷 | medium | automatic-or-hybrid | `file/project` |
| CSTD-14.1 | 禁止销毁正在使用的互斥锁 | MUST | 有效 | high | hybrid | `module/runtime` |
| CSTD-14.2 | 多线程访问位域应防止数据竞争 | MUST | 有效，但示例有缺陷 | critical | hybrid | `module/runtime` |

## 5. 规则正文

### 第 3 章 书写格式

> 章节标签：`formatting`, `layout`

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.1","section":"3.1","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout","functions","loops"]} -->

#### CSTD-3.1｜3.1 缩进排版

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.1` |
| 原始章节 | `3.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout`, `functions`, `loops` |
| 摘要 | 程序块要采用缩进风格编写，缩进的英文空格数为4个。 |

##### 原子检查项

- `CSTD-3.1-01` [MUST] 程序块要采用缩进风格编写，缩进的英文空格数为4个。
- `CSTD-3.1-02` [MUST] 函数或过程的开始、结构的定义及循环、判断等语句中的代码需要采用缩进排版，case语句下的情况处理语句也需遵守缩进排版的要求。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

程序块要采用缩进风格编写，缩进的英文空格数为4个。对于由开发工具自动生成的代码允许有不一致。

函数或过程的开始、结构的定义及循环、判断等语句中的代码需要采用缩进排版，case语句下的情况处理语句也需遵守缩进排版的要求。

**示例：**

```c
if(data != 0)
{
    varible = data * 100;          /*  programe code  */
}
```

<!-- KB_CHUNK_END rule_id="CSTD-3.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.2","section":"3.2","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout"]} -->

#### CSTD-3.2｜3.2 对齐方法

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.2` |
| 原始章节 | `3.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout` |
| 摘要 | 对齐可使用空格键，也可使用Tab键，但是Tab必须等效为4个空格。 |

##### 原子检查项

- `CSTD-3.2-01` [MUST] 对齐可使用空格键，也可使用Tab键，但是Tab必须等效为4个空格。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对齐可使用空格键，也可使用Tab键，但是Tab必须等效为4个空格。

<!-- KB_CHUNK_END rule_id="CSTD-3.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.3","section":"3.3","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/file","tags":["formatting","layout"]} -->

#### CSTD-3.3｜3.3 添加空行

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.3` |
| 原始章节 | `3.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout` |
| 摘要 | 相对独立的程序块之间、变量说明之后必须加空行。 |

##### 原子检查项

- `CSTD-3.3-01` [MUST] 相对独立的程序块之间、变量说明之后必须加空行。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

相对独立的程序块之间、变量说明之后必须加空行。

**示例：**

**如下例子不符合规范：**

```c
if (!valid_ni(ni))
{
    /*  program code  */
}
repssn_ind = ssn_data[index].repssn_index;
repssn_ni = ssn_data[index].ni;
```

**应如下书写：**

```c
if (!valid_ni(ni))
{
    /*  program code  */
}
/* 添加空行 */
repssn_ind = ssn_data[index].repssn_index;
repssn_ni	= ssn_data[index].ni;
```

<!-- KB_CHUNK_END rule_id="CSTD-3.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.4","section":"3.4","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout","functions","loops"]} -->

#### CSTD-3.4｜3.4 代码行长度

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.4` |
| 原始章节 | `3.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout`, `functions`, `loops` |
| 摘要 | 一行代码的长度要合理，以小于80字符为宜，不要写得过长。 |

##### 原子检查项

- `CSTD-3.4-01` [MUST] 一行代码的长度要合理，以小于80字符为宜，不要写得过长。
- `CSTD-3.4-02` [MUST] 较长的逻辑运算语句（>80字符）要分成多行书写，每行应以“\”结束，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，划分出的新行要进行适当的缩进，使排版整齐，语句可读。
- `CSTD-3.4-03` [MUST] 循环、判断等语句中若有较长的表达式或语句，则要进行适当的划分，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，每行应以“\”结束。
- `CSTD-3.4-04` [MUST] 若函数或过程中的参数较长，则要进行适当的划分，每行应以“\”结束。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原文要求普通 C/C++ 长表达式换行时每行以反斜杠结束。现代 C/C++ 仅在预处理宏等需要行拼接的场景才需要反斜杠；普通表达式可直接在语法允许的位置换行。
- 在项目未明确确认前，不应因普通表达式换行未使用反斜杠而自动判违规。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

一行代码的长度要合理，以小于80字符为宜，不要写得过长。

较长的逻辑运算语句（>80字符）要分成多行书写，每行应以“\”结束，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，划分出的新行要进行适当的缩进，使排版整齐，语句可读。

**示例1：**

```c
perm_count_msg.head.len = NO7_TO_STAT_PERM_COUNT_LEN   \
    + STAT_SIZE_PER_FRAM * sizeof( _UL );
act_task_table[frame_id * STAT_TASK_CHECK_NUMBER + index].occupied   \
    = stat_poi[index].occupied;
act_task_table[taskno].duration_true_or_false   \
    = SYS_get_sccp_statistic_state( stat_item );
report_or_not_flag = ((taskno < MAX_ACT_TASK_NUMBER)   \
    && (n7stat_stat_item_valid (stat_item))&& (act_task_table[taskno].result_data != 0));
```

循环、判断等语句中若有较长的表达式或语句，则要进行适当的划分，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，每行应以“\”结束。

**示例2：**

```c
if ((taskno < max_act_task_number)        \
&& (n7stat_stat_item_valid (stat_item)))
{
    /*  program code  */
}
for (i = 0, j = 0; (i < BufferKeyword[word_index].word_length)      \
&& (j < NewKeyword.word_length); i++, j++)
{
    /*  program code  */
}
for (i = 0, j = 0;      \
(i < first_word_length) && (j < second_word_length);i++, j++)
{
    /*  program code  */
}
```

若函数或过程中的参数较长，则要进行适当的划分，每行应以“\”结束。

**示例3：**

```c
nvstat_str_compare((uint8 *) & stat_object,     \
                (uint8 *) & (act_task_table[taskno].stat_object),      \
                sizeof (_STAT_OBJECT));
nvstat_flash_act_duration(stat_item,frame_id * STAT_TASK_CHECK_NUMBER    \
    + index, stat_object );
```

<!-- KB_CHUNK_END rule_id="CSTD-3.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.5","section":"3.5","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout"]} -->

#### CSTD-3.5｜3.5 单条语句

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.5` |
| 原始章节 | `3.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout` |
| 摘要 | 不允许把多个短语句写在一行中，即一行只写一条语句。 |

##### 原子检查项

- `CSTD-3.5-01` [MUST] 不允许把多个短语句写在一行中，即一行只写一条语句。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不允许把多个短语句写在一行中，即一行只写一条语句。

**示例：**

**如下例子不符合规范：**

```c
rect.length = 0;  rect.width = 0;
```

**应如下书写：**

```c
rect.length = 0;
rect.width = 0;
```

<!-- KB_CHUNK_END rule_id="CSTD-3.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.6","section":"3.6","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout"]} -->

#### CSTD-3.6｜3.6 逻辑控制语句排版

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.6` |
| 原始章节 | `3.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout` |
| 摘要 | if、for、do、while、case、switch、default等语句自占一行，且if、for、do、while等语句的执行语句部分必须添加括号{}。 |

##### 原子检查项

- `CSTD-3.6-01` [MUST] if、for、do、while、case、switch、default等语句自占一行，且if、for、do、while等语句的执行语句部分必须添加括号{}。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

if、for、do、while、case、switch、default等语句自占一行，且if、for、do、while等语句的执行语句部分必须添加括号{}。

**示例：**

**如下例子不符合规范:**

```c
if (NULL == pUserCR)
return;
```

**应如下书写：**

```c
if (NULL == pUserCR)
{
return;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-3.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.7","section":"3.7","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout","functions"]} -->

#### CSTD-3.7｜3.7 程序块的分界符

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.7` |
| 原始章节 | `3.7` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout`, `functions` |
| 摘要 | 程序块分界符（如 `{`、`}`）应各自独占一行、处于同一列，并与引用它们的语句左对齐。 |

##### 原子检查项

- `CSTD-3.7-01` [MUST] 程序块分界符（如 `{`、`}`）应各自独占一行、处于同一列，并与引用它们的语句左对齐。
- `CSTD-3.7-02` [MUST] 函数体、类、结构体、枚举以及控制语句中的程序块应按规定缩进。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

程序块的分界符（如C/C++语言的大括号‘{’和‘}’）应各独占一行并且位于同一列，同时与引用它们的语句左对齐。在函数体的开始、类的定义、结构的定义、枚举的定义以及if、for、do、while、switch、case语句中的程序都要采用上文要求的缩进方式。

**示例：**

**如下例子不符合规范：**

```c
for (...) {
    /*  program code  */
}
if (...){
    /*  program code  */
}
void example_fun( void ){
    /*  program code  */
}
```

**应如下书写：**

```c
for (...)
{
    /*  program code  */
}
if (...)
{
    /*  program code  */
}
void example_fun( void )
{
    /*  program code  */
}
```

<!-- KB_CHUNK_END rule_id="CSTD-3.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.8","section":"3.8","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout","pointers","bit-fields","operators"]} -->

#### CSTD-3.8｜3.8 操作符前后格式

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.8` |
| 原始章节 | `3.8` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout`, `pointers`, `bit-fields`, `operators` |
| 摘要 | 二元比较、赋值、算术、逻辑和位运算符前后应加空格。 |

##### 原子检查项

- `CSTD-3.8-01` [MUST] 二元比较、赋值、算术、逻辑和位运算符前后应加空格。
- `CSTD-3.8-02` [MUST] 一元运算符与操作数之间不加空格。
- `CSTD-3.8-03` [MUST] 成员访问运算符 `->`、`.` 前后不加空格。
- `CSTD-3.8-04` [MUST] 括号内侧和多重括号之间不要求添加空格。
- `CSTD-3.8-05` [MUST] 不得为操作符保留两个及以上连续空格。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

在两个以上的关键字、变量、常量进行对等操作时，它们之间的操作符之前、之后或者前后要加空格；进行非对等操作时，如果是关系密切的立即操作符（如－>）后不要加空格。

在结构清晰的语句中不需要留空格。如果语句已足够清晰则括号内侧(即左括号后面和右括号前面)不需要加空格，多重括号间不必加空格。在长语句中，如果需要加的空格非常多，那么应该保证整体结构清晰，而在局部不加空格。给操作符不得留两个及以上的连续空格。

比较操作符, 赋值操作符"="、 "+="，算术操作符"+"、"%"，逻辑操作符"&&"、"||"，位域操作符"<<"、"^"等双目操作符的前后加空格，见示例1。 "!"、"~"、"++"、"--"、"&"（地址运算符）等单目操作符前后不加空格，见示例2。 "->"、"."前后不加空格，见示例3。

**示例1：**

```c
if (current_time >= MAX_TIME_VALUE)
a = b + c;
a *= 2;
a = b ^ 2;
```

**示例2：**

*p = 'a';	          // 内容操作"*"与内容之间不加空格

Flag = !isEmpty;    // 非操作"!"与内容之间不加空格

p = &mem;	  	  // 地址操作"&" 与内容之间不加空格

i++;	              // "++","--"与内容之间不加空格

**示例3：**

p->id = pid;		  // "->"指针前后不加空格

<!-- KB_CHUNK_END rule_id="CSTD-3.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-3.9","section":"3.9","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","tags":["formatting","layout"]} -->

#### CSTD-3.9｜3.9 文件末尾

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-3.9` |
| 原始章节 | `3.9` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/file` |
| 标签 | `formatting`, `layout` |
| 摘要 | 在文件末尾添加空行。 |

##### 原子检查项

- `CSTD-3.9-01` [MUST] 在文件末尾添加空行。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

在文件末尾添加空行。

<!-- KB_CHUNK_END rule_id="CSTD-3.9" -->

### 第 4 章 注释

> 章节标签：`comments`, `documentation`

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.1","section":"4.1","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.1｜4.1 注释量

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.1` |
| 原始章节 | `4.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 源程序有效注释量(Code line)必须在20％以上。 |

##### 原子检查项

- `CSTD-4.1-01` [MUST] 源程序有效注释量(Code line)必须在20％以上。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- “有效注释量必须在 20% 以上”属于可量化但容易被无意义注释满足的项目指标，不能替代注释质量审核。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

源程序有效注释量(Code line)必须在20％以上。

<!-- KB_CHUNK_END rule_id="CSTD-4.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.2","section":"4.2","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.2｜4.2 注释语言

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.2` |
| 原始章节 | `4.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 注释语言必须使用英文。 |

##### 原子检查项

- `CSTD-4.2-01` [MUST] 注释语言必须使用英文。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 注释必须使用英语属于团队语言政策，不是通用 C/C++ 正确性要求。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

注释语言必须使用英文。

<!-- KB_CHUNK_END rule_id="CSTD-4.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.3","section":"4.3","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.3｜4.3 注释格式

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.3` |
| 原始章节 | `4.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需修订原规范 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 注释格式必须统一，使用“/* …… */”，在注释中不得使用字符“/*”及“*/”。 |

##### 原子检查项

- `CSTD-4.3-01` [MUST] 注释格式必须统一，使用“/* …… */”，在注释中不得使用字符“/*”及“*/”。

##### 审核判定

- 默认行为：`needs_review`：原规范存在技术冲突，修订前不自动判违规。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- C99 及 C++ 支持 `//` 注释；仅允许 `/* ... */` 属于项目风格政策。
- 原文禁止在块注释中再次出现块注释定界符的要求是合理的，因为 C/C++ 块注释不可嵌套。
- 原规范其他章节的示例多次使用 `//`，与本条“只使用块注释”的要求内部不一致；应先统一项目决定。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

注释格式必须统一，使用“/* …… */”，在注释中不得使用字符“/*”及“*/”。

<!-- KB_CHUNK_END rule_id="CSTD-4.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.4","section":"4.4","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","tags":["comments","documentation","functions","headers"]} -->

#### CSTD-4.4｜4.4 文件的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.4` |
| 原始章节 | `4.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation`, `functions`, `headers` |
| 摘要 | 说明性文件（如头文件.h文件）头部应进行注释。 |

##### 原子检查项

- `CSTD-4.4-01` [MUST] 说明性文件（如头文件.h文件）头部应进行注释。
- `CSTD-4.4-02` [MUST] 注释必须列出：版权说明、版本号、生成日期、作者、内容、功能、与其它文件的关系、修改日志等，头文件的注释中还应有函数功能简要说明。
- `CSTD-4.4-03` [MUST] 推荐图1所示头文件的头注释格式，无论使用何种格式都必须包含上述信息，每个项目中的头注释格式应相同。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原文引用“图1”，但源文件中没有实际图像或完整模板；不得据此臆造缺失格式。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

说明性文件（如头文件.h文件）头部应进行注释。

注释必须列出：版权说明、版本号、生成日期、作者、内容、功能、与其它文件的关系、修改日志等，头文件的注释中还应有函数功能简要说明。

推荐图1所示头文件的头注释格式，无论使用何种格式都必须包含上述信息，每个项目中的头注释格式应相同。

图1 头文件注释

<!-- KB_CHUNK_END rule_id="CSTD-4.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.5","section":"4.5","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","tags":["comments","documentation","functions"]} -->

#### CSTD-4.5｜4.5 函数的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.5` |
| 原始章节 | `4.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation`, `functions` |
| 摘要 | 函数头部注释应包含函数目的或功能、输入参数、输出参数、返回值和调用关系等信息。 |

##### 原子检查项

- `CSTD-4.5-01` [MUST] 函数头部注释应包含函数目的或功能、输入参数、输出参数、返回值和调用关系等信息。
- `CSTD-4.5-02` [MUST] 同一项目中的函数注释格式应保持一致。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原函数注释示例使用了多个 `/*` 且结尾定界不完整，不能直接复制为合法 C/C++ 注释模板；应只采用其字段要求。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数头部的注释要列出：函数的目的/功能、输入参数、输出参数、返回值、调用关系（函数、表）等。推荐如下示例中的函数注释格式，无论使用何种格式都必须包含上述信息，每个项目中的函数注释格式应相同。

**示例：**

```c
/***********************************************************
/* Function name: MyFunc( uint8 X)
/* Description: Short Description, including preconditions
/* Parameter X : Description
/* Return value: None
/* Remarks: global variables used, side effects
/***********************************************************/
Void MyFunc( uint8 X)
```

<!-- KB_CHUNK_END rule_id="CSTD-4.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.6","section":"4.6","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.6｜4.6 代码注释内容要求

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.6` |
| 原始章节 | `4.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 保证注释与代码的一致性。 |

##### 原子检查项

- `CSTD-4.6-01` [MUST] 保证注释与代码的一致性。
- `CSTD-4.6-02` [MUST] 无用的注释要删除。
- `CSTD-4.6-03` [MUST] 注释的内容要清楚、明了，含义准确，防止注释二义性。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

保证注释与代码的一致性。无用的注释要删除。注释的内容要清楚、明了，含义准确，防止注释二义性。在代码的功能、意图层次上进行注释，提供有用、额外的信息。

**示例：**

如下注释无用可删除：

```c
/* if receive_flag is TRUE */
if (receive_flag)
```

如下的注释为有效注释：

```c
/* if mtp receive a message from links */
if (receive_flag)
```

<!-- KB_CHUNK_END rule_id="CSTD-4.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.7","section":"4.7","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.7｜4.7 注释缩写

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.7` |
| 原始章节 | `4.7` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 避免在注释中使用缩写，特别是非常用缩写。 |

##### 原子检查项

- `CSTD-4.7-01` [SHOULD] 避免在注释中使用缩写，特别是非常用缩写。
- `CSTD-4.7-02` [SHOULD] 在使用缩写时或之前，应对缩写进行必要的说明。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

避免在注释中使用缩写，特别是非常用缩写。 在使用缩写时或之前，应对缩写进行必要的说明。

<!-- KB_CHUNK_END rule_id="CSTD-4.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.8","section":"4.8","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.8｜4.8 注释位置

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.8` |
| 原始章节 | `4.8` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 注释应与其描述的代码相近，对代码的注释（对单条语句、变量、常量、数据结构等的注释）应放在其上方或右方相邻位置，不可放在下面。 |

##### 原子检查项

- `CSTD-4.8-01` [MUST] 注释应与其描述的代码相近，对代码的注释（对单条语句、变量、常量、数据结构等的注释）应放在其上方或右方相邻位置，不可放在下面。
- `CSTD-4.8-02` [MUST] 禁止在一行代码或表达式中间插入注释，否则容易使代码可理解性变差。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

注释应与其描述的代码相近，对代码的注释（对单条语句、变量、常量、数据结构等的注释）应放在其上方或右方相邻位置，不可放在下面。

禁止在一行代码或表达式中间插入注释，否则容易使代码可理解性变差。

**示例：**

**如下例子不符合规范：**

```c
repssn_ind = ssn_data[index].repssn_index;
repssn_ni = ssn_data[index].ni;
/* get replicate sub system index and net indicator */
```

**应如下书写：**

```c
/* get replicate sub system index and net indicator */
repssn_ind = ssn_data[index].repssn_index;
repssn_ni = ssn_data[index].ni;
```

<!-- KB_CHUNK_END rule_id="CSTD-4.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.9","section":"4.9","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.9｜4.9 变量及常量的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.9` |
| 原始章节 | `4.9` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 对于所有具有物理含义的变量、常量，如果其命名不是充分自注释的，在声明时都必须加以注释，说明其物理含义。 |

##### 原子检查项

- `CSTD-4.9-01` [MUST] 对于所有具有物理含义的变量、常量，如果其命名不是充分自注释的，在声明时都必须加以注释，说明其物理含义。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对于所有具有物理含义的变量、常量，如果其命名不是充分自注释的，在声明时都必须加以注释，说明其物理含义。

**示例：**

```c
/* active statistic task number */
#define MAX_ACT_TASK_NUMBER 1000
```

或

```c
#define MAX_ACT_TASK_NUMBER 1000 /* active statistic task number */
```

<!-- KB_CHUNK_END rule_id="CSTD-4.9" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.10","section":"4.10","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","tags":["comments","documentation","arrays","structs"]} -->

#### CSTD-4.10｜4.10 数据结构的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.10` |
| 原始章节 | `4.10` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation`, `arrays`, `structs` |
| 摘要 | 数据结构声明(包括数组、结构体、枚举等)，如果其命名不是充分自注释的，必须加以注释。 |

##### 原子检查项

- `CSTD-4.10-01` [MUST] 数据结构声明(包括数组、结构体、枚举等)，如果其命名不是充分自注释的，必须加以注释。
- `CSTD-4.10-02` [MUST] 对数据结构的注释应放在其上方相邻位置；对结构体中的每个域的注释放在此域的右方。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

数据结构声明(包括数组、结构体、枚举等)，如果其命名不是充分自注释的，必须加以注释。

对数据结构的注释应放在其上方相邻位置；对结构体中的每个域的注释放在此域的右方。

**示例：**

**可按如下形式说明枚举、数据、联合结构：**

```c
/* sccp interface with sccp user primitive message name */
enum SCCP_USER_PRIMITIVE
{N_UNITDATA_IND, /* sccp notify sccp user unit data come */
    N_NOTICE_IND,/* sccp notify user the No.7 network can not transmission this message */
    N_UNITDATA_REQ /* sccp user's unit data transmission request*/
};
```

<!-- KB_CHUNK_END rule_id="CSTD-4.10" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.11","section":"4.11","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"line/function/file","tags":["comments","documentation","functions"]} -->

#### CSTD-4.11｜4.11 全局变量的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.11` |
| 原始章节 | `4.11` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation`, `functions` |
| 摘要 | 全局变量要有较详细的注释，包括对其功能、取值范围、哪些函数或过程存取它以及存取时注意事项等说明。 |

##### 原子检查项

- `CSTD-4.11-01` [SHOULD] 全局变量要有较详细的注释，包括对其功能、取值范围、哪些函数或过程存取它以及存取时注意事项等说明。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

全局变量要有较详细的注释，包括对其功能、取值范围、哪些函数或过程存取它以及存取时注意事项等说明。

**示例：**

```c
/* The ErrorCode when SCCP translate */
/* Global Title failure, as follows */
/* 0 － SUCCESS	1 － GT Table error */
/* 2 － GT error  Others － no use	*/
/* only function SCCPTranslate() in */
/* this modual can modify it,	and	other module can visit it through call */
/* the function GetGTTransErrorCode() */	uint8 g_GTTranErrorCode;
```

<!-- KB_CHUNK_END rule_id="CSTD-4.11" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.12","section":"4.12","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.12｜4.12 注释的排版

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.12` |
| 原始章节 | `4.12` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 为使程序排版整齐，并方便注释的阅读与理解，注释应与所描述内容进行同样的缩排。 |

##### 原子检查项

- `CSTD-4.12-01` [MUST] 为使程序排版整齐，并方便注释的阅读与理解，注释应与所描述内容进行同样的缩排。
- `CSTD-4.12-02` [MUST] 注释应与其上的代码用空行隔开。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

为使程序排版整齐，并方便注释的阅读与理解，注释应与所描述内容进行同样的缩排。

**示例1：**

```c
void example_fun( void )
{    CodeBlock One  /* code one comments */
    CodeBlock Two  /* code two comments */
}
```

注释应与其上的代码用空行隔开。

**示例2：**

**如下例子，显得代码过于紧凑：**

```c
/* code one comments */
```

program code one

```c
/* code two comments */
```

program code two

**应如下书写：**

```c
/* code one comments */
```

program code one

```c
//空行
/* code two comments */
```

program code two

<!-- KB_CHUNK_END rule_id="CSTD-4.12" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.13","section":"4.13","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","tags":["comments","documentation","loops"]} -->

#### CSTD-4.13｜4.13 逻辑控制语句的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.13` |
| 原始章节 | `4.13` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation`, `loops` |
| 摘要 | 对条件分支、循环语句等逻辑控制语句必须编写注释。 |

##### 原子检查项

- `CSTD-4.13-01` [MUST] 对条件分支、循环语句等逻辑控制语句必须编写注释。
- `CSTD-4.13-02` [MUST] 对于switch语句下的case语句，如果因为特殊情况需要处理完一个case后进入下一个case处理，必须在该case语句处理完、下一个case语句前加上明确的注释。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 要求每个条件分支和循环都写注释可能产生复述代码的低价值注释；建议重点审核复杂意图、边界原因和有意 fallthrough。
- 本条允许带明确注释的 case fallthrough，但 CSTD-11.5 又要求所有非空 case 以 break 结束，两条规则需由项目统一。
- 原文中的“正文件切分”为文档处理残留，已清除。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对条件分支、循环语句等逻辑控制语句必须编写注释。

对于switch语句下的case语句，如果因为特殊情况需要处理完一个case后进入下一个case处理，必须在该case语句处理完、下一个case语句前加上明确的注释。

**示例：**

```c
case CMD_FWD:
    ProcessFwd();
if (...)
{
        break;
}
else
{
        ProcessCFW_B();	// now jump into case CMD_A
}
case CMD_A:
    ProcessA();
    break;
```

<!-- KB_CHUNK_END rule_id="CSTD-4.13" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-4.14","section":"4.14","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","tags":["comments","documentation"]} -->

#### CSTD-4.14｜4.14 代码屏蔽

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-4.14` |
| 原始章节 | `4.14` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `line/function/file` |
| 标签 | `comments`, `documentation` |
| 摘要 | 代码段不予编译或需屏蔽的地方，应该使用条件编译实现（如带注释的#if或 #ifdef结构）。 |

##### 原子检查项

- `CSTD-4.14-01` [MUST] 代码段不予编译或需屏蔽的地方，应该使用条件编译实现（如带注释的#if或 #ifdef结构）。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`line/function/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

代码段不予编译或需屏蔽的地方，应该使用条件编译实现（如带注释的#if或 #ifdef结构）。

<!-- KB_CHUNK_END rule_id="CSTD-4.14" -->

### 第 5 章 命名规则

> 章节标签：`naming`

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.1","section":"5.1","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.1｜5.1 标识符的命名基本要求

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.1` |
| 原始章节 | `5.1` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 标识符的命名要清晰、明了，有明确含义，同时使用完整的单词或大家基本可以理解的缩写，避免使人产生误解。 |

##### 原子检查项

- `CSTD-5.1-01` [SHOULD] 标识符的命名要清晰、明了，有明确含义，同时使用完整的单词或大家基本可以理解的缩写，避免使人产生误解。
- `CSTD-5.1-02` [SHOULD] 较短的单词可通过去掉“元音”形成缩写；较长的单词可取单词的头几个字母形成缩写；宜用大家公认的缩写单词。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

标识符的命名要清晰、明了，有明确含义，同时使用完整的单词或大家基本可以理解的缩写，避免使人产生误解。

较短的单词可通过去掉“元音”形成缩写；较长的单词可取单词的头几个字母形成缩写；宜用大家公认的缩写单词。

**示例：**

temp可缩写为tmp; flag可缩写为flg; statistic可缩写为stat ; increment 可缩写为inc; message可缩写为msg。

<!-- KB_CHUNK_END rule_id="CSTD-5.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.2","section":"5.2","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming","comments"]} -->

#### CSTD-5.2｜5.2 命名中的注释

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.2` |
| 原始章节 | `5.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming`, `comments` |
| 摘要 | 命名中若使用特殊约定或难以理解的缩写，要有注释说明。 |

##### 原子检查项

- `CSTD-5.2-01` [MUST] 命名中若使用特殊约定或难以理解的缩写，要有注释说明。
- `CSTD-5.2-02` [MUST] 应该在源文件的开始之处，对文件中所使用的缩写或约定，特别是特殊的缩写，进行必要的注释说明。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

命名中若使用特殊约定或难以理解的缩写，要有注释说明。

应该在源文件的开始之处，对文件中所使用的缩写或约定，特别是特殊的缩写，进行必要的注释说明。

<!-- KB_CHUNK_END rule_id="CSTD-5.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.3","section":"5.3","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.3｜5.3 命名风格的前后一致性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.3` |
| 原始章节 | `5.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 自己特有的命名风格，要自始至终保持一致，不可来回变化。 |

##### 原子检查项

- `CSTD-5.3-01` [MUST] 自己特有的命名风格，要自始至终保持一致，不可来回变化。
- `CSTD-5.3-02` [MUST] 个人的命名风格，在符合所在项目组或产品组的命名规则的前提下，才可使用（即命名规则中没有规定到的地方才可有个人命名风格）。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

自己特有的命名风格，要自始至终保持一致，不可来回变化。

个人的命名风格，在符合所在项目组或产品组的命名规则的前提下，才可使用（即命名规则中没有规定到的地方才可有个人命名风格）。

<!-- KB_CHUNK_END rule_id="CSTD-5.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.4","section":"5.4","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.4｜5.4 命名风格的系统一致性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.4` |
| 原始章节 | `5.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 命名规范必须与所使用的系统风格保持一致，并在同一项目中统一。 |

##### 原子检查项

- `CSTD-5.4-01` [MUST] 命名规范必须与所使用的系统风格保持一致，并在同一项目中统一。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

命名规范必须与所使用的系统风格保持一致，并在同一项目中统一。比如采用全小写加下划线的风格或大小写混排的方式。

<!-- KB_CHUNK_END rule_id="CSTD-5.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.5","section":"5.5","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.5｜5.5 禁用数字或奇怪的字符命名

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.5` |
| 原始章节 | `5.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 命名中不能出现无意义的数字或奇怪字符。 |

##### 原子检查项

- `CSTD-5.5-01` [MUST] 命名中不能出现无意义的数字或奇怪字符。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

命名中不能出现无意义的数字或奇怪字符。

**示例：**

不可使用如下命名。

```c
#define EXAMPLE_0_TEST_
#define EXAMPLE_1_TEST_
void set_sls00( uint8 sls );
```

<!-- KB_CHUNK_END rule_id="CSTD-5.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.6","section":"5.6","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.6｜5.6 接口部分标示符命名

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.6` |
| 原始章节 | `5.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 对接口部分的标识符应该有更严格限制，防止冲突。 |

##### 原子检查项

- `CSTD-5.6-01` [MUST] 对接口部分的标识符应该有更严格限制，防止冲突。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对接口部分的标识符应该有更严格限制，防止冲突。如可规定接口部分的变量与常量之前加上“模块”标识等。

<!-- KB_CHUNK_END rule_id="CSTD-5.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.7","section":"5.7","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"identifier/file/project","tags":["naming","functions","concurrency"]} -->

#### CSTD-5.7｜5.7 函数的命名

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.7` |
| 原始章节 | `5.7` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming`, `functions`, `concurrency` |
| 摘要 | 具有互斥含义的变量或相反动作的函数，宜使用成对且语义正确的反义词命名。 |

##### 原子检查项

- `CSTD-5.7-01` [SHOULD] 具有互斥含义的变量或相反动作的函数，宜使用成对且语义正确的反义词命名。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

用正确的反义词组命名具有互斥意义的变量或相反动作的函数等。

下面是一些在软件中常用的反义词组：

add / remove、begin / end、create / destroy、insert / delete、first / last、get / release、increment / decrement 、put / get、add / delete、lock / unlock、open / close、min / max、old / new、start / stop、next / previous、source / target、show / hide、send / receive、source / destination、cut / paste、up / down。

**示例：**

```c
uint32  min_sum;
uint32  max_sum;
uint32  add_user( uint8 *user_name );
uint32  delete_user( uint8 *user_name );
```

<!-- KB_CHUNK_END rule_id="CSTD-5.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.8","section":"5.8","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"automatic-or-hybrid","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.8｜5.8 下划线开始和结尾的定义

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.8` |
| 原始章节 | `5.8` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 避免使用_EXAMPLE_TEST_之类以下划线开始和结尾的定义。 |

##### 原子检查项

- `CSTD-5.8-01` [SHOULD] 避免使用_EXAMPLE_TEST_之类以下划线开始和结尾的定义。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

避免使用_EXAMPLE_TEST_之类以下划线开始和结尾的定义。

<!-- KB_CHUNK_END rule_id="CSTD-5.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-5.9","section":"5.9","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"identifier/file/project","tags":["naming"]} -->

#### CSTD-5.9｜5.9 标识符长度

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-5.9` |
| 原始章节 | `5.9` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `identifier/file/project` |
| 标签 | `naming` |
| 摘要 | 标识符长度不能超过31个字符。 |

##### 原子检查项

- `CSTD-5.9-01` [MUST] 标识符长度不能超过31个字符。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`identifier/file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 31 字符上限源于历史实现限制；现代工具链通常支持更长标识符。若保留，应作为项目兼容性政策。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

标识符长度不能超过31个字符。

<!-- KB_CHUNK_END rule_id="CSTD-5.9" -->

### 第 6 章 可读性

> 章节标签：`readability`

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.1","section":"6.1","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"expression/function","tags":["readability","operators"]} -->

#### CSTD-6.1｜6.1 运算符的优先级

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.1` |
| 原始章节 | `6.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `readability`, `operators` |
| 摘要 | 应使用括号明确表达式的求值顺序，避免依赖不易理解的默认运算符优先级。 |

##### 原子检查项

- `CSTD-6.1-01` [SHOULD] 应使用括号明确表达式的求值顺序，避免依赖不易理解的默认运算符优先级。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

注意运算符的优先级，并用括号明确表达式的操作顺序，避免使用默认优先级。

**示例：**

下列语句中的表达式：

```c
word = (high << 8) | low
if ((a | b) && (a & c))
if ((a | b) < (c & d))
```

不得书写为：

```c
word = high << 8 | low																(1)
if (a | b && a & c)                                                                	(2)
if (a | b < c & d)                                                                  	(3)
```

由于

```c
high << 8 | low = ( high << 8) | low,
```

a | b && a & c = (a | b) && (a & c)，(1)(2)不会出错，但语句不易理解；

a | b < c & d = a |（b < c）& d,(3)造成了判断条件出错。

<!-- KB_CHUNK_END rule_id="CSTD-6.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.2","section":"6.2","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function","tags":["readability","macros"]} -->

#### CSTD-6.2｜6.2 有意义标识的使用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.2` |
| 原始章节 | `6.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `expression/function` |
| 标签 | `readability`, `macros` |
| 摘要 | 避免使用不易理解的数字，用有意义的标识来替代。 |

##### 原子检查项

- `CSTD-6.2-01` [SHOULD] 避免使用不易理解的数字，用有意义的标识来替代。
- `CSTD-6.2-02` [MUST] 涉及物理状态或者含有物理意义的常量，不应直接使用数字，必须用有意义的枚举或宏来代替。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

避免使用不易理解的数字，用有意义的标识来替代。涉及物理状态或者含有物理意义的常量，不应直接使用数字，必须用有意义的枚举或宏来代替。

**示例：**

如下的程序可读性差：

```c
if (0 ==   Trunk[index].trunk_state)
{
    Trunk[index].trunk_state = 1;
    /* program code */
}
```

**应改为如下形式：**

```c
#define TRUNK_IDLE 0
#define TRUNK_BUSY 1
if (TRUNK_IDLE == Trunk[index].trunk_state)
{
    Trunk[index].trunk_state = TRUNK_BUSY;
    /* program code */
}
```

<!-- KB_CHUNK_END rule_id="CSTD-6.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.3","section":"6.3","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"expression/function","tags":["readability"]} -->

#### CSTD-6.3｜6.3 关系紧密的代码位置

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.3` |
| 原始章节 | `6.3` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `expression/function` |
| 标签 | `readability` |
| 摘要 | 关系紧密的代码宜相邻放置，以便阅读和查找。 |

##### 原子检查项

- `CSTD-6.3-01` [SHOULD] 关系紧密的代码宜相邻放置，以便阅读和查找。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

使关系密切的代码位置相邻便于程序阅读和查找。

**示例：**

以下代码布局不太合理：

```c
rect.length = 10;
char_poi = str;
rect.width = 5;
```

若按如下形式书写，可能更清晰一些。

```c
rect.length = 10;
```

rect.width = 5; // 矩形的长与宽关系较密切，放在一起。

```c
char_poi = str;
```

<!-- KB_CHUNK_END rule_id="CSTD-6.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.4","section":"6.4","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function","tags":["readability"]} -->

#### CSTD-6.4｜6.4 语句的技巧性和易读性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.4` |
| 原始章节 | `6.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `expression/function` |
| 标签 | `readability` |
| 摘要 | 表达式的值必须在任何求值顺序下保持一致，不要使用难懂的技巧性很高的语句。 |

##### 原子检查项

- `CSTD-6.4-01` [MUST] 表达式的值必须在任何求值顺序下保持一致，不要使用难懂的技巧性很高的语句。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

表达式的值必须在任何求值顺序下保持一致，不要使用难懂的技巧性很高的语句。

**示例：**

如下表达式，考虑不周就可能出问题，也较难理解。

```c
* stat_poi++ += 1;
* ++stat_poi += 1;
```

应分别改为如下。

```c
*stat_poi += 1;
```

stat_poi++;	// 此二语句功能相当于“ * stat_poi ++ += 1; ”

```c
++stat_poi;
```

*stat_poi += 1; // 此二语句功能相当于“ * ++ stat_poi += 1; ”

<!-- KB_CHUNK_END rule_id="CSTD-6.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.5","section":"6.5","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["readability"]} -->

#### CSTD-6.5｜6.5 逗号操作符

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.5` |
| 原始章节 | `6.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `readability` |
| 摘要 | 不允许使用逗号操作符，为防止阅读混乱，逗号操作符可用其他等价形式替换。 |

##### 原子检查项

- `CSTD-6.5-01` [MUST] 不允许使用逗号操作符，为防止阅读混乱，逗号操作符可用其他等价形式替换。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不允许使用逗号操作符，为防止阅读混乱，逗号操作符可用其他等价形式替换。

<!-- KB_CHUNK_END rule_id="CSTD-6.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-6.6","section":"6.6","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["readability"]} -->

#### CSTD-6.6｜6.6 嵌套

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-6.6` |
| 原始章节 | `6.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `readability` |
| 摘要 | 圆括号嵌套不超过32级。 |

##### 原子检查项

- `CSTD-6.6-01` [MUST] 圆括号嵌套不超过32级。
- `CSTD-6.6-02` [MUST] if-else嵌套不超过15级。
- `CSTD-6.6-03` [MUST] #include文件不超过8级。
- `CSTD-6.6-04` [MUST] #if 嵌套不超过8级。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 固定嵌套层数与编译器、静态分析器和项目复杂度预算有关，应由项目确认。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

嵌套规则为：

- 圆括号嵌套不超过32级。
- if-else嵌套不超过15级。
- #include文件不超过8级。
- #if 嵌套不超过8级。

<!-- KB_CHUNK_END rule_id="CSTD-6.6" -->

### 第 7 章 常量、变量、结构体

> 章节标签：`types`, `variables`, `structs`

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.1","section":"7.1","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.1｜7.1 没有必要的公共变量

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.1` |
| 原始章节 | `7.1` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 公共变量是增大模块间耦合的原因之一，故减少没必要的公共变量以降低模块间的耦合度。 |

##### 原子检查项

- `CSTD-7.1-01` [SHOULD] 公共变量是增大模块间耦合的原因之一，故减少没必要的公共变量以降低模块间的耦合度。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

公共变量是增大模块间耦合的原因之一，故减少没必要的公共变量以降低模块间的耦合度。

<!-- KB_CHUNK_END rule_id="CSTD-7.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.2","section":"7.2","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs","functions"]} -->

#### CSTD-7.2｜7.2 公共变量耦合度

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.2` |
| 原始章节 | `7.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `functions` |
| 摘要 | 降低公共变量的耦合度，构造仅有一个模块或函数可以修改、创建，而其余有关模块或函数只访问的公共变量，禁止多个不同模块或函数都可以修改、创建同一公共变量的现象。 |

##### 原子检查项

- `CSTD-7.2-01` [MUST] 降低公共变量的耦合度，构造仅有一个模块或函数可以修改、创建，而其余有关模块或函数只访问的公共变量，禁止多个不同模块或函数都可以修改、创建同一公共变量的现象。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

降低公共变量的耦合度，构造仅有一个模块或函数可以修改、创建，而其余有关模块或函数只访问的公共变量，禁止多个不同模块或函数都可以修改、创建同一公共变量的现象。

<!-- KB_CHUNK_END rule_id="CSTD-7.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.3","section":"7.3","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.3｜7.3 公共变量的数据传递

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.3` |
| 原始章节 | `7.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 当向公共变量传递数据时，要防止赋予不合理的值或越界等现象发生。 |

##### 原子检查项

- `CSTD-7.3-01` [MUST] 当向公共变量传递数据时，要防止赋予不合理的值或越界等现象发生。
- `CSTD-7.3-02` [MUST] 对公共变量赋值时，应有必要进行合法性检查，以提高代码的可靠性、稳定性。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

当向公共变量传递数据时，要防止赋予不合理的值或越界等现象发生。

对公共变量赋值时，应有必要进行合法性检查，以提高代码的可靠性、稳定性。

<!-- KB_CHUNK_END rule_id="CSTD-7.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.4","section":"7.4","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.4｜7.4 局部变量与全局变量同名

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.4` |
| 原始章节 | `7.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 禁止局部变量与全局变量同名。 |

##### 原子检查项

- `CSTD-7.4-01` [MUST] 禁止局部变量与全局变量同名。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止局部变量与全局变量同名。

<!-- KB_CHUNK_END rule_id="CSTD-7.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.5","section":"7.5","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.5｜7.5 自动变量赋值

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.5` |
| 原始章节 | `7.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 所有的自动变量在使用前都应被赋值。 |

##### 原子检查项

- `CSTD-7.5-01` [MUST] 所有的自动变量在使用前都应被赋值。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

所有的自动变量在使用前都应被赋值。

<!-- KB_CHUNK_END rule_id="CSTD-7.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.6","section":"7.6","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.6｜7.6 数据类型的使用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.6` |
| 原始章节 | `7.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 必须用typedef 显式标识出各数据类型的长度和符号特性,避免直接使用标准数据类型。 |

##### 原子检查项

- `CSTD-7.6-01` [MUST] 必须用typedef 显式标识出各数据类型的长度和符号特性,避免直接使用标准数据类型。
- `CSTD-7.6-02` [MUST] 不可使用_BOOL关键字。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 固定宽度整数优先使用 `<stdint.h>` 的 `int8_t`、`uint32_t` 等类型。
- 原示例把 `signed long` 定义为 `int64_t`，但 `long` 并不保证为 64 位，示例不可作为跨平台依据。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

必须用typedef 显式标识出各数据类型的长度和符号特性,避免直接使用标准数据类型。

不可使用_BOOL关键字。

**示例：**

一个32 位的整数系统,可定义如下:

```c
typedef char char_t ;
typedef signed char int8_t ;
typedef signed short int16_t ;
typedef signed int int32_t ;
typedef signed long int64_t ;
typedef unsigned char uint8_t ;
typedef unsigned short uint16_t ;
typedef unsigned int uint32_t ;
typedef unsigned long uint64_t ;
```

<!-- KB_CHUNK_END rule_id="CSTD-7.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.7","section":"7.7","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.7｜7.7 八进制的使用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.7` |
| 原始章节 | `7.7` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 不得使用八进制常数(0除外) 或八进制转义符。 |

##### 原子检查项

- `CSTD-7.7-01` [MUST] 不得使用八进制常数(0除外) 或八进制转义符。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不得使用八进制常数(0除外) 或八进制转义符。

<!-- KB_CHUNK_END rule_id="CSTD-7.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.8","section":"7.8","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.8｜7.8 结构体功能单一

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.8` |
| 原始章节 | `7.8` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 结构体的功能要单一，是针对一种事务的抽象。 |

##### 原子检查项

- `CSTD-7.8-01` [MUST] 结构体的功能要单一，是针对一种事务的抽象。
- `CSTD-7.8-02` [SHOULD] 设计结构体时应力争使结构体代表一种现实事务的抽象，而不是同时代表多种。
- `CSTD-7.8-03` [MUST] 结构体中的各元素应代表同一事务的不同侧面，而不应把描述没有关系或关系很弱的不同事务的元素放到同一结构体中。
- `CSTD-7.8-04` [SHOULD] 不要设计面面俱到、非常灵活的数据结构。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

结构体的功能要单一，是针对一种事务的抽象。设计结构体时应力争使结构体代表一种现实事务的抽象，而不是同时代表多种。结构体中的各元素应代表同一事务的不同侧面，而不应把描述没有关系或关系很弱的不同事务的元素放到同一结构体中。

不要设计面面俱到、非常灵活的数据结构。

**示例1所示设计不够合理，应改为示例2。**

**示例1：**

```c
typedef struct STUDENT_STRU
{
    uint8 name[8]; /* student's name */
    uint8 age;	/* student's age */
    uint8 sex;	/* student's sex, as follows */
    /* 0 - FEMALE; 1 - MALE */
    uint8 teacher_name[8]; /* the student teacher's name */
    uint8 teacher_sex;	/* his teacher sex */
} STUDENT;
```

**示例2：**

```c
typedef struct TEACHER_STRU
{
    uint8 name[8]; /* teacher name */
    uint8 sex;	/* teacher sex, as follows */
    /* 0 - FEMALE; 1 - MALE */
} TEACHER;
typedef struct STUDENT_STRU
{
    uint8 name[8];	/* student's name */
    uint8 age;	/* student's age */
    uint8 sex;	/* student's sex, as follows */
    /* 0 - FEMALE; 1 - MALE */
    uint32 teacher_ind; /* his teacher index */
} STUDENT;
```

<!-- KB_CHUNK_END rule_id="CSTD-7.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.9","section":"7.9","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.9｜7.9 结构体与结构体之间

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.9` |
| 原始章节 | `7.9` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 不同结构体间的关系不要过于复杂。 |

##### 原子检查项

- `CSTD-7.9-01` [SHOULD] 不同结构体间的关系不要过于复杂。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不同结构体间的关系不要过于复杂。若两个结构体间关系较复杂、密切，则应合为一个结构体。

由于示例1两个结构体都是描述同一事物的，则合成一个结构体，如示例2。

**示例1：**

```c
typedef struct PERSON_ONE_STRU
{
    uint8 name[8];
    uint8 addr[40];
    uint8 sex;
    uint8 city[15];
} PERSON_ONE;
typedef struct PERSON_TWO_STRU
{
    uint8 name[8];
    uint8 age;
    uint8 tel;
} PERSON_TWO;
```

**示例2：**

```c
typedef struct PERSON_STRU
{
    uint8 name[8];
    uint8 age;
    uint8 sex;
    uint8 addr[40];
    uint8 city[15];
    uint8 tel;
} PERSON;
```

<!-- KB_CHUNK_END rule_id="CSTD-7.9" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.10","section":"7.10","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.10｜7.10 结构体中元素的个数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.10` |
| 原始章节 | `7.10` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 结构体中元素个数适中，若结构体中元素个数过多可考虑依据某种原则把元素组成不同的子结构体，以减少原结构体中元素的个数，增加结构体的可理解性、可操作性和可维护性。 |

##### 原子检查项

- `CSTD-7.10-01` [SHOULD] 结构体中元素个数适中，若结构体中元素个数过多可考虑依据某种原则把元素组成不同的子结构体，以减少原结构体中元素的个数，增加结构体的可理解性、可操作性和可维护性。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

结构体中元素个数适中，若结构体中元素个数过多可考虑依据某种原则把元素组成不同的子结构体，以减少原结构体中元素的个数，增加结构体的可理解性、可操作性和可维护性。

**示例：**

```c
typedef struct PERSON_BASE_INFO_STRU
{
    uint8 name[8];
    uint8 age;
    uint8 sex;
} PERSON_BASE_INFO;
typedef struct PERSON_ADDRESS_STRU
{
    uint8 addr[40];
    uint8 city[15];
    uint8 tel;
} PERSON_ADDRESS;
typedef struct PERSON_STRU
{
     PERSON_BASE_INFO person_base;
     PERSON_ADDRESS person_addr;
} PERSON;
```

<!-- KB_CHUNK_END rule_id="CSTD-7.10" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.11","section":"7.11","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","tags":["types","variables","structs","memory","bit-fields"]} -->

#### CSTD-7.11｜7.11 结构体元素的布局及排列

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.11` |
| 原始章节 | `7.11` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `memory`, `bit-fields` |
| 摘要 | 结构体成员的布局和排列应兼顾可理解性、空间占用和误用风险。 |

##### 原子检查项

- `CSTD-7.11-01` [SHOULD] 结构体成员的布局和排列应兼顾可理解性、空间占用和误用风险。
- `CSTD-7.11-02` [MUST] 位域应单独定义为结构体；在其他结构体中使用时，应作为独立成员。
- `CSTD-7.11-03` [SHOULD] 使用结构体时应考虑不同编译器和 ABI 的对齐差异。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

仔细设计结构体中元素的布局与排列顺序，使结构体容易理解、节省占用空间，并减少引起误用现象。

位域应单独定义为一个结构体。在结构体中如需使用时，应单独作为其他结构体一个元素。

在使用结构体时应注意不同的编译器的对齐长度差异，可能为1、2、4个字节对齐。

**示例2比示例1，可读性好，也节省内存空间。**

**示例1：**

```c
typedef struct EXAMPLE_STRU
{
    uint8 valid;
    uint32 person;
    uint8 set_flg;
} EXAMPLE;
```

**示例2：**

```c
typedef struct EXAMPLE_STRU
{
    uint8 valid;
    uint8 set_flg;
    uint32 person ;
} EXAMPLE;
```

本例中也有两个未使用的字节。

<!-- KB_CHUNK_END rule_id="CSTD-7.11" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.12","section":"7.12","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","type-conversion"]} -->

#### CSTD-7.12｜7.12 数据类型转换

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.12` |
| 原始章节 | `7.12` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `type-conversion` |
| 摘要 | 禁止数据大小超限的强制数据类型转换和隐性数据类型转换。 |

##### 原子检查项

- `CSTD-7.12-01` [MUST] 禁止数据大小超限的强制数据类型转换和隐性数据类型转换。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对编译系统默认的数据类型转换，要有充分的认识。

禁止数据大小超限的强制数据类型转换和隐性数据类型转换。

**示例：**

如下赋值，多数编译器不产生告警，但却影响值的含义。

```c
uint8 chr;
uint16 exam;
chr = -1;
```

exam = chr; // 编译器不产生告警，此时 exam 为 0xFFFF。

<!-- KB_CHUNK_END rule_id="CSTD-7.12" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.13","section":"7.13","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","pointers","functions","type-conversion"]} -->

#### CSTD-7.13｜7.13 函数指针的类型转换

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.13` |
| 原始章节 | `7.13` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `pointers`, `functions`, `type-conversion` |
| 摘要 | 指向某一函数的指针不可强制转换为指向另一函数的指针。 |

##### 原子检查项

- `CSTD-7.13-01` [MUST] 指向某一函数的指针不可强制转换为指向另一函数的指针。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

指向某一函数的指针不可强制转换为指向另一函数的指针。

<!-- KB_CHUNK_END rule_id="CSTD-7.13" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.14","section":"7.14","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","pointers","type-conversion"]} -->

#### CSTD-7.14｜7.14 指针属性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.14` |
| 原始章节 | `7.14` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `pointers`, `type-conversion` |
| 摘要 | 类型转换过程中不能丢失指针的const、volatile属性。 |

##### 原子检查项

- `CSTD-7.14-01` [MUST] 类型转换过程中不能丢失指针的const、volatile属性。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

类型转换过程中不能丢失指针的const、volatile属性。

**示例：**

下面示例是非法操作。

```c
uint16_t x;
uint16_t * const	 cpi = &x; /* const pointer */
uint16_t * const	 * pcpi ; /* pointer to const pointer */
const uint16_t * 	 * ppci ; /* pointer to pointer to const */
uint16_t * 		 * ppi;
const uint16_t 	 * pci; /* pointer to const */
volatile uint16_t	 * pvi; /* pointer to volatile */
uint16_t 			 * pi;
```

…

```c
pi = cpi;              /* Compliant – no conversion no cast required */
pi = (uint16_t *)pci;    /* Not compliant */
pi = (uint16_t *)pvi ;   /* Not compliant */
ppi = (uint16_t *)pcpi ; /* Not compliant */
ppi = (uint16_t *)ppci ; /* Not compliant */
```

<!-- KB_CHUNK_END rule_id="CSTD-7.14" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.15","section":"7.15","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.15｜7.15 常量

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.15` |
| 原始章节 | `7.15` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 在所有unsigned 类型的常量后应添加后缀“U”。 |

##### 原子检查项

- `CSTD-7.15-01` [MUST] 在所有unsigned 类型的常量后应添加后缀“U”。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

在所有unsigned 类型的常量后应添加后缀“U”。

<!-- KB_CHUNK_END rule_id="CSTD-7.15" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.16","section":"7.16","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.16｜7.16 重复定义类型

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.16` |
| 原始章节 | `7.16` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 禁止重复定义类型。 |

##### 原子检查项

- `CSTD-7.16-01` [MUST] 禁止重复定义类型。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止重复定义类型。

<!-- KB_CHUNK_END rule_id="CSTD-7.16" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.17","section":"7.17","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","bit-fields"]} -->

#### CSTD-7.17｜7.17 对位域的定义

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.17` |
| 原始章节 | `7.17` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `bit-fields` |
| 摘要 | 对结构中位域的宽度不能大于int类型的宽度（一般为32位）。 |

##### 原子检查项

- `CSTD-7.17-01` [MUST] 对结构中位域的宽度不能大于int类型的宽度（一般为32位）。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 位域宽度应以其声明基类型和具体实现为依据，不宜一概以 32 位 `int` 为通用上限。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对结构中位域的宽度不能大于int类型的宽度（一般为32位）。

**以下示例位域的宽度超过了32位。**

**示例：**

```c
typedef   struct
{
    UINT64  Key         :64;
   ……
}
```

<!-- KB_CHUNK_END rule_id="CSTD-7.17" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.18","section":"7.18","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.18｜7.18 二进制的使用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.18` |
| 原始章节 | `7.18` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 不得使用二进制常数(0 除外)。 |

##### 原子检查项

- `CSTD-7.18-01` [MUST] 不得使用二进制常数(0 除外)。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 二进制整数字面量在 C++14 和 C23 已标准化；是否禁用取决于目标语言版本和工具链。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不得使用二进制常数(0 除外)。

<!-- KB_CHUNK_END rule_id="CSTD-7.18" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.19","section":"7.19","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.19｜7.19 十六进制转义字符、非标准转义字符、特殊字符

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.19` |
| 原始章节 | `7.19` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 不得使用十六进制转义字符、非标准转义字符及其他特殊字符。 |

##### 原子检查项

- `CSTD-7.19-01` [MUST] 不得使用十六进制转义字符、非标准转义字符及其他特殊字符。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 十六进制转义字符本身是标准 C/C++ 语法；全面禁用属于项目可读性或编码政策。非标准转义字符则应禁止。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不得使用十六进制转义字符、非标准转义字符及其他特殊字符。

**示例：**

不得使用如下赋值操作。

```c
char pc1 = '\x41';                      /* Message 3610 */
char pc2 = '\x0D';                      /* Message 3610 */
const char *s1 = "Return: \x0D";        	/* Message 3610 */
const char esc = '\c';               		/* Message 0235 */
const char esz = '\z';               		/* Message 0235 */
```

<!-- KB_CHUNK_END rule_id="CSTD-7.19" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.20","section":"7.20","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.20｜7.20 结构体初始化

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.20` |
| 原始章节 | `7.20` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 结构体初始化不可省略相应的{}。 |

##### 原子检查项

- `CSTD-7.20-01` [MUST] 结构体初始化不可省略相应的{}。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

结构体初始化不可省略相应的{}。

<!-- KB_CHUNK_END rule_id="CSTD-7.20" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.21","section":"7.21","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","pointers","operators"]} -->

#### CSTD-7.21｜7.21 运算符左值右值取值范围

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.21` |
| 原始章节 | `7.21` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `pointers`, `operators` |
| 摘要 | `*`、`/` 的两个操作数必须为算术类型。 |

##### 原子检查项

- `CSTD-7.21-01` [MUST] `*`、`/` 的两个操作数必须为算术类型。
- `CSTD-7.21-02` [MUST] `+` 的两个操作数必须均为算术类型，或一个为指针、另一个为整数类型。
- `CSTD-7.21-03` [MUST] `-` 的两个操作数必须均为算术类型，或均为兼容指针类型，或左侧为指针且右侧为整数类型。
- `CSTD-7.21-04` [MUST] 关系运算符 `<`、`<=`、`>=`、`>` 的操作数必须满足算术类型或可进行关系比较的指针类型要求。
- `CSTD-7.21-05` [MUST] 相等运算符 `==`、`!=` 的操作数必须满足算术类型或语言允许的指针比较要求。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

*、/运算符的两个操作数必须为算数类型。

+运算符的两个操作数必须为算数类型；或者一个为指针，另一个为整型。

-运算符的两个操作数必须为算数类型；或者两个操作数都为同类型指针；或者左值为指针，右值为整型。

<、<=、>=、>运算符的两个操作数必须为算数类型；或都为相同指针类型。

==、！=运算符的两个操作数必须为算数类型；或两侧都为相同指针类型；或者一个为指针，另一个为void类型指针；或者一个为指针，另一个为NULL。

<!-- KB_CHUNK_END rule_id="CSTD-7.21" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.22","section":"7.22","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.22｜7.22 有符号数赋值

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.22` |
| 原始章节 | `7.22` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 禁止使用十六进制对有符号数进行赋初值。 |

##### 原子检查项

- `CSTD-7.22-01` [MUST] 禁止使用十六进制对有符号数进行赋初值。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止使用十六进制对有符号数进行赋初值。

<!-- KB_CHUNK_END rule_id="CSTD-7.22" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.23","section":"7.23","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.23｜7.23 使用合适的存储期声明目标

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.23` |
| 原始章节 | `7.23` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 禁止访问超出存续时间的目标，否则会导致未定义行为。 |

##### 原子检查项

- `CSTD-7.23-01` [MUST] 禁止访问超出存续时间的目标，否则会导致未定义行为。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止访问超出存续时间的目标，否则会导致未定义行为。

**错误示例：**

```c
#include <stdio.h>
const char *p;
void dont_do_this(void) {
    const char c_str[] = “This will change”;
    p = c_str; /* Dangerous */
}
void innocuous(void) {
    printf(“%s\n”, p);
}
int main(void) {
    dont_do_this();
    innocuous();
    return 0;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-7.23" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.24","section":"7.24","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","arrays"]} -->

#### CSTD-7.24｜7.24 使用正确语法声明柔性数组成员

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.24` |
| 原始章节 | `7.24` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `arrays` |
| 摘要 | 柔性数组成员必须是结构体的最后一个成员。 |

##### 原子检查项

- `CSTD-7.24-01` [MUST] 柔性数组成员必须是结构体的最后一个成员。
- `CSTD-7.24-02` [MUST] 数组元素类型的结构体不能包含柔性数组成员。
- `CSTD-7.24-03` [MUST] 包含柔性数组成员的结构体不能作为其他结构体的普通成员；原规范仅允许其位于外层结构体最后一个成员的位置。
- `CSTD-7.24-04` [MUST] 包含柔性数组成员的结构体还必须至少包含一个其他命名成员。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

使用柔性数组的结构体必须满足下列条件：

1. 不完整数组类型必须为结构体最后一个元素；
2. 结构体数组不能包含柔性数组成员；
3. 包含柔性数组的结构体不能是其他结构体的成员，除非它为其他结构体的最后一个成员；
4. 结构体除包含柔性数组成员外，还必须包含至少一个命名成员；
包含柔性数组的结构体示例：

```c
struct flexArrayStruct {
    int num;
    int data[];
};
void func(size_t array_size) {
    /* Space is allocated for the struct */
    struct flexArrayStruct *structP
      = (struct flexArrayStruct *)
      malloc(sizeof(struct flexArrayStruct)
          + sizeof(int) * array_size);
    if (!structP) {
        /* Handle malloc failure */
    }
    structP->num = array_size;
    /* Access data[] as if it had been allocated
as data[array_size]. */
        for  (size_t i = 0; i < array_size; ++i) {
            structP->data[i] = 1;
        }
}
```

<!-- KB_CHUNK_END rule_id="CSTD-7.24" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.25","section":"7.25","normative_level":"MUST","policy_status":"active","risk":"critical","review_mode":"hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs"]} -->

#### CSTD-7.25｜7.25 越过可信边界传递结构体时应避免信息泄露

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.25` |
| 原始章节 | `7.25` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `critical` |
| 审核方式 | `hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs` |
| 摘要 | 结构体或共用体越过可信边界前，必须防止填充字节或填充位泄露未初始化信息。 |

##### 原子检查项

- `CSTD-7.25-01` [MUST] 结构体或共用体越过可信边界前，必须防止填充字节或填充位泄露未初始化信息。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

结构体的填充字节和共用体变量的填充位存在未说明的值，在进行数据结构体的传递时或造成信息泄露。

**错误示例：**

```c
#include <stddef.h>
struct test {
    int a;
    char b;
    int c;
};
/* Safely copy bytes to user space */
extern int copy_to_user(void *dest, void *src, size_t size);
void do_stuff(void *usr_buf) {
    struct test arg = {.a = 1, .b = 2, .c = 3};
    copy_to_user(usr_buf, &arg, sizeof(arg));
}
```

<!-- KB_CHUNK_END rule_id="CSTD-7.25" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-7.26","section":"7.26","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","tags":["types","variables","structs","pointers"]} -->

#### CSTD-7.26｜7.26 不要将指针强制转换为对其要求更加严格的指针类型

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-7.26` |
| 原始章节 | `7.26` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `declaration/function/module` |
| 标签 | `types`, `variables`, `structs`, `pointers` |
| 摘要 | 如果一个指针要转换为指向另一不同目标类型的指针，则后者必须有更加宽松的对其要求；否则，将导致未定义的结果。 |

##### 原子检查项

- `CSTD-7.26-01` [MUST] 如果一个指针要转换为指向另一不同目标类型的指针，则后者必须有更加宽松的对其要求；否则，将导致未定义的结果。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`declaration/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

如果一个指针要转换为指向另一不同目标类型的指针，则后者必须有更加宽松的对其要求；否则，将导致未定义的结果。

**错误示例：**

```c
void func(void) {
    char c = ‘x’;
    int *ip = (int *)&c; /* This can lose information */
    char *cp = (char *)ip;
    /* Will fail on some conforming implementation */
    assert(cp == &c);
}
```

<!-- KB_CHUNK_END rule_id="CSTD-7.26" -->

### 第 8 章 数组

> 章节标签：`arrays`, `pointers`

<!-- KB_CHUNK_START {"rule_id":"CSTD-8.1","section":"8.1","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["arrays","pointers"]} -->

#### CSTD-8.1｜8.1 数组大小

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-8.1` |
| 原始章节 | `8.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `arrays`, `pointers` |
| 摘要 | 数组的大小应该显式声明或者通过初始化进行隐式定义，且数组大小不能超过32767个字节。 |

##### 原子检查项

- `CSTD-8.1-01` [MUST] 数组的大小应该显式声明或者通过初始化进行隐式定义，且数组大小不能超过32767个字节。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 数组总大小不超过 32767 字节是平台相关限制，不是现代 C/C++ 的通用上限。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

数组的大小应该显式声明或者通过初始化进行隐式定义，且数组大小不能超过32767个字节。

**示例：**

以下数组定义是非法的，即：

```c
uint8 x[40][1000]; /* 数组大小超过32767个字节 */
extern uint32 array2[] ; /* 没有声明数组大小 */
```

以下数组的声明都是合法的：

```c
extern uint32 array2[100] ; /* Compliant */
uint32 array2[] = { 0, 10, 15 }; /* Compliant */
```

<!-- KB_CHUNK_END rule_id="CSTD-8.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-8.2","section":"8.2","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["arrays","pointers"]} -->

#### CSTD-8.2｜8.2 数组初始化

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-8.2` |
| 原始章节 | `8.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `arrays`, `pointers` |
| 摘要 | 除 `{0}` 外，原规范要求数组初始化项数量不得少于数组大小。 |

##### 原子检查项

- `CSTD-8.2-01` [MUST] 除 `{0}` 外，原规范要求数组初始化项数量不得少于数组大小。
- `CSTD-8.2-02` [MUST] 数组初始化不得省略相应层级的花括号。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- C/C++ 允许聚合对象部分初始化，未显式给出的其余元素会按语言规则初始化；原文将其一律判为非法属于更严格的项目政策。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

数组初始化个数不应该小于数组大小，但{0}除外；数组初始化不应省略相应的{}。

**示例1：**

```c
uint32 buf3[4] = { 1, 2, 3 };
uint32 buf5[3][3] = { { 1, 2, 3 } };
```

都是非法的，应该修改为：

```c
uint32 buf3[4]    = { 1, 2, 3, 4 };
uint32 buf4[3][3] = {{0,1,2},{1, 2, 3}, {4, 5, 6} };
```

另外，以下示例也是合法的。

**示例2：**

```c
uint32 buf1[4] = { 0 };
```

<!-- KB_CHUNK_END rule_id="CSTD-8.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-8.3","section":"8.3","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["arrays","pointers","memory","functions","operators"]} -->

#### CSTD-8.3｜8.3 没有指向同一个数组的2个指针之间不能相减和比较

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-8.3` |
| 原始章节 | `8.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `arrays`, `pointers`, `memory`, `functions`, `operators` |
| 摘要 | 不指向同一数组（含 one-past）的两个指针不得相减。 |

##### 原子检查项

- `CSTD-8.3-01` [MUST] 不指向同一数组（含 one-past）的两个指针不得相减。
- `CSTD-8.3-02` [MUST] 不指向同一数组的两个指针不得使用 `<`、`<=`、`>=`、`>` 做关系比较。
- `CSTD-8.3-03` [MUST] 任意两个指针可使用 `==`、`!=` 做相等性比较。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 标题中的“比较”容易被误解；正文已明确：不同数组指针不得做关系比较或相减，但 `==`、`!=` 可以比较。
- 原错误示例中的 `& - next_num_ptr` 疑似缺失数组末端指针表达式。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对2个没有指向同一数组的指针进行减法操作，以及使用关系运算符<、<=、>=、>进行比较没有意义，会导致未定义结果；然而，使用==和!=可以比较任意2个指针，没有限制性要求。

**错误示例：**

```c
void func(void) {
    int nums[32];
    int end;
    int *next_num_ptr = nums;
    size_t free_elements;
    /* Increment next_num_ptr as array fills */
    free_elements = & - next_num_ptr;
}
```

上述函数示例中假设nums数组与end变量在内存中相邻，计算还有多少个未使用的元素；然而，编译器会在2个变量之间插入填充位或是对他俩在内存中重新排序。

<!-- KB_CHUNK_END rule_id="CSTD-8.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-8.4","section":"8.4","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","tags":["arrays","pointers","memory","functions","structs"]} -->

#### CSTD-8.4｜8.4 不要对指向非数组目标的指针进行加减

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-8.4` |
| 原始章节 | `8.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function` |
| 标签 | `arrays`, `pointers`, `memory`, `functions`, `structs` |
| 摘要 | 不得通过对非数组对象成员的指针进行递增、递减或偏移来遍历对象布局。 |

##### 原子检查项

- `CSTD-8.4-01` [MUST] 不得通过对非数组对象成员的指针进行递增、递减或偏移来遍历对象布局。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 该条是保守规则；实施时应按目标 C/C++ 标准对单对象、数组元素及 one-past 指针的规则精确判断。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

指针的算术操作仅限于指向数组元素的指针。

**错误示例：**

```c
struct numbers {
    short num_a, num_b, num_c;
};
int sum_numbers(const struct numbers *numb) {
    int total = 0;
    const short *numb_ptr;
    for (numb_ptr = &numb->num_a;
        numb_ptr <= &numb->num_c;
        numb_ptr++) {
        total += *(numb_ptr);
    }
    return total;
}
```

上述函数使用指针的算术操作访问结构体成员，然而结构体成员在内存中的排布不保证连续。

<!-- KB_CHUNK_END rule_id="CSTD-8.4" -->

### 第 9 章 函数、过程

> 章节标签：`functions`, `interfaces`

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.1","section":"9.1","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.1｜9.1 函数参数检查

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.1` |
| 原始章节 | `9.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 对接口函数参数的合法性检查应由接口函数本身负责。 |

##### 原子检查项

- `CSTD-9.1-01` [MUST] 对接口函数参数的合法性检查应由接口函数本身负责。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对接口函数参数的合法性检查应由接口函数本身负责。

<!-- KB_CHUNK_END rule_id="CSTD-9.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.2","section":"9.2","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.2｜9.2 函数的参数处理

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.2` |
| 原始章节 | `9.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 对于必须修改的输出参数，原规范要求先在局部变量中完成计算，最后再写回参数。 |

##### 原子检查项

- `CSTD-9.2-01` [MUST] 对于必须修改的输出参数，原规范要求先在局部变量中完成计算，最后再写回参数。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对必须改变的参数，先用局部变量代之，最后再将该局部变量的内容赋给该参数。

**示例：**

禁止以下函数的实现：

```c
void sum_data( uint32 num, sint32 *data, sint32 *sum )
{
    uint32 count;
    *sum = 0;
for (count = 0; count < num; count++)
{
    *sum + = data[count];
}
}
```

**应改为如下：**

```c
void sum_data( uint32 num, sint32 *data, sint32 *sum )
{
    uint32 count ;
    int sum_temp;
    sum_temp = 0;
for (count = 0; count < num; count ++)
{
    sum_temp + = data[count];
}
    *sum = sum_temp;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-9.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.3","section":"9.3","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces","comments"]} -->

#### CSTD-9.3｜9.3 函数的规模

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.3` |
| 原始章节 | `9.3` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces`, `comments` |
| 摘要 | 函数的规模尽量限制在200行以内，不包括注释和空格行。 |

##### 原子检查项

- `CSTD-9.3-01` [SHOULD] 函数的规模尽量限制在200行以内，不包括注释和空格行。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数的规模尽量限制在200行以内，不包括注释和空格行。

<!-- KB_CHUNK_END rule_id="CSTD-9.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.4","section":"9.4","normative_level":"SHOULD","policy_status":"active-example-warning","risk":"low","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.4｜9.4 为重复实现的功能编写函数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.4` |
| 原始章节 | `9.4` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 一个函数宜只完成一项明确功能；重复实现的功能宜提取为函数。 |

##### 原子检查项

- `CSTD-9.4-01` [SHOULD] 一个函数宜只完成一项明确功能；重复实现的功能宜提取为函数。
- `CSTD-9.4-02` [SHOULD] 原规范要求所编写的函数具备可重入性。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- “所有函数均应可重入”属于特定系统要求，通用项目需结合线程模型确认。
- 原文后续宏式 MAX 示例若重复求值实参可能产生副作用，不能作为无条件推荐。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

一个函数仅完成一件功能。函数可使功能明确化，增加程序可读性，亦可方便维护、测试。

所编写的函数应为可重入函数。

**示例：**

如下语句的功能不很明显。

```c
value = ( a > b ) ? a : b ;
```

改为如下：

```c
sint32 max (sint32 a, sint32 b)
{
    return ((a > b) ? a : b);
}
value = max (a, b);
```

或改为如下：

```c
#define MAX (a, b) (((a) > (b)) ? (a) : (b))
value = MAX (a, b);
```

<!-- KB_CHUNK_END rule_id="CSTD-9.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.5","section":"9.5","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.5｜9.5 函数功能的可预测性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.5` |
| 原始章节 | `9.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数在相同输入和相同约定状态下应产生可预测的输出。 |

##### 原子检查项

- `CSTD-9.5-01` [MUST] 函数在相同输入和相同约定状态下应产生可预测的输出。
- `CSTD-9.5-02` [MUST] 应避免使用未在接口契约中说明的静态局部状态改变函数结果。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数的功能应该是可以预测的，即只要输入数据相同就应产生同样的输出。

带有内部“存储器”的函数的功能可能是不可预测的，因为它的输出可能取决于内部存储器（如某标记）的状态。这样的函数既不易于理解又不利于测试和维护。在C语言中，函数的static局部变量是函数的内部存储器，有可能使函数的功能不可预测。

**示例：**

如下函数，其返回值（即功能）是不可预测的。

```c
uint32 integer_sum( uint32 base )
{
    uint32 index;
    static uint32 sum = 0;
// 若改为auto类型，则函数即变为可预测。
for (index = 1; index <= base; index++)
{
    sum += index;
}
    return sum;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-9.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.6","section":"9.6","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.6｜9.6 减少函数参数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.6` |
| 原始章节 | `9.6` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 不使用的参数从接口中去掉，目的为了减少函数间接口的复杂度。 |

##### 原子检查项

- `CSTD-9.6-01` [SHOULD] 不使用的参数从接口中去掉，目的为了减少函数间接口的复杂度。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不使用的参数从接口中去掉，目的为了减少函数间接口的复杂度。

<!-- KB_CHUNK_END rule_id="CSTD-9.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.7","section":"9.7","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","tags":["functions","interfaces","pointers","arrays"]} -->

#### CSTD-9.7｜9.7 函数形参

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.7` |
| 原始章节 | `9.7` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces`, `pointers`, `arrays` |
| 摘要 | 函数形参禁止使用数组，应使用指针形式。 |

##### 原子检查项

- `CSTD-9.7-01` [MUST] 函数形参禁止使用数组，应使用指针形式。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 函数形参数组声明在语言层面会调整为指针类型；禁用数组写法主要是接口风格政策。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数形参禁止使用数组，应使用指针形式。

<!-- KB_CHUNK_END rule_id="CSTD-9.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.8","section":"9.8","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.8｜9.8 非调度函数的参数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.8` |
| 原始章节 | `9.8` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 非调度函数宜减少或避免控制参数，优先只接收数据参数。 |

##### 原子检查项

- `CSTD-9.8-01` [SHOULD] 非调度函数宜减少或避免控制参数，优先只接收数据参数。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

非调度函数应减少或防止控制参数，只使用数据参数。目的是防止函数间的控制耦合。调度函数是指根据输入的消息类型或控制命令，来启动相应的功能实体（即函数或过程），而本身并不完成具体功能。控制参数是指改变函数功能行为的参数，即函数要根据此参数来决定具体怎样工作。非调度函数的控制参数增加了函数间的控制耦合，很可能使函数间的耦合度增大，并使函数的功能不唯一。

**示例：**

如下函数构造不太合理：

```c
sint32 add_sub(sint32 a, sint32 b,uint8 add_sub_flg)
{
if (add_sub_flg == INTEGER_ADD)
{
    return (a + b);
}
else
{
    return(a - b);
}
}
```

不如分为如下两个函数清晰。

```c
sint32 add(sint32 a, sint32 b )
{
    return (a + b);
}
sint32 sub(sint32 a, sint32 b )
{
    return(a - b);
}
```

<!-- KB_CHUNK_END rule_id="CSTD-9.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.9","section":"9.9","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.9｜9.9 函数参数输入与非参数输入的有效性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.9` |
| 原始章节 | `9.9` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数使用参数前必须检查所有参数输入的有效性。 |

##### 原子检查项

- `CSTD-9.9-01` [MUST] 函数使用参数前必须检查所有参数输入的有效性。
- `CSTD-9.9-02` [MUST] 函数使用全局变量等非参数输入前必须检查其有效性。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

检查函数所有参数输入的有效性。

检查函数所有非参数输入的有效性，如公共变量等。

函数的输入主要有两种：一种是参数输入；另一种是全局变量即非参数输入。函数在使用输入之前，应进行必要的检查。

<!-- KB_CHUNK_END rule_id="CSTD-9.9" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.10","section":"9.10","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.10｜9.10 函数返回值

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.10` |
| 原始章节 | `9.10` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 不要把与函数返回值类型不同的变量，以编译系统默认的转换方式或强制的转换方式作为返回值返回。 |

##### 原子检查项

- `CSTD-9.10-01` [MUST] 不要把与函数返回值类型不同的变量，以编译系统默认的转换方式或强制的转换方式作为返回值返回。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

不要把与函数返回值类型不同的变量，以编译系统默认的转换方式或强制的转换方式作为返回值返回。

<!-- KB_CHUNK_END rule_id="CSTD-9.10" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.11","section":"9.11","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces","type-conversion"]} -->

#### CSTD-9.11｜9.11 函数的调用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.11` |
| 原始章节 | `9.11` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces`, `type-conversion` |
| 摘要 | 不得使用函数参与逻辑运算。 |

##### 原子检查项

- `CSTD-9.11-01` [MUST] 不得使用函数参与逻辑运算。
- `CSTD-9.11-02` [SHOULD] 在调用函数填写参数时，减少没有必要的默认数据类型转换或强制数据类型转换。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- “不得使用函数参与逻辑运算”过于宽泛；返回布尔值的谓词函数参与条件表达式是常见合法写法。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

调用的原则：

- 不得使用函数参与逻辑运算。
- 在调用函数填写参数时，减少没有必要的默认数据类型转换或强制数据类型转换。

<!-- KB_CHUNK_END rule_id="CSTD-9.11" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.12","section":"9.12","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.12｜9.12 禁止随机内聚

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.12` |
| 原始章节 | `9.12` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数或过程不得包含彼此无关或关联很弱的随机内聚语句。 |

##### 原子检查项

- `CSTD-9.12-01` [MUST] 函数或过程不得包含彼此无关或关联很弱的随机内聚语句。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

防止函数或过程内出现随机内聚。随机内聚是指将没有关联或关联很弱的语句放到同一个函数或过程中。随机内聚给函数或过程的维护、测试及以后的升级等造成了不便，同时也使函数或过程的功能不明确。使用随机内聚函数，容易出现在一种应用场合需要改进此函数，而另一种应用场合又不允许这种改进，从而陷入困境。若这些代码关联较大并且是完成一个功能的，那么这种构造是合理的，否则这种构造将产生随机内聚的函数。

**示例：**

如下函数就是一种随机内聚。

```c
void Init_Bsw( void )
{
    Rect.length = 0;
    Rect.width = 0; /* 初始化矩形的长与宽 */
    Point.x = 10;
    Point.y = 10;	/* 初始化“点”的坐标 */
}
```

矩形的长、宽与点的坐标基本没有任何关系，故以上函数是随机内聚。

**应如下分为两个函数：**

```c
void Init_Adc( void )
{
    Rect.length = 0;
    Rect.width = 0; /* 初始化矩形的长与宽 */
}
void Init_Spi( void )
{
    Point.x = 10;
    Point.y = 10;	/* 初始化“点”的坐标 */
}
```

<!-- KB_CHUNK_END rule_id="CSTD-9.12" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.13","section":"9.13","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.13｜9.13 高扇入、合理扇出的函数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.13` |
| 原始章节 | `9.13` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数设计宜具有较高扇入和合理扇出。 |

##### 原子检查项

- `CSTD-9.13-01` [MUST] 函数设计宜具有较高扇入和合理扇出。
- `CSTD-9.13-02` [MUST] 原规范建议非调度函数的扇出通常为 3～5；该数值只能作为启发式参考。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 扇出 3～5 是设计启发式，不应脱离模块职责和调用图直接判违规。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

设计高扇入、合理扇出的函数。

扇出过大，表明函数过分复杂，需要控制和协调过多的下级函数；而扇出过小，如总是1，表明函数的调用层次可能过多，这样不利程序阅读和函数结构的分析，并且程序运行时会对系统资源如堆栈空间等造成压力。函数较合理的扇出（调度函数除外）通常是3~5。

<!-- KB_CHUNK_END rule_id="CSTD-9.13" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.14","section":"9.14","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.14｜9.14 递归函数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.14` |
| 原始章节 | `9.14` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 禁止使用函数本身或函数间的递归调用。 |

##### 原子检查项

- `CSTD-9.14-01` [MUST] 禁止使用函数本身或函数间的递归调用。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 全面禁止递归属于嵌入式或栈资源受限项目政策；通用项目应结合深度上界和资源预算判断。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止使用函数本身或函数间的递归调用。递归调用会占用较多的资源（如栈空间），也不利于测试。

<!-- KB_CHUNK_END rule_id="CSTD-9.14" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.15","section":"9.15","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.15｜9.15 函数返回值的引用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.15` |
| 原始章节 | `9.15` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 对于提供了返回值的函数，在引用时要使用其返回值。 |

##### 原子检查项

- `CSTD-9.15-01` [MUST] 对于提供了返回值的函数，在引用时要使用其返回值。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 部分 API 的返回值可按契约安全忽略；应结合函数声明、属性和接口文档判定。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

对于提供了返回值的函数，在引用时要使用其返回值。

<!-- KB_CHUNK_END rule_id="CSTD-9.15" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.16","section":"9.16","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.16｜9.16 函数出口唯一性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.16` |
| 原始章节 | `9.16` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数只能有一个出口，这个出口必须在函数末尾。 |

##### 原子检查项

- `CSTD-9.16-01` [MUST] 函数只能有一个出口，这个出口必须在函数末尾。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 单一出口不是通用最佳实践；用于参数校验或错误处理的早返回可能更清晰。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数只能有一个出口，这个出口必须在函数末尾。

<!-- KB_CHUNK_END rule_id="CSTD-9.16" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.17","section":"9.17","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","tags":["functions","interfaces"]} -->

#### CSTD-9.17｜9.17 函数原型声明

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.17` |
| 原始章节 | `9.17` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces` |
| 摘要 | 函数应声明原型。 |

##### 原子检查项

- `CSTD-9.17-01` [MUST] 函数应声明原型。
- `CSTD-9.17-02` [MUST] 函数声明与函数定义中的参数标识符应保持一致。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

函数应该声明原型，并且函数声明与函数定义中使用的标识符应该保持一致。

**示例：**

以下这种函数声明是不合适的：

```c
extern uint32 INJ_CurrentSet_Task()；
void   MD5Init(MD5_CTX  *);
```

应该修改为：

```c
extern uint32 INJ_CurrentSet_Task(void);
void   MD5Init(MD5_CTX  *Ptr);
```

<!-- KB_CHUNK_END rule_id="CSTD-9.17" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-9.18","section":"9.18","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","tags":["functions","interfaces","headers"]} -->

#### CSTD-9.18｜9.18 外部对象声明唯一性

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-9.18` |
| 原始章节 | `9.18` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `function/module` |
| 标签 | `functions`, `interfaces`, `headers` |
| 摘要 | 外部对象应该声明在唯一的头文件中，该对象可以是变量或函数。 |

##### 原子检查项

- `CSTD-9.18-01` [MUST] 外部对象应该声明在唯一的头文件中，该对象可以是变量或函数。
- `CSTD-9.18-02` [MUST] 通常在一个头文件中声明一个外部标识符，而在定义或使用该标识符的文件中包含这个头文件，不可直接在C文件中声明。
- `CSTD-9.18-03` [MUST] 引用其他模块变量需要包含该变量所在模块的头文件。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

外部对象应该声明在唯一的头文件中，该对象可以是变量或函数。通常在一个头文件中声明一个外部标识符，而在定义或使用该标识符的文件中包含这个头文件，不可直接在C文件中声明。

引用其他模块变量需要包含该变量所在模块的头文件。

**示例：**

在文件AC.h中声明外部变量g_AC_B

```c
extern t_AC_BlockIO g_AC_B;
```

然后在AC.c中包含AC.h

```c
#include “AC.h”
```

<!-- KB_CHUNK_END rule_id="CSTD-9.18" -->

### 第 10 章 程序效率

> 章节标签：`performance`

<!-- KB_CHUNK_START {"rule_id":"CSTD-10.1","section":"10.1","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module/runtime","tags":["performance"]} -->

#### CSTD-10.1｜10.1 空间效率

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-10.1` |
| 原始章节 | `10.1` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `function/module/runtime` |
| 标签 | `performance` |
| 摘要 | 通过对系统数据结构的划分与组织的改进，以及对程序算法的优化来提高空间效率。 |

##### 原子检查项

- `CSTD-10.1-01` [SHOULD] 通过对系统数据结构的划分与组织的改进，以及对程序算法的优化来提高空间效率。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module/runtime`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

通过对系统数据结构的划分与组织的改进，以及对程序算法的优化来提高空间效率。这种方式是解决软件空间效率的根本办法。

**示例：**

如下记录学生学习成绩的结构不合理：

```c
typedef struct STUDENT_SCORE_STRU
{
     uint8 name[8];
     uint8 age;
     uint8 sex;
     uint8 class;
     uint8 subject;
    float score;
} STUDENT_SCORE;
```

因为每位学生都有多科学习成绩，故如上结构将占用较大空间。如下改进（分为两个结构），总的存贮空间将变小，操作也变得更方便。

```c
typedef struct STUDENT_STRU
{
     uint8 name[8];
     uint8 age;
     uint8 sex;
     uint8 class;
} STUDENT;
typedef struct STUDENT_SCORE_STRU
{
    uint32  student_index;
    uint8 subject;
    float score;
} STUDENT_SCORE;
```

<!-- KB_CHUNK_END rule_id="CSTD-10.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-10.2","section":"10.2","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module/runtime","tags":["performance","loops"]} -->

#### CSTD-10.2｜10.2 循环体内工作量最小化

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-10.2` |
| 原始章节 | `10.2` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `function/module/runtime` |
| 标签 | `performance`, `loops` |
| 摘要 | 应仔细考虑循环体内的语句是否可以放在循环体之外，使循环体内工作量最小，从而提高程序的时间效率。 |

##### 原子检查项

- `CSTD-10.2-01` [MUST] 应仔细考虑循环体内的语句是否可以放在循环体之外，使循环体内工作量最小，从而提高程序的时间效率。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`function/module/runtime`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

应仔细考虑循环体内的语句是否可以放在循环体之外，使循环体内工作量最小，从而提高程序的时间效率。

**示例：**

如下代码效率不高：

```c
for (ind = 0; ind < MAX_ADD_NUMBER; ind ++)
{
    sum += ind;
    back_sum = sum; /* backup sum */
}
```

**应改为如下：**

```c
for (ind = 0; ind < MAX_ADD_NUMBER; ind ++)
{
    sum += ind;
}
    back_sum = sum; /* backup sum */
```

<!-- KB_CHUNK_END rule_id="CSTD-10.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-10.3","section":"10.3","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","tags":["performance","functions","loops"]} -->

#### CSTD-10.3｜10.3 提高效率的其他方法

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-10.3` |
| 原始章节 | `10.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需修订原规范 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `function/module/runtime` |
| 标签 | `performance`, `functions`, `loops` |
| 摘要 | 应分析并优化模块内函数的划分和组织方式。 |

##### 原子检查项

- `CSTD-10.3-01` [MUST] 应分析并优化模块内函数的划分和组织方式。
- `CSTD-10.3-02` [MUST] 原规范要求在多重循环中将循环次数最多的循环放在最内层。
- `CSTD-10.3-03` [SHOULD] 宜减少循环嵌套层次。
- `CSTD-10.3-04` [MUST] 当循环内判断与循环变量无关时，宜将判断移到循环外层。
- `CSTD-10.3-05` [MUST] 原规范要求用乘法或其他方法替代除法，并禁止浮点运算。

##### 审核判定

- 默认行为：`needs_review`：原规范存在技术冲突，修订前不自动判违规。
- 适用证据范围：`function/module/runtime`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

其他方法有：

- 对模块中函数的划分及组织方式进行分析、优化，改进模块中函数的组织结构，提高程序效率。
- 在多重循环中，将循环次数最多的循环放在最内层。
**示例1：**

如下代码效率不高:

```c
for (row = 0; row < 100; row++)
{
    for (col = 0; col < 5; col++)
    {
        sum += a[row][col];
    }
}
```

**可以改为如下方式，以提高效率。**

```c
for (col = 0; col < 5; col++)
{
    for (row = 0; row < 100; row++)
    {
        sum += a[row][col];
    }
}
```

- 减少循环嵌套层次。
- 避免循环体内含判断语句，应将循环语句置于判断语句的代码块之中。
**示例2：**

如下代码效率稍低:

```c
for (ind = 0; ind < MAX_RECT_NUMBER; ind ++)
{
    if (data_type == RECT_AREA)
    {
        area_sum += rect_area[ind];
    }
    else
    {
        rect_length_sum += rect[ind].length;
        rect_width_sum += rect[ind].width;
    }
}
```

因为判断语句与循环变量无关，故可如下改进，以减少判断次数。

```c
if (data_type == RECT_AREA)
{
    for (ind = 0; ind < MAX_RECT_NUMBER; ind ++)
    {
        area_sum += rect_area[ind];
    }
}
else
{
    for (ind = 0; ind < MAX_RECT_NUMBER; ind++)
    {
        rect_length_sum += rect[ind].length;
        rect_width_sum += rect[ind].width;
    }
}
```

- 用乘法或其它方法代替除法，不得使用浮点运算。
**示例3：**

如下表达式运算可能要占较多 CPU 资源。

```c
#define PAI 3.1416
radius = circle_length / (2 * PAI);
```

**应改为如下：**

```c
#define PAI_RECIPROCAL (1 / 3.1416 )  // 编译器编译时，将生成具体浮点数
radius = circle_length * PAI_RECIPROCAL / 2;
```

<!-- KB_CHUNK_END rule_id="CSTD-10.3" -->

### 第 11 章 质量保证

> 章节标签：`quality`, `safety`

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.1","section":"11.1","normative_level":"MUST","policy_status":"active-example-warning","risk":"critical","review_mode":"hybrid","evidence_scope":"expression/function/module","tags":["quality","safety","memory","pointers","arrays"]} -->

#### CSTD-11.1｜11.1 防止内存操作越界

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.1` |
| 原始章节 | `11.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `critical` |
| 审核方式 | `hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety`, `memory`, `pointers`, `arrays` |
| 摘要 | 所有数组、指针和内存地址操作必须保持在有效对象边界内。 |

##### 原子检查项

- `CSTD-11.1-01` [MUST] 所有数组、指针和内存地址操作必须保持在有效对象边界内。
- `CSTD-11.1-02` [MUST] 使用外部输入作为数组索引或内存偏移前，必须验证其取值范围。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原“解决示例”仅把索引改为 `usr_no - 1`，仍未检查 `usr_no` 是否处于 1～10；输入为 0 或大于 10 时仍可能越界。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

内存操作主要是指对数组、指针、内存地址等的操作。

假设某软件系统最多可由10个用户同时使用，用户号为 1-10，那么如下程序存在问题。

**示例1：**

```c
#define MAX_USR_NUM 10
uint8 usr_login_flg[MAX_USR_NUM]= "";
void set_usr_login_flg( uint8 usr_no )
{
if (!usr_login_flg[usr_no])
{
usr_login_flg[usr_no]  =  TRUE;
}
}
```

当 usr_no为10时，将使用 usr_login_flg 越界。可采用如下方式解决：

**示例2：**

```c
void set_usr_login_flg( uint8 usr_no )
{
if (!usr_login_flg[usr_no - 1])
{
usr_login_flg[usr_no - 1]  =  TRUE;
}
}
```

<!-- KB_CHUNK_END rule_id="CSTD-11.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.2","section":"11.2","normative_level":"MUST","policy_status":"active","risk":"critical","review_mode":"hybrid","evidence_scope":"expression/function/module","tags":["quality","safety","memory","pointers"]} -->

#### CSTD-11.2｜11.2 禁止访问已经释放的内存空间

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.2` |
| 原始章节 | `11.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `critical` |
| 审核方式 | `hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety`, `memory`, `pointers` |
| 摘要 | 禁止访问已经释放的内存空间。 |

##### 原子检查项

- `CSTD-11.2-01` [MUST] 禁止访问已经释放的内存空间。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

通过指针访问一块被释放的内存空间会导致未定义结果。

**错误示例：**

```c
struct node {
    int value;
    struct node *next;
};
void free_list(struct node *head) {
    for (struct node *p = head; p != NULL; p = p->next) {
free(p);
}
}
```

<!-- KB_CHUNK_END rule_id="CSTD-11.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.3","section":"11.3","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"expression/function/module","tags":["quality","safety","memory","pointers"]} -->

#### CSTD-11.3｜11.3 动态分配的内存已不再使用时应被及时释放

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.3` |
| 原始章节 | `11.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety`, `memory`, `pointers` |
| 摘要 | 在指向动态分配的内存的最后一个指针的生命到期之前，需要对其使用free()释放。 |

##### 原子检查项

- `CSTD-11.3-01` [MUST] 在指向动态分配的内存的最后一个指针的生命到期之前，需要对其使用free()释放。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

在指向动态分配的内存的最后一个指针的生命到期之前，需要对其使用free()释放。

**错误示例：**

```c
int f(void) {
   char *text_buffer = (char *)malloc(32);
   if (!text_buffer) {
        return -1;
    }
    return 0;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-11.3" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.4","section":"11.4","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.4｜11.4 模块的设置和配置更改权限

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.4` |
| 原始章节 | `11.4` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `medium` |
| 审核方式 | `manual` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | 严禁更改其它模块或系统的有关设置和配置，应通过模块负责人进行修改。 |

##### 原子检查项

- `CSTD-11.4-01` [MUST] 严禁更改其它模块或系统的有关设置和配置，应通过模块负责人进行修改。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

严禁更改其它模块或系统的有关设置和配置，应通过模块负责人进行修改。

<!-- KB_CHUNK_END rule_id="CSTD-11.4" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.5","section":"11.5","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.5｜11.5 选择语句的分支语句

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.5` |
| 原始章节 | `11.5` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需修订原规范 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | if… else if结构必须以else子句结束。 |

##### 原子检查项

- `CSTD-11.5-01` [MUST] if… else if结构必须以else子句结束。
- `CSTD-11.5-02` [MUST] switch语句必须有default分支,并且所有非空的switch 子句都应该用break 语句结束。

##### 审核判定

- 默认行为：`needs_review`：原规范存在技术冲突，修订前不自动判违规。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 本条要求所有非空 `case` 以 `break` 结束，与 CSTD-4.13 允许带明确注释的有意 fallthrough 相冲突。
- 项目应明确是全面禁止 fallthrough，还是允许使用标准属性/明确注释的受控 fallthrough；统一前不自动执行本条。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

if… else if结构必须以else子句结束。switch语句必须有default分支,并且所有非空的switch 子句都应该用break 语句结束。

<!-- KB_CHUNK_END rule_id="CSTD-11.5" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.6","section":"11.6","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.6｜11.6 禁止使用goto语句

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.6` |
| 原始章节 | `11.6` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | goto语句会破坏程序的结构性，禁止使用goto语句。 |

##### 原子检查项

- `CSTD-11.6-01` [MUST] goto语句会破坏程序的结构性，禁止使用goto语句。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 全面禁止 `goto` 属于项目政策；某些 C 资源清理路径可受控使用，但必须服从本项目最终决定。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

goto语句会破坏程序的结构性，禁止使用goto语句。

<!-- KB_CHUNK_END rule_id="CSTD-11.6" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.7","section":"11.7","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"expression/function/module","tags":["quality","safety","macros","functions"]} -->

#### CSTD-11.7｜11.7 汇编语句使用

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.7` |
| 原始章节 | `11.7` |
| 规范强度 | SHOULD（建议） |
| 规则状态 | 有效 |
| 风险等级 | `low` |
| 审核方式 | `manual` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety`, `macros`, `functions` |
| 摘要 | 使用汇编语言，应将汇编语言封装并隔离，可以通过汇编函数、C函数、宏实现。 |

##### 原子检查项

- `CSTD-11.7-01` [SHOULD] 使用汇编语言，应将汇编语言封装并隔离，可以通过汇编函数、C函数、宏实现。

##### 审核判定

- 默认行为：`advisory`：作为改进建议报告，不默认阻断合入。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

使用汇编语言，应将汇编语言封装并隔离，可以通过汇编函数、C函数、宏实现。

<!-- KB_CHUNK_END rule_id="CSTD-11.7" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.8","section":"11.8","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.8｜11.8 有符号数位操作

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.8` |
| 原始章节 | `11.8` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | 禁止对有符号数进行位操作，主要的位操作符有&、\|、~、<<、>>、^。 |

##### 原子检查项

- `CSTD-11.8-01` [MUST] 禁止对有符号数进行位操作，主要的位操作符有&、|、~、<<、>>、^。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 有符号位运算应针对负数、移位宽度、溢出和实现定义行为精确检查；全面禁用是保守项目政策。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止对有符号数进行位操作，主要的位操作符有&、|、~、<<、>>、^。

**示例：**

以下操作就是非法的：

```c
sint16 temp;
Temp >> 8;
```

<!-- KB_CHUNK_END rule_id="CSTD-11.8" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.9","section":"11.9","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.9｜11.9 判断条件中的赋值语句

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.9` |
| 原始章节 | `11.9` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | 禁止在 `if`、`while` 等判断条件中执行赋值。 |

##### 原子检查项

- `CSTD-11.9-01` [MUST] 禁止在 `if`、`while` 等判断条件中执行赋值。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止在判断条件中使用赋值语句，例如以下语句非法。

**示例：**

```c
if（x = y）
```

应该修改为：

```c
if (x == y)
```

<!-- KB_CHUNK_END rule_id="CSTD-11.9" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.10","section":"11.10","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.10｜11.10 判断条件

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.10` |
| 原始章节 | `11.10` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | 非布尔操作数作为判断条件时，应显式与 0 或目标值比较。 |

##### 原子检查项

- `CSTD-11.10-01` [MUST] 非布尔操作数作为判断条件时，应显式与 0 或目标值比较。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 非布尔值显式与 0 比较属于风格政策；布尔表达式无需冗余比较。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

判断条件应为显示，判断一个值是否为0应该是显式的，除非该操作数是一个布尔值。

例如以下语句非法。

**示例：**

```c
if(x)
```

应该修改为：

```c
if(x != 0)
```

<!-- KB_CHUNK_END rule_id="CSTD-11.10" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-11.11","section":"11.11","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","tags":["quality","safety"]} -->

#### CSTD-11.11｜11.11 Continue语句

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-11.11` |
| 原始章节 | `11.11` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `expression/function/module` |
| 标签 | `quality`, `safety` |
| 摘要 | 禁止使用Continue语句。 |

##### 原子检查项

- `CSTD-11.11-01` [MUST] 禁止使用Continue语句。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`expression/function/module`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 全面禁止 `continue` 属于控制流风格政策，不是语言正确性要求。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止使用Continue语句。

<!-- KB_CHUNK_END rule_id="CSTD-11.11" -->

### 第 12 章 宏

> 章节标签：`macros`, `preprocessor`

<!-- KB_CHUNK_START {"rule_id":"CSTD-12.1","section":"12.1","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","tags":["macros","preprocessor","functions"]} -->

#### CSTD-12.1｜12.1 函数宏

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-12.1` |
| 原始章节 | `12.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `macro/file` |
| 标签 | `macros`, `preprocessor`, `functions` |
| 摘要 | 函数式宏的每个参数引用都应使用小括号包围，作为 `#` 或 `##` 操作数的情况除外。 |

##### 原子检查项

- `CSTD-12.1-01` [MUST] 函数式宏的每个参数引用都应使用小括号包围，作为 `#` 或 `##` 操作数的情况除外。
- `CSTD-12.1-02` [MUST] 函数式宏的整体表达式应使用小括号或安全的 `do { ... } while (0)` 结构保护。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`macro/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原 `abs(x)` 宏会多次求值 `x`，传入带副作用的表达式会出错，且名称可能与标准库 `abs` 冲突；只能用于说明括号规则，不能作为推荐实现。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

在定义函数宏时，每个参数都应该以小括号括起来，除非它们是用作#或##的操作数。

函数宏的定义中，参数应该用小括号括起来。

**示例：**

一个abs 函数可以定义为：

```c
#define 	 abs(x) 	( ( (x) >= 0 ) ? (x) : -(x) )
```

**不能定义为：**

```c
#define abs (x) ( ( (x) >= 0 ) ? x : -x )
```

<!-- KB_CHUNK_END rule_id="CSTD-12.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-12.2","section":"12.2","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","tags":["macros","preprocessor","functions"]} -->

#### CSTD-12.2｜12.2 宏参数

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-12.2` |
| 原始章节 | `12.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `macro/file` |
| 标签 | `macros`, `preprocessor`, `functions` |
| 摘要 | 调用宏时，实参不得包含自增、自减等会在重复求值时产生额外副作用的变化。 |

##### 原子检查项

- `CSTD-12.2-01` [MUST] 调用宏时，实参不得包含自增、自减等会在重复求值时产生额外副作用的变化。
- `CSTD-12.2-02` [MUST] 函数式宏的实参不得包含预处理指令。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`macro/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

使用宏时，不允许参数发生变化。

**示例：**

如下用法可能导致错误。

```c
#define SQUARE( a ) ((a) * (a))
uint8 a = 5;
uint8 b;
```

b = SQUARE( a++ ); // 结果：a = 7，即执行了两次增1。

正确的用法是：

```c
b = SQUARE( a );
```

a++; // 结果：a = 6，即只执行了一次增1。

使用函数宏时，参数不允许包含预处理指令，比如#define、#ifdef、#include，否则会导致未定义行为的发生。

**错误示例：**

```c
void func(const char *src) {
    /* Validate the source string; calculate size */
    char *dest;
    /* malloc() destination string */
```

memcpy(dest, src,

```c
      #ifdef PLATFORM1
```

12

```c
      #else
```

24

```c
    );
    /* ... */
}
```

如果上述代码段中memcpy使用宏函数实现，那么此段代码会导致未定义行为。

<!-- KB_CHUNK_END rule_id="CSTD-12.2" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-12.3","section":"12.3","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","tags":["macros","preprocessor"]} -->

#### CSTD-12.3｜12.3 宏内容

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-12.3` |
| 原始章节 | `12.3` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `high` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `macro/file` |
| 标签 | `macros`, `preprocessor` |
| 摘要 | C的宏只能扩展为用大括号括起来的初始化、常量、小括号括起来的表达式、类型限定符、存储类标识符或do-while-zero 结构。 |

##### 原子检查项

- `CSTD-12.3-01` [MUST] C的宏只能扩展为用大括号括起来的初始化、常量、小括号括起来的表达式、类型限定符、存储类标识符或do-while-zero 结构。
- `CSTD-12.3-02` [MUST] 禁止使用符号连接##生成通用字符名称，否则会导致未定义行为。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`macro/file`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原示例中的 `#define I NIT(value)` 疑似排版破损。
- 多语句宏应使用 `do { ... } while (0)` 并评估参数副作用；原示例不可直接复制。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

C的宏只能扩展为用大括号括起来的初始化、常量、小括号括起来的表达式、类型限定符、存储类标识符或do-while-zero 结构。

**示例：**

```c
/* The following are compliant */
#define 	PI	 3.14159F						/* Constant */
#define 	XSTAL	 10000000				    /* Constant */
#define 	CLOCK	 (XSTAL / 16) 				/* Constant expression */
#define 	PLUS2(X)	 ( (X) + 2 )		    /* Macro expanding to expression       */
#define	 STOR 	extern 							/* storage class specifier */
#define I	NIT(value)	 { (value), 0, 0 }	    /* braced initialiser */
#define READ_TIME_32 () \
do { \
DISABLE_INTERRUPTS (); \
time_now = (uint32_t) TIMER_HI << 16; \
ENABLE_INTERRUPTS (); \
} while (0)									 /* example of do-while-zero */
/* the following are NOT compliant */
#define int32_t long						 /* use typedef instead */
#define STARTIF if ( 		/* unbalanced () and language redefinition */
```

禁止使用符号连接##生成通用字符名称，否则会导致未定义行为。

**错误示例：**

```c
#define assign(uc1, uc2, val) uc1##uc2 = val
void func(void) {
    int \u0401;
    /* ... */
assign(\u04, 01, 4);
/* ... */
}
```

<!-- KB_CHUNK_END rule_id="CSTD-12.3" -->

### 第 13 章 头文件

> 章节标签：`headers`, `dependencies`

<!-- KB_CHUNK_START {"rule_id":"CSTD-13.1","section":"13.1","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","tags":["headers","dependencies","functions"]} -->

#### CSTD-13.1｜13.1 头文件内容

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-13.1` |
| 原始章节 | `13.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 需项目确认 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `file/project` |
| 标签 | `headers`, `dependencies`, `functions` |
| 摘要 | 一般每一个.c文件应对应一个.h文件，用于声明需要对外公开的接口（变量、函数），XXX_PBCfg.c除外。 |

##### 原子检查项

- `CSTD-13.1-01` [MUST] 一般每一个.c文件应对应一个.h文件，用于声明需要对外公开的接口（变量、函数），XXX_PBCfg.c除外。
- `CSTD-13.1-02` [MUST] 禁止在头文件中定义变量。

##### 审核判定

- 默认行为：`needs_review`：项目未明确启用该政策时，不自动判违规。
- 适用证据范围：`file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 一个 `.c` 文件对应一个 `.h` 文件属于项目组织约定；禁止在头文件中定义可产生多重定义的对象是核心要求。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

一般每一个.c文件应对应一个.h文件，用于声明需要对外公开的接口（变量、函数），XXX_PBCfg.c除外。

禁止在头文件中定义变量。

<!-- KB_CHUNK_END rule_id="CSTD-13.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-13.2","section":"13.2","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","tags":["headers","dependencies","loops"]} -->

#### CSTD-13.2｜13.2 头文件要求

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-13.2` |
| 原始章节 | `13.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `medium` |
| 审核方式 | `automatic-or-hybrid` |
| 证据范围 | `file/project` |
| 标签 | `headers`, `dependencies`, `loops` |
| 摘要 | 禁止头文件循环依赖。 |

##### 原子检查项

- `CSTD-13.2-01` [MUST] 禁止头文件循环依赖。
- `CSTD-13.2-02` [MUST] .c/.h中禁止包含无用的头文件。
- `CSTD-13.2-03` [MUST] 头文件应有#define保护符。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`file/project`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 完整 include guard 应包含匹配的 `#ifndef`、`#define`、`#endif`；原文只写“#define 保护符”不够完整。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

禁止头文件循环依赖。

.c/.h中禁止包含无用的头文件。

头文件应有#define保护符。

<!-- KB_CHUNK_END rule_id="CSTD-13.2" -->

### 第 14 章 并发执行

> 章节标签：`concurrency`, `thread-safety`

<!-- KB_CHUNK_START {"rule_id":"CSTD-14.1","section":"14.1","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"module/runtime","tags":["concurrency","thread-safety"]} -->

#### CSTD-14.1｜14.1 禁止销毁正在使用的互斥锁

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-14.1` |
| 原始章节 | `14.1` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效 |
| 风险等级 | `high` |
| 审核方式 | `hybrid` |
| 证据范围 | `module/runtime` |
| 标签 | `concurrency`, `thread-safety` |
| 摘要 | 禁止销毁仍处于使用状态或仍可能被并发访问的互斥锁。 |

##### 原子检查项

- `CSTD-14.1-01` [MUST] 禁止销毁仍处于使用状态或仍可能被并发访问的互斥锁。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`module/runtime`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

正在使用的互斥锁被销毁，那么相关共享资源将不再得到保护。

<!-- KB_CHUNK_END rule_id="CSTD-14.1" -->

<!-- KB_CHUNK_START {"rule_id":"CSTD-14.2","section":"14.2","normative_level":"MUST","policy_status":"active-example-warning","risk":"critical","review_mode":"hybrid","evidence_scope":"module/runtime","tags":["concurrency","thread-safety","bit-fields"]} -->

#### CSTD-14.2｜14.2 多线程访问位域应防止数据竞争

| 字段 | 值 |
|---|---|
| 规则 ID | `CSTD-14.2` |
| 原始章节 | `14.2` |
| 规范强度 | MUST（必须） |
| 规则状态 | 有效，但示例有缺陷 |
| 风险等级 | `critical` |
| 审核方式 | `hybrid` |
| 证据范围 | `module/runtime` |
| 标签 | `concurrency`, `thread-safety`, `bit-fields` |
| 摘要 | 多线程访问同一位域或共享同一存储单元的相邻位域时，必须使用同步或存储隔离措施防止数据竞争。 |

##### 原子检查项

- `CSTD-14.2-01` [MUST] 多线程访问同一位域或共享同一存储单元的相邻位域时，必须使用同步或存储隔离措施防止数据竞争。

##### 审核判定

- 默认行为：`violation`：仅在适用且存在明确、最小化代码证据时判定。
- 适用证据范围：`module/runtime`。
- 证据不足、只看到局部代码或需要运行时/项目配置时，输出 `needs_review`。
- 不得仅因代码与原示例长得不同而判违规；必须对应到具体原子检查项。

##### 最佳实践校验

- 原示例存在结构体名称不一致、缺少分号等编译问题；只应采用“共享位域访问必须同步”的规则意图。

##### 原规范内容与示例

> 以下内容按原文语义保留并进行 Markdown 排版。标记为“示例有缺陷”的规则，其示例仅供追溯，不得作为可直接复制的标准实现。

相邻位域可能会被保存在同一存储单元中，共享同一BYTE或是WORD空间，所以多线程访问同一位域与多线程访问相邻位域都可能造成数据竞争问题，解决前者可以使用互斥锁保护共享位域资源，解决后者则可以在相邻位域之间插入非位域成员，将其隔绝在不同的存储单元中。

**正确示例：**

```c
struct multi_threaded_flags {
    unsigned int flags1 : 2;
    unsigned int flags2 : 2;
}
struct mtf_mutex {
    struct multi_thread_flags s;
    mtx_t mutex;
};
struct mtf_mutex flags;
int thread1(void *arg) {
    if (thrd_success != mtx_lock(&flags.mutex)) {
        /* Handle error */
}
flags.s.flags1 = 1;
if (thrd_success != mtx_unlock(&flags.mutex)) {
    /* Handle error */
}
return 0;
}
int thread2(void *arg) {
    if (thrd_success != mtx_lock(&flags.mutex)) {
        /* Handle error */
}
flags.s.flags2 = 2;
if (thrd_success != mtx_unlock(&flags.mutex)) {
    /* Handle error */
}
return 0;
}
```

<!-- KB_CHUNK_END rule_id="CSTD-14.2" -->

## 6. 知识库导入与切分建议

- 优先按 `KB_CHUNK_START` / `KB_CHUNK_END` 切分，每个块只包含一条原规则。
- 不应按固定字符数跨规则切分；若平台必须二次切分，每个子块都应重复规则 ID、规则状态和原子检查项。
- 检索时提高 `critical`、`high` 风险规则权重；格式和命名规则应在安全问题之后展示。
- 查询中包含语言版本、平台、编译器或项目政策时，应优先召回“需项目确认”的规则。
- 审核输出引用 `check_id`，知识库追溯引用 `rule_id`。
- 示例文本的检索权重应低于原子检查项与审核判定，防止模型从破损示例中学习。

## 7. 维护规则

- 既有规则 ID 永不复用；废弃规则保留 ID 并标记状态。
- 原规则新增独立义务时，追加新的原子检查项编号，不改变已有检查项含义。
- 修改“需项目确认”规则前，应记录适用语言版本、目标平台、批准人和生效日期。
- 修复原示例时应保留变更记录，并区分“原文示例”和“修订后推荐示例”。
- 每次生成后必须校验规则数、检查项数、ID 唯一性、代码围栏、编码和源文件哈希。

## 8. 源文清洗记录

- 删除 `正文件切分`：疑似文档处理残留，不属于编程规范。
- 保留“图1”引用并标记图像缺失，没有臆造原图内容。
- 保留原文中的拼写、代码和语法缺陷，并在相应规则的“最佳实践校验”中提示。

<!-- source_sha256: cffcc4d638985d179945c8cfe1d61ccb9d86f80fcdc886c4708084b1b955b59d -->

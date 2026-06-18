# [CSTD-3.1-01] 缩进排版

<!-- KB_METADATA {"check_id":"CSTD-3.1-01","rule_id":"CSTD-3.1","section":"3.1","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.1-01`
- 父规则 ID：`CSTD-3.1`
- 原规范章节：`3.1 缩进排版`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

程序块要采用缩进风格编写，缩进的英文空格数为4个。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.1-02] 缩进排版

<!-- KB_METADATA {"check_id":"CSTD-3.1-02","rule_id":"CSTD-3.1","section":"3.1","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.1-02`
- 父规则 ID：`CSTD-3.1`
- 原规范章节：`3.1 缩进排版`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

函数或过程的开始、结构的定义及循环、判断等语句中的代码需要采用缩进排版，case语句下的情况处理语句也需遵守缩进排版的要求。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.2-01] 对齐方法

<!-- KB_METADATA {"check_id":"CSTD-3.2-01","rule_id":"CSTD-3.2","section":"3.2","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout"]} -->

## 元数据

- 检查项 ID：`CSTD-3.2-01`
- 父规则 ID：`CSTD-3.2`
- 原规范章节：`3.2 对齐方法`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`

## 审核要求

对齐可使用空格键，也可使用Tab键，但是Tab必须等效为4个空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.3-01] 添加空行

<!-- KB_METADATA {"check_id":"CSTD-3.3-01","rule_id":"CSTD-3.3","section":"3.3","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout"]} -->

## 元数据

- 检查项 ID：`CSTD-3.3-01`
- 父规则 ID：`CSTD-3.3`
- 原规范章节：`3.3 添加空行`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`

## 审核要求

相对独立的程序块之间、变量说明之后必须加空行。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.3`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.4-01] 代码行长度

<!-- KB_METADATA {"check_id":"CSTD-3.4-01","rule_id":"CSTD-3.4","section":"3.4","category":"书写格式","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.4-01`
- 父规则 ID：`CSTD-3.4`
- 原规范章节：`3.4 代码行长度`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

一行代码的长度要合理，以小于80字符为宜，不要写得过长。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原文要求普通 C/C++ 长表达式换行时每行以反斜杠结束。现代 C/C++ 仅在预处理宏等需要行拼接的场景才需要反斜杠；普通表达式可直接在语法允许的位置换行。
- 在项目未明确确认前，不应因普通表达式换行未使用反斜杠而自动判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.4`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.4-02] 代码行长度

<!-- KB_METADATA {"check_id":"CSTD-3.4-02","rule_id":"CSTD-3.4","section":"3.4","category":"书写格式","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.4-02`
- 父规则 ID：`CSTD-3.4`
- 原规范章节：`3.4 代码行长度`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

较长的逻辑运算语句（>80字符）要分成多行书写，每行应以“\”结束，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，划分出的新行要进行适当的缩进，使排版整齐，语句可读。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原文要求普通 C/C++ 长表达式换行时每行以反斜杠结束。现代 C/C++ 仅在预处理宏等需要行拼接的场景才需要反斜杠；普通表达式可直接在语法允许的位置换行。
- 在项目未明确确认前，不应因普通表达式换行未使用反斜杠而自动判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.4`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.4-03] 代码行长度

<!-- KB_METADATA {"check_id":"CSTD-3.4-03","rule_id":"CSTD-3.4","section":"3.4","category":"书写格式","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.4-03`
- 父规则 ID：`CSTD-3.4`
- 原规范章节：`3.4 代码行长度`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

循环、判断等语句中若有较长的表达式或语句，则要进行适当的划分，长表达式要在低优先级操作符处划分新行，操作符放在新行之首，每行应以“\”结束。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原文要求普通 C/C++ 长表达式换行时每行以反斜杠结束。现代 C/C++ 仅在预处理宏等需要行拼接的场景才需要反斜杠；普通表达式可直接在语法允许的位置换行。
- 在项目未明确确认前，不应因普通表达式换行未使用反斜杠而自动判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.4`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.4-04] 代码行长度

<!-- KB_METADATA {"check_id":"CSTD-3.4-04","rule_id":"CSTD-3.4","section":"3.4","category":"书写格式","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["formatting","layout","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-3.4-04`
- 父规则 ID：`CSTD-3.4`
- 原规范章节：`3.4 代码行长度`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`formatting`, `layout`, `functions`, `loops`

## 审核要求

若函数或过程中的参数较长，则要进行适当的划分，每行应以“\”结束。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原文要求普通 C/C++ 长表达式换行时每行以反斜杠结束。现代 C/C++ 仅在预处理宏等需要行拼接的场景才需要反斜杠；普通表达式可直接在语法允许的位置换行。
- 在项目未明确确认前，不应因普通表达式换行未使用反斜杠而自动判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.4`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.5-01] 单条语句

<!-- KB_METADATA {"check_id":"CSTD-3.5-01","rule_id":"CSTD-3.5","section":"3.5","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout"]} -->

## 元数据

- 检查项 ID：`CSTD-3.5-01`
- 父规则 ID：`CSTD-3.5`
- 原规范章节：`3.5 单条语句`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`

## 审核要求

不允许把多个短语句写在一行中，即一行只写一条语句。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.5`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.6-01] 逻辑控制语句排版

<!-- KB_METADATA {"check_id":"CSTD-3.6-01","rule_id":"CSTD-3.6","section":"3.6","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout"]} -->

## 元数据

- 检查项 ID：`CSTD-3.6-01`
- 父规则 ID：`CSTD-3.6`
- 原规范章节：`3.6 逻辑控制语句排版`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`

## 审核要求

if、for、do、while、case、switch、default等语句自占一行，且if、for、do、while等语句的执行语句部分必须添加括号{}。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.6`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.7-01] 程序块的分界符

<!-- KB_METADATA {"check_id":"CSTD-3.7-01","rule_id":"CSTD-3.7","section":"3.7","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-3.7-01`
- 父规则 ID：`CSTD-3.7`
- 原规范章节：`3.7 程序块的分界符`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `functions`

## 审核要求

程序块分界符（如 `{`、`}`）应各自独占一行、处于同一列，并与引用它们的语句左对齐。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.7`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.7-02] 程序块的分界符

<!-- KB_METADATA {"check_id":"CSTD-3.7-02","rule_id":"CSTD-3.7","section":"3.7","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-3.7-02`
- 父规则 ID：`CSTD-3.7`
- 原规范章节：`3.7 程序块的分界符`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `functions`

## 审核要求

函数体、类、结构体、枚举以及控制语句中的程序块应按规定缩进。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.7`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.8-01] 操作符前后格式

<!-- KB_METADATA {"check_id":"CSTD-3.8-01","rule_id":"CSTD-3.8","section":"3.8","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","pointers","bit-fields","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-3.8-01`
- 父规则 ID：`CSTD-3.8`
- 原规范章节：`3.8 操作符前后格式`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `pointers`, `bit-fields`, `operators`

## 审核要求

二元比较、赋值、算术、逻辑和位运算符前后应加空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.8`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.8-02] 操作符前后格式

<!-- KB_METADATA {"check_id":"CSTD-3.8-02","rule_id":"CSTD-3.8","section":"3.8","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","pointers","bit-fields","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-3.8-02`
- 父规则 ID：`CSTD-3.8`
- 原规范章节：`3.8 操作符前后格式`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `pointers`, `bit-fields`, `operators`

## 审核要求

一元运算符与操作数之间不加空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.8`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.8-03] 操作符前后格式

<!-- KB_METADATA {"check_id":"CSTD-3.8-03","rule_id":"CSTD-3.8","section":"3.8","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","pointers","bit-fields","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-3.8-03`
- 父规则 ID：`CSTD-3.8`
- 原规范章节：`3.8 操作符前后格式`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `pointers`, `bit-fields`, `operators`

## 审核要求

成员访问运算符 `->`、`.` 前后不加空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.8`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.8-04] 操作符前后格式

<!-- KB_METADATA {"check_id":"CSTD-3.8-04","rule_id":"CSTD-3.8","section":"3.8","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","pointers","bit-fields","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-3.8-04`
- 父规则 ID：`CSTD-3.8`
- 原规范章节：`3.8 操作符前后格式`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `pointers`, `bit-fields`, `operators`

## 审核要求

括号内侧和多重括号之间不要求添加空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.8`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.8-05] 操作符前后格式

<!-- KB_METADATA {"check_id":"CSTD-3.8-05","rule_id":"CSTD-3.8","section":"3.8","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout","pointers","bit-fields","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-3.8-05`
- 父规则 ID：`CSTD-3.8`
- 原规范章节：`3.8 操作符前后格式`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`, `pointers`, `bit-fields`, `operators`

## 审核要求

不得为操作符保留两个及以上连续空格。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.8`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-3.9-01] 文件末尾

<!-- KB_METADATA {"check_id":"CSTD-3.9-01","rule_id":"CSTD-3.9","section":"3.9","category":"书写格式","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/file","default_result":"violation","target_languages":["C","C++"],"tags":["formatting","layout"]} -->

## 元数据

- 检查项 ID：`CSTD-3.9-01`
- 父规则 ID：`CSTD-3.9`
- 原规范章节：`3.9 文件末尾`
- 分类：书写格式
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`formatting`, `layout`

## 审核要求

在文件末尾添加空行。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-3.9`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.1-01] 注释量

<!-- KB_METADATA {"check_id":"CSTD-4.1-01","rule_id":"CSTD-4.1","section":"4.1","category":"注释","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.1-01`
- 父规则 ID：`CSTD-4.1`
- 原规范章节：`4.1 注释量`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`comments`, `documentation`

## 审核要求

源程序有效注释量(Code line)必须在20％以上。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- “有效注释量必须在 20% 以上”属于可量化但容易被无意义注释满足的项目指标，不能替代注释质量审核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.2-01] 注释语言

<!-- KB_METADATA {"check_id":"CSTD-4.2-01","rule_id":"CSTD-4.2","section":"4.2","category":"注释","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.2-01`
- 父规则 ID：`CSTD-4.2`
- 原规范章节：`4.2 注释语言`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`comments`, `documentation`

## 审核要求

注释语言必须使用英文。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 注释必须使用英语属于团队语言政策，不是通用 C/C++ 正确性要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.3-01] 注释格式

<!-- KB_METADATA {"check_id":"CSTD-4.3-01","rule_id":"CSTD-4.3","section":"4.3","category":"注释","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.3-01`
- 父规则 ID：`CSTD-4.3`
- 原规范章节：`4.3 注释格式`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`comments`, `documentation`

## 审核要求

注释格式必须统一，使用“/* …… */”，在注释中不得使用字符“/*”及“*/”。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- C99 及 C++ 支持 `//` 注释；仅允许 `/* ... */` 属于项目风格政策。
- 原文禁止在块注释中再次出现块注释定界符的要求是合理的，因为 C/C++ 块注释不可嵌套。
- 原规范其他章节的示例多次使用 `//`，与本条“只使用块注释”的要求内部不一致；应先统一项目决定。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.3`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.4-01] 文件的注释

<!-- KB_METADATA {"check_id":"CSTD-4.4-01","rule_id":"CSTD-4.4","section":"4.4","category":"注释","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","functions","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-4.4-01`
- 父规则 ID：`CSTD-4.4`
- 原规范章节：`4.4 文件的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `functions`, `headers`

## 审核要求

说明性文件（如头文件.h文件）头部应进行注释。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 原文引用“图1”，但源文件中没有实际图像或完整模板；不得据此臆造缺失格式。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.4`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.4-02] 文件的注释

<!-- KB_METADATA {"check_id":"CSTD-4.4-02","rule_id":"CSTD-4.4","section":"4.4","category":"注释","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","functions","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-4.4-02`
- 父规则 ID：`CSTD-4.4`
- 原规范章节：`4.4 文件的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `functions`, `headers`

## 审核要求

注释必须列出：版权说明、版本号、生成日期、作者、内容、功能、与其它文件的关系、修改日志等，头文件的注释中还应有函数功能简要说明。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 原文引用“图1”，但源文件中没有实际图像或完整模板；不得据此臆造缺失格式。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.4`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.4-03] 文件的注释

<!-- KB_METADATA {"check_id":"CSTD-4.4-03","rule_id":"CSTD-4.4","section":"4.4","category":"注释","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","functions","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-4.4-03`
- 父规则 ID：`CSTD-4.4`
- 原规范章节：`4.4 文件的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `functions`, `headers`

## 审核要求

推荐图1所示头文件的头注释格式，无论使用何种格式都必须包含上述信息，每个项目中的头注释格式应相同。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 原文引用“图1”，但源文件中没有实际图像或完整模板；不得据此臆造缺失格式。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.4`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.5-01] 函数的注释

<!-- KB_METADATA {"check_id":"CSTD-4.5-01","rule_id":"CSTD-4.5","section":"4.5","category":"注释","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-4.5-01`
- 父规则 ID：`CSTD-4.5`
- 原规范章节：`4.5 函数的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `functions`

## 审核要求

函数头部注释应包含函数目的或功能、输入参数、输出参数、返回值和调用关系等信息。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 原函数注释示例使用了多个 `/*` 且结尾定界不完整，不能直接复制为合法 C/C++ 注释模板；应只采用其字段要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.5-02] 函数的注释

<!-- KB_METADATA {"check_id":"CSTD-4.5-02","rule_id":"CSTD-4.5","section":"4.5","category":"注释","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-4.5-02`
- 父规则 ID：`CSTD-4.5`
- 原规范章节：`4.5 函数的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `functions`

## 审核要求

同一项目中的函数注释格式应保持一致。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 原函数注释示例使用了多个 `/*` 且结尾定界不完整，不能直接复制为合法 C/C++ 注释模板；应只采用其字段要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.6-01] 代码注释内容要求

<!-- KB_METADATA {"check_id":"CSTD-4.6-01","rule_id":"CSTD-4.6","section":"4.6","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.6-01`
- 父规则 ID：`CSTD-4.6`
- 原规范章节：`4.6 代码注释内容要求`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

保证注释与代码的一致性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.6`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.6-02] 代码注释内容要求

<!-- KB_METADATA {"check_id":"CSTD-4.6-02","rule_id":"CSTD-4.6","section":"4.6","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.6-02`
- 父规则 ID：`CSTD-4.6`
- 原规范章节：`4.6 代码注释内容要求`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

无用的注释要删除。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.6`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.6-03] 代码注释内容要求

<!-- KB_METADATA {"check_id":"CSTD-4.6-03","rule_id":"CSTD-4.6","section":"4.6","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.6-03`
- 父规则 ID：`CSTD-4.6`
- 原规范章节：`4.6 代码注释内容要求`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

注释的内容要清楚、明了，含义准确，防止注释二义性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.6`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.7-01] 注释缩写

<!-- KB_METADATA {"check_id":"CSTD-4.7-01","rule_id":"CSTD-4.7","section":"4.7","category":"注释","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"line/function/file","default_result":"advisory","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.7-01`
- 父规则 ID：`CSTD-4.7`
- 原规范章节：`4.7 注释缩写`
- 分类：注释
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`comments`, `documentation`

## 审核要求

避免在注释中使用缩写，特别是非常用缩写。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.7`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.7-02] 注释缩写

<!-- KB_METADATA {"check_id":"CSTD-4.7-02","rule_id":"CSTD-4.7","section":"4.7","category":"注释","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"line/function/file","default_result":"advisory","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.7-02`
- 父规则 ID：`CSTD-4.7`
- 原规范章节：`4.7 注释缩写`
- 分类：注释
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`comments`, `documentation`

## 审核要求

在使用缩写时或之前，应对缩写进行必要的说明。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.7`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.8-01] 注释位置

<!-- KB_METADATA {"check_id":"CSTD-4.8-01","rule_id":"CSTD-4.8","section":"4.8","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.8-01`
- 父规则 ID：`CSTD-4.8`
- 原规范章节：`4.8 注释位置`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

注释应与其描述的代码相近，对代码的注释（对单条语句、变量、常量、数据结构等的注释）应放在其上方或右方相邻位置，不可放在下面。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.8`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.8-02] 注释位置

<!-- KB_METADATA {"check_id":"CSTD-4.8-02","rule_id":"CSTD-4.8","section":"4.8","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.8-02`
- 父规则 ID：`CSTD-4.8`
- 原规范章节：`4.8 注释位置`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

禁止在一行代码或表达式中间插入注释，否则容易使代码可理解性变差。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.8`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.9-01] 变量及常量的注释

<!-- KB_METADATA {"check_id":"CSTD-4.9-01","rule_id":"CSTD-4.9","section":"4.9","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.9-01`
- 父规则 ID：`CSTD-4.9`
- 原规范章节：`4.9 变量及常量的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

对于所有具有物理含义的变量、常量，如果其命名不是充分自注释的，在声明时都必须加以注释，说明其物理含义。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.9`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.10-01] 数据结构的注释

<!-- KB_METADATA {"check_id":"CSTD-4.10-01","rule_id":"CSTD-4.10","section":"4.10","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","arrays","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-4.10-01`
- 父规则 ID：`CSTD-4.10`
- 原规范章节：`4.10 数据结构的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `arrays`, `structs`

## 审核要求

数据结构声明(包括数组、结构体、枚举等)，如果其命名不是充分自注释的，必须加以注释。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.10`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.10-02] 数据结构的注释

<!-- KB_METADATA {"check_id":"CSTD-4.10-02","rule_id":"CSTD-4.10","section":"4.10","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation","arrays","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-4.10-02`
- 父规则 ID：`CSTD-4.10`
- 原规范章节：`4.10 数据结构的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`, `arrays`, `structs`

## 审核要求

对数据结构的注释应放在其上方相邻位置；对结构体中的每个域的注释放在此域的右方。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.10`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.11-01] 全局变量的注释

<!-- KB_METADATA {"check_id":"CSTD-4.11-01","rule_id":"CSTD-4.11","section":"4.11","category":"注释","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"line/function/file","default_result":"advisory","target_languages":["C","C++"],"tags":["comments","documentation","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-4.11-01`
- 父规则 ID：`CSTD-4.11`
- 原规范章节：`4.11 全局变量的注释`
- 分类：注释
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`comments`, `documentation`, `functions`

## 审核要求

全局变量要有较详细的注释，包括对其功能、取值范围、哪些函数或过程存取它以及存取时注意事项等说明。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.11`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.12-01] 注释的排版

<!-- KB_METADATA {"check_id":"CSTD-4.12-01","rule_id":"CSTD-4.12","section":"4.12","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.12-01`
- 父规则 ID：`CSTD-4.12`
- 原规范章节：`4.12 注释的排版`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

为使程序排版整齐，并方便注释的阅读与理解，注释应与所描述内容进行同样的缩排。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.12`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.12-02] 注释的排版

<!-- KB_METADATA {"check_id":"CSTD-4.12-02","rule_id":"CSTD-4.12","section":"4.12","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.12-02`
- 父规则 ID：`CSTD-4.12`
- 原规范章节：`4.12 注释的排版`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

注释应与其上的代码用空行隔开。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.12`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.13-01] 逻辑控制语句的注释

<!-- KB_METADATA {"check_id":"CSTD-4.13-01","rule_id":"CSTD-4.13","section":"4.13","category":"注释","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["comments","documentation","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-4.13-01`
- 父规则 ID：`CSTD-4.13`
- 原规范章节：`4.13 逻辑控制语句的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`comments`, `documentation`, `loops`

## 审核要求

对条件分支、循环语句等逻辑控制语句必须编写注释。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 要求每个条件分支和循环都写注释可能产生复述代码的低价值注释；建议重点审核复杂意图、边界原因和有意 fallthrough。
- 本条允许带明确注释的 case fallthrough，但 CSTD-11.5 又要求所有非空 case 以 break 结束，两条规则需由项目统一。
- 原文中的“正文件切分”为文档处理残留，已清除。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.13`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.13-02] 逻辑控制语句的注释

<!-- KB_METADATA {"check_id":"CSTD-4.13-02","rule_id":"CSTD-4.13","section":"4.13","category":"注释","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"needs_review","target_languages":["C","C++"],"tags":["comments","documentation","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-4.13-02`
- 父规则 ID：`CSTD-4.13`
- 原规范章节：`4.13 逻辑控制语句的注释`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`comments`, `documentation`, `loops`

## 审核要求

对于switch语句下的case语句，如果因为特殊情况需要处理完一个case后进入下一个case处理，必须在该case语句处理完、下一个case语句前加上明确的注释。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 最佳实践与质量提示

- 要求每个条件分支和循环都写注释可能产生复述代码的低价值注释；建议重点审核复杂意图、边界原因和有意 fallthrough。
- 本条允许带明确注释的 case fallthrough，但 CSTD-11.5 又要求所有非空 case 以 break 结束，两条规则需由项目统一。
- 原文中的“正文件切分”为文档处理残留，已清除。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.13`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-4.14-01] 代码屏蔽

<!-- KB_METADATA {"check_id":"CSTD-4.14-01","rule_id":"CSTD-4.14","section":"4.14","category":"注释","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"line/function/file","default_result":"violation","target_languages":["C","C++"],"tags":["comments","documentation"]} -->

## 元数据

- 检查项 ID：`CSTD-4.14-01`
- 父规则 ID：`CSTD-4.14`
- 原规范章节：`4.14 代码屏蔽`
- 分类：注释
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`comments`, `documentation`

## 审核要求

代码段不予编译或需屏蔽的地方，应该使用条件编译实现（如带注释的#if或 #ifdef结构）。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`line/function/file`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-4.14`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.1-01] 标识符的命名基本要求

<!-- KB_METADATA {"check_id":"CSTD-5.1-01","rule_id":"CSTD-5.1","section":"5.1","category":"命名规则","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"advisory","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.1-01`
- 父规则 ID：`CSTD-5.1`
- 原规范章节：`5.1 标识符的命名基本要求`
- 分类：命名规则
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`naming`

## 审核要求

标识符的命名要清晰、明了，有明确含义，同时使用完整的单词或大家基本可以理解的缩写，避免使人产生误解。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.1-02] 标识符的命名基本要求

<!-- KB_METADATA {"check_id":"CSTD-5.1-02","rule_id":"CSTD-5.1","section":"5.1","category":"命名规则","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"advisory","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.1-02`
- 父规则 ID：`CSTD-5.1`
- 原规范章节：`5.1 标识符的命名基本要求`
- 分类：命名规则
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`naming`

## 审核要求

较短的单词可通过去掉“元音”形成缩写；较长的单词可取单词的头几个字母形成缩写；宜用大家公认的缩写单词。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.2-01] 命名中的注释

<!-- KB_METADATA {"check_id":"CSTD-5.2-01","rule_id":"CSTD-5.2","section":"5.2","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming","comments"]} -->

## 元数据

- 检查项 ID：`CSTD-5.2-01`
- 父规则 ID：`CSTD-5.2`
- 原规范章节：`5.2 命名中的注释`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`, `comments`

## 审核要求

命名中若使用特殊约定或难以理解的缩写，要有注释说明。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.2-02] 命名中的注释

<!-- KB_METADATA {"check_id":"CSTD-5.2-02","rule_id":"CSTD-5.2","section":"5.2","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming","comments"]} -->

## 元数据

- 检查项 ID：`CSTD-5.2-02`
- 父规则 ID：`CSTD-5.2`
- 原规范章节：`5.2 命名中的注释`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`, `comments`

## 审核要求

应该在源文件的开始之处，对文件中所使用的缩写或约定，特别是特殊的缩写，进行必要的注释说明。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.3-01] 命名风格的前后一致性

<!-- KB_METADATA {"check_id":"CSTD-5.3-01","rule_id":"CSTD-5.3","section":"5.3","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.3-01`
- 父规则 ID：`CSTD-5.3`
- 原规范章节：`5.3 命名风格的前后一致性`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`

## 审核要求

自己特有的命名风格，要自始至终保持一致，不可来回变化。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.3-02] 命名风格的前后一致性

<!-- KB_METADATA {"check_id":"CSTD-5.3-02","rule_id":"CSTD-5.3","section":"5.3","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.3-02`
- 父规则 ID：`CSTD-5.3`
- 原规范章节：`5.3 命名风格的前后一致性`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`

## 审核要求

个人的命名风格，在符合所在项目组或产品组的命名规则的前提下，才可使用（即命名规则中没有规定到的地方才可有个人命名风格）。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.4-01] 命名风格的系统一致性

<!-- KB_METADATA {"check_id":"CSTD-5.4-01","rule_id":"CSTD-5.4","section":"5.4","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.4-01`
- 父规则 ID：`CSTD-5.4`
- 原规范章节：`5.4 命名风格的系统一致性`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`

## 审核要求

命名规范必须与所使用的系统风格保持一致，并在同一项目中统一。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.4`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.5-01] 禁用数字或奇怪的字符命名

<!-- KB_METADATA {"check_id":"CSTD-5.5-01","rule_id":"CSTD-5.5","section":"5.5","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.5-01`
- 父规则 ID：`CSTD-5.5`
- 原规范章节：`5.5 禁用数字或奇怪的字符命名`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`

## 审核要求

命名中不能出现无意义的数字或奇怪字符。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.5`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.6-01] 接口部分标示符命名

<!-- KB_METADATA {"check_id":"CSTD-5.6-01","rule_id":"CSTD-5.6","section":"5.6","category":"命名规则","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"violation","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.6-01`
- 父规则 ID：`CSTD-5.6`
- 原规范章节：`5.6 接口部分标示符命名`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`naming`

## 审核要求

对接口部分的标识符应该有更严格限制，防止冲突。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.6`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.7-01] 函数的命名

<!-- KB_METADATA {"check_id":"CSTD-5.7-01","rule_id":"CSTD-5.7","section":"5.7","category":"命名规则","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"identifier/file/project","default_result":"advisory","target_languages":["C","C++"],"tags":["naming","functions","concurrency"]} -->

## 元数据

- 检查项 ID：`CSTD-5.7-01`
- 父规则 ID：`CSTD-5.7`
- 原规范章节：`5.7 函数的命名`
- 分类：命名规则
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`naming`, `functions`, `concurrency`

## 审核要求

具有互斥含义的变量或相反动作的函数，宜使用成对且语义正确的反义词命名。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.7`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.8-01] 下划线开始和结尾的定义

<!-- KB_METADATA {"check_id":"CSTD-5.8-01","rule_id":"CSTD-5.8","section":"5.8","category":"命名规则","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"automatic-or-hybrid","evidence_scope":"identifier/file/project","default_result":"advisory","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.8-01`
- 父规则 ID：`CSTD-5.8`
- 原规范章节：`5.8 下划线开始和结尾的定义`
- 分类：命名规则
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`naming`

## 审核要求

避免使用_EXAMPLE_TEST_之类以下划线开始和结尾的定义。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.8`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-5.9-01] 标识符长度

<!-- KB_METADATA {"check_id":"CSTD-5.9-01","rule_id":"CSTD-5.9","section":"5.9","category":"命名规则","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"identifier/file/project","default_result":"needs_review","target_languages":["C","C++"],"tags":["naming"]} -->

## 元数据

- 检查项 ID：`CSTD-5.9-01`
- 父规则 ID：`CSTD-5.9`
- 原规范章节：`5.9 标识符长度`
- 分类：命名规则
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`naming`

## 审核要求

标识符长度不能超过31个字符。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`identifier/file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 31 字符上限源于历史实现限制；现代工具链通常支持更长标识符。若保留，应作为项目兼容性政策。

## 追溯信息

- 本检查项来自父规则 `CSTD-5.9`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.1-01] 运算符的优先级

<!-- KB_METADATA {"check_id":"CSTD-6.1-01","rule_id":"CSTD-6.1","section":"6.1","category":"可读性","normative_level":"SHOULD","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"expression/function","default_result":"advisory","target_languages":["C","C++"],"tags":["readability","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-6.1-01`
- 父规则 ID：`CSTD-6.1`
- 原规范章节：`6.1 运算符的优先级`
- 分类：可读性
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`advisory`
- 标签：`readability`, `operators`

## 审核要求

应使用括号明确表达式的求值顺序，避免依赖不易理解的默认运算符优先级。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 可先自动发现候选问题，再结合上下文进行人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.2-01] 有意义标识的使用

<!-- KB_METADATA {"check_id":"CSTD-6.2-01","rule_id":"CSTD-6.2","section":"6.2","category":"可读性","normative_level":"SHOULD","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function","default_result":"advisory","target_languages":["C","C++"],"tags":["readability","macros"]} -->

## 元数据

- 检查项 ID：`CSTD-6.2-01`
- 父规则 ID：`CSTD-6.2`
- 原规范章节：`6.2 有意义标识的使用`
- 分类：可读性
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`advisory`
- 标签：`readability`, `macros`

## 审核要求

避免使用不易理解的数字，用有意义的标识来替代。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.2-02] 有意义标识的使用

<!-- KB_METADATA {"check_id":"CSTD-6.2-02","rule_id":"CSTD-6.2","section":"6.2","category":"可读性","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["readability","macros"]} -->

## 元数据

- 检查项 ID：`CSTD-6.2-02`
- 父规则 ID：`CSTD-6.2`
- 原规范章节：`6.2 有意义标识的使用`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`readability`, `macros`

## 审核要求

涉及物理状态或者含有物理意义的常量，不应直接使用数字，必须用有意义的枚举或宏来代替。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.3-01] 关系紧密的代码位置

<!-- KB_METADATA {"check_id":"CSTD-6.3-01","rule_id":"CSTD-6.3","section":"6.3","category":"可读性","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"expression/function","default_result":"advisory","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.3-01`
- 父规则 ID：`CSTD-6.3`
- 原规范章节：`6.3 关系紧密的代码位置`
- 分类：可读性
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`readability`

## 审核要求

关系紧密的代码宜相邻放置，以便阅读和查找。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.3`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.4-01] 语句的技巧性和易读性

<!-- KB_METADATA {"check_id":"CSTD-6.4-01","rule_id":"CSTD-6.4","section":"6.4","category":"可读性","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.4-01`
- 父规则 ID：`CSTD-6.4`
- 原规范章节：`6.4 语句的技巧性和易读性`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`readability`

## 审核要求

表达式的值必须在任何求值顺序下保持一致，不要使用难懂的技巧性很高的语句。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.4`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.5-01] 逗号操作符

<!-- KB_METADATA {"check_id":"CSTD-6.5-01","rule_id":"CSTD-6.5","section":"6.5","category":"可读性","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.5-01`
- 父规则 ID：`CSTD-6.5`
- 原规范章节：`6.5 逗号操作符`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`readability`

## 审核要求

不允许使用逗号操作符，为防止阅读混乱，逗号操作符可用其他等价形式替换。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.5`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.6-01] 嵌套

<!-- KB_METADATA {"check_id":"CSTD-6.6-01","rule_id":"CSTD-6.6","section":"6.6","category":"可读性","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.6-01`
- 父规则 ID：`CSTD-6.6`
- 原规范章节：`6.6 嵌套`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`readability`

## 审核要求

圆括号嵌套不超过32级。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 固定嵌套层数与编译器、静态分析器和项目复杂度预算有关，应由项目确认。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.6`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.6-02] 嵌套

<!-- KB_METADATA {"check_id":"CSTD-6.6-02","rule_id":"CSTD-6.6","section":"6.6","category":"可读性","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.6-02`
- 父规则 ID：`CSTD-6.6`
- 原规范章节：`6.6 嵌套`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`readability`

## 审核要求

if-else嵌套不超过15级。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 固定嵌套层数与编译器、静态分析器和项目复杂度预算有关，应由项目确认。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.6`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.6-03] 嵌套

<!-- KB_METADATA {"check_id":"CSTD-6.6-03","rule_id":"CSTD-6.6","section":"6.6","category":"可读性","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.6-03`
- 父规则 ID：`CSTD-6.6`
- 原规范章节：`6.6 嵌套`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`readability`

## 审核要求

#include文件不超过8级。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 固定嵌套层数与编译器、静态分析器和项目复杂度预算有关，应由项目确认。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.6`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-6.6-04] 嵌套

<!-- KB_METADATA {"check_id":"CSTD-6.6-04","rule_id":"CSTD-6.6","section":"6.6","category":"可读性","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["readability"]} -->

## 元数据

- 检查项 ID：`CSTD-6.6-04`
- 父规则 ID：`CSTD-6.6`
- 原规范章节：`6.6 嵌套`
- 分类：可读性
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`readability`

## 审核要求

#if 嵌套不超过8级。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 固定嵌套层数与编译器、静态分析器和项目复杂度预算有关，应由项目确认。

## 追溯信息

- 本检查项来自父规则 `CSTD-6.6`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.1-01] 没有必要的公共变量

<!-- KB_METADATA {"check_id":"CSTD-7.1-01","rule_id":"CSTD-7.1","section":"7.1","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.1-01`
- 父规则 ID：`CSTD-7.1`
- 原规范章节：`7.1 没有必要的公共变量`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`

## 审核要求

公共变量是增大模块间耦合的原因之一，故减少没必要的公共变量以降低模块间的耦合度。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.2-01] 公共变量耦合度

<!-- KB_METADATA {"check_id":"CSTD-7.2-01","rule_id":"CSTD-7.2","section":"7.2","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-7.2-01`
- 父规则 ID：`CSTD-7.2`
- 原规范章节：`7.2 公共变量耦合度`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `functions`

## 审核要求

降低公共变量的耦合度，构造仅有一个模块或函数可以修改、创建，而其余有关模块或函数只访问的公共变量，禁止多个不同模块或函数都可以修改、创建同一公共变量的现象。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.3-01] 公共变量的数据传递

<!-- KB_METADATA {"check_id":"CSTD-7.3-01","rule_id":"CSTD-7.3","section":"7.3","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.3-01`
- 父规则 ID：`CSTD-7.3`
- 原规范章节：`7.3 公共变量的数据传递`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

当向公共变量传递数据时，要防止赋予不合理的值或越界等现象发生。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.3-02] 公共变量的数据传递

<!-- KB_METADATA {"check_id":"CSTD-7.3-02","rule_id":"CSTD-7.3","section":"7.3","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.3-02`
- 父规则 ID：`CSTD-7.3`
- 原规范章节：`7.3 公共变量的数据传递`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

对公共变量赋值时，应有必要进行合法性检查，以提高代码的可靠性、稳定性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.4-01] 局部变量与全局变量同名

<!-- KB_METADATA {"check_id":"CSTD-7.4-01","rule_id":"CSTD-7.4","section":"7.4","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.4-01`
- 父规则 ID：`CSTD-7.4`
- 原规范章节：`7.4 局部变量与全局变量同名`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

禁止局部变量与全局变量同名。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.4`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.5-01] 自动变量赋值

<!-- KB_METADATA {"check_id":"CSTD-7.5-01","rule_id":"CSTD-7.5","section":"7.5","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.5-01`
- 父规则 ID：`CSTD-7.5`
- 原规范章节：`7.5 自动变量赋值`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

所有的自动变量在使用前都应被赋值。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.5`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.6-01] 数据类型的使用

<!-- KB_METADATA {"check_id":"CSTD-7.6-01","rule_id":"CSTD-7.6","section":"7.6","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.6-01`
- 父规则 ID：`CSTD-7.6`
- 原规范章节：`7.6 数据类型的使用`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

必须用typedef 显式标识出各数据类型的长度和符号特性,避免直接使用标准数据类型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 固定宽度整数优先使用 `<stdint.h>` 的 `int8_t`、`uint32_t` 等类型。
- 原示例把 `signed long` 定义为 `int64_t`，但 `long` 并不保证为 64 位，示例不可作为跨平台依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.6`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.6-02] 数据类型的使用

<!-- KB_METADATA {"check_id":"CSTD-7.6-02","rule_id":"CSTD-7.6","section":"7.6","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.6-02`
- 父规则 ID：`CSTD-7.6`
- 原规范章节：`7.6 数据类型的使用`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

不可使用_BOOL关键字。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 固定宽度整数优先使用 `<stdint.h>` 的 `int8_t`、`uint32_t` 等类型。
- 原示例把 `signed long` 定义为 `int64_t`，但 `long` 并不保证为 64 位，示例不可作为跨平台依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.6`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.7-01] 八进制的使用

<!-- KB_METADATA {"check_id":"CSTD-7.7-01","rule_id":"CSTD-7.7","section":"7.7","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.7-01`
- 父规则 ID：`CSTD-7.7`
- 原规范章节：`7.7 八进制的使用`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

不得使用八进制常数(0除外) 或八进制转义符。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.7`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.8-01] 结构体功能单一

<!-- KB_METADATA {"check_id":"CSTD-7.8-01","rule_id":"CSTD-7.8","section":"7.8","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.8-01`
- 父规则 ID：`CSTD-7.8`
- 原规范章节：`7.8 结构体功能单一`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

结构体的功能要单一，是针对一种事务的抽象。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.8`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.8-02] 结构体功能单一

<!-- KB_METADATA {"check_id":"CSTD-7.8-02","rule_id":"CSTD-7.8","section":"7.8","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.8-02`
- 父规则 ID：`CSTD-7.8`
- 原规范章节：`7.8 结构体功能单一`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`

## 审核要求

设计结构体时应力争使结构体代表一种现实事务的抽象，而不是同时代表多种。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.8`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.8-03] 结构体功能单一

<!-- KB_METADATA {"check_id":"CSTD-7.8-03","rule_id":"CSTD-7.8","section":"7.8","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.8-03`
- 父规则 ID：`CSTD-7.8`
- 原规范章节：`7.8 结构体功能单一`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

结构体中的各元素应代表同一事务的不同侧面，而不应把描述没有关系或关系很弱的不同事务的元素放到同一结构体中。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.8`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.8-04] 结构体功能单一

<!-- KB_METADATA {"check_id":"CSTD-7.8-04","rule_id":"CSTD-7.8","section":"7.8","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.8-04`
- 父规则 ID：`CSTD-7.8`
- 原规范章节：`7.8 结构体功能单一`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`

## 审核要求

不要设计面面俱到、非常灵活的数据结构。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.8`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.9-01] 结构体与结构体之间

<!-- KB_METADATA {"check_id":"CSTD-7.9-01","rule_id":"CSTD-7.9","section":"7.9","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.9-01`
- 父规则 ID：`CSTD-7.9`
- 原规范章节：`7.9 结构体与结构体之间`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`

## 审核要求

不同结构体间的关系不要过于复杂。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.9`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.10-01] 结构体中元素的个数

<!-- KB_METADATA {"check_id":"CSTD-7.10-01","rule_id":"CSTD-7.10","section":"7.10","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.10-01`
- 父规则 ID：`CSTD-7.10`
- 原规范章节：`7.10 结构体中元素的个数`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`

## 审核要求

结构体中元素个数适中，若结构体中元素个数过多可考虑依据某种原则把元素组成不同的子结构体，以减少原结构体中元素的个数，增加结构体的可理解性、可操作性和可维护性。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.10`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.11-01] 结构体元素的布局及排列

<!-- KB_METADATA {"check_id":"CSTD-7.11-01","rule_id":"CSTD-7.11","section":"7.11","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs","memory","bit-fields"]} -->

## 元数据

- 检查项 ID：`CSTD-7.11-01`
- 父规则 ID：`CSTD-7.11`
- 原规范章节：`7.11 结构体元素的布局及排列`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`, `memory`, `bit-fields`

## 审核要求

结构体成员的布局和排列应兼顾可理解性、空间占用和误用风险。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.11`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.11-02] 结构体元素的布局及排列

<!-- KB_METADATA {"check_id":"CSTD-7.11-02","rule_id":"CSTD-7.11","section":"7.11","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","memory","bit-fields"]} -->

## 元数据

- 检查项 ID：`CSTD-7.11-02`
- 父规则 ID：`CSTD-7.11`
- 原规范章节：`7.11 结构体元素的布局及排列`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `memory`, `bit-fields`

## 审核要求

位域应单独定义为结构体；在其他结构体中使用时，应作为独立成员。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.11`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.11-03] 结构体元素的布局及排列

<!-- KB_METADATA {"check_id":"CSTD-7.11-03","rule_id":"CSTD-7.11","section":"7.11","category":"常量、变量、结构体","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"declaration/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["types","variables","structs","memory","bit-fields"]} -->

## 元数据

- 检查项 ID：`CSTD-7.11-03`
- 父规则 ID：`CSTD-7.11`
- 原规范章节：`7.11 结构体元素的布局及排列`
- 分类：常量、变量、结构体
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`types`, `variables`, `structs`, `memory`, `bit-fields`

## 审核要求

使用结构体时应考虑不同编译器和 ABI 的对齐差异。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.11`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.12-01] 数据类型转换

<!-- KB_METADATA {"check_id":"CSTD-7.12-01","rule_id":"CSTD-7.12","section":"7.12","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","type-conversion"]} -->

## 元数据

- 检查项 ID：`CSTD-7.12-01`
- 父规则 ID：`CSTD-7.12`
- 原规范章节：`7.12 数据类型转换`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `type-conversion`

## 审核要求

禁止数据大小超限的强制数据类型转换和隐性数据类型转换。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.12`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.13-01] 函数指针的类型转换

<!-- KB_METADATA {"check_id":"CSTD-7.13-01","rule_id":"CSTD-7.13","section":"7.13","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","functions","type-conversion"]} -->

## 元数据

- 检查项 ID：`CSTD-7.13-01`
- 父规则 ID：`CSTD-7.13`
- 原规范章节：`7.13 函数指针的类型转换`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `functions`, `type-conversion`

## 审核要求

指向某一函数的指针不可强制转换为指向另一函数的指针。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.13`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.14-01] 指针属性

<!-- KB_METADATA {"check_id":"CSTD-7.14-01","rule_id":"CSTD-7.14","section":"7.14","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","type-conversion"]} -->

## 元数据

- 检查项 ID：`CSTD-7.14-01`
- 父规则 ID：`CSTD-7.14`
- 原规范章节：`7.14 指针属性`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `type-conversion`

## 审核要求

类型转换过程中不能丢失指针的const、volatile属性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.14`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.15-01] 常量

<!-- KB_METADATA {"check_id":"CSTD-7.15-01","rule_id":"CSTD-7.15","section":"7.15","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.15-01`
- 父规则 ID：`CSTD-7.15`
- 原规范章节：`7.15 常量`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

在所有unsigned 类型的常量后应添加后缀“U”。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.15`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.16-01] 重复定义类型

<!-- KB_METADATA {"check_id":"CSTD-7.16-01","rule_id":"CSTD-7.16","section":"7.16","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.16-01`
- 父规则 ID：`CSTD-7.16`
- 原规范章节：`7.16 重复定义类型`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

禁止重复定义类型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.16`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.17-01] 对位域的定义

<!-- KB_METADATA {"check_id":"CSTD-7.17-01","rule_id":"CSTD-7.17","section":"7.17","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["types","variables","structs","bit-fields"]} -->

## 元数据

- 检查项 ID：`CSTD-7.17-01`
- 父规则 ID：`CSTD-7.17`
- 原规范章节：`7.17 对位域的定义`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`types`, `variables`, `structs`, `bit-fields`

## 审核要求

对结构中位域的宽度不能大于int类型的宽度（一般为32位）。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 位域宽度应以其声明基类型和具体实现为依据，不宜一概以 32 位 `int` 为通用上限。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.17`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.18-01] 二进制的使用

<!-- KB_METADATA {"check_id":"CSTD-7.18-01","rule_id":"CSTD-7.18","section":"7.18","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.18-01`
- 父规则 ID：`CSTD-7.18`
- 原规范章节：`7.18 二进制的使用`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`types`, `variables`, `structs`

## 审核要求

不得使用二进制常数(0 除外)。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 二进制整数字面量在 C++14 和 C23 已标准化；是否禁用取决于目标语言版本和工具链。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.18`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.19-01] 十六进制转义字符、非标准转义字符、特殊字符

<!-- KB_METADATA {"check_id":"CSTD-7.19-01","rule_id":"CSTD-7.19","section":"7.19","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.19-01`
- 父规则 ID：`CSTD-7.19`
- 原规范章节：`7.19 十六进制转义字符、非标准转义字符、特殊字符`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`types`, `variables`, `structs`

## 审核要求

不得使用十六进制转义字符、非标准转义字符及其他特殊字符。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 十六进制转义字符本身是标准 C/C++ 语法；全面禁用属于项目可读性或编码政策。非标准转义字符则应禁止。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.19`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.20-01] 结构体初始化

<!-- KB_METADATA {"check_id":"CSTD-7.20-01","rule_id":"CSTD-7.20","section":"7.20","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.20-01`
- 父规则 ID：`CSTD-7.20`
- 原规范章节：`7.20 结构体初始化`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

结构体初始化不可省略相应的{}。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.20`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.21-01] 运算符左值右值取值范围

<!-- KB_METADATA {"check_id":"CSTD-7.21-01","rule_id":"CSTD-7.21","section":"7.21","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-7.21-01`
- 父规则 ID：`CSTD-7.21`
- 原规范章节：`7.21 运算符左值右值取值范围`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `operators`

## 审核要求

`*`、`/` 的两个操作数必须为算术类型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.21`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.21-02] 运算符左值右值取值范围

<!-- KB_METADATA {"check_id":"CSTD-7.21-02","rule_id":"CSTD-7.21","section":"7.21","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-7.21-02`
- 父规则 ID：`CSTD-7.21`
- 原规范章节：`7.21 运算符左值右值取值范围`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `operators`

## 审核要求

`+` 的两个操作数必须均为算术类型，或一个为指针、另一个为整数类型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.21`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.21-03] 运算符左值右值取值范围

<!-- KB_METADATA {"check_id":"CSTD-7.21-03","rule_id":"CSTD-7.21","section":"7.21","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-7.21-03`
- 父规则 ID：`CSTD-7.21`
- 原规范章节：`7.21 运算符左值右值取值范围`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `operators`

## 审核要求

`-` 的两个操作数必须均为算术类型，或均为兼容指针类型，或左侧为指针且右侧为整数类型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.21`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.21-04] 运算符左值右值取值范围

<!-- KB_METADATA {"check_id":"CSTD-7.21-04","rule_id":"CSTD-7.21","section":"7.21","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-7.21-04`
- 父规则 ID：`CSTD-7.21`
- 原规范章节：`7.21 运算符左值右值取值范围`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `operators`

## 审核要求

关系运算符 `<`、`<=`、`>=`、`>` 的操作数必须满足算术类型或可进行关系比较的指针类型要求。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.21`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.21-05] 运算符左值右值取值范围

<!-- KB_METADATA {"check_id":"CSTD-7.21-05","rule_id":"CSTD-7.21","section":"7.21","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-7.21-05`
- 父规则 ID：`CSTD-7.21`
- 原规范章节：`7.21 运算符左值右值取值范围`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`, `operators`

## 审核要求

相等运算符 `==`、`!=` 的操作数必须满足算术类型或语言允许的指针比较要求。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.21`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.22-01] 有符号数赋值

<!-- KB_METADATA {"check_id":"CSTD-7.22-01","rule_id":"CSTD-7.22","section":"7.22","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.22-01`
- 父规则 ID：`CSTD-7.22`
- 原规范章节：`7.22 有符号数赋值`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

禁止使用十六进制对有符号数进行赋初值。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.22`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.23-01] 使用合适的存储期声明目标

<!-- KB_METADATA {"check_id":"CSTD-7.23-01","rule_id":"CSTD-7.23","section":"7.23","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.23-01`
- 父规则 ID：`CSTD-7.23`
- 原规范章节：`7.23 使用合适的存储期声明目标`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

禁止访问超出存续时间的目标，否则会导致未定义行为。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.23`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.24-01] 使用正确语法声明柔性数组成员

<!-- KB_METADATA {"check_id":"CSTD-7.24-01","rule_id":"CSTD-7.24","section":"7.24","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-7.24-01`
- 父规则 ID：`CSTD-7.24`
- 原规范章节：`7.24 使用正确语法声明柔性数组成员`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `arrays`

## 审核要求

柔性数组成员必须是结构体的最后一个成员。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.24`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.24-02] 使用正确语法声明柔性数组成员

<!-- KB_METADATA {"check_id":"CSTD-7.24-02","rule_id":"CSTD-7.24","section":"7.24","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-7.24-02`
- 父规则 ID：`CSTD-7.24`
- 原规范章节：`7.24 使用正确语法声明柔性数组成员`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `arrays`

## 审核要求

数组元素类型的结构体不能包含柔性数组成员。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.24`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.24-03] 使用正确语法声明柔性数组成员

<!-- KB_METADATA {"check_id":"CSTD-7.24-03","rule_id":"CSTD-7.24","section":"7.24","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-7.24-03`
- 父规则 ID：`CSTD-7.24`
- 原规范章节：`7.24 使用正确语法声明柔性数组成员`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `arrays`

## 审核要求

包含柔性数组成员的结构体不能作为其他结构体的普通成员；原规范仅允许其位于外层结构体最后一个成员的位置。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.24`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.24-04] 使用正确语法声明柔性数组成员

<!-- KB_METADATA {"check_id":"CSTD-7.24-04","rule_id":"CSTD-7.24","section":"7.24","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-7.24-04`
- 父规则 ID：`CSTD-7.24`
- 原规范章节：`7.24 使用正确语法声明柔性数组成员`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `arrays`

## 审核要求

包含柔性数组成员的结构体还必须至少包含一个其他命名成员。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.24`，该父规则共拆分为 4 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.25-01] 越过可信边界传递结构体时应避免信息泄露

<!-- KB_METADATA {"check_id":"CSTD-7.25-01","rule_id":"CSTD-7.25","section":"7.25","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"critical","review_mode":"hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-7.25-01`
- 父规则 ID：`CSTD-7.25`
- 原规范章节：`7.25 越过可信边界传递结构体时应避免信息泄露`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`critical`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`

## 审核要求

结构体或共用体越过可信边界前，必须防止填充字节或填充位泄露未初始化信息。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.25`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-7.26-01] 不要将指针强制转换为对其要求更加严格的指针类型

<!-- KB_METADATA {"check_id":"CSTD-7.26-01","rule_id":"CSTD-7.26","section":"7.26","category":"常量、变量、结构体","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"declaration/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["types","variables","structs","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-7.26-01`
- 父规则 ID：`CSTD-7.26`
- 原规范章节：`7.26 不要将指针强制转换为对其要求更加严格的指针类型`
- 分类：常量、变量、结构体
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`types`, `variables`, `structs`, `pointers`

## 审核要求

如果一个指针要转换为指向另一不同目标类型的指针，则后者必须有更加宽松的对其要求；否则，将导致未定义的结果。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`declaration/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-7.26`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.1-01] 数组大小

<!-- KB_METADATA {"check_id":"CSTD-8.1-01","rule_id":"CSTD-8.1","section":"8.1","category":"数组","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["arrays","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-8.1-01`
- 父规则 ID：`CSTD-8.1`
- 原规范章节：`8.1 数组大小`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`arrays`, `pointers`

## 审核要求

数组的大小应该显式声明或者通过初始化进行隐式定义，且数组大小不能超过32767个字节。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 数组总大小不超过 32767 字节是平台相关限制，不是现代 C/C++ 的通用上限。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.2-01] 数组初始化

<!-- KB_METADATA {"check_id":"CSTD-8.2-01","rule_id":"CSTD-8.2","section":"8.2","category":"数组","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["arrays","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-8.2-01`
- 父规则 ID：`CSTD-8.2`
- 原规范章节：`8.2 数组初始化`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`arrays`, `pointers`

## 审核要求

除 `{0}` 外，原规范要求数组初始化项数量不得少于数组大小。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- C/C++ 允许聚合对象部分初始化，未显式给出的其余元素会按语言规则初始化；原文将其一律判为非法属于更严格的项目政策。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.2-02] 数组初始化

<!-- KB_METADATA {"check_id":"CSTD-8.2-02","rule_id":"CSTD-8.2","section":"8.2","category":"数组","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["arrays","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-8.2-02`
- 父规则 ID：`CSTD-8.2`
- 原规范章节：`8.2 数组初始化`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`arrays`, `pointers`

## 审核要求

数组初始化不得省略相应层级的花括号。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- C/C++ 允许聚合对象部分初始化，未显式给出的其余元素会按语言规则初始化；原文将其一律判为非法属于更严格的项目政策。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.3-01] 没有指向同一个数组的2个指针之间不能相减和比较

<!-- KB_METADATA {"check_id":"CSTD-8.3-01","rule_id":"CSTD-8.3","section":"8.3","category":"数组","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["arrays","pointers","memory","functions","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-8.3-01`
- 父规则 ID：`CSTD-8.3`
- 原规范章节：`8.3 没有指向同一个数组的2个指针之间不能相减和比较`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`arrays`, `pointers`, `memory`, `functions`, `operators`

## 审核要求

不指向同一数组（含 one-past）的两个指针不得相减。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 标题中的“比较”容易被误解；正文已明确：不同数组指针不得做关系比较或相减，但 `==`、`!=` 可以比较。
- 原错误示例中的 `& - next_num_ptr` 疑似缺失数组末端指针表达式。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.3`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.3-02] 没有指向同一个数组的2个指针之间不能相减和比较

<!-- KB_METADATA {"check_id":"CSTD-8.3-02","rule_id":"CSTD-8.3","section":"8.3","category":"数组","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["arrays","pointers","memory","functions","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-8.3-02`
- 父规则 ID：`CSTD-8.3`
- 原规范章节：`8.3 没有指向同一个数组的2个指针之间不能相减和比较`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`arrays`, `pointers`, `memory`, `functions`, `operators`

## 审核要求

不指向同一数组的两个指针不得使用 `<`、`<=`、`>=`、`>` 做关系比较。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 标题中的“比较”容易被误解；正文已明确：不同数组指针不得做关系比较或相减，但 `==`、`!=` 可以比较。
- 原错误示例中的 `& - next_num_ptr` 疑似缺失数组末端指针表达式。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.3`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.3-03] 没有指向同一个数组的2个指针之间不能相减和比较

<!-- KB_METADATA {"check_id":"CSTD-8.3-03","rule_id":"CSTD-8.3","section":"8.3","category":"数组","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"violation","target_languages":["C","C++"],"tags":["arrays","pointers","memory","functions","operators"]} -->

## 元数据

- 检查项 ID：`CSTD-8.3-03`
- 父规则 ID：`CSTD-8.3`
- 原规范章节：`8.3 没有指向同一个数组的2个指针之间不能相减和比较`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`arrays`, `pointers`, `memory`, `functions`, `operators`

## 审核要求

任意两个指针可使用 `==`、`!=` 做相等性比较。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 标题中的“比较”容易被误解；正文已明确：不同数组指针不得做关系比较或相减，但 `==`、`!=` 可以比较。
- 原错误示例中的 `& - next_num_ptr` 疑似缺失数组末端指针表达式。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.3`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-8.4-01] 不要对指向非数组目标的指针进行加减

<!-- KB_METADATA {"check_id":"CSTD-8.4-01","rule_id":"CSTD-8.4","section":"8.4","category":"数组","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function","default_result":"needs_review","target_languages":["C","C++"],"tags":["arrays","pointers","memory","functions","structs"]} -->

## 元数据

- 检查项 ID：`CSTD-8.4-01`
- 父规则 ID：`CSTD-8.4`
- 原规范章节：`8.4 不要对指向非数组目标的指针进行加减`
- 分类：数组
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`high`
- 默认结果：`needs_review`
- 标签：`arrays`, `pointers`, `memory`, `functions`, `structs`

## 审核要求

不得通过对非数组对象成员的指针进行递增、递减或偏移来遍历对象布局。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 该条是保守规则；实施时应按目标 C/C++ 标准对单对象、数组元素及 one-past 指针的规则精确判断。

## 追溯信息

- 本检查项来自父规则 `CSTD-8.4`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.1-01] 函数参数检查

<!-- KB_METADATA {"check_id":"CSTD-9.1-01","rule_id":"CSTD-9.1","section":"9.1","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.1-01`
- 父规则 ID：`CSTD-9.1`
- 原规范章节：`9.1 函数参数检查`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

对接口函数参数的合法性检查应由接口函数本身负责。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.2-01] 函数的参数处理

<!-- KB_METADATA {"check_id":"CSTD-9.2-01","rule_id":"CSTD-9.2","section":"9.2","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.2-01`
- 父规则 ID：`CSTD-9.2`
- 原规范章节：`9.2 函数的参数处理`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

对于必须修改的输出参数，原规范要求先在局部变量中完成计算，最后再写回参数。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.3-01] 函数的规模

<!-- KB_METADATA {"check_id":"CSTD-9.3-01","rule_id":"CSTD-9.3","section":"9.3","category":"函数、过程","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["functions","interfaces","comments"]} -->

## 元数据

- 检查项 ID：`CSTD-9.3-01`
- 父规则 ID：`CSTD-9.3`
- 原规范章节：`9.3 函数的规模`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`functions`, `interfaces`, `comments`

## 审核要求

函数的规模尽量限制在200行以内，不包括注释和空格行。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.3`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.4-01] 为重复实现的功能编写函数

<!-- KB_METADATA {"check_id":"CSTD-9.4-01","rule_id":"CSTD-9.4","section":"9.4","category":"函数、过程","normative_level":"SHOULD","policy_status":"active-example-warning","risk":"low","review_mode":"manual","evidence_scope":"function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.4-01`
- 父规则 ID：`CSTD-9.4`
- 原规范章节：`9.4 为重复实现的功能编写函数`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：有效，但示例有缺陷
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`functions`, `interfaces`

## 审核要求

一个函数宜只完成一项明确功能；重复实现的功能宜提取为函数。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- “所有函数均应可重入”属于特定系统要求，通用项目需结合线程模型确认。
- 原文后续宏式 MAX 示例若重复求值实参可能产生副作用，不能作为无条件推荐。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.4`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.4-02] 为重复实现的功能编写函数

<!-- KB_METADATA {"check_id":"CSTD-9.4-02","rule_id":"CSTD-9.4","section":"9.4","category":"函数、过程","normative_level":"SHOULD","policy_status":"active-example-warning","risk":"low","review_mode":"manual","evidence_scope":"function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.4-02`
- 父规则 ID：`CSTD-9.4`
- 原规范章节：`9.4 为重复实现的功能编写函数`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：有效，但示例有缺陷
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`functions`, `interfaces`

## 审核要求

原规范要求所编写的函数具备可重入性。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- “所有函数均应可重入”属于特定系统要求，通用项目需结合线程模型确认。
- 原文后续宏式 MAX 示例若重复求值实参可能产生副作用，不能作为无条件推荐。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.4`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.5-01] 函数功能的可预测性

<!-- KB_METADATA {"check_id":"CSTD-9.5-01","rule_id":"CSTD-9.5","section":"9.5","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.5-01`
- 父规则 ID：`CSTD-9.5`
- 原规范章节：`9.5 函数功能的可预测性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数在相同输入和相同约定状态下应产生可预测的输出。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.5-02] 函数功能的可预测性

<!-- KB_METADATA {"check_id":"CSTD-9.5-02","rule_id":"CSTD-9.5","section":"9.5","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.5-02`
- 父规则 ID：`CSTD-9.5`
- 原规范章节：`9.5 函数功能的可预测性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

应避免使用未在接口契约中说明的静态局部状态改变函数结果。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.6-01] 减少函数参数

<!-- KB_METADATA {"check_id":"CSTD-9.6-01","rule_id":"CSTD-9.6","section":"9.6","category":"函数、过程","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"hybrid","evidence_scope":"function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.6-01`
- 父规则 ID：`CSTD-9.6`
- 原规范章节：`9.6 减少函数参数`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`functions`, `interfaces`

## 审核要求

不使用的参数从接口中去掉，目的为了减少函数间接口的复杂度。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.6`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.7-01] 函数形参

<!-- KB_METADATA {"check_id":"CSTD-9.7-01","rule_id":"CSTD-9.7","section":"9.7","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces","pointers","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-9.7-01`
- 父规则 ID：`CSTD-9.7`
- 原规范章节：`9.7 函数形参`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`, `pointers`, `arrays`

## 审核要求

函数形参禁止使用数组，应使用指针形式。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 函数形参数组声明在语言层面会调整为指针类型；禁用数组写法主要是接口风格政策。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.7`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.8-01] 非调度函数的参数

<!-- KB_METADATA {"check_id":"CSTD-9.8-01","rule_id":"CSTD-9.8","section":"9.8","category":"函数、过程","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.8-01`
- 父规则 ID：`CSTD-9.8`
- 原规范章节：`9.8 非调度函数的参数`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`functions`, `interfaces`

## 审核要求

非调度函数宜减少或避免控制参数，优先只接收数据参数。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.8`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.9-01] 函数参数输入与非参数输入的有效性

<!-- KB_METADATA {"check_id":"CSTD-9.9-01","rule_id":"CSTD-9.9","section":"9.9","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.9-01`
- 父规则 ID：`CSTD-9.9`
- 原规范章节：`9.9 函数参数输入与非参数输入的有效性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数使用参数前必须检查所有参数输入的有效性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.9`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.9-02] 函数参数输入与非参数输入的有效性

<!-- KB_METADATA {"check_id":"CSTD-9.9-02","rule_id":"CSTD-9.9","section":"9.9","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.9-02`
- 父规则 ID：`CSTD-9.9`
- 原规范章节：`9.9 函数参数输入与非参数输入的有效性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数使用全局变量等非参数输入前必须检查其有效性。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.9`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.10-01] 函数返回值

<!-- KB_METADATA {"check_id":"CSTD-9.10-01","rule_id":"CSTD-9.10","section":"9.10","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.10-01`
- 父规则 ID：`CSTD-9.10`
- 原规范章节：`9.10 函数返回值`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

不要把与函数返回值类型不同的变量，以编译系统默认的转换方式或强制的转换方式作为返回值返回。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.10`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.11-01] 函数的调用

<!-- KB_METADATA {"check_id":"CSTD-9.11-01","rule_id":"CSTD-9.11","section":"9.11","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces","type-conversion"]} -->

## 元数据

- 检查项 ID：`CSTD-9.11-01`
- 父规则 ID：`CSTD-9.11`
- 原规范章节：`9.11 函数的调用`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`, `type-conversion`

## 审核要求

不得使用函数参与逻辑运算。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- “不得使用函数参与逻辑运算”过于宽泛；返回布尔值的谓词函数参与条件表达式是常见合法写法。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.11`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.11-02] 函数的调用

<!-- KB_METADATA {"check_id":"CSTD-9.11-02","rule_id":"CSTD-9.11","section":"9.11","category":"函数、过程","normative_level":"SHOULD","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces","type-conversion"]} -->

## 元数据

- 检查项 ID：`CSTD-9.11-02`
- 父规则 ID：`CSTD-9.11`
- 原规范章节：`9.11 函数的调用`
- 分类：函数、过程
- 规范强度：`SHOULD`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`, `type-conversion`

## 审核要求

在调用函数填写参数时，减少没有必要的默认数据类型转换或强制数据类型转换。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- “不得使用函数参与逻辑运算”过于宽泛；返回布尔值的谓词函数参与条件表达式是常见合法写法。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.11`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.12-01] 禁止随机内聚

<!-- KB_METADATA {"check_id":"CSTD-9.12-01","rule_id":"CSTD-9.12","section":"9.12","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.12-01`
- 父规则 ID：`CSTD-9.12`
- 原规范章节：`9.12 禁止随机内聚`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数或过程不得包含彼此无关或关联很弱的随机内聚语句。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.12`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.13-01] 高扇入、合理扇出的函数

<!-- KB_METADATA {"check_id":"CSTD-9.13-01","rule_id":"CSTD-9.13","section":"9.13","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.13-01`
- 父规则 ID：`CSTD-9.13`
- 原规范章节：`9.13 高扇入、合理扇出的函数`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`

## 审核要求

函数设计宜具有较高扇入和合理扇出。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 扇出 3～5 是设计启发式，不应脱离模块职责和调用图直接判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.13`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.13-02] 高扇入、合理扇出的函数

<!-- KB_METADATA {"check_id":"CSTD-9.13-02","rule_id":"CSTD-9.13","section":"9.13","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.13-02`
- 父规则 ID：`CSTD-9.13`
- 原规范章节：`9.13 高扇入、合理扇出的函数`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`

## 审核要求

原规范建议非调度函数的扇出通常为 3～5；该数值只能作为启发式参考。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 扇出 3～5 是设计启发式，不应脱离模块职责和调用图直接判违规。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.13`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.14-01] 递归函数

<!-- KB_METADATA {"check_id":"CSTD-9.14-01","rule_id":"CSTD-9.14","section":"9.14","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.14-01`
- 父规则 ID：`CSTD-9.14`
- 原规范章节：`9.14 递归函数`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`

## 审核要求

禁止使用函数本身或函数间的递归调用。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 全面禁止递归属于嵌入式或栈资源受限项目政策；通用项目应结合深度上界和资源预算判断。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.14`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.15-01] 函数返回值的引用

<!-- KB_METADATA {"check_id":"CSTD-9.15-01","rule_id":"CSTD-9.15","section":"9.15","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.15-01`
- 父规则 ID：`CSTD-9.15`
- 原规范章节：`9.15 函数返回值的引用`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`

## 审核要求

对于提供了返回值的函数，在引用时要使用其返回值。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 部分 API 的返回值可按契约安全忽略；应结合函数声明、属性和接口文档判定。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.15`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.16-01] 函数出口唯一性

<!-- KB_METADATA {"check_id":"CSTD-9.16-01","rule_id":"CSTD-9.16","section":"9.16","category":"函数、过程","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.16-01`
- 父规则 ID：`CSTD-9.16`
- 原规范章节：`9.16 函数出口唯一性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`functions`, `interfaces`

## 审核要求

函数只能有一个出口，这个出口必须在函数末尾。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 单一出口不是通用最佳实践；用于参数校验或错误处理的早返回可能更清晰。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.16`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.17-01] 函数原型声明

<!-- KB_METADATA {"check_id":"CSTD-9.17-01","rule_id":"CSTD-9.17","section":"9.17","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.17-01`
- 父规则 ID：`CSTD-9.17`
- 原规范章节：`9.17 函数原型声明`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数应声明原型。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.17`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.17-02] 函数原型声明

<!-- KB_METADATA {"check_id":"CSTD-9.17-02","rule_id":"CSTD-9.17","section":"9.17","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces"]} -->

## 元数据

- 检查项 ID：`CSTD-9.17-02`
- 父规则 ID：`CSTD-9.17`
- 原规范章节：`9.17 函数原型声明`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`

## 审核要求

函数声明与函数定义中的参数标识符应保持一致。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.17`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.18-01] 外部对象声明唯一性

<!-- KB_METADATA {"check_id":"CSTD-9.18-01","rule_id":"CSTD-9.18","section":"9.18","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-9.18-01`
- 父规则 ID：`CSTD-9.18`
- 原规范章节：`9.18 外部对象声明唯一性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`, `headers`

## 审核要求

外部对象应该声明在唯一的头文件中，该对象可以是变量或函数。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.18`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.18-02] 外部对象声明唯一性

<!-- KB_METADATA {"check_id":"CSTD-9.18-02","rule_id":"CSTD-9.18","section":"9.18","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-9.18-02`
- 父规则 ID：`CSTD-9.18`
- 原规范章节：`9.18 外部对象声明唯一性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`, `headers`

## 审核要求

通常在一个头文件中声明一个外部标识符，而在定义或使用该标识符的文件中包含这个头文件，不可直接在C文件中声明。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.18`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-9.18-03] 外部对象声明唯一性

<!-- KB_METADATA {"check_id":"CSTD-9.18-03","rule_id":"CSTD-9.18","section":"9.18","category":"函数、过程","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"function/module","default_result":"violation","target_languages":["C","C++"],"tags":["functions","interfaces","headers"]} -->

## 元数据

- 检查项 ID：`CSTD-9.18-03`
- 父规则 ID：`CSTD-9.18`
- 原规范章节：`9.18 外部对象声明唯一性`
- 分类：函数、过程
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`functions`, `interfaces`, `headers`

## 审核要求

引用其他模块变量需要包含该变量所在模块的头文件。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-9.18`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.1-01] 空间效率

<!-- KB_METADATA {"check_id":"CSTD-10.1-01","rule_id":"CSTD-10.1","section":"10.1","category":"程序效率","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"advisory","target_languages":["C","C++"],"tags":["performance"]} -->

## 元数据

- 检查项 ID：`CSTD-10.1-01`
- 父规则 ID：`CSTD-10.1`
- 原规范章节：`10.1 空间效率`
- 分类：程序效率
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`performance`

## 审核要求

通过对系统数据结构的划分与组织的改进，以及对程序算法的优化来提高空间效率。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.2-01] 循环体内工作量最小化

<!-- KB_METADATA {"check_id":"CSTD-10.2-01","rule_id":"CSTD-10.2","section":"10.2","category":"程序效率","normative_level":"MUST","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"violation","target_languages":["C","C++"],"tags":["performance","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.2-01`
- 父规则 ID：`CSTD-10.2`
- 原规范章节：`10.2 循环体内工作量最小化`
- 分类：程序效率
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`violation`
- 标签：`performance`, `loops`

## 审核要求

应仔细考虑循环体内的语句是否可以放在循环体之外，使循环体内工作量最小，从而提高程序的时间效率。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.3-01] 提高效率的其他方法

<!-- KB_METADATA {"check_id":"CSTD-10.3-01","rule_id":"CSTD-10.3","section":"10.3","category":"程序效率","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"needs_review","target_languages":["C","C++"],"tags":["performance","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.3-01`
- 父规则 ID：`CSTD-10.3`
- 原规范章节：`10.3 提高效率的其他方法`
- 分类：程序效率
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`performance`, `functions`, `loops`

## 审核要求

应分析并优化模块内函数的划分和组织方式。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.3`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.3-02] 提高效率的其他方法

<!-- KB_METADATA {"check_id":"CSTD-10.3-02","rule_id":"CSTD-10.3","section":"10.3","category":"程序效率","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"needs_review","target_languages":["C","C++"],"tags":["performance","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.3-02`
- 父规则 ID：`CSTD-10.3`
- 原规范章节：`10.3 提高效率的其他方法`
- 分类：程序效率
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`performance`, `functions`, `loops`

## 审核要求

原规范要求在多重循环中将循环次数最多的循环放在最内层。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.3`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.3-03] 提高效率的其他方法

<!-- KB_METADATA {"check_id":"CSTD-10.3-03","rule_id":"CSTD-10.3","section":"10.3","category":"程序效率","normative_level":"SHOULD","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"needs_review","target_languages":["C","C++"],"tags":["performance","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.3-03`
- 父规则 ID：`CSTD-10.3`
- 原规范章节：`10.3 提高效率的其他方法`
- 分类：程序效率
- 规范强度：`SHOULD`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`performance`, `functions`, `loops`

## 审核要求

宜减少循环嵌套层次。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.3`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.3-04] 提高效率的其他方法

<!-- KB_METADATA {"check_id":"CSTD-10.3-04","rule_id":"CSTD-10.3","section":"10.3","category":"程序效率","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"needs_review","target_languages":["C","C++"],"tags":["performance","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.3-04`
- 父规则 ID：`CSTD-10.3`
- 原规范章节：`10.3 提高效率的其他方法`
- 分类：程序效率
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`performance`, `functions`, `loops`

## 审核要求

当循环内判断与循环变量无关时，宜将判断移到循环外层。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.3`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-10.3-05] 提高效率的其他方法

<!-- KB_METADATA {"check_id":"CSTD-10.3-05","rule_id":"CSTD-10.3","section":"10.3","category":"程序效率","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"manual","evidence_scope":"function/module/runtime","default_result":"needs_review","target_languages":["C","C++"],"tags":["performance","functions","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-10.3-05`
- 父规则 ID：`CSTD-10.3`
- 原规范章节：`10.3 提高效率的其他方法`
- 分类：程序效率
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`performance`, `functions`, `loops`

## 审核要求

原规范要求用乘法或其他方法替代除法，并禁止浮点运算。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`function/module/runtime`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原文把循环次数最多的循环放在最内层作为固定优化，但 C 行优先数组的访问局部性可能使示例改写更慢。
- “用乘法替代除法”和“不得使用浮点运算”依赖目标硬件、精度和编译器；示例中的倒数仍是浮点表达式。
- 本条不得自动判违规，应以性能测量、目标平台和数值精度要求为依据。

## 追溯信息

- 本检查项来自父规则 `CSTD-10.3`，该父规则共拆分为 5 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.1-01] 防止内存操作越界

<!-- KB_METADATA {"check_id":"CSTD-11.1-01","rule_id":"CSTD-11.1","section":"11.1","category":"质量保证","normative_level":"MUST","policy_status":"active-example-warning","risk":"critical","review_mode":"hybrid","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety","memory","pointers","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-11.1-01`
- 父规则 ID：`CSTD-11.1`
- 原规范章节：`11.1 防止内存操作越界`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`critical`
- 默认结果：`violation`
- 标签：`quality`, `safety`, `memory`, `pointers`, `arrays`

## 审核要求

所有数组、指针和内存地址操作必须保持在有效对象边界内。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原“解决示例”仅把索引改为 `usr_no - 1`，仍未检查 `usr_no` 是否处于 1～10；输入为 0 或大于 10 时仍可能越界。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.1-02] 防止内存操作越界

<!-- KB_METADATA {"check_id":"CSTD-11.1-02","rule_id":"CSTD-11.1","section":"11.1","category":"质量保证","normative_level":"MUST","policy_status":"active-example-warning","risk":"critical","review_mode":"hybrid","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety","memory","pointers","arrays"]} -->

## 元数据

- 检查项 ID：`CSTD-11.1-02`
- 父规则 ID：`CSTD-11.1`
- 原规范章节：`11.1 防止内存操作越界`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`critical`
- 默认结果：`violation`
- 标签：`quality`, `safety`, `memory`, `pointers`, `arrays`

## 审核要求

使用外部输入作为数组索引或内存偏移前，必须验证其取值范围。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原“解决示例”仅把索引改为 `usr_no - 1`，仍未检查 `usr_no` 是否处于 1～10；输入为 0 或大于 10 时仍可能越界。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.2-01] 禁止访问已经释放的内存空间

<!-- KB_METADATA {"check_id":"CSTD-11.2-01","rule_id":"CSTD-11.2","section":"11.2","category":"质量保证","normative_level":"MUST","policy_status":"active","risk":"critical","review_mode":"hybrid","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety","memory","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-11.2-01`
- 父规则 ID：`CSTD-11.2`
- 原规范章节：`11.2 禁止访问已经释放的内存空间`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`critical`
- 默认结果：`violation`
- 标签：`quality`, `safety`, `memory`, `pointers`

## 审核要求

禁止访问已经释放的内存空间。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.3-01] 动态分配的内存已不再使用时应被及时释放

<!-- KB_METADATA {"check_id":"CSTD-11.3-01","rule_id":"CSTD-11.3","section":"11.3","category":"质量保证","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety","memory","pointers"]} -->

## 元数据

- 检查项 ID：`CSTD-11.3-01`
- 父规则 ID：`CSTD-11.3`
- 原规范章节：`11.3 动态分配的内存已不再使用时应被及时释放`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`quality`, `safety`, `memory`, `pointers`

## 审核要求

在指向动态分配的内存的最后一个指针的生命到期之前，需要对其使用free()释放。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.3`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.4-01] 模块的设置和配置更改权限

<!-- KB_METADATA {"check_id":"CSTD-11.4-01","rule_id":"CSTD-11.4","section":"11.4","category":"质量保证","normative_level":"MUST","policy_status":"active","risk":"medium","review_mode":"manual","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.4-01`
- 父规则 ID：`CSTD-11.4`
- 原规范章节：`11.4 模块的设置和配置更改权限`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`quality`, `safety`

## 审核要求

严禁更改其它模块或系统的有关设置和配置，应通过模块负责人进行修改。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.4`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.5-01] 选择语句的分支语句

<!-- KB_METADATA {"check_id":"CSTD-11.5-01","rule_id":"CSTD-11.5","section":"11.5","category":"质量保证","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.5-01`
- 父规则 ID：`CSTD-11.5`
- 原规范章节：`11.5 选择语句的分支语句`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

if… else if结构必须以else子句结束。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 本条要求所有非空 `case` 以 `break` 结束，与 CSTD-4.13 允许带明确注释的有意 fallthrough 相冲突。
- 项目应明确是全面禁止 fallthrough，还是允许使用标准属性/明确注释的受控 fallthrough；统一前不自动执行本条。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.5-02] 选择语句的分支语句

<!-- KB_METADATA {"check_id":"CSTD-11.5-02","rule_id":"CSTD-11.5","section":"11.5","category":"质量保证","normative_level":"MUST","policy_status":"source-review-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.5-02`
- 父规则 ID：`CSTD-11.5`
- 原规范章节：`11.5 选择语句的分支语句`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需修订原规范
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

switch语句必须有default分支,并且所有非空的switch 子句都应该用break 语句结束。

## 判定规则

- 原规范存在冲突或技术问题；修订并确认前不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 本条要求所有非空 `case` 以 `break` 结束，与 CSTD-4.13 允许带明确注释的有意 fallthrough 相冲突。
- 项目应明确是全面禁止 fallthrough，还是允许使用标准属性/明确注释的受控 fallthrough；统一前不自动执行本条。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.5`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.6-01] 禁止使用goto语句

<!-- KB_METADATA {"check_id":"CSTD-11.6-01","rule_id":"CSTD-11.6","section":"11.6","category":"质量保证","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.6-01`
- 父规则 ID：`CSTD-11.6`
- 原规范章节：`11.6 禁止使用goto语句`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

goto语句会破坏程序的结构性，禁止使用goto语句。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 全面禁止 `goto` 属于项目政策；某些 C 资源清理路径可受控使用，但必须服从本项目最终决定。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.6`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.7-01] 汇编语句使用

<!-- KB_METADATA {"check_id":"CSTD-11.7-01","rule_id":"CSTD-11.7","section":"11.7","category":"质量保证","normative_level":"SHOULD","policy_status":"active","risk":"low","review_mode":"manual","evidence_scope":"expression/function/module","default_result":"advisory","target_languages":["C","C++"],"tags":["quality","safety","macros","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-11.7-01`
- 父规则 ID：`CSTD-11.7`
- 原规范章节：`11.7 汇编语句使用`
- 分类：质量保证
- 规范强度：`SHOULD`
- 规则状态：有效
- 风险等级：`low`
- 默认结果：`advisory`
- 标签：`quality`, `safety`, `macros`, `functions`

## 审核要求

使用汇编语言，应将汇编语言封装并隔离，可以通过汇编函数、C函数、宏实现。

## 判定规则

- 作为改进建议报告，默认不阻断合入。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 该条主要依赖语义、设计或项目背景，应由人工复核。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.7`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.8-01] 有符号数位操作

<!-- KB_METADATA {"check_id":"CSTD-11.8-01","rule_id":"CSTD-11.8","section":"11.8","category":"质量保证","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.8-01`
- 父规则 ID：`CSTD-11.8`
- 原规范章节：`11.8 有符号数位操作`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`high`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

禁止对有符号数进行位操作，主要的位操作符有&、|、~、<<、>>、^。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 有符号位运算应针对负数、移位宽度、溢出和实现定义行为精确检查；全面禁用是保守项目政策。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.8`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.9-01] 判断条件中的赋值语句

<!-- KB_METADATA {"check_id":"CSTD-11.9-01","rule_id":"CSTD-11.9","section":"11.9","category":"质量保证","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"violation","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.9-01`
- 父规则 ID：`CSTD-11.9`
- 原规范章节：`11.9 判断条件中的赋值语句`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`quality`, `safety`

## 审核要求

禁止在 `if`、`while` 等判断条件中执行赋值。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.9`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.10-01] 判断条件

<!-- KB_METADATA {"check_id":"CSTD-11.10-01","rule_id":"CSTD-11.10","section":"11.10","category":"质量保证","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.10-01`
- 父规则 ID：`CSTD-11.10`
- 原规范章节：`11.10 判断条件`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

非布尔操作数作为判断条件时，应显式与 0 或目标值比较。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 非布尔值显式与 0 比较属于风格政策；布尔表达式无需冗余比较。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.10`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-11.11-01] Continue语句

<!-- KB_METADATA {"check_id":"CSTD-11.11-01","rule_id":"CSTD-11.11","section":"11.11","category":"质量保证","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"expression/function/module","default_result":"needs_review","target_languages":["C","C++"],"tags":["quality","safety"]} -->

## 元数据

- 检查项 ID：`CSTD-11.11-01`
- 父规则 ID：`CSTD-11.11`
- 原规范章节：`11.11 Continue语句`
- 分类：质量保证
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`quality`, `safety`

## 审核要求

禁止使用Continue语句。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`expression/function/module`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 全面禁止 `continue` 属于控制流风格政策，不是语言正确性要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-11.11`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.1-01] 函数宏

<!-- KB_METADATA {"check_id":"CSTD-12.1-01","rule_id":"CSTD-12.1","section":"12.1","category":"宏","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-12.1-01`
- 父规则 ID：`CSTD-12.1`
- 原规范章节：`12.1 函数宏`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`, `functions`

## 审核要求

函数式宏的每个参数引用都应使用小括号包围，作为 `#` 或 `##` 操作数的情况除外。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原 `abs(x)` 宏会多次求值 `x`，传入带副作用的表达式会出错，且名称可能与标准库 `abs` 冲突；只能用于说明括号规则，不能作为推荐实现。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.1-02] 函数宏

<!-- KB_METADATA {"check_id":"CSTD-12.1-02","rule_id":"CSTD-12.1","section":"12.1","category":"宏","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-12.1-02`
- 父规则 ID：`CSTD-12.1`
- 原规范章节：`12.1 函数宏`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`, `functions`

## 审核要求

函数式宏的整体表达式应使用小括号或安全的 `do { ... } while (0)` 结构保护。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原 `abs(x)` 宏会多次求值 `x`，传入带副作用的表达式会出错，且名称可能与标准库 `abs` 冲突；只能用于说明括号规则，不能作为推荐实现。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.2-01] 宏参数

<!-- KB_METADATA {"check_id":"CSTD-12.2-01","rule_id":"CSTD-12.2","section":"12.2","category":"宏","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-12.2-01`
- 父规则 ID：`CSTD-12.2`
- 原规范章节：`12.2 宏参数`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`, `functions`

## 审核要求

调用宏时，实参不得包含自增、自减等会在重复求值时产生额外副作用的变化。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.2-02] 宏参数

<!-- KB_METADATA {"check_id":"CSTD-12.2-02","rule_id":"CSTD-12.2","section":"12.2","category":"宏","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-12.2-02`
- 父规则 ID：`CSTD-12.2`
- 原规范章节：`12.2 宏参数`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`, `functions`

## 审核要求

函数式宏的实参不得包含预处理指令。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.2`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.3-01] 宏内容

<!-- KB_METADATA {"check_id":"CSTD-12.3-01","rule_id":"CSTD-12.3","section":"12.3","category":"宏","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor"]} -->

## 元数据

- 检查项 ID：`CSTD-12.3-01`
- 父规则 ID：`CSTD-12.3`
- 原规范章节：`12.3 宏内容`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`

## 审核要求

C的宏只能扩展为用大括号括起来的初始化、常量、小括号括起来的表达式、类型限定符、存储类标识符或do-while-zero 结构。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原示例中的 `#define I NIT(value)` 疑似排版破损。
- 多语句宏应使用 `do { ... } while (0)` 并评估参数副作用；原示例不可直接复制。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-12.3-02] 宏内容

<!-- KB_METADATA {"check_id":"CSTD-12.3-02","rule_id":"CSTD-12.3","section":"12.3","category":"宏","normative_level":"MUST","policy_status":"active-example-warning","risk":"high","review_mode":"automatic-or-hybrid","evidence_scope":"macro/file","default_result":"violation","target_languages":["C","C++"],"tags":["macros","preprocessor"]} -->

## 元数据

- 检查项 ID：`CSTD-12.3-02`
- 父规则 ID：`CSTD-12.3`
- 原规范章节：`12.3 宏内容`
- 分类：宏
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`macros`, `preprocessor`

## 审核要求

禁止使用符号连接##生成通用字符名称，否则会导致未定义行为。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`macro/file`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。

## 最佳实践与质量提示

- 原示例中的 `#define I NIT(value)` 疑似排版破损。
- 多语句宏应使用 `do { ... } while (0)` 并评估参数副作用；原示例不可直接复制。

## 追溯信息

- 本检查项来自父规则 `CSTD-12.3`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-13.1-01] 头文件内容

<!-- KB_METADATA {"check_id":"CSTD-13.1-01","rule_id":"CSTD-13.1","section":"13.1","category":"头文件","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","default_result":"needs_review","target_languages":["C","C++"],"tags":["headers","dependencies","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-13.1-01`
- 父规则 ID：`CSTD-13.1`
- 原规范章节：`13.1 头文件内容`
- 分类：头文件
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`headers`, `dependencies`, `functions`

## 审核要求

一般每一个.c文件应对应一个.h文件，用于声明需要对外公开的接口（变量、函数），XXX_PBCfg.c除外。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 一个 `.c` 文件对应一个 `.h` 文件属于项目组织约定；禁止在头文件中定义可产生多重定义的对象是核心要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-13.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-13.1-02] 头文件内容

<!-- KB_METADATA {"check_id":"CSTD-13.1-02","rule_id":"CSTD-13.1","section":"13.1","category":"头文件","normative_level":"MUST","policy_status":"project-confirmation-required","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","default_result":"needs_review","target_languages":["C","C++"],"tags":["headers","dependencies","functions"]} -->

## 元数据

- 检查项 ID：`CSTD-13.1-02`
- 父规则 ID：`CSTD-13.1`
- 原规范章节：`13.1 头文件内容`
- 分类：头文件
- 规范强度：`MUST`
- 规则状态：需项目确认
- 风险等级：`medium`
- 默认结果：`needs_review`
- 标签：`headers`, `dependencies`, `functions`

## 审核要求

禁止在头文件中定义变量。

## 判定规则

- 该条属于项目、平台或语言版本政策；项目未明确启用时不得自动判违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 一个 `.c` 文件对应一个 `.h` 文件属于项目组织约定；禁止在头文件中定义可产生多重定义的对象是核心要求。

## 追溯信息

- 本检查项来自父规则 `CSTD-13.1`，该父规则共拆分为 2 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-13.2-01] 头文件要求

<!-- KB_METADATA {"check_id":"CSTD-13.2-01","rule_id":"CSTD-13.2","section":"13.2","category":"头文件","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","default_result":"violation","target_languages":["C","C++"],"tags":["headers","dependencies","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-13.2-01`
- 父规则 ID：`CSTD-13.2`
- 原规范章节：`13.2 头文件要求`
- 分类：头文件
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`headers`, `dependencies`, `loops`

## 审核要求

禁止头文件循环依赖。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 完整 include guard 应包含匹配的 `#ifndef`、`#define`、`#endif`；原文只写“#define 保护符”不够完整。

## 追溯信息

- 本检查项来自父规则 `CSTD-13.2`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-13.2-02] 头文件要求

<!-- KB_METADATA {"check_id":"CSTD-13.2-02","rule_id":"CSTD-13.2","section":"13.2","category":"头文件","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","default_result":"violation","target_languages":["C","C++"],"tags":["headers","dependencies","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-13.2-02`
- 父规则 ID：`CSTD-13.2`
- 原规范章节：`13.2 头文件要求`
- 分类：头文件
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`headers`, `dependencies`, `loops`

## 审核要求

.c/.h中禁止包含无用的头文件。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 完整 include guard 应包含匹配的 `#ifndef`、`#define`、`#endif`；原文只写“#define 保护符”不够完整。

## 追溯信息

- 本检查项来自父规则 `CSTD-13.2`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-13.2-03] 头文件要求

<!-- KB_METADATA {"check_id":"CSTD-13.2-03","rule_id":"CSTD-13.2","section":"13.2","category":"头文件","normative_level":"MUST","policy_status":"active-example-warning","risk":"medium","review_mode":"automatic-or-hybrid","evidence_scope":"file/project","default_result":"violation","target_languages":["C","C++"],"tags":["headers","dependencies","loops"]} -->

## 元数据

- 检查项 ID：`CSTD-13.2-03`
- 父规则 ID：`CSTD-13.2`
- 原规范章节：`13.2 头文件要求`
- 分类：头文件
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`medium`
- 默认结果：`violation`
- 标签：`headers`, `dependencies`, `loops`

## 审核要求

头文件应有#define保护符。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`file/project`。
- 优先使用词法、语法树、符号表、数据流或静态分析结果定位证据。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 完整 include guard 应包含匹配的 `#ifndef`、`#define`、`#endif`；原文只写“#define 保护符”不够完整。

## 追溯信息

- 本检查项来自父规则 `CSTD-13.2`，该父规则共拆分为 3 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-14.1-01] 禁止销毁正在使用的互斥锁

<!-- KB_METADATA {"check_id":"CSTD-14.1-01","rule_id":"CSTD-14.1","section":"14.1","category":"并发执行","normative_level":"MUST","policy_status":"active","risk":"high","review_mode":"hybrid","evidence_scope":"module/runtime","default_result":"violation","target_languages":["C","C++"],"tags":["concurrency","thread-safety"]} -->

## 元数据

- 检查项 ID：`CSTD-14.1-01`
- 父规则 ID：`CSTD-14.1`
- 原规范章节：`14.1 禁止销毁正在使用的互斥锁`
- 分类：并发执行
- 规范强度：`MUST`
- 规则状态：有效
- 风险等级：`high`
- 默认结果：`violation`
- 标签：`concurrency`, `thread-safety`

## 审核要求

禁止销毁仍处于使用状态或仍可能被并发访问的互斥锁。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`module/runtime`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 追溯信息

- 本检查项来自父规则 `CSTD-14.1`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

KBBOUNDARYCSTDV1

# [CSTD-14.2-01] 多线程访问位域应防止数据竞争

<!-- KB_METADATA {"check_id":"CSTD-14.2-01","rule_id":"CSTD-14.2","section":"14.2","category":"并发执行","normative_level":"MUST","policy_status":"active-example-warning","risk":"critical","review_mode":"hybrid","evidence_scope":"module/runtime","default_result":"violation","target_languages":["C","C++"],"tags":["concurrency","thread-safety","bit-fields"]} -->

## 元数据

- 检查项 ID：`CSTD-14.2-01`
- 父规则 ID：`CSTD-14.2`
- 原规范章节：`14.2 多线程访问位域应防止数据竞争`
- 分类：并发执行
- 规范强度：`MUST`
- 规则状态：有效，但示例有缺陷
- 风险等级：`critical`
- 默认结果：`violation`
- 标签：`concurrency`, `thread-safety`, `bit-fields`

## 审核要求

多线程访问同一位域或共享同一存储单元的相邻位域时，必须使用同步或存储隔离措施防止数据竞争。

## 判定规则

- 规则适用且存在明确、最小化代码证据时，可判定为违规。
- 必须指出文件、行号和最小代码证据，并说明证据如何违反本检查项。
- 证据不足、规则不适用或需要项目配置时，输出 `needs_review` 或 `not_applicable`，不得猜测。
- 不得仅凭代码与示例写法不同而判违规。

## 取证建议

- 证据范围：`module/runtime`。
- 可先自动发现候选问题，再结合上下文进行人工复核。
- 仅靠局部源码不足以确认时，应结合运行时行为、并发模型或性能测量。
- 涉及跨文件、模块或项目一致性时，不得仅凭单个代码片段下结论。

## 最佳实践与质量提示

- 原示例存在结构体名称不一致、缺少分号等编译问题；只应采用“共享位域访问必须同步”的规则意图。

## 追溯信息

- 本检查项来自父规则 `CSTD-14.2`，该父规则共拆分为 1 个原子检查项。
- 本知识块是独立审核单元；需要完整原文和示例时，应查阅“最佳实践完整版”中的同名父规则。

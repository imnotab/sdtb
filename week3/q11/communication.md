## Issue
**环境**：Linux(Ubuntu) Python3
**复现命令**：`sdt-greet --name " "`
**实际结果**：输出 `Hello,    !`，进程退出码 0
**期望结果**：检测全空白name，以退出码2终止，不输出问候
**其他信息**：待确认Windows平台是否存在相同行为

## Git 提交信息
fix: reject blank‑only name argument

Detect input name that consists purely of whitespace.
Exit with code 2 instead of producing empty greeting output.


## 评审意见
> Blocking
行为：传入全空白字符串时工具仍然生成空问候并返回0。
风险：调用方无法区分合法空问候与错误输入。
建议：增加空白校验，遇到仅空白输入以状态码2退出。


- 提示：--name传入全空白字符，应当SystemExit(2)退出，只修改cli.py，pytest验证。
- AI改动：增加isspace()空白判断，使用parser.error触发退出码2。
- 人工验证：普通名字正常输出；全空白输入返回码2，全部pytest用例通过。


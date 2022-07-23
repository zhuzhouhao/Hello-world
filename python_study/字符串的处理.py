#字符串操作
str = "hello world"
print(str.upper())
print(str.split(" "))
print(str.center(20,"="))
print(str.strip("hdel"))
print(",".join(str))

#字符串格式化
print("{}:hello!today is 2022-6-30".format("zhuzhouhao"))
print("{0:=^20}".format(str.upper()))
'''

:后面有六个格式控制
前三个：<填充（即你想把剩余的宽度添加什么字符）><对齐(<为作左对齐，>为右对齐，^为居中对齐)><宽度>
后三个：<数字千位分隔符(使用,表示)><.精度><类型>
类型的控制：
b 二进制
c 字符形式
d 十进制整数
o 八进制
x 十六进制
X 大写的十六进制表示
e 用科学计数法e表示浮点数
E 用科学计数法E表示浮点数
f 以非科学计数法表示浮点数
% 以百分数表示

'''

'''
异常处理：
try 和 except
格式：
try:
    语句块1
except 异常类型:
    语句块2
else:
    语句块3
finally:
    语句块4

说明：
1.finally对应的无论如何一定会执行
2.else对应的在不发生异常时会执行

'''

try:
    num = eval(input("请输入一个整数："))
    print(num ** 2)
except:
    print("输入的不是整数")

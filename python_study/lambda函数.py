'''
lambda函数返回函数名作为结果
lambda函数是匿名函数，即没有名字的函数
使用lambda保留字定义，函数名是返回结果
<函数名> = lambda<参数>:<表达式>
谨慎使用lambda函数
'''
#lambda 函数定义
f= lambda x,y : x+y
p = f(10,15)
print(p)
print(lambda x,y:x + y)

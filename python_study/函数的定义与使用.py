'''
def 函数名(<非可选参数><可选参数>)
    <函数体>
    return <返回值>

def 函数名(<非可选参数><可变参数*b>)
    <函数体>
    return <返回值>

return 可以返回多个值,用,分隔，返回的是一个元组
全局变量用global表示
规则1：局部变量和全局变量是不同变量，结束后，局部变量会被释放，全局变量和局部变量即使名字相同，都是不同变量
规则2：局部变量如果是组合数据类型或未创建，等同于全局变量
'''

#计算n！
def func(n):
    sum = 1
    for i in range(1,n+1):
        sum = i * sum
    return sum,n
print(func(10))

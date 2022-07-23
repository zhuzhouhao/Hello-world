'''
集合类型由不可变的元素组成的
集合类型各元素不一样
集合中元素是无序的
用{}表示,用,分隔
建立集合要用{}或set()函数
建立空集合必须用set()函数
集合运算：
S|T    返回一个新集合，返回在S和T中所有元素集合
S-T    返回在S中不在T中的元素集合
S&T    返回同时在S和T中的元素集合
S^T    返回S和T中的不相同元素
S<=T 或 S < T 返回True/False,判断S和T的子集关系
S>=T 或 S>T   返回Ture/False,判断S和T的包含关系

集合的处理方法：
S.add(x)
如果x不在集合S中，将x添加到S中

S.discard(x)
移除S中元素x,如果x不在集合S中，不报错

S.remove(x)
移除S中元素x,如果x不在集合S中，报KeyError的异常

S.clear()
移除S中所有元素

S.pop()
随机返回S的一个元素，更新S,若S为空产生KeyError异常

S.copy()
返回S的一个副本

len(S)
返回集合S的元素个数

x in S
判断S中元素x是否在S中

set(x)
将其他类型的变量x转化为集合类型
'''
a = {'p',4,'y'}
b = set("pypy123")
a |= b
print(a)

for i in a:
    print(i,end='')
print('')
try:
    while True:
        print(a.pop(),end = '')
except:
    print('Error')
l = ['r','e','r','r','t','r',]
ls = set(l)
print('')
print(ls)

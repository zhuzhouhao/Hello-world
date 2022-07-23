'''
计算机产生的是伪随机数
函数：
基本随机数函数：seed(),random()
扩展随机数函数：randint(),getrandbits(),uniform(),randrange(),choice(),shuffle()

seed()
初始化给定随机数种子，默认是当前系统的时间

random()产生随机数，范围0到1

randint(a,b)
生成a到b的整数

getrandbits(k)
生成一个k比特长的随机整数

uniform(a,b)
生成a到b的随机小数，精度16为

randrange(m,n[,k])
生成一个[m,n)之间的以k为步长的随机整数

choice(seq)
从序列seq中随机选择一个元素

shuffle(seq)
将seq中的元素随机排列，并返回打乱后的序列

'''
import random
random.seed()
print(random.random())
print(random.randint(1,10))
print(random.randrange(10,100,10))
seq = [1,2,3,4,5,6,7,8,9]
random.shuffle(seq)
print(seq)

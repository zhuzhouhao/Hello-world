'''



'''

#换行的
import time
print('------执行开始------')
scale = 10
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print('{:^3.0f}%[{}->{}]'.format(c,a,b))
    time.sleep(0.1)
print('------执行结束------')

#单行动态刷新
for j in range(101):
    print('\r{:3}%'.format(j),end=" ")
    time.sleep(0.1) 

#完整执行
scale = 50
print('执行开始'.center(scale//2,'-'))
start = time.perf_counter()
for k in range(scale+1):
    a = '*' * k
    b = '.' * (scale - k)
    c = (k/scale) * 100
    dur = time.perf_counter() - start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,'-'))

'''

'''
#计算阶乘
def fact(n):
    result = 1
    if(n == 1):
        return 1
    else:
        return n * fact(n - 1)
print(fact(3))

#将字符串反转
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]
string = 'hello world'
print(string[::-1])
print(rvs(string))

#汉诺塔问题
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","B","C")
print(count)

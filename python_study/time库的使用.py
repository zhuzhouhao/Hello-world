'''
time库包含三类函数
时间获取：time(),ctime(),gmtime()
时间格式化：strftime(),strptime()
程序计时：sleep(),perf_counter()

时间获取
time()获取系统的时间戳,返回一个浮点数，为1970.1.1到现在的秒数
ctime()返回一个字符串，以易读的方式来表示
gmtime()获得一个可以让系统比较容易处理的时间格式
localtime()将时间戳转化为系统易读的时间格式

时间格式化
strftime(tpl,ts)
tpl  是格式化模板字符串，用来定义输出效果
ts   是计算机内部时间类型变量
%Y 表示年份,为0000到9999
%m 表示月份,是01到12的数字
%B 表示月份名称，是January到December
%b 表示月份名称的缩写，如Apr
%d 表示日期，01到31
%A 表示星期，为Monday到Sunday
%a 表示星期的缩写
%H 小时（24小时制）00到23
%I 小时（12小时制）01到12
%p 上下午 AM和PM
%M 分钟 00到59
%S 秒 00到59
strptime(str,tpl)
str 是字符串形式的时间值
tpl 是格式化模板字符串，用来定义输入效果
即strftime()是将时间变量表示为字符串，strptime()是将字符串变成时间变量,两者相反

程序计时
测量时间：perf_counter()
返回一个CPU级别的精确时间计数值，单位为秒
使用是通常需要有开始和结束
产生时间：sleep()
让程序休眠多少秒
'''

import time
print(time.time())
print(time.ctime())
print(time.gmtime())
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))
timeStr = '2022-6-30 18:04:20'
print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))

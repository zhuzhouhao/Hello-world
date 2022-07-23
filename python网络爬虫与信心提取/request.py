'''
requests.get(url,params = None,**kwargs)
url:拟获取页面的url链接
params:url中的额外参数，字典或字节流格式，可选
**kwargs:12个控制访问的参数

r.status_code
状态码，200成功，404失败

r.text
HTTP响应内容的字符串形式,即url对应的页面内容

r.encoding
从HTTP header中猜测的响应内容的编码形式

r.apparent_encoding
从内容中分析出的响应内容编码方式

r.content
HTTP响应内容的二进制形式

异常：
requests.ConnectionError
网络连接错误异常,如DNS查询失败，拒绝连接等
requests.HTTPError
HTTP错误异常
requests.URLRequired
URL缺失异常
requests.TooManyRedirects
超过最大重定向次数，产生重定向异常
requests.ConnectionTimeout
连接远程服务器超时异常
requests.Timeout
请求URL超时，产生超时异常

r.raise_for_status()
如果不是200，产生异常requests.HTTPError

requests库其中方法
requests.request(method,url,**kwargs)
method:请求方式，对应get/put/post等7种
url:拟获取的页面url链接
**kwargs:控制访问参数，共13个

method共7种
get:
head:
post:
put:
patch:
delete:
options:向服务器获取一些服务器和客户端能够打交道的参数

**kwargs:13个参数

params:字典或字节序列，作为参数增加到url中
实例：
kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params = kv)
print(r.url)
结果：
http://python123.io/ws?key1=value1&key2=value2

data:字典、字节序列或文件对象，作为request的内容
实例：
kv = {'key1':'value1','key2':'value2'}
r = requests.request('POST','http://python123.io/ws',data = kv)
body = '主体内容'
r = requests.request('POST','http://python123.io/ws',data = body)

json:JSON格式的数据，作为request的数据
实例：
kv = {'key1':'value1','key2':'value2'}
r = requests.request('POST','http://python123.io/ws',json = kv)

headers:字典，HTTP定制头，可以模拟浏览器来访问
实例：
hd = {'user-agent':'Chrome/10'}
r = requests.request('POST','http://python123.io/ws',headers = hd)

cookies:字典或CookieJar，request中的cookie

auth:元组，支持HTTP认证

files:字典类型，传输文件，可以向某一个链接提交文件
实例：
fs = {'file':open('data.xls','rb')}
r = requests.request('POST','http://python123.io/ws',files = fs)

timeout:设定超时时间，秒为单位
实例：
r = requests.request('GET','http://www.baidu.com',timeout = 10)

proxies:字典类型，设定访问代理服务器，可以增加登录认证，可以隐藏IP地址
实例：
pxs = {'http':'http://user:pass@10.10.10.1:1234'   \
        'https':'https://10.10.10.1:4321'}
r = requests.request('GET','http://www.baidu.com',proxies = pxs)

allow_redirects:True/False,默认为True,重定向开关
stream:True/False,默认为True,获取内容立即下载开关
verify:True/False，默认为True,认证SSL证书开关
cert:本地SSL证书路径


'''
#通用代码框架
import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = r.apparent_encoding
        print(r.encoding)
        return r.text
    except:
        return "产生异常"
#if _name_ == "_main_":
url = "https://www.msms7.club/forum.php"
print(getHTMLText(url))



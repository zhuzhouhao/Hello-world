'''
百度的关键词接口：
http://www.baidu.com/s?wd = keyword
360关键词接口：
http://www.so.com/s?q = keyword

'''
import requests
keyword = 'python'
try:
    kv = {'wd':keyword}
    r = requests.get('http://baidu.com/s',params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')

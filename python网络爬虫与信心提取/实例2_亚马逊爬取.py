import requests
url = 'https://www.amazon.cn/dp/B07MV9V7DL/ref=   \
        sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9    \
        %80%8A%E7%BD%91%E7%AB%99&crid=38FGH9824   \
        5R3B&keywords=%E5%8D%8E%E4%B8%BA%E6%89%8B  \
        %E6%9C%BA&qid=1657090935&sprefix=%E5%8D%8E%  \
        E4%B8%BA%E6%89%8B%E6%9C%BA%2Caps%2C76&sr=8-1'
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')

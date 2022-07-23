import requests
url = 'https://ip38.com/ip.php?ip='
try:
    r = requests.get(url + '36.152.44.95')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')

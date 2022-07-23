'''

'''
import requests
import os
url = 'https://www.jseea.cn/webfile/upload/2022/07-04/11-07-1808741215610799.pdf'
root = 'e:\\python网络爬虫与信心提取'
path = root + '\\招生计划.pdf'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取失败')

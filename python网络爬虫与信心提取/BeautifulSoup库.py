'''
安装：
pip install beautifulsoup4

代码：
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())

from bs4 import BeautifulSoup
soup = BeautifulSoup("<html>data</html>","html.parser")
soup2 = BeautifulSoup(open("d://demo.html"),"html.parser")


BeautifulSoup库的解析器

bs4的HTML解析器    BeautifulSoup(mk,"html.parser")    安装bs4库
lxml的HTML解析器   BeautifulSoup(mk,"lxml")           pip install lxml
lxml的XML解析器    BeautifulSoup(mk,"xml")            pip install lxml
html5lib的解析器   BeautifulSoup(mk,"html5lib")       pip install html5lib


基本元素:
Tag:标签，最基本的信息组织单元用<></>表明
Name:标签的名字，用<tag>.name获得
Attributes:标签的属性,字典形式组织，格式为:<tag>.attrs
NavigableString:标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment:标签内字符串的注释部分，一种特殊的Comment类型


对节点的遍历

上行遍历
.parent
父节点
.parents
节点先辈标签

平行遍历
.next_sibling
返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling
返回按照HTML文本顺序的上一个平行节点标签
.next_siblings
迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings
迭代类型，返回按照HTML文本顺序的前续所有平行节点标签

下行遍历
.contents
返回列表类型
.children
返回迭代类型
.descendants
返回迭代类型


基于bs4库的HTML格式化和编码
print(soup.prettify())
'''

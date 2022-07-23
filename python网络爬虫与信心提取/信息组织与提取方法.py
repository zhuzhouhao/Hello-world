'''
信息标记的三种方式
HTML(hyper text markup language)
JSON(JavaScript Object Notation)用键值对表示，可以嵌套使用
JAML(YAML Ain't Markup Language)用无类型的键值对表示，用缩进表示所属关系，用-表达并列关系，用|表达整块数据，用#表示注释
如：
name:
    newname:北京理工大学
    oldname:延安自然科学院

name:
-北京理工大学
-延安自然科学院

text: | #学校简介
北京理工大学创立于1940年，前身是延安自然科学院，是中国共产党创办的第一所理工科大学，毛泽东同志亲自题写校名，李富春、徐特立、李强等老一辈无产阶级革命家先后担任学校的主要领导。

信息提取的一般方法
方法一：完整解析信息的标记形式，再提取关键信息，需要标记解析器
方法二：无视任何信息标记形式，直接搜索关键信息
融合方法：结合形式解析与搜索方法

基于bs4库的HTML查找方法：
<>.find_all(name,attrs,recursive,string,**kwargs)
返回一个列表类型，存储查找的结果
name:对标签名称的检索字符串
attrs:对标签属性值的检索字符串，可标注属性检索
'''

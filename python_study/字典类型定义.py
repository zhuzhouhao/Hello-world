'''
字典类型是映射的体现
字典是键值对的集合
字典用{}或dict()来创建字典，键值对用:表示，可以通过[]来获得值
可以用{}来生成一个字典类型
注意，集合类型不能使用{}来生成一个空的集合，因为{}是用来生成字典的
函数或方法：
del d[k]
删除字典d中键k对应的数据值
k in d
判断k是否在d中
d.keys()
返回字典d中所有的键信息
d.values()
返回字典d中所有的值信息
d.items()
返回字典d中所有的键值对信息
d.get(k,<default>)
若k存在，则返回对应的值，若k不存在，则返回<default>的值
d.pop(k,<default>)
若k存在，则取出对应的值，若k不存在，则返回<default>的值
d.popitem()
随机从字典中取出一个键值对，以元组的形式返回
d.clear()
删除所有的键值对
len(d)
返回字典d中元素的个数
'''
d = {"中国":"北京","美国":"华盛顿","英国":"伦敦"}
print(d.keys())
print(d.values())
print(d.items())
print("中国" in d)
print(d["美国"])
print(d.get("中国","不存在！"))
print(d.pop("美国","enenn "))
print(d.keys())
print(d.popitem())

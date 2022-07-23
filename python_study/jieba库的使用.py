'''
jieba库是中文分词的第三方库
更新：
D:\python\python.exe -m pip install --upgrade pip
三种模式：
精确模式：把文本精确地切分开，不存在冗余单词
全模式：把文本中所有可能的词语都扫描出来，有冗余
搜索引擎模式：在精确模式的基础上，对长词再次切分
函数：
jieba.lcut(s)
精确模式，返回一个列表类型的分词结果
jieba.lcut(s,cut_all = True)
全模式，返回一个列表类型的分词结果，存在冗余
jeiba.lcut_for_search(s)
搜索引擎模式，返回一个列表类型的分词结果，也有冗余
jieba.add_word(w)
将新词添加到词库中
'''
import jieba
s = "中国是一个伟大的国家,他物产丰富，地域辽阔"
print(jieba.lcut(s))
print(jieba.lcut(s,cut_all = True))

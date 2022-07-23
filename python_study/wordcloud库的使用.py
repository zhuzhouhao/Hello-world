'''
更新：
D:\python\python.exe -m pip install --upgrade pip
步骤：
1.生成一个词云对象，c = wordcloud.WordCloud()
2.给对象一个字符串，c.generate("hello world")
3.把生成的词云输出到图片中c.to_file("out.jpg")

配置对象参数
width
height
指定高度宽度
min_font_size
max_font_size
指定最小最大的字号
font_step
指定词云字体字号的步进间隔，默认为1
font_path
指定字体文件的路径，默认为None
max_words
指定最大的词云显示词语数量
stop_words
指定词云中排除词列表，即不显示的单词
w = wordcloud.WordCloud(stop.words = {"python"})
mask
指定词云的形状，默认为长方形，需要引用imread()函数
from scipy.misc import imread
mk = imread("pic.png")
w = wordcloud.WordCloud(mask = mk)
background_color
指定背景颜色，默认为黑色
'''
'''
import wordcloud
c = wordcloud.WordCloud()

c.to_file("out.jpg")
'''
#中文词云
import jieba,wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，\
它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理"
w = wordcloud.WordCloud(width = 1000,height = 700,font_path = "msyh.ttc")
k = " ".join(jieba.lcut(txt))
print(k)
w.generate(k)
w.to_file("pywcloud.png")

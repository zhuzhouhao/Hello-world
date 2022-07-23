'''

'''
#hamlet
def getText():#降噪，去除特殊字符，并将大写全改为小写
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!@#$%^&*()_+-=[]{}|\:;"<,>.?/':
        txt = txt.replace(ch," ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

#三国演义
import jieba
txt = open("三国演义.txt","r",encoding = "utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","左右","军士","军马","引兵","次日","大喜","天下"\
            ,"东吴","于是","今日","不敢"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if(len(word) == 1):
        continue
    elif(word == "诸葛亮" or word == "孔明曰"):
        rword = "孔明"
    elif(word == "云长" or word  == "关公"):
        rword = "关羽"
    elif(word == "玄德" or word == "玄德曰"):
        rword = "刘备"
    elif(word == "孟德" or word == "丞相"):
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) +1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

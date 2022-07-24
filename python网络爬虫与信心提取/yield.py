'''
生成器比一次列出更具有优势
    更节省存储空间
    响应更快
    使用更灵活
'''
def gen(n):
    for i in range(n):
        yield i**2
for i in gen(5):
    print(i,"",end = "")
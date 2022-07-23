'''

'''
import os
libs = {}
try:
    for lib in libs:
        os.system("pip install " + lib)
        os.system("color 3")
    print("successful")
    os.system("color 7")
except:
    os.system("color 3")
    print("failed somehow")
    os.system("color 7")

'''

'''

p = "hello"
print(','.join(p))
for i in p:
    print(i,end = ',')
print('')
for c in "PYTHON":
    if c == 'T':
        continue
    print(c,end = ',')

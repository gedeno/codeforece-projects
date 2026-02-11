v = '1+2+6+4+7+5'
x = list(map(str, v))
x.sort()
for i in x:
    if i == '+':
        x.remove('+')
print(x)


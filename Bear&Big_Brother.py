v = list(map(int, input().split()))
a = v[0]
b = v[1]
c = 0
while True:
    a = a*3
    b = b*2
    c += 1
    if a > b:
        break
print(c)
shose = list(map(int, input().split()))
b = 0
for i in shose:
    if b > 0:
        b = b + 1
    else:
        pass
    a = shose.count(i)
    if a > b:
        b = a
print(b-1)
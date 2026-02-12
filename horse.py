shose = list(map(int, input().split()))
b = 0
shose.sort()
for i in shose:
    a = shose.count(i)
    if shose[0]==shose[1] and shose[2]==shose[3] and shose[1]!=shose[2]:
        b+=3
        break
    elif a > b:
        b = a
print(b-1)
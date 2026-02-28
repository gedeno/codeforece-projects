day = int(input())
price = list(map(int, input().split()))
n = price[0]
a = 0
le = 0
for i in price:
    if a >= le:
        le = a
    if i>=n:
        n = i
        a += 1
        if a >= le:
            le = a
    elif i < n:
        n = i
        a = 1
print(le)
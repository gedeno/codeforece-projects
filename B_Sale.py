a , b = list(map(int,input().split()))
price = list(map(int,input().split()))
d = []
for i in range(a):
    if price[i] <= 0:
        d.append(price[i])
d.sort()
f = b
g = abs(sum(d[0:f]))
print(g)
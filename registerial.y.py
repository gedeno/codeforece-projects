sums = list(map(int, input().split()))
b = []
x = max(sums)
for i in sums:
    if i == x:
        pass
    else:
        a = x - i
        b.append(a)
b.reverse()
for j in b:
    print(j,end=' ')





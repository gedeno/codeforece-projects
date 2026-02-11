qustion = int(input())
y = 0
for i in range(qustion):
    x = list(map(int,input().split()))
    x.sort()
    if x == [0,1,1] or x == [1,1,1]:
        y += 1
    else:
        pass
print(y)
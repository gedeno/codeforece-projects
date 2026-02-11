n = int(input())
m = 60
all = []
for i in range(n):
    h = list(map(int, input().split()))
    h1 = h[0]*m + h[1]
    h2 = 24*m -h1
    all.append(h2)
for i in all :
    print(i)
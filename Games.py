n = int(input())
a1 = []
b1 = []
e = 0
for i in range(n):
    team = list(map(int,input().split()))
    a = team[0]
    b = team[1]
    a1.append(a)
    b1.append(b)
for i in a1 :
    if i in b1:
        bn = b1.count(i)

        e = bn + e

print(e)



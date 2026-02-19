members = int(input())
cosd = []

for i in range(members):
    asb = list(map(int, input().split()))
    asb.sort()
    b = asb[1] + asb[2]
    if b >= 10:
        cosd.append('YES')
    else:
        cosd.append('NO')
for i in cosd:
    print(i)
n = int(input())
x = 0
y = 0
z = 0
for i in range(n):
    lines = list(map(int, input().split()))
    x += lines[0]
    y += lines[1]
    z += lines[2]
if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')
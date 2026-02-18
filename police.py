event = int(input())
ev = list(map(int,input().split()))

while True:
    if ev[-1] > 0:
        ev.pop()
    else:
        break
ev.reverse()
su = 0
for i in ev:

    if su > 0:
        su = 0
    else:
        su += i

if su >= 0:
    print(0)
else:
    print(-su)
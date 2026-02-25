event = int(input())
ev = list(map(int,input().split()))
su = 0
if event > 1:
    while True:
        if len(ev) == 0 or ev[-1] < 0:
            break
        if ev[-1] >= 0:
            ev.pop()
    ev.reverse()
    for i in ev:
        su += i
        if su > 0:
            su = 0
    if su < 0:
        print(-su)
    else:
        print(0)
else:
    if ev[0] >= 0:
        print(0)
    else:
        print(1)
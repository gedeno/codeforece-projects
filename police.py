event = int(input())
evv = list(map(int,input().split()))
while True:
    if evv[-1] > 0:
        evv.pop()
    else:
        break
if sum(evv) >= 0:
    print(0)
else:
    print(-sum(evv))
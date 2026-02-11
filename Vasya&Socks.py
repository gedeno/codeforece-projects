pack = list(map(int,input().split()))
u = pack[0]
mom = pack[1]
day = 0

while u > 0 :
    day += 1
    u -= 1
    if day%mom == 0 :
        u += 1
print(day)


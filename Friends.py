pi = int(input())
codi = []
for i in range(pi):
    info = list(map(int,input().split()))
    aria = info[0]*info[1]
    c = info[2]
    if info[0]%2 == 0 or info[1]%2 == 0 or info[2] == 1:
        Y = 'YES'
        codi.append(Y)
    else:
        Y = 'NO'
        codi.append(Y)
for i in codi :
    print(i)




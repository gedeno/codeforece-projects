a , b = list(map(int,input().split()))
price = list(map(int,input().split()))

if a == 1 :
    print(0)
elif a == 2 :
    print(0)
elif a > 1:
    chl = []
    for i in range(a):
        chl.append(price[i])
    Mx = max(chl)
    My = min(chl)
    print(Mx-My)

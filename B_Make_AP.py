nob = int(input())
for i in range(nob):
    a , b , c = list(map(int, input().split()))
    if (2*b - c)%a ==0 and (2*b - c) >0:
        print('YES')
    elif (c + a)%(2*b) == 0:
        print('YES')
    elif (2*b - a)%c == 0 and (2*b - a) >0:
        print('YES')
    else:
        print('NO')
n = int(input())
ns = list(map(int, input().split()))
m = int(input())
if n > 1:
    for j in range(m):
        a, b = map(int, input().split())
        if a == 1:
            ns[1] += ns[0] - b
            ns[0] = 0
        elif a == n:
            ns[n-2] += ns[n-1] - (ns[a-1] - b) - 1
        else:
            ns[a-2] += ns[a-1] - (ns[a-1] - b) - 1
            ns[a] +=  ns[a-1] - b
        ns[a - 1] = 0
    for i in ns:
        print(i)
else:
    if n == 1 and m != 0:
        a, b = map(int, input().split())
        if a == 1:
            print(0)
        else:
            print(ns[0])
    if m == 0:
        print(ns[0])
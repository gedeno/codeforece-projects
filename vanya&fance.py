N = list(map(int, input().split()))
ns = list(map(int, input().split()))
n = N[0]
h = N[1]
w = 0
for i in ns:
    if i > h:
        w += 2

    elif i < h:
        w +=1

    elif i == h:
        w +=1
print(w)
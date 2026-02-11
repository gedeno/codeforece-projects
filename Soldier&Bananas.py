nob = list(map(int, input().split()))
k = nob[0]
n = nob[1]
w = nob[2]
v = 0

for i in range(w):
    u = (i+1)*k
    v += u
if n < v:
    print(v-n)

else:
    print(0)

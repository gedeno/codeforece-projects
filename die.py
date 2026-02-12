ny = list(map(int,input().split()))
n = [1,2,3,4,5,6]

if ny[0]>ny[1]:
    ot = ny[0]
elif ny[1] >ny[0]:
    ot = ny[1]
o =[]
for i in n:
    if ot <= i:
        o.append(i)
p = len(o)
if p%2 == 0 :
    p = int(p/2)
    print(f"{p}/3")
elif p%3 == 0:
    p = int(p/3)
    print(f"{p}/2")
else:
    print(f"{p}/6")
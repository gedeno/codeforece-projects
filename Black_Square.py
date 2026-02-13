kal_val  = list(map(int,input().split()))
a = kal_val[0]
b = kal_val[1]
c = kal_val[2]
d = kal_val[3]
total = 0
tuch = str(input())
for i in tuch :
    if i == '1' :
        total = total + a
    elif i == '2' :
        total = total + b
    elif i == '3' :
        total = total + c
    elif i == '4' :
        total = total + d
print(total)
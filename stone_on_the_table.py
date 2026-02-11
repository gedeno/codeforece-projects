n = int(input())
color = str(input())
c = 0
for i in range(n-1):
    if color[i] == color[i+1]:
        c +=1
print(c)
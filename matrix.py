row = []
for i in range(5):
    row.append(list(map(int, input().split())))
z = 1
for i in row:
    if sum(i) == 1 :
        break
    z += 1 
cal = row[z-1].index(1) +1
vs = abs(3 - z)+ abs(3 - cal)
print(vs)
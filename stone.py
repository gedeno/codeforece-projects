stone = str(input())
instrunct = str(input())
X = len(stone)
v = 0
for j in instrunct:
    if stone[v] == j :
        v = v + 1
print(v+1)






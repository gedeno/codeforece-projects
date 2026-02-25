a, b = map(int,input().split())

n = 0
while True:
    n += 1
    if n*a%10 == 0 or (a*n - b)%10 == 0:
        break
print(n)
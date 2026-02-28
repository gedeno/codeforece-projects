coins = int(input())
amount = list(map(int,input().split()))
amount.sort()
amount.reverse()
a = 0
b = 0
division = sum(amount)/2
for i in amount:
     if a <= division:
         b = b + 1
         a += i

print(b)

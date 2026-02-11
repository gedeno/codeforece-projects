q = int(input())
x = str(input())
y = x.count('A')
z = x.count('D')
if y == z:
    print('Friendship')
elif y > z:
    print('Anton')
elif y < z:
    print('Danik')
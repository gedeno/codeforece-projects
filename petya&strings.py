a1 = input('enter the first word :')
b1 = input('enter the second word :')
a = a1.upper()
b = b1.upper()
if a < b:
    print(-1)
elif a > b:
    print(1)
elif a == b:
    print(0)

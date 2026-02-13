z = "abcdefghijklmnopqrstuvwxyz"
name = str(input("Enter your name: "))
c = 0
for i in name :
    if i in z :
        c += z.index(i)
print(c)
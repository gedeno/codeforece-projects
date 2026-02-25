s = input()
cur = 'a'
a = 97
z = 122
mv = 0
for i in s:
    if ord(i) > 110 and ord(cur) > 110:
        mv += abs(ord(i) - ord(cur))
    elif ord(i) < 110 and ord(cur) < 110:
        mv += abs(ord(i) - ord(cur))
    else:
        if abs(ord(i) - ord(cur)) < 13:
            mv += abs(ord(i) - ord(cur))
        else:
            mv += 26 - abs(ord(i) - ord(cur))
    cur = i
print(mv)
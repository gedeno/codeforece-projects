x = input()
lens = len(x)
v = []
for i in x:
    if i in v:
        pass
    else:
        v.append(i)
gen = len(v)
gender = gen%2
if gender == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
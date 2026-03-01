acc = str(input())
mx = list(acc)
mx.pop()
mi = acc[:-2] + acc[-1]
valm = int(''.join(mx))
valmi = int(''.join(mi))
ac = int(acc)
if valm > valmi:
    if valm > ac:
        print(valm)
    else:
        print(acc)
elif valm < valmi:
    if valmi > ac:
        print(valmi)
    else:
        print(acc)
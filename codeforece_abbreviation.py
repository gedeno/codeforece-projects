words = int(input('enter the number of words:'))
words_abriv = []
for i in range(words):
    x1 = input('enter :')
    x = list(x1)
    lngth = len(x)
    if lngth >=  10:
        y = x[0]
        z = x[-1]
        w = y+str(lngth)+z
        words_abriv.append(w)
    elif len(x) < 10:
        words_abriv.append(str(x1))
for abvs in words_abriv:
    print(abvs)
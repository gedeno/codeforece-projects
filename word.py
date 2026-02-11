word = str(input())
UP = 0
LO = 0
for i in word:
    if i == i.upper():
        UP += 1
    elif i == i.lower():
        LO += 1

if UP > LO:
    print(word.upper())
elif UP < LO:
    print(word.lower())
elif UP == LO:
    print(word.lower())

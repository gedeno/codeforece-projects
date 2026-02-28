year = int(input())
while True:
    year += 1
    y = set(list(str(year)))
    if len(y) == 4:
        print(year)
        break
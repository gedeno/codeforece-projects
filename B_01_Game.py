tast_case = int(input())
for i in range(tast_case):
    game = str(input())
    a = game.count('1')
    b = game.count('0')
    if a >= b:
        if b%2 != 0:
            print('DA')
        else:
            print('NET')
    elif b >= a :
        if a%2 != 0:
            print('DA')
        else:
            print('NET')


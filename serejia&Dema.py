card = int(input())
cards = list(map(int, input().split()))

sr = 0
di = 0
i = 0
while len(cards) != 0 :
    if i % 2 == 0:
        if cards[0] > cards[-1]:
            sr = sr + cards[0]
            cards.remove(cards[0])
        else:
            sr += cards[-1]
            cards.remove(cards[-1])
    elif i % 2 != 0:
        if cards[0] > cards[-1]:
            di += cards[0]
            cards.remove(cards[0])
        else:
            di += cards[-1]
            cards.remove(cards[-1])
    i = i + 1
print(sr,di)
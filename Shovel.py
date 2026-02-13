shovels = list(map(int,input().split()))
price  = shovels[0]
m = shovels[1]
c = 0
while True :
    c = c + 1
    prs = price%10
    sheff = price*c
    if sheff
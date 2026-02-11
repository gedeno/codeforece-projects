rows = int(input())
col = list(map(int, input().split()))
col.sort()
print(' '.join(map(str,col)))
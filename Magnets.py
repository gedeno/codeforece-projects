no_mag = int(input())
mags = []
a = 1
for i in range(no_mag):
    mag = str(input())
    mags.append(mag)
for mag in range(len(mags)-1):
    if mags[mag] != mags[mag+1]:
        a += 1
print(a)


import sys, math

coord = {}
r = 0

for line in sys.stdin:
    lst = list(map(int,line.split(" ")))
    for i in range(len(lst)):
        coord[lst[i]]=(r,i)
    r += 1

pr,pc = coord[1]
dist = 0
for i in range(2,10):
    dist += math.hypot(pr-coord[i][0],pc-coord[i][1])
    pr,pc = coord[i]

print(dist)
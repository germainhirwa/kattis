import sys

fl = True
cw = []
valid = []

for line in sys.stdin:
    if fl:
        r,c = list(map(int,line.split(" ")))
        fl = False
    else:
        cw.append(list(line.strip()))

cwt = [[cw[i][j] for i in range(r)] for j in range(c)]

for i in range(r):
    valid += ''.join(cw[i]).split('#')
for i in range(c):
    valid += ''.join(cwt[i]).split('#')
valid = list(filter(lambda x: len(x) >= 2, valid))

print(sorted(valid)[0])
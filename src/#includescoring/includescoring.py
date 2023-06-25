from math import ceil
lth = [[*map(int, input().split()), i] for i in range(int(input()))]
pts = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18] + list(range(16, -1, -1))
pts += [0]*(len(lth)-len(pts))
lth.sort(key=lambda x: (-x[0], x[1], x[2]))
for i in range(len(lth)): lth[i].append(i)
f = {}
for a, b, c, x, _, rk in lth:
    if (a, b, c) not in f: f[(a, b, c)] = []
    f[(a, b, c)].append(pts[rk])
for a, b, c in f: f[(a, b, c)] = ceil(sum(f[(a, b, c)])/len(f[(a, b, c)]))
scores = [0]*len(lth)
for a, b, c, x, i, _ in lth: scores[i] = f[(a, b, c)] + x
for i in scores: print(i)
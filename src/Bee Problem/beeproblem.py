import sys
h, n, m = map(int, input().split())
b = []
for l in sys.stdin: b.append([*l.strip('\r\n')])
maxc = max(len(i) for i in b)
for i in b:
    if len(i) != maxc: i.append(' ')
delta = ((1, 1), (1, -1), (-1, 1), (-1, -1), (0, 2), (0, -2))
g, vis = {}, set()
for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] != '.': continue
        g[i*len(b[0])+j] = []
        for di, dj in delta:
            if 0<=i+di<len(b) and 0<=j+dj<len(b[0]):
                if b[i+di][j+dj] == '.': g[i*len(b[0])+j].append((i+di)*len(b[0])+j+dj)
cc = []
for i in g:
    if i not in vis:
        cc.append(0)
        stack = [i]
        while stack:
            u = stack.pop()
            if u in vis: continue
            vis.add(u); cc[-1] += 1
            for w in g[u]: stack.append(w)
idx = 0; cc.sort(reverse=True)
while h > 0: h -= cc[idx]; idx += 1
print(idx)
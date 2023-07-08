import sys

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = int(input())
g = [[] for _ in range(V)]
words = list(map(lambda x: x.strip(), sys.stdin))
for i in range(V):
    for j in range(i+1, V):
        diff = 0
        for k in range(len(words[i])): diff += words[i][k] != words[j][k]
        if diff == 2: g[i].append(j), g[j].append(i)
match, mcbm = [-1]*V, 0
free = {*range(V)}

for l in range(V):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[candidates[0]] = l

for f in free:
    vis = [0]*V
    mcbm += aug(f)

print(V-mcbm//2)
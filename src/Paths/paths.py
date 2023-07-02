import sys
v, e, k = map(int, input().split())
m = 1<<k
col = []
g = [[] for _ in range(v)]
for l in sys.stdin:
    if not col: col = list(map(lambda x: 1<<(int(x)-1), l.split())); continue
    a, b = map(int, l.split())
    a -= 1; b -= 1
    g[a].append(b), g[b].append(a)
mem = [[-1]*m for _ in range(v)]
def f(c, s=0):
    if mem[c][s]+1 : return mem[c][s]
    ans, s2 = 0, s|col[c]
    for c2 in g[c]:
        if s2|col[c2] != s2: ans += f(c2, s2) + 1
    mem[c][s] = ans
    return ans
print(sum(f(i, 0) for i in range(v)))
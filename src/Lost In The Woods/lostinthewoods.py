v, e = map(int, input().split())
g, f = [[] for _ in range(v)], 0
p = [1] + [0]*(v-1)
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b), g[b].append(a)
for t in range(10000):
    p2 = [0]*v
    for i in range(v-1):
        if g[i]:
            x = p[i]/len(g[i])
            for j in g[i]: p2[j] += x 
    p = p2
    f += p[-1]*(t+1)
print(f)
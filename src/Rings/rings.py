import sys; input = sys.stdin.readline
while True:
    n = int(input())
    if n == -1: break
    circs = [[*map(float, input().split())] for _ in range(n)]
    g = [[] for _ in range(n)]
    for i in range(n-1):
        x, y, r = circs[i]
        for j in range(i+1, n):
            x2, y2, r2 = circs[j]
            if abs(r-r2)**2 < (x-x2)**2 + (y-y2)**2 < (r+r2)**2: g[i].append(j), g[j].append(i)
    vis = set()
    ccs = []
    for i in range(n):
        if i not in vis:
            stack, c = [i], 0
            while stack:
                u = stack.pop()
                if u in vis: continue
                vis.add(u); c += 1
                for v in g[u]: stack.append(v)
            ccs.append(c)
    x = max(ccs); print(f'The largest component contains {x} ring{"s" if x > 1 else ""}.')
g = {input().strip():[] for _ in range(int(input()))}
for _ in range(int(input())):
    a, b = input().strip().split()
    g[a].append(b), g[b].append(a)
col = {i: -1 for i in g}

for i in g:
    if col[i] == -1:
        s = [(i, 0)]
        while s:
            u, c = s.pop()
            if col[u] == -1:
                col[u] = c
                for j in g[u]: s.append((j, 1-c))
            elif col[u] != c: print('impossible'); exit(0)
w, j = [], []
for i in col: [w, j][col[i]].append(i)
print(*w), print(*j)
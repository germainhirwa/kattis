import sys; input = sys.stdin.readline
n = int(input())
m = [input().strip() for _ in range(n)]
g = [[] for _ in range(3*n)]
for i in range(n-1):
    for j in range(2):
        if m[i][j] == m[i][j+1] and m[i][j] in '.*' : g[3*i+j].append(3*i+j+1), g[3*i+j+1].append(3*i+j)
    for j in range(3):
        if m[i][j] == m[i+1][j] and m[i][j] in '.*': g[3*i+j].append(3*i+j+3), g[3*i+j+3].append(3*i+j)
        if m[i][j] == '/' and m[i+1][j] == '*' or m[i][j] == '*' and m[i+1][j] == '.' or m[i][j] == '.' and m[i+1][j] == '/': g[3*i+j].append(3*i+j+3)
s = [i for i in range(3) if m[0][i] == '.']
v = [0]*3*n
while s:
    u = s.pop()
    if u//3 == n-1: print('YES'), exit(0)
    if v[u]: continue
    v[u] = 1
    for w in g[u]: s.append(w)
print('NO')
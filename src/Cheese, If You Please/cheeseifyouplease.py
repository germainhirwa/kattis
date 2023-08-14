import sys; input = sys.stdin.readline
n, m = map(int, input().split())
w = [*map(int, input().split())]
pp = [[*map(float, input().split())] for _ in range(m)]
c = [[0]*(m+n+1) for _ in range(n+1)]
for i in range(m):
    c[-1][i] = -pp[i][-1]
    for j in range(n): c[j][i] = pp[i][j]/100
for i in range(n): c[i][i+m] = 1; c[i][-1] = w[i]

# Simplex method
# m = number of variables, n = number of constraints
while True:
    if (col:=min([(i,e) for i,e in enumerate(c[-1]) if e<0], key=lambda x: x[1], default=[-1])[0]) == -1: break
    if (row:=min([(i,e,c[i][-1]/c[i][col]) for i,e in enumerate(c[t][col] for t in range(n)) if e>0], key=lambda x: x[2], default=[-1])[0]) == -1: break
    k = c[row][col]
    for i in range(m+n+1): c[row][i] /= k
    for i in range(n+1):
        if i == row: continue
        k = c[i][col]
        for j in range(m+n+1): c[i][j] -= k*c[row][j]
print('%.2f'%c[-1][-1])
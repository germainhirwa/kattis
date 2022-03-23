h, w = map(int, input().split())
u, l, r, d = map(int, input().split())
m = []
wds = []

for _ in range(h):
    wds.append(input())

for _ in range(u + d + h):
    m.append([''] * (l + r + w))

for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j] = '#.'[(i + j) % 2]

for i in range(h):
    for j in range(w):
        m[i + u][j + l] = wds[i][j]

for r in m:
    print(''.join(r))
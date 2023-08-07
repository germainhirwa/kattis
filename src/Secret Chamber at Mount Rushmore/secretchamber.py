n, m = map(int, input().split())
D = [[0]*26 for _ in range(26)]
for i in range(26): D[i][i] = 1
for _ in range(n):
    a, b = input().split(); a = ord(a)-97; b = ord(b)-97
    D[a][b] = 1
for k in range(26):
    for i in range(26):
        for j in range(26): D[i][j] |= D[i][k] & D[k][j]
for _ in range(m):
    a, b = input().split()
    if len(a) != len(b): print('no')
    else: print(['no', 'yes'][all(D[ord(a[i])-97][ord(b[i])-97] for i in range(len(a)))])
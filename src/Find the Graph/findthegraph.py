n = int(input()); adj = [[0]*n for _ in range(n)]; deg = [0]*n
for i in range(n): print('? 1', i+1); deg[i] = int(input())
for i in range(n-1):
    for j in range(i+1, n): print('? 2', i+1, j+1); adj[i][j] = adj[j][i] = int(deg[i]+deg[j]-2==int(input()))
print('!')
for r in adj: print(*r)
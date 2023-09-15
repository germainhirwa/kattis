import sys; input = sys.stdin.readline
from collections import defaultdict
while (n:=int(input()))+1:
    G = [[' ']*130 for _ in range(130)]
    D = defaultdict(lambda: ' ')
    for i in range(5):
        for j in range(5):
            D[chr(65+5*i+j)] = (60+i, 60+j); G[60+i][60+j] = chr(65+5*i+j)
    mv = [input().strip().split() for _ in range(n)]
    for l, d in mv:
        sr, sc = D[l]
        if d[0] == 'u':
            pos = sr
            while G[pos][sc] != ' ': pos -= 1
            for i in range(pos, sr):
                G[i][sc] = G[i+1][sc]
                D[G[i][sc]] = (i, sc)
            G[sr][sc] = ' '
        elif d[0] == 'd':
            pos = sr
            while G[pos][sc] != ' ': pos += 1
            for i in range(pos, sr, -1):
                G[i][sc] = G[i-1][sc]
                D[G[i][sc]] = (i, sc)
        elif d[0] == 'r':
            pos = sc
            while G[sr][pos] != ' ': pos += 1
            for i in range(pos, sc, -1):
                G[sr][i] = G[sr][i-1]
                D[G[sr][i]] = (sr, i)
        else: # left
            pos = sc
            while G[sr][pos] != ' ': pos -= 1
            for i in range(pos, sc):
                G[sr][i] = G[sr][i+1]
                D[G[sr][i]] = (sr, i)
        G[sr][sc] = ' '
    if ' ' in D: del D[' ']
    mir, mic = min(i[0] for i in D.values()), min(i[1] for i in D.values())
    mar, mac = max(i[0] for i in D.values()), max(i[1] for i in D.values())
    for i in range(mir, mar+1):
        print(''.join(G[i][mic:mac+1]).rstrip())
    print()
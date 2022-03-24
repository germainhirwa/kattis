import sys
sys.setrecursionlimit(200000)

g = {}
for _ in range(int(input())):
    r = input().split()
    b = r[0][:-1]
    for s in r[1:]:
        if s not in g:
            g[s] = []
        g[s].append(b)

top = []
vis = set()
def DFS(s):
    vis.add(s)
    if s in g:
        for v in g[s]:
            if v not in vis:
                DFS(v) 
    top.append(s)

DFS(input())
for v in top[::-1]:
    print(v)
import sys; input = sys.stdin.readline
from heapq import *
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split()); s -= 1; g -= 1; h -= 1
    al = [{} for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        al[a-1][b-1] = al[b-1][a-1] = d
    x = sorted(int(input())-1 for _ in range(t))
    D = [[float('inf')]*2 for _ in range(n)]
    D[s][0] = 0
    pq = [(0, s, 0)]
    while pq:
        dd, vv, gh = heappop(pq)
        if dd == D[vv][gh]:
            for nn in al[vv]:
                gh_used = gh|((vv,nn)==(g,h)or(vv,nn)==(h,g))
                if D[nn][gh_used] > (new:=dd+al[vv][nn]): D[nn][gh_used] = new; heappush(pq, (D[nn][gh_used], nn, gh_used))
    print(*(i+1 for i in x if D[i][0]>=D[i][1]!=float('inf')))
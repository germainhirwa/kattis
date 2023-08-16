import sys; sys.setrecursionlimit(10**4)
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n):
    i1, i2 = map(int, input().split())
    g[i1].append(i2), g[i2].append(i1)
cnt = [0]*(n+2)
best = [(1e9, -1)]
def dfs(curr, pre):
    cnt[curr] = 1
    v = []
    for nxt in g[curr]:
        if nxt != pre:
            dfs(nxt, curr)
            cnt[curr] += cnt[nxt]
            v.append(cnt[nxt])
    # given tree rooted at 0,
    # v = number of vertices are under each branch of curr
    # cnt = sum(v)+1
    v.append(n+1-cnt[curr]) # everything above curr is a single connected component
    # if we remove curr, the number of connected pairs is sum(C(x, 2) for x in v)
    n1 = sum(x*(x-1)//2 for x in v)
    v.sort(); v.append((v.pop()if v else 0)+(v.pop()if v else 0)) # when reconnecting, take the two largest and combine them
    n2 = sum(x*(x-1)//2 for x in v)
    best[0] = min(best[0], (n1, n2))
dfs(0, -1)
n1, n2 = best[0]
print(n*(n-1)//2-n1, n*(n-1)//2-n2)
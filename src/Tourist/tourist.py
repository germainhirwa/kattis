import sys; input = sys.stdin.readline
INF = 1e18
deltas = ((1, 0), (0, 1))
for _ in range(int(input())):
    C, R = map(int, input().split())
    s, t = 2*R*C, 2*R*C+1
    n = t+1
    al, el, k = [[] for _ in range(n)], [], INF
    m = [input() for _ in range(R)]

    def add_edge(u, v, c, w):
        e1, e2 = [u, v, c, w, 0, len(al[v])], [v, u, 0, -w, 0, len(al[u])]
        al[u].append(len(el)), el.append(e1), al[v].append(len(el)), el.append(e2)

    add_edge(s, 0, 2, 0)
    add_edge(s-1, t, 2, 0)
    for i in range(R):
        for j in range(C):
            if m[i][j] == '#': continue
            for di, dj in deltas:
                if 0<=i+di<R and 0<=j+dj<C and m[i+di][j+dj] != '#':
                    add_edge(2*(i*C+j)+1, 2*((i+di)*C+j+dj), INF, 0)
            if m[i][j]=='*':    add_edge(2*(i*C+j), 2*(i*C+j)+1, 1, 0), add_edge(2*(i*C+j), 2*(i*C+j)+1, 1, -1)
            else:               add_edge(2*(i*C+j), 2*(i*C+j)+1, 2, 0)

    flow = cost = 0
    while flow < k:
        id, d, q, p, pe = [0]*n, [INF]*n, [0]*n, [0]*n, [0]*n
        qh = qt = 0
        q[qt] = s; qt += 1
        d[s] = 0
        while qh != qt:
            v = q[qh]; qh += 1
            id[v] = 2
            if qh == n: qh = 0
            for i in range(len(al[v])):
                r = el[al[v][i]]
                if r[4] < r[2] and d[v]+r[3] < d[r[1]]:
                    d[r[1]] = d[v]+r[3]
                    if id[r[1]] == 0:
                        q[qt] = r[1]; qt += 1
                        if qt == n: qt = 0
                    elif id[r[1]] == 2:
                        qh -= 1
                        if qh == -1: qh = n-1
                        q[qh] = r[1]
                    id[r[1]] = 1; p[r[1]] = v; pe[r[1]] = i
        if d[t] == INF: break
        addflow, v = k-flow, t
        while v != s:
            ee = al[p[v]][pe[v]]
            addflow = min(addflow, el[ee][2]-el[ee][4])
            v = p[v]
        v = t
        while v != s:
            ee = al[p[v]][pe[v]]
            el[ee][4] += addflow
            el[al[v][el[ee][5]]][4] -= addflow
            cost += el[ee][3]*addflow
            v = p[v]
        flow += addflow
    print(-cost)
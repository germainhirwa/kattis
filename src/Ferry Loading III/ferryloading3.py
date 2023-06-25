from collections import deque
for _ in range(int(input())):
    n, t, m = map(int, input().split())
    q1, q2 = deque(), deque()
    for i in range(m):
        a, d = input().strip().split()
        [q1, q2][d=='right'].append((int(a), i))
    s, tt, f = 0, 0, [0]*m
    while q1 or q2:
        q = [q1, q2][s]
        qx = [q1, q2][1-s]
        c = []
        for _ in range(min(len(q), n)):
            tx, _ = q[0]
            if tx <= tt: c.append(q.popleft())
            else: break
        if not c:
            wc = q[0][0] if q else 1e9
            wo = qx[0][0] if qx else 1e9
            if wc <= wo:
                while q and q[0][0] == wc and len(c) < n: c.append(q.popleft())
            else: tt = max(tt, wo)
        if c: tt = max(tt, c[-1][0])
        tt += t
        s = 1-s
        for _, i in c: f[i] = tt
    for i in f: print(i)
    print()
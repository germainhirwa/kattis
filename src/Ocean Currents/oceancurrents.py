import sys
from collections import deque
r, c = map(int, input().split())
m, n, q = [], r*c, -1
K = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
for l in sys.stdin:
    if len(m) != n:
        m.extend(map(int, l.strip()))
    elif q == -1: q = None
    else:
        rs, cs, rd, cd = map(int, l.split())
        rs, cs, rd, cd = rs-1, cs-1, rd-1, cd-1
        s, d = rs*c+cs, rd*c+cd
        q, v = deque([(s, 0)]), set()
        f = [q.appendleft, q.append]
        while q:
            u, x = q.popleft()
            if u == d: print(x); break
            if u in v: continue
            v.add(u)
            rr, cc = u//c, u%c
            for i in range(8):
                (dr, dc), t = K[i], i!=m[u]
                if 0<=rr+dr<r and 0<=cc+dc<c: f[t]((u+dr*c+dc, x+t))
from collections import Counter
def win(h):
    def bt(c, p):
        if sum(c.values()) == 0: return 1
        # pong
        for i in range(1, 10):
            if c[i] >= 3:
                c[i] -= 3
                if bt(c, p): return 1
                c[i] += 3
        # pair
        for i in range(1, 10):
            if c[i] >= 2 and not p:
                c[i] -= 2
                if bt(c, 1): return 1
                c[i] += 2
        # chi
        for i in range(1, 8):
            if c[i] and c[i+1] and c[i+2]:
                c[i] -= 1; c[i+1] -= 1; c[i+2] -= 1
                if bt(c, p): return 1
                c[i] += 1; c[i+1] += 1; c[i+2] += 1
        return 0
    return bt(h, 0)
x = int(input()); rest = [*range(1, 10)]*4; best = 0
mj = [*map(int, input().split())]; mjs = {*mj}
for i in mj: rest.remove(i)
mj = Counter(mj); rest = Counter(rest)
for t in mjs:
    mj[t] -= 1; pts = 0
    for u, v in rest.items():
        mj[u] += 1
        if win(mj.copy()): pts += v*(1+mj[x])
        mj[u] -= 1
    best = max(best, pts/22)
    mj[t] += 1
print(best)
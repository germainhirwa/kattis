import sys; input = sys.stdin.readline
while True:
    p = None; h = {}; c = {}
    while True:
        s = input().strip()
        if s == '1':
            for k, v in c.items():
                if len(v) == 1: continue
                for p in v: h[p].discard(k)
            for k, v in sorted(h.items(), key=lambda x: (-len(x[1]), x[0])): print(k, len(v))
            break
        elif s == '0': exit(0)
        if s.isupper(): p = s; h[p] = set()
        else:
            h[p].add(s)
            if s not in c: c[s] = set()
            c[s].add(p)
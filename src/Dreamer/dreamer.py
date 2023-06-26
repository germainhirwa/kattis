from itertools import permutations
from datetime import *
for _ in range(int(input())):
    can = best = 0
    for p in sorted(set(permutations(input().strip().replace(' ', ''))), key=lambda x: (x[4:], x[2:4], x[:2])):
        y = int(''.join(p[4:]))
        if y < 2000: continue
        m = int(p[2]+p[3])
        if not (0 < m < 13): continue
        d = int(p[0]+p[1])
        try:
            dt = datetime(y, m, d)
            can += 1
            if best == 0: best = (d, m, y)
        except: pass
    if not can: print(0)
    else: print(can, str(best[0]).zfill(2), str(best[1]).zfill(2), best[2])
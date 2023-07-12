import sys; input = sys.stdin.readline
from math import ceil
t = 1
while True:
    w, n = map(int, input().split())
    if not w: break
    h = []
    for _ in range(n): a, b = input().split(); h.append((a, int(b)))
    cmax = max(i[1] for i in h)
    W, H, C = -10, 0, 0
    for ww, cw in h:
        p = 8+ceil(40*(cw-4)/(cmax-4))
        lw = ceil(9/16*len(ww)*p) + 10
        if W + lw <= w: W += lw; C = max(C, p)
        else: W = lw-10; H += C; C = p
    print(f'CLOUD {t}:', H+C); t += 1
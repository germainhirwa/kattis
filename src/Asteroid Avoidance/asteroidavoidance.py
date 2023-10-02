import sys; input = sys.stdin.readline
w, h = map(int, input().split())
n, m = map(int, input().split())
aa = [[*map(int, input().split())] for _ in range(n)]
for _ in range(m):
    xr, yr = map(int, input().split()); no = 0
    p = ((xr, yr), (xr+w, yr), (xr, yr+h), (xr+w, yr+h))
    for xa, ya, ra in aa:
        if xr <= xa <= xr+w and yr <= ya <= yr+h: no = 1; break
        if (xr-ra <= xa <= xr or xr+w <= xa <= xr+w+ra) and yr <= ya <= yr+h: no = 1; break
        if xr <= xa <= xr+w and (yr-ra <= ya <= yr or yr+h <= ya <= yr+h+ra): no = 1; break
        if min((xa-x)**2 + (ya-y)**2 for x, y in p) <= ra**2: no = 1; break
    print('DOOMSLUG '+['GO!','STOP!'][no])
import sys; input = sys.stdin.readline
n, t = map(int, input().split())
w = [[*map(int, input().split())] for _ in range(n)]
def f(x): return sum(d/(s+x) for d, s in w)
lo, hi = -min(i[1] for i in w), 1e9
while abs(lo-hi)>1e-7:
    mi = (lo+hi)/2
    if f(mi) > t: lo = mi
    else: hi = mi
print(mi)
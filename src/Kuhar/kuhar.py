import sys; input = sys.stdin.readline
n, m = map(int, input().split())
p = [[*map(int, input().split())] for _ in range(n)]
def f(s):
    tc = 0
    for x, y, sm, pm, sv, pv in p:
        if (need:=x*s-y) > 0:
            cost = 1e7
            for i in range(need//sm+2): cost = min(cost, pm*i+pv*max((need-i*sm+sv-1)//sv, 0))
            tc += cost
    return tc <= m
lo, hi = 0, m
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): lo = mi
    else: hi = mi-1
print(hi if f(hi) else hi-1)
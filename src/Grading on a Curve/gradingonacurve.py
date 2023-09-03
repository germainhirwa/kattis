import sys; input = sys.stdin.readline
n, t = map(int, input().split())
s = [*map(int, sys.stdin)]
def f(k):
    a = b = c = 0
    for i in s: a += i/k >= 0.9; b += i/k >= 0.8; c += i/k >= 0.7
    return 4*a>=n and 2*b>=n and 4*c>=3*n
lo, hi = 1, 10**6
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): lo = mi
    else: hi = mi-1
ans = hi if f(hi) else hi-1
if ans and f(ans): print(ans)
else: print(-1)
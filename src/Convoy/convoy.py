import sys; input = sys.stdin.readline

def f(x):
    c = 0
    for i in range(k):
        if t[i] > x: break
        r = x//t[i]; c += (r+1)//2*4+1 
    return c >= n

n, k = map(int, input().split()); k = min(k, n)
t = sorted(int(input()) for _ in range(n))
lo, hi = 0, 10**12
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): hi = mi
    else: lo = mi+1
print(lo if f(lo) else lo+1)
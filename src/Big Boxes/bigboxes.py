import sys; input = sys.stdin.readline
n, k = map(int, input().split())
w = [*map(int, input().split())]

def f(x):
    c = r = 0
    for i in w:
        if c+i > x: c = i; r += 1
        else: c += i
    return r+(c>0)<= k

lo, hi = max(w), 10**9
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): hi = mi
    else: lo = mi+1
print(lo if f(lo) else lo+1)
import sys; input = sys.stdin.readline
n, M = map(int, input().split())
pc = [[*map(int, input().split())] for _ in range(n)]
def f(x): return sum(max(p*x-c, 0) for p, c in pc) >= M
lo, hi = 0, 10**10
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): hi = mi
    else: lo = mi+1
print(lo if f(lo) else lo+1)
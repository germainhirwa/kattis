import sys; input = sys.stdin.readline

def sum_binom(n, r, k):
    ans = 0; f = 1
    for i in range(r):
        f *= n-i; f //= i+1; ans += f
        if ans > k: break
    return ans

for _ in range(int(input())):
    n, k = map(int, input().split())
    lo, hi = 0, n
    while hi-lo > 1:
        mid = (lo+hi)//2
        if sum_binom(mid, k, n) < n: lo = mid
        else: hi = mid
    print('Impossible' if lo > 31 else lo+1)
import sys; input = sys.stdin.readline
def f(n):
    if n < 10: return -int(n==-1) # zero case
    l, r = n, 0; ans = 0; p = 1
    while l:
        ans += l//10*p if l%10 else (l//10-1)*p+r+1
        r += (l%10)*p; l //= 10; p *= 10
    return ans
while True:
    m, n = map(int, input().split())
    if m+1==n+1==0: break
    print(f(n)-f(m-1))
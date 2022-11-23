dp = [[[0]*101 for _ in range(101)] for _ in range(11)]

def f(k, s, e):
    if k == 0:
        return 1e9
    elif k == 1:
        return e*(e+1)//2 - s*(s+1)//2
    elif s == e:
        return 0
    elif dp[k][s][e] == 0:
        r = 1e9
        for i in range(s+1, e+1):
            r = min(r, i + max(f(k-1, s, i-1), f(k, i, e)))
        dp[k][s][e] = r
    return dp[k][s][e]


n = int(input())
for _ in range(n):
    k, m = map(int, input().split())
    print(f(k, 0, m))
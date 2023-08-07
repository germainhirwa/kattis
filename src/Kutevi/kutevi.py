n, k = map(int, input().split()); a = [*map(int, input().split())]; q = [*map(int, input().split())]
dp = [0]*360
for i in a:
    dp[i] = 1
    for j in range(360):
        for k in range(360): dp[(j+k*i)%360] |= dp[j]
for i in q: print(['NO', 'YES'][dp[i]])
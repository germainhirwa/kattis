n = int(input())
dp = [0]*43201
for d, t in [[*map(int, input().split())] for _ in range(n)]: dp[t-2*d] += 1; dp[t-d] += 1; dp[t] += 1
print((max(dp)+1)//2)
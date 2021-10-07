import sys

def knapsack(capacity, vals, weights):
    dp = []
    n, w = len(vals), max(weights)
    zeroes = [0]*(capacity+1)
    for i in range(n+1):
        dp.append(zeroes.copy())
        
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j-weights[i-1]] + vals[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp

capacity, n, vals, weights = 0, 0, [], []
for line in sys.stdin:
    if n == 0:
        capacity, n = list(map(int, line.split(" ")))
    else:
        v, w = list(map(int, line.split(" ")))
        vals.append(v)
        weights.append(w)
        n -= 1
        if n == 0:
            ks = knapsack(capacity, vals, weights) # size of len(vals) * capacity
            result = []
            i, j = len(vals), capacity
            while i and j:
                if ks[i][j] == 0:
                    break
                if ks[i][j] == ks[i-1][j]:
                    i -= 1
                else:
                    i -= 1
                    j -= weights[i]
                    result.append(str(i))
            
            print(len(result))
            print(" ".join(result))
            capacity, vals, weights = 0, [], []

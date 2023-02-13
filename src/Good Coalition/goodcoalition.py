import sys

def knapsack(vals, weights):
    n, w = len(vals), max(weights)
    dp = [1]*151
    for i in range(1,n+1):
        tmp = dp.copy()
        for j in range(1,151):
            if j >= weights[i-1]:
                tmp[j] = min(dp[j-weights[i-1]]*vals[i-1], dp[j])
        dp = tmp
    return min(dp[:75])

n, vals, weights = 0, [], []
input()
for line in sys.stdin:
    if n == 0:
        n = int(line)
    else:
        w, v = map(int, line.split())
        vals.append(v/100)
        weights.append(w)
        n -= 1
        if n == 0:
            ks = knapsack(vals, weights)
            p = 1
            for pp in vals: p *= pp
            print(100*p/ks)
            vals.clear()
            weights.clear()
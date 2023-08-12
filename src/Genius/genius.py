k, t, p, q, x1 = map(int, input().split())
dp = [1]
for _ in range(t):
    w0, w1, w2, w3 = map(int, input().split())
    c = x1%4
    if c == 0: pp = w0/(w0+w1)*w2/(w2+w3)*w0/(w0+w2) + w0/(w0+w1)*w3/(w2+w3)*w0/(w0+w3)
    elif c == 1: pp = w1/(w0+w1)*w2/(w2+w3)*w1/(w1+w2) + w1/(w0+w1)*w3/(w2+w3)*w1/(w1+w3)
    elif c == 2: pp = w2/(w2+w3)*w0/(w0+w1)*w2/(w0+w2) + w2/(w2+w3)*w1/(w0+w1)*w2/(w1+w2)
    else: pp = w3/(w2+w3)*w0/(w0+w1)*w3/(w0+w3) + w3/(w2+w3)*w1/(w0+w1)*w3/(w1+w3)
    x1 = p*x1%q
    dp2 = [0]*(len(dp)+1)
    for i in range(len(dp)): dp2[i+1] += dp[i]*pp; dp2[i] += dp[i]*(1-pp)
    dp = dp2
print(sum(dp[k:]))
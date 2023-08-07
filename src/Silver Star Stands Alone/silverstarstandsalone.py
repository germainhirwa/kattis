P = int(input())
LIMIT = 211
spf = list(range(LIMIT+1))
primes = []
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
dp = [0]*212; dp[2] = 1
for i in primes[1:]:
    for j in range(max(2, i-14), i): dp[i] += dp[j]
print(dp[P])
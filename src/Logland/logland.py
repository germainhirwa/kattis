input(); MOD = 10**9+7; ans = ex = 0; val = 1
for qty in [*map(int, input().split())]:
    qty += ex # equivalently `qty` many coins with value `val`
    if qty % 2 and not ex: ans += val; ans %= MOD # cannot even up from previous `val`
    val *= 2; ex = qty//2; val %= MOD
print(ans)
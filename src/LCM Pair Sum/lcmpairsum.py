import sys; input = sys.stdin.readline
MOD = 10**9+7
for T in range(int(input())):
    F = []; ans = ans2 = 1
    for _ in range(C:=int(input())): F.append([*map(int, input().split())])
    for p, k in F: ans *= pow(p, k, MOD); ans %= MOD; ans2 *= (k+1)*pow(p, k, MOD)+(pow(p, k, MOD)-1)*pow(p-1, -1, MOD); ans2 %= MOD
    print(f'Case {T+1}:', (ans+ans2)%MOD)
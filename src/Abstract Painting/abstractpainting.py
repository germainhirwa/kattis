MOD = 10**9+7
for _ in range(int(input())):
    r, c = map(int, input().split())
    print(pow(3, r+c, MOD)*pow(2, r*c, MOD)%MOD)
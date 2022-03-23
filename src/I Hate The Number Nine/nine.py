import sys

input()
MOD = 1000000007
def powmod(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m
    elif b % 2:
        return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)
        

for line in sys.stdin:
    print(8 * powmod(9, int(line) - 1, MOD) % MOD)
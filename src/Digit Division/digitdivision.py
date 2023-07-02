from collections import deque
n, m = map(int, input().split())
d = deque(input().strip())
p, c = 0, 0
while d:
    c *= 10
    c += int(d.popleft())
    if c % m == 0: p += 1; c = 0

def powmod(a, b, m):
    if b == 0: return 1
    elif b == 1: return a % m
    elif b % 2: return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)

if c or not p: print(0)
else: print(powmod(2, p-1, 10**9+7))
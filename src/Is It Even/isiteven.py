import sys
n, k = map(int, input().split()); b = 0
for l in sys.stdin:
    l = int(l)
    while l % 2 == 0: b += 1; l //= 2
print(int(b >= k))
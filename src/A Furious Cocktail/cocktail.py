import sys
n, t = map(int, input().split())
arr = sorted(map(int, sys.stdin))
for i in range(n):
    if arr[i]-t*i <= 0: print('NO'), sys.exit(0)
print('YES')
import sys

input()
for line in sys.stdin:
    p, r, f = map(int, line.split())
    cnt = 0
    while p <= f:
        p *= r
        cnt += 1
    print(cnt)
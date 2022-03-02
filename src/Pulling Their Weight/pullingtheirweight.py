import sys

n = int(input())
m = {}
w = 0
for line in sys.stdin:
    k = int(line)
    w += k
    if k not in m:
        m[k] = 1
    else:
        m[k] += 1

left = 0
for k in sorted(m):
    if left == w - left - m[k] * k:
        print(k)
        sys.exit(0)
    left += m[k] * k
    if left == w - left:
        print(k + 1)
        sys.exit(0)
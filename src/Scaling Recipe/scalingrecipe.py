import sys

_, a, b = map(int, input().split())
for line in sys.stdin:
    print(int(line) * b // a)
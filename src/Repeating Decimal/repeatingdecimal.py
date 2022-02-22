import sys

for line in sys.stdin:
    a, b, c = list(map(int, line.split()))
    k = str(a * 10**c // b)
    print(f'0.{"0" * (c - len(k))}{k}')
import sys

m = [0, 1, 2, 5, 9, 8, 6]
for line in sys.stdin:
    n = int(line)
    while n != 0:
        print(m[n % 7], end='')
        n //= 7
    print()
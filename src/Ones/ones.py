import sys

for line in sys.stdin:
    n = 9 * int(line)
    x, e = 10, 1
    while x % n != 1:
        x *= 10
        x %= n
        e += 1
    print(e)
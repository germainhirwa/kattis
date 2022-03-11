import sys
input()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def bezout(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        p, q = bezout(b, a % b)
        return (q, p - q * (a // b))
    
for line in sys.stdin:
    # Swap m and n for convenience
    a, m, b, n = map(int, line.split())
    d = gcd(m, n)
    k = m * n
    if (a - b) % d != 0:
        print('no solution')
    else:
        u, _ = bezout(m, n)
        print((a - m * u * (a - b) // d) % k, k)
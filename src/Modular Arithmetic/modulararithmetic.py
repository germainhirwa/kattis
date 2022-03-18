def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inv_mod(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception
    else:
        return x % m

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    for _ in range(n):
        q = input().split()
        a, b = int(q[0]), int(q[2])
        if q[1] == '+':
            print((a + b) % m)
        elif q[1] == '-':
            print((a - b) % m)
        elif q[1] == '*':
            print((a * b) % m)
        elif q[1] == '/':
            try:
                print((a * inv_mod(b, m)) % m)
            except:
                print(-1)
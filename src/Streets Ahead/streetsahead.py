r, (n, q) = {}, map(int, input().split())
for _ in range(n): r[input()] = len(r)
for _ in range(q):
    a, b = input().strip().split()
    print((abs(r[b]-r[a])-1) % n)
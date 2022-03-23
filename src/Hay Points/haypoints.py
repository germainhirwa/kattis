p, d = map(int, input().split())
pts = {}
for _ in range(p):
    w, pt = input().split()
    pts[w] = int(pt)
for _ in range(d):
    n = 0
    while True:
        s = input()
        if s == '.':
            break
        n += sum(map(lambda x: pts.get(x, 0), s.split()))
    print(n)
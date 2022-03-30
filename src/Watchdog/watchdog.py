for _ in range(int(input())):
    s, q = map(int, input().split())
    h = set()
    for _ in range(q):
        h.add(tuple(map(int, input().split())))

    def do():
        for x in range(1, s):
            for y in range(1, s):
                if (x, y) in h:
                    continue
                limit = min(s - x, s - y, x, y)
                possible = True
                for xh, yh in h:
                    if (xh - x)**2 + (yh - y)**2 > limit**2:
                        possible = False
                        break
                if possible:
                    print(x, y)
                    return
        print('poodle')
    do()
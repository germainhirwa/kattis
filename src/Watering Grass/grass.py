import sys; input = sys.stdin.readline
while True:
    try: n, l, w = map(int, input().split())
    except: break
    ints = []
    for _ in range(n):
        x, r = map(int, input().split())
        if r <= w/2: continue
        d = (r**2-w**2/4)**0.5
        ints.append((max(0, x-d), min(l, max(0, x+d))))
    ints.sort(), ints.append((l+10, l+10))
    start, end = 0, -1; cnt = pos = 0
    while pos < len(ints):
        if ints[pos][0] <= start: end = max(ints[pos][1], end); pos += 1
        else:
            start = end; cnt += 1
            if ints[pos][0] > end or end >= l: break
    print(cnt if end >= l else -1)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for i in range(1, n + 1):
        d[i] = arr[i - 1]
    ok = False
    for _ in range(n):
        # Match
        d2 = {}
        for k in d:
            if k != d[k]:
                d2[k] = d[k]
        d = d2

        if not d:
            ok = True
            print('All can eat.')
            break

        # Hat and Snatch
        d2 = {}
        for k in d:
            d2[k] = d[d[k]]
        d = d2

    if not ok:
        print('Some starve.')
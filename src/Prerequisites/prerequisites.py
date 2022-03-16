try:
    while True:
        k, m = map(int, input().split())
        courses = set(map(int, input().split()))
        ok = 1
        for _ in range(m):
            arr = tuple(map(int, input().split()))
            r, cl, cnt = arr[1], arr[2:], 0
            for cid in cl:
                if cid in courses:
                    cnt += 1
                if r == cnt:
                    break
            if cnt < r:
                ok = 0
        print(['no', 'yes'][ok])
except:
    pass
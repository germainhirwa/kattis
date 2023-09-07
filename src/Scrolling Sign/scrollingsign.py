for _ in range(int(input())):
    k, w = map(int, input().split())
    prev = '.'*k; ans = 0
    for _ in range(w):
        curr = input().strip(); pos = 0
        while pos < k:
            if prev[pos] == curr[0]:
                ok = 1
                for i in range(pos, k):
                    if prev[i] != curr[i-pos]: ok = 0; break
                if ok: break
            pos += 1
        ans += pos; prev = curr
    print(ans)
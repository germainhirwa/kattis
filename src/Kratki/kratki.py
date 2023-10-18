n, k = map(int, input().split())
if k*k < n: print(-1)
else:
    s1, s2, s3 = [*range(1, n+1)], [], []
    while s1:
        for _ in range(k):
            if s1: s2.append(s1.pop())
        s3.extend(s2[::-1]), s2.clear()
    print(*s3)
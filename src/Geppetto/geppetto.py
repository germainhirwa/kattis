n, m = map(int, input().split())
cannot = [[*map(int, input().split())] for _ in range(m)]
ans = 0
for bm in range(1<<n):
    s = set()
    for i in range(n):
        if bm&(1<<i): s.add(i+1)
    ans += 1
    for a, b in cannot:
        if a in s and b in s: ans -= 1; break
print(ans)
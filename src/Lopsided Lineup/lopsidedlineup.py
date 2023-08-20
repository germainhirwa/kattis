import sys; input = sys.stdin.readline
n = int(input()); m = [[*map(int, input().split())] for _ in range(n)]
t = sorted((sum(m[i]), i) for i in range(n))
w, s = t[:n//2], t[n//2:]; ans = 0
for i in range(n//2-1):
    for j in range(i+1, n//2): ans += m[s[i][1]][s[j][1]]-m[w[i][1]][w[j][1]]
print(ans)
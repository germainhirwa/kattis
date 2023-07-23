n, m = map(int, input().split())
if m < n-1 or m > 2*n-3: print(-1), exit(0)
used = set()
for i in range(min(m, n-1)): print(i%n+1, (i+1)%n+1), used.add(i%n+(i+1)%n+2)
e = m-min(m, n-1)
for i in range(2, n+1):
    for j in range(1, i):
        if e == 0: exit(0)
        if i+j not in used: used.add(i+j), print(i, j); e -= 1
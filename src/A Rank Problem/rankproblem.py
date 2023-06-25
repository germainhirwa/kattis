n, m = map(int, input().split())
teams = [f'T{i+1}' for i in range(n)]
for i in range(m):
    a, b = input().strip().split()
    c, d = teams.index(a), teams.index(b)
    if c > d: teams.pop(d), teams.insert(c, b)
print(*teams)
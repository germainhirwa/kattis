p, u = {tuple(map(int, input().split())) for _ in range(int(input()))}, 0
delta = [(0, 2018), (1118, 1680), (1680, 1118), (2018, 0), (-1118, 1680), (-1680, 1118)]
for x, y in p:
    for dx, dy in delta: u += (x+dx, y+dy) in p
print(u)
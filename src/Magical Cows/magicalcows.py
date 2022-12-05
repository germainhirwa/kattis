c, n, m = map(int, input().split())
farm = {}
for _ in range(n):
    f = int(input())
    if f not in farm: farm[f] = 0
    farm[f] += 1
days = [int(input()) for _ in range(m)]
h = {}
for d in range(51):
    h[d] = sum(farm.values())
    new_farm = {}
    for k in farm:
        if 2*k > c:
            new_farm[k] = new_farm.get(k, 0) + 2*farm[k]
        else:
            new_farm[2*k] = new_farm.get(2*k, 0) + farm[k]
    farm = new_farm
for d in days:
    print(h[d])
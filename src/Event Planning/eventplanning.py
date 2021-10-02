n, b, h, w = list(map(int, input().split(" ")))
found = False
min_cost = b

for _ in range(h):
    p = int(input())
    a = list(map(int, input().split(" ")))
    for beds in a:
        if beds >= n and n*p <= b:
            found = True
            min_cost = min(min_cost, n*p)

print(["stay home", min_cost][int(found)])
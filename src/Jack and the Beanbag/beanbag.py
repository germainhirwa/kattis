b = int(input()); v = [*map(int, input().split())]; best = 0
tt = [sum(1<<(int(a)-1) for a in map(int, input().split()[1:])) for _ in range(int(input()))]
for bm in range(1, 1<<b):
    if all(bm&i for i in tt): best = max(best, sum(v[i] for i in range(b) if ~bm&(1<<i)))
print(best)
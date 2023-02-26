ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
for i in range(5001):
    if (i+ds) % ys or (i+dm) % ym: continue
    print(i); break
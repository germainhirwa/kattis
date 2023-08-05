n = int(input())
ans = [0]*n
for t in range(len(bin(n))-1):
    q = []
    for i in range(n):
        if i&(1<<t): q.append(i+1)
    if not q: break
    print('ASK', len(q), *q, flush=True)
    out = [*map(int, input().split())]
    for l, r in zip(q, out):
        ans[r-1] += 1<<t
print('ANSWER', *[i+1 for i in ans])
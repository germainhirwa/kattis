l, h, k = map(int, input().split())
m = [['_']*l for _ in range(h)]
for i in range(k):
    l, h, a, b = map(int, input().split())
    for y in range(h):
        for x in range(l):
            try: m[b+y][a+x] = chr(97+i)
            except: pass
for r in m: print(''.join(r))
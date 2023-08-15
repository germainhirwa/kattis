pt, p1, p2 = map(lambda x: round(100*float(x)), input().split())
v = []
for i in range(pt//p1+1):
    if (pt-p1*i) % p2 != 0: continue
    if (pt-p1*i)//p2 >= 0: v.append((i, (pt-p1*i)//p2))
if not v: print('none')
else: [print(*i) for i in v]
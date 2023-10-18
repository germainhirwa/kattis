c, e, m = map(int, input().split())
if c != 4 or e % 2: print('impossible'), exit(0)
if m == 0: print(2, e//2+2), exit(0)
for h in range(1, int(m**0.5+1)):
    if m%h == 0 and h+m//h == e//2: print(h+2, m//h+2), exit(0)
print('impossible')
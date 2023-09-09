from random import *
n = int(input()); ans = []; l = [*'PIZA']
for _ in range(n):
    shuffle(l); ok = 0
    for c in l[:3]:
        ans.append(c)
        print(''.join(ans))
        if (v:=int(input())) == 1: ok = 1; break
        elif v == 2: exit(0)
        ans.pop()
    if not ok: ans.append(l[-1])
print(''.join(ans))
from collections import *
n = int(input()); q = deque(input().split()); s = input()
wo, bo = q.popleft(), q.popleft(); wd, bd = q.popleft(), q.popleft(); ss = []; dyn = [None, None, 0]; w = (wo, wd); b = (bo, bd)
for i in s:
    if i == 'W':
        if dyn[:2] in [[wo, wd], [wd, wo]]: dyn[2] += 1
        else: ss.append([*dyn]); dyn = [*w, 1]
        wo, wd = wd, wo; q.append(bd); bo, bd = q.popleft(), bo; b = (bd, bo)
    else:
        if dyn[:2] in [[bo, bd], [bd, bo]]: dyn[2] += 1
        else: ss.append([*dyn]); dyn = [*b, 1]
        bo, bd = bd, bo; q.append(wd); wo, wd = q.popleft(), wo; w = (wd, wo)
ss.append([*dyn]); m = max(map(lambda x: x[2], ss))
for i in ss:
    if i[2] == m: print(i[0], i[1])
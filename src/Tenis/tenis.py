a, b = input().split()
valid = {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 5), (7, 6)}
for _ in range(int(input())):
    m = input().split()
    if len(m) > 3: print('ne'); continue
    aa = bb = 0; ok = True
    for s in m[:2]:
        s1, s2 = map(int, s.split(':'))
        if s1 < s2:
            if (s2, s1) not in valid: ok = False; break
            elif a == 'federer': ok = False; break
            else: bb += 1
        elif s1 > s2:
            if (s1, s2) not in valid: ok = False; break
            elif b == 'federer': ok = False; break
            else: aa += 1
        else: ok = False; break
    if not ok or (abs(aa-bb)==2 and len(m)>2) or (aa==bb and len(m)<3) or abs(aa-bb)==1: print('ne'); continue
    for s in m[2:]:
        s1, s2 = map(int, s.split(':'))
        if s1 < s2:
            if not (s2 == 6 or (s2 > 6 and s2-s1 == 2)): ok = False; break
            elif a == 'federer': ok = False; break
        elif s1 > s2:
            if not (s1 == 6 or (s1 > 6 and s1-s2 == 2)): ok = False; break
            elif b == 'federer': ok = False; break
        else: ok = False; break
    print(['ne', 'da'][ok])
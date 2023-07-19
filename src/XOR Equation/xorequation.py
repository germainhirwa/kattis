a, xor, b, eq, c = input().split()
a, b, c = sorted([a, b, c], key=lambda x: x.count('?'))
ac, bc, cc = a.count('?'), b.count('?'), c.count('?')
ans = [0]
def bt(aa, bb, x, pa, pb):
    if x == 0:
        cc = str(aa^bb)
        if len(cc) == len(c):
            works = 1
            for i in range(len(c)):
                if cc[i] != c[i] != '?': works = 0; break
            if works: ans[0] += 1
        return
    if pa < len(a):
        if a[pa] == '?':
            mul = 10**(len(a)-pa-1)
            for i in range(int(pa==0 and len(a)>1), 10): bt(aa+i*mul, bb, x-1, pa+1, pb)
        else: return bt(aa, bb, x, pa+1, pb)
    elif pb < len(b):
        if b[pb] == '?':
            mul = 10**(len(b)-pb-1)
            for i in range(int(pb==0 and len(b)>1), 10): bt(aa, bb+i*mul, x-1, pa, pb+1)
        else: return bt(aa, bb, x, pa, pb+1)
na = nb = 0
for i in a: na *= 10; na += int(i) if i != '?' else 0
for i in b: nb *= 10; nb += int(i) if i != '?' else 0
bt(na, nb, ac+bc, 0, 0), print(ans[0])
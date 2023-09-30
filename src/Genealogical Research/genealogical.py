import sys

def do(hm, a):
    if a in hm:
        s = sorted([(p, 1) for p in hm[a]], reverse=True)
        while s:
            u, sp = s.pop()
            if u not in dmy: print(' '*sp, u)
            elif len(dmy[u]) == 1: print(' '*sp, u, dmy[u][0], '-')
            else: print(' '*sp, u, dmy[u][0], '-', dmy[u][1])
            if u in hm:
                for p in sorted(hm[u], reverse=True): s.append((p, sp+2))

anc, dec, dmy = {}, {}, {}; fi = 1
for l in sys.stdin:
    l = l.strip()
    if l[0] == 'Q': break
    elif l[0] == 'B':
        c, d, m, f = l[6:].split(' : ')
        anc[c] = [m, f]; dmy[c] = [d]
        if m not in dec: dec[m] = []
        if f not in dec: dec[f] = []
        dec[m].append(c), dec[f].append(c)
    elif l[2] == 'A': p, d = l[6:].split(' : '); dmy[p].append(d)
    elif l[0] == 'A':
        if fi: fi = 0
        else: print()
        a = l[10:]; print('ANCESTORS of', a), do(anc, a)
    else:
        if fi: fi = 0
        else: print()
        d = l[12:]; print('DESCENDANTS of', d), do(dec, d)
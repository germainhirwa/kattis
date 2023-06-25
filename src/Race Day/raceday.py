while True:
    n = int(input())
    if n == 0: break
    d = {}
    for _ in range(n):
        f, l, bib = input().strip().split()
        d[bib] = {'n': f'{l}, {f}'}
    for _ in range(3*n):
        b, s, t = input().strip().split()
        d[b][s] = t
    table = [['NAME', 'BIB', 'SPLIT1', 'RANK', 'SPLIT2', 'RANK', 'FINISH', 'RANK']]
    for s in ['S1', 'S2', 'F']:
        t = []
        for b in d:
            h, m = map(int, d[b][s].split(':'))
            t.append([60*h+m, b])
        t.sort()
        r, w = 0, -1
        for i in range(n):
            if w == t[i][0]: r += 1
            else: r = 0
            t[i].append(i+1-r)
            w = max(w, t[i][0])
        for _, b, rk in t:
            d[b][f'r{s}'] = rk
    rows = []
    for bib, st in d.items():
        r = [st['n'], bib]
        for s in ['S1', 'S2', 'F']: r.extend([st[s], str(st[f'r{s}'])])
        rows.append(r)
    table.extend(sorted(rows))
    for row in table:
        for i, col in enumerate(row):
            if i == 0: print(col.ljust(20), end='')
            else: print(col.rjust(10), end='')
        print()
    print()
import sys
d = 1
for l in sys.stdin:
    l = l.strip()
    if l == 'OPEN': print('Day', d); h = {}; c = {}
    elif l == 'CLOSE':
        for k, v in sorted(h.items()): print(k, f'${"%.2f"%(v/10)}')
        print(); d += 1
    else:
        p, n, m = l.split()
        m = int(m)
        if p == 'ENTER': c[n] = m
        else:
            if n not in h: h[n] = 0
            h[n] += m-c[n]
import sys

def process(t):
    h, m, s = map(int, t.split(':'))
    return 3600*h + 60*m + s

t, v, d = 0, 0, 0
for line in sys.stdin:
    if len(line.split()) == 2:
        t2, v2 = line.split()
        t2, v2 = process(t2), int(v2)
        d += (t2 - t)/3600*v
        t, v = t2, v2
    else:
        t2 = process(line)
        d += (t2 - t)/3600*v
        print(line.strip(), '%.2f'%d, 'km')
        t = t2
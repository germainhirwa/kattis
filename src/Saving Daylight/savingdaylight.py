import sys

for line in sys.stdin:
    m, d, y, t1, t2 = line.strip().split()
    t1, t2 = t1.split(':'), t2.split(':')
    h1, m1 = map(int, t1)
    h2, m2 = map(int, t2)
    dd = 60 * (h2 - h1) + (m2 - m1)
    hh = dd // 60
    mm = dd % 60
    print(m, d, y, hh, 'hours', mm, 'minutes')
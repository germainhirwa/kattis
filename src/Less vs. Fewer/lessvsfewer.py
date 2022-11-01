n, p = map(int, input().split())
c, m = set(), set()
valid_c = ['number of', 'most', 'fewest', 'more', 'fewer', 'many', 'few']
valid_m = ['amount of', 'most', 'least', 'more', 'less', 'much', 'little']
for _ in range(n):
    a, b = input().split()
    {'c': c, 'm': m}[b].add(a)
for _ in range(p):
    s = input().split()
    a, b = ' '.join(s[:-1]), s[-1]
    print(['Not on my watch!', 'Correct!'][int(
        (b in c and a in valid_c) or
        (b in m and a in valid_m)
    )])
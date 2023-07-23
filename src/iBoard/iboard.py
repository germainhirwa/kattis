import sys
for l in sys.stdin:
    l = [*map(lambda x: bin(ord(x))[2:].zfill(7), l.strip())]
    o = z = 0
    for i in l: o += i.count('1'); z += i.count('0')
    print(['free', 'trapped'][o%2 or z%2])
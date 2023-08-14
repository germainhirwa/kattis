import sys; input = sys.stdin.readline
h = 0
while (n:=int(input())):
    v = set()
    if h: print()
    for _ in range(n):
        p, *s = input().split(); s = [*map(int, s)]
        r = []
        for i in s: r.extend([p]*i); p = '.' if p == '#' else '#'
        print(''.join(r)); v.add(len(r))
    if len(v) != 1: print('Error decoding image')
    h = 1
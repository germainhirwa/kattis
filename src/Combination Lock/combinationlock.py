import sys

for l in sys.stdin:
    d, c1, c2, c3 = map(int, l.split())
    if d + c1 + c2 + c3: print(9*(120+(d-c1)%40+(c2-c1)%40+(c2-c3)%40))
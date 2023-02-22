import sys
for line in sys.stdin:
    r, s = map(float, line.split())
    print(round(((r*(min(s,.12)+.16))/.067)**0.5))
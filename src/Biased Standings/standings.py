import sys
input()
for line in sys.stdin:
    line = line.strip().split()
    if line:
        if len(line) == 1: p, n = [], int(line[0])
        else: p.append(int(line[1])-1)
        if len(p) == n: print(sum(abs(i-e) for i, e in enumerate(sorted(p))))
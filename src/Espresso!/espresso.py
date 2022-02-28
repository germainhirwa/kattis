import sys

n, s = list(map(int, input().split()))
fill = 0
vol = s
for line in sys.stdin:
    line = line.strip()
    if line[-1] == 'L':
        check = int(line[:-1]) + 1
    else:
        check = int(line)
    if vol < check:
        fill += 1
        vol = s
    vol -= check
print(fill)
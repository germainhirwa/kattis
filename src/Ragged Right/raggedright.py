import sys

lines = []
m = 0
for line in sys.stdin:
    l = line.strip()
    lines.append(l)
    m = max(m, len(l))
print(sum(map(lambda x: (len(x) - m)**2, lines[:-1])))
import sys

skip, m = input(), []
for line in sys.stdin:
    m.append(line.strip())
m = list(map(list, zip(*m)))
print(m.count(['_'] * int(skip.split()[0])) + 1)
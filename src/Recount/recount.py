import sys

d = {}
for line in sys.stdin:
    line = line.strip()
    if line == '***':
        break
    if line not in d:
        d[line] = 1
    else:
        d[line] += 1

m, b = 0, None
for k, v in d.items():
    if v > m:
        m, b = v, k
for k, v in d.items():
    if v == m and k != b:
        print('Runoff!')
        sys.exit(0)
print(b)
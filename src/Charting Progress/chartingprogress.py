import sys

def process(lines):
    x = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '*':
                x.append(i)
    x.sort()
    res = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for i in range(len(x)):
        res[x[i]][-i-1] = '*'
    for r in res: print(''.join(r))

lines = []
for line in sys.stdin:
    if line.strip():
        lines.append(line.strip())
    else:
        process(lines)
        print()
        lines.clear()
process(lines)
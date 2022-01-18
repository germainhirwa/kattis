import sys

m = []
for line in sys.stdin:
    m.append(line.strip())

def knight(r, c):
    res = []
    for i in [-2, -1, 1, 2]:
        for j in [-2, -1, 1, 2]:
            if abs(i) + abs(j) == 3:
                res.append((r + i, c + j))
    return res

valid = True
k = 0
for i in range(5):
    for j in range(5):
        if m[i][j] == 'k':
            k += 1
            valid = valid and all(map(lambda x: m[x[0]][x[1]] == '.', filter(lambda x: x[0] in range(5) and x[1] in range(5), knight(i, j))))
print(['invalid', 'valid'][int(valid and k == 9)])
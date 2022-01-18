# Could've been faster but this passes so
from copy import deepcopy

c, p = list(map(int, input().split()))
h = list(map(int, input().split()))
m = []
for _ in range(max(h) + 5):
    m.append([0] * c)
for i in range(c):
    for j in range(h[i]):
        m[j][i] = 1

t = {
    1: ((0, 0), (0, 1), (0, 2), (0, 3)),
    2: ((0, 0), (0, 1), (1, 0), (1, 1)),
    3: ((0, 0), (1, 0), (1, 1), (2, 1)),
    4: ((0, 0), (1, 0), (1, -1), (2, -1)),
    5: ((0, 0), (1, 0), (1, 1), (2, 0)),
    6: ((0, 0), (1, 0), (2, 0), (2, 1)),
    7: ((0, 0), (0, 1), (1, 0), (2, 0))
}

# double-check
for k in t:
    t[k] = tuple(sorted(t[k]))

def rot(tetromino):
    temp = sorted(map(lambda x: (-x[1], x[0]), tetromino))
    minx = min(map(lambda x: x[0], temp))
    miny = min(map(lambda x: x[1], temp))
    return tuple(map(lambda x: (x[0] - minx, x[1] - miny), temp))

def check(m):
    for i in range(len(m[0])):
        j = 0
        while j < len(m) and m[j][i]:
            j += 1
        while j < len(m) and not m[j][i]:
            j += 1
        if j != len(m):
            return False
    return True

def can_put(m, h, tetromino, pos):
    m2 = deepcopy(m)
    try:
        cx, cy = pos - tetromino[0][0], h[pos] - tetromino[0][1]
        for x, y in tetromino:
            if m2[cy + y][cx + x]:
                return False
            m2[cy + y][cx + x] = 1
        return check(m2)
    except:
        return False

ans = set()
for i in range(c):
    tet = t[p]
    for _ in range(4):
        tet = rot(tet)
        if can_put(m, h, tet, i):
            ans.add((tet, i))
print(len(ans))
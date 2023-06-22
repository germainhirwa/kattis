import sys

def intersects(s1, s2):
    x1, y1, x3, y3 = s1
    x2, y2, x4, y4 = s2

    def on(x1, y1, x2, y2, x, y):
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)
    def ori(x1, y1, x2, y2, x3, y3):
        check = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
        if check > 0: return 1
        elif check < 0: return 2
        return 0

    o1 = ori(x1, y1, x3, y3, x2, y2)
    o2 = ori(x1, y1, x3, y3, x4, y4)
    o3 = ori(x2, y2, x4, y4, x1, y1)
    o4 = ori(x2, y2, x4, y4, x3, y3)

    return ((o1 != o2) and (o3 != o4)) or \
        ((o1 == 0) and on(x1, y1, x3, y3, x2, y2)) or \
        ((o2 == 0) and on(x1, y1, x3, y3, x4, y4)) or \
        ((o3 == 0) and on(x2, y2, x4, y4, x1, y1)) or \
        ((o4 == 0) and on(x2, y2, x4, y4, x3, y3))

n = -1
for line in sys.stdin:
    if n == -1:
        n = int(line)
        if n == 0: break
        s = []
    else:
        n -= 1
        s.append([*map(float, line.split())])
        if n == 0:
            n = -1
            m = len(s)
            t = 0
            for i in range(m):
                for j in range(i+1, m):
                    if intersects(s[i], s[j]):
                        for k in range(j+1, m): t += intersects(s[i], s[k]) and intersects(s[j], s[k])
            print(t)
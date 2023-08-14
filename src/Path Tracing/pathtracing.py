import sys
p = [(0, 0)]; x = y = 0
for l in sys.stdin:
    l = l.strip()
    if l[0] == 'd': y += 1
    elif l[0] == 'u': y -= 1
    elif l[0] == 'l': x -= 1
    else: x += 1
    p.append((x, y))
minx, maxx, miny, maxy = [f(t[i] for t in p) for i in range(2) for f in (min, max)]
m = [[' ']*(maxx-minx+3) for _ in range(maxy-miny+3)]
for i in range(len(m)): m[i][0] = m[i][-1] = '#'
for i in range(len(m[0])): m[0][i] = m[-1][i] = '#'
for x, y in p: m[y-miny+1][x-minx+1] = '*'
ax, ay = p[-1]
m[ay-miny+1][ax-minx+1] = 'E'
m[1-miny][1-minx] = 'S'
for w in m: print(''.join(w))
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pm = self

    def __gt__(self, other):
        point_min = self.pm
        o = orientation(point_min, self, other)
        if o == 0:
            return sq_dist(self, point_min) > sq_dist(other, point_min)
        if o == 1:
            return True
        return False

def double_area(p, q, r):
    return (p.y - q.y) * (q.x - r.x) - (q.y - r.y) * (p.x - q.x)

def sq_dist(p, q):
    return (p.y - q.y)**2 + (p.x - q.x)**2

def orientation(p, q, r):
    da = double_area(p, q, r)
    if da < 0:      return -1
    elif da > 0:    return 1
    return 0

def convex_hull(points):
    n = len(points)
    point_min = Point(float('inf'), float('inf'))
    ind = -1

    for i in range(n):
        if point_min.y > points[i].y:
            point_min.y, point_min.x = points[i].y, points[i].x
            ind = i
        elif point_min.y == points[i].y and point_min.x > points[i].x:
            point_min.x = points[i].x
            ind = i
    points[ind] = points[0]
    points[0] = point_min

    for p in points[1:]:
        p.pm = points[0]
    points = [points[0]] + sorted(points[1:])

    stack = [points[0]]
    for k in range(1, n - 1):
        if orientation(points[0], points[k], points[k + 1]) != 0:
            break

    stack.append(points[k])

    for i in range(k + 1, n):
        top = stack.pop()
        while stack and orientation(stack[-1], top, points[i]) >= 0:
            top = stack.pop()
        stack.extend([top, points[i]])

    return stack[::-1]

def rotating_caliper(points):
    n = len(points)
    if n == 1:
        return 0
    elif n == 2:
        return sq_dist(points[0], points[1])**0.5
    
    chull = convex_hull(points)
    n = len(chull)
    k = 1
    while abs(double_area(chull[n - 1], chull[0], chull[(k + 1) % n])) > abs(double_area(chull[n - 1], chull[0], chull[k])):
        k += 1

    res = 0
    i, j = 0, k
    while i <= k and j < n:
        res = max(res, sq_dist(chull[i], chull[j])**0.5)

        while j < n and abs(double_area(chull[i], chull[(i + 1) % n], chull[(j + 1) % n])) > abs(double_area(chull[i], chull[(i + 1) % n], chull[j])):
            res = max(res, sq_dist(chull[i], chull[(j + 1) % n])**0.5)
            j += 1
        i += 1

    return res

import sys
skip = input()
pts = []
for line in sys.stdin:
    pts.append(Point(*list(map(int, line.split()))))
print(rotating_caliper(pts))
from math import *
Bx, Cx, Cy = map(float, input().split())

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else ((x1, y1) if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
    elif d == e == 0: return (x3, y3) if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a*f != c*d or b*f != c*e: return None
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: return i1
                elif i1:                    return (i1, i2)
                else:                       return None

# convert sides to coordinates
A = (0, 0); B = (Bx, 0); C = (Cx, Cy)
a, b, c = dist(B, C), dist(C, A), dist(A, B)

# perimeter
p = a+b+c

# incenter
I = ((a*A[0]+b*B[0]+c*C[0])/p, (a*A[1]+b*B[1]+c*C[1])/p)

# midpoint
Ma, Mb = ((B[0]+C[0])/2, (B[1]+C[1])/2), ((A[0]+C[0])/2, (A[1]+C[1])/2)

# perpendicular bisector slope + segment
Pa, Pb = (B[0]-C[0], C[1]-B[1]), (A[0]-C[0], C[1]-A[1])
Ba, Bb = ((Ma[0]-100*Pa[1], Ma[1]-100*Pa[0]), (Ma[0]+100*Pa[1], Ma[1]+100*Pa[0])), ((Mb[0]-100*Pb[1], Mb[1]-100*Pb[0]), (Mb[0]+100*Pb[1], Mb[1]+100*Pb[0]))

# circumcenter
O = intersect(Ba, Bb)
R = dist(A, O)

# find angle w.r.t. O
aA = atan2(A[1]-O[1], A[0]-O[0])%(2*pi)
aB = atan2(B[1]-O[1], B[0]-O[0])%(2*pi)
aC = atan2(C[1]-O[1], C[0]-O[0])%(2*pi)
aP = ((aA+aB)/2 + pi*(aA>aB))%(2*pi)
aM = ((aB+aC)/2 + pi*(aB>aC))%(2*pi)
aN = ((aC+aA)/2 + pi*(aC>aA))%(2*pi)

# find coordinates of M, N, P
M = (O[0]+R*cos(aM), O[1]+R*sin(aM))
N = (O[0]+R*cos(aN), O[1]+R*sin(aN))
P = (O[0]+R*cos(aP), O[1]+R*sin(aP))

# find coordinates of E, F, G, H, J, K
E = intersect((N, P), (A, B))
F = intersect((N, P), (A, C))
G = intersect((N, M), (A, C))
H = intersect((N, M), (B, C))
J = intersect((M, P), (B, C))
K = intersect((M, P), (A, B))

# wrap-up
print(dist(E, F), dist(F, G), dist(G, H), dist(H, J), dist(J, K), dist(K, E))
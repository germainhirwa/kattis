from math import *
for _ in range(int(input())):
    p_in = [[*map(int, input().split())] for _ in range(int(input()))]
    p_out = [[*map(int, input().split())] for _ in range(int(input()))]
    p_in.append(p_in[0]), p_out.append(p_out[0])
    s_in = [*zip(p_in, p_in[1:])]
    s_out = [*zip(p_out, p_out[1:])]
    D = 1e9
    for x, y in p_in:
        for (x1, y1), (x2, y2) in s_out:
            a, b = x1-x2, y1-y2
            c = a*x+b*y
            d, e, f = y1-y2, x2-x1, y1*(x2-x1)-x1*(y2-y1)
            det = b*d-a*e # det != 0
            xi, yi = (b*f-c*e)/det, (c*d-a*f)/det
            if not (min(x1, x2) <= xi <= max(x1, x2) and min(y1, y2) <= yi <= max(y1, y2)): D = min(D, min(hypot(x-x1, y-y1), hypot(x-x2, y-y2)))
            else: D = min(D, hypot(x-xi, y-yi))
    print(D/2)
X, Y = input().split(); X, Y = [*map(int, X)], [*map(int, Y)]
m = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
chg = {(0, 8), (1, 7), (3, 9), (5, 6), (5, 9), (6, 8), (9, 8)}
move = {(0, 9), (0, 6), (6, 9), (9, 6), (6, 0), (9, 0), (2, 3), (3, 2), (3, 5), (5, 3)}
x = sum(m[i] for i in X)
y = sum(m[i] for i in Y)
z = [*zip(X, Y)]
if x != y: print('no')
elif sum(a!=b for a, b in z) < 3:
    diff = [(a, b) for a, b in z if a != b]
    if len(diff) == 1: print('yneos'[1-(diff[0] in move)::2])
    else: (a, b), (c, d) = diff; print('yneos'[1-(((a, b) in chg and (d, c) in chg) or ((b, a) in chg and (c, d) in chg))::2])
else: print('no')
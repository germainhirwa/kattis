import sys; input = sys.stdin.readline
R, C, ch = input().strip().split(); R, C, ch = int(R), int(C), ch[1]
m1 = [list(input().strip()) for _ in range(R)]; input()
m2 = [input() for _ in range(R)]
f1, f2 = set(), set()
mf = ((m1, f1), (m2, f2))
for i in range(R):
    for j in range(C):
        for m, f in mf:
            if m[i][j] != ch: m1[i][j] = m[i][j]
            else: f.add(i*C+j)
cmp = lambda x: (x//C,-x%C)
ul, ur, dl, dr, ul2, ur2, dl2, dr2 = min(f1), min(f1, key=cmp), max(f1, key=cmp), max(f1), min(f2), min(f2, key=cmp), max(f2, key=cmp), max(f2)
deltas = {i:sum((rc//C+i[0])*C+rc%C+i[1] in f2 for rc in f1) for i in ((ul2//C-ul//C,ul2%C-ul%C), (ur2//C-ur//C,ur2%C-ur%C), (dl2//C-dl//C,dl2%C-dl%C), (dr2//C-dr//C,dr2%C-dr%C))}
mv = max(deltas.values())
for (dr, dc), v in deltas.items():
    if v == mv: dr *= 2; dc *= 2; break
for rc in f1:
    r, c = rc//C+dr, rc%C+dc
    if 0<=r<R and 0<=c<C: m1[r][c] = ch
for i in m1: print(''.join(i))
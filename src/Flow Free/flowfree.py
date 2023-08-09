m = [[*input()] for _ in range(4)]
s = [(i, j) for i in range(4) for j in range(4) if m[i][j] == 'W']
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
r, g, b, y = [[4*i+j for i in range(4) for j in range(4) if m[i][j] == c] for c in 'RGBY']
if y:
    for c1 in 'RGBY':
        for c2 in 'RGBY':
            for c3 in 'RGBY':
                for c4 in 'RGBY':
                    for c5 in 'RGBY':
                        for c6 in 'RGBY':
                            for c7 in 'RGBY':
                                for c8 in 'RGBY':
                                    C = [c1, c2, c3, c4, c5, c6, c7, c8]
                                    R, G, B, Y = len(r)+C.count('R'), len(g)+C.count('G'), len(b)+C.count('B'), len(y)+C.count('Y')
                                    for c, (i, j) in zip(C, s): m[i][j] = c+'@'
                                    solvable = True
                                    for t, c, k in zip('RGBY', (r, g, b, y), (R, G, B, Y)):
                                        st = [(c[0], {c[0]})]; ss = 0
                                        while st:
                                            rc, p = st.pop()
                                            if rc == c[1]: ss = max(ss, len(p)); continue
                                            rr, cc = rc//4, rc%4
                                            for dr, dc in delta:
                                                if 0<=rr+dr<4 and 0<=cc+dc<4 and m[rr+dr][cc+dc][0] == t:
                                                    n = 4*(rr+dr)+cc+dc
                                                    if n not in p: st.append((n, p|{n}))
                                        if ss != k: solvable = False; break
                                    if solvable: print('solvable'), exit(0)
else:
    for c1 in 'RGB':
        for c2 in 'RGB':
            for c3 in 'RGB':
                for c4 in 'RGB':
                    for c5 in 'RGB':
                        for c6 in 'RGB':
                            for c7 in 'RGB':
                                for c8 in 'RGB':
                                    for c9 in 'RGB':
                                        for c10 in 'RGB':
                                            C = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
                                            R, G, B = len(r)+C.count('R'), len(g)+C.count('G'), len(b)+C.count('B')
                                            for c, (i, j) in zip(C, s): m[i][j] = c+'@'
                                            solvable = True
                                            for t, c, k in zip('RGB', (r, g, b), (R, G, B)):
                                                st = [(c[0], {c[0]})]; ss = 0
                                                while st:
                                                    rc, p = st.pop()
                                                    if rc == c[1]: ss = max(ss, len(p)); continue
                                                    rr, cc = rc//4, rc%4
                                                    for dr, dc in delta:
                                                        if 0<=rr+dr<4 and 0<=cc+dc<4 and m[rr+dr][cc+dc][0] == t:
                                                            n = 4*(rr+dr)+cc+dc
                                                            if n not in p: st.append((n, p|{n}))
                                                if ss != k: solvable = False; break
                                            if solvable: print('solvable'), exit(0)
print('not solvable')
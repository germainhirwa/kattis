s = [input().strip().split() for _ in range(6)]
for i in range(6):
    for j in range(6):
        s[i][j] = [*map(int, s[i][j].replace('-', '0').split('/'))]

def bt(r, c, idx, val):
    if r == 6:
        for rr in s:
            print(*(f'{i[0]}/{i[1]}' if len(i)==2 else i[0] for i in rr))
        exit(0)
    if c == 6: return bt(r+1, 0, 0, val)
    if idx == len(s[r][c]): return bt(r, c+1, 0, val)
    if idx == 1 and s[r][c][0] > val: return
    if s[r][c][idx] and s[r][c][idx] != val: return
    if s[r][c][idx]:
        for i in range(1, 10): bt(r, c, idx+1, i)
        return
    s[r][c][idx] = val
    rr = set(); cc = set(); sg = set(); ok = True
    for i in range(6):
        for j in range(len(s[r][i])):
            if s[r][i][j]:
                if s[r][i][j] not in rr: rr.add(s[r][i][j])
                else: ok = False; break
        if not ok: break
    if not ok: s[r][c][idx] = 0; return
    for i in range(6):
        for j in range(len(s[i][c])):
            if s[i][c][j]:
                if s[i][c][j] not in cc: cc.add(s[i][c][j])
                else: ok = False; break
        if not ok: break
    if not ok: s[r][c][idx] = 0; return
    for i in range(r//2*2, r//2*2+2):
        for j in range(c//3*3, c//3*3+3):
            for k in range(len(s[i][j])):
                if s[i][j][k]:
                    if s[i][j][k] not in sg: sg.add(s[i][j][k])
                    else: ok = False; break
        if not ok: break
    if not ok: s[r][c][idx] = 0; return
    for i in range(1, 10): bt(r, c, idx+1, i)
    s[r][c][idx] = 0
for i in range(1, 10): bt(0, 0, 0, i)
valid = [[(1, 3), (2, 5)], [(3, 6), (4, 8)], [(4, 7), (5, 9)], [(1, 0), (4, 5), (6, 10), (7, 12)], [(7, 11), (8, 13)], [(2, 0), (4, 3), (8, 12), (9, 14)], [(3, 1), (7, 8)], [(4, 2), (8, 9)], [(4, 1), (7, 6)], [(5, 2), (8, 7)], [(6, 3), (11, 12)], [(7, 4), (12, 13)], [(7, 3), (8, 5), (11, 10), (13, 14)], [(8, 4), (12, 11)], [(9, 5), (13, 12)]]
def backtrack(c, peg):
    s = ''.join(peg)
    if s in mem: return mem[s]
    branch = False
    for i in range(15):
        if peg[i] != '__': continue
        for j, k in valid[i]:
            if peg[j] != '__' and peg[k] != '__':
                branch = True
                old = peg[j]; peg[j] = '__'
                peg[i], peg[k] = peg[k], peg[i]
                t = backtrack(c, peg)
                peg[i], peg[k] = peg[k], peg[i]
                peg[j] = old
                if t: mem[s] = t; return t
    if not branch: mem[s] = peg.count(c) == 1 and peg.count('__') == 14; return mem[s]
    mem[s] = False; return False
import sys; input = sys.stdin.readline
while True:
    c = input().strip()
    if c == '**': break
    peg = []
    for _ in range(5):
        s = input().strip()
        for i in range(len(s)//2): peg.append(s[2*i]+s[2*i+1])
    mem = {}; print(['Impossible', 'Possible'][backtrack(c, peg)])
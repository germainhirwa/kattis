import sys

m = {}
def parse(t, i=0):
    if i == len(t): return None, i
    if t[i] == 'group':
        n, k, i = t[i+1], int(t[i+2]), i+3
        m[n] = set(t[i:i+k])
        return parse(t, i+k)
    if t[i] in m: return m[t[i]], i
    op = t[i]
    s1, i = parse(t, i+1)
    s2, i = parse(t, i+1)
    if op == 'union': s = s1 | s2
    if op == 'intersection': s = s1 & s2
    if op == 'difference': s = s1 - s2
    return s, i

for l in sys.stdin:
    r, _ = parse(l.strip().split())
    if r != None: print(*sorted(r))
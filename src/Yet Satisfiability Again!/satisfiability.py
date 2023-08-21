import sys; input = sys.stdin.readline
from array import array
for _ in range(int(input())):
    n, m = map(int, input().split()); sat = []
    for _ in range(m):
        c = input().strip().split(' v '); d = array('i', [0]*n); red = False
        for i in c:
            if i[0] == '~':
                k = int(i[2:])-1
                if d[k] == 0: d[k] = -1
                elif d[k] == 1: red = True; break
            else:
                k = int(i[1:])-1
                if d[k] == 0: d[k] = 1
                elif d[k] == -1: red = True; break
        if not red: sat.append(d)
    a = 0
    for i in range(1<<n):
        ok = 1
        for dd in sat:
            v = 0
            for j in range(n):
                if (dd[j] == 1 and i&(1<<j)) or (dd[j] == -1 and not i&(1<<j)): v = 1; break
            if not v: ok = 0; break
        if ok: a = 1; break
    print('un'*(1-a)+'satisfiable')
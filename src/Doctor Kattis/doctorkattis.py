import sys
from heapq import heappush, heappop

pq, m, nm, mn = [], {}, {}, {}
pqs, n = 0, 0
skip = input()
for line in sys.stdin:
    cmd = line.split()
    if cmd[0] == '0':
        name, lvl = cmd[1], int(cmd[2])
        m[name], nm[n], mn[name] = lvl, name, n
        heappush(pq, (-m[name], n))
        pqs += 1
        n += 1
    elif cmd[0] == '1':
        name, inc = cmd[1], int(cmd[2])
        m[name] = min(m[name] + inc, 100)
        heappush(pq, (-m[name], mn[name]))
    elif cmd[0] == '2':
        del m[cmd[1].strip()]
        pqs -= 1
    else:
        if pqs == 0:
            sys.stdout.write('The clinic is empty\n')
        else:
            while pq and nm[pq[0][1]] not in m:
                heappop(pq)
            sys.stdout.write(nm[pq[0][1]] + '\n')
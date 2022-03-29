import sys

input()
secs = [0] * 86400
jobs = 0
for line in sys.stdin:
    h, m, s = line.split()
    if h == '*':
        h = list(range(24))
    else:
        temp = []
        h = h.split(',')
        for i in h:
            i = i.split('-')
            if len(i) == 1:
                temp.append(int(i[0]))
            else:
                temp.extend(range(int(i[0]), int(i[1]) + 1))
        h = temp
    
    if m == '*':
        m = list(range(60))
    else:
        temp = []
        m = m.split(',')
        for i in m:
            i = i.split('-')
            if len(i) == 1:
                temp.append(int(i[0]))
            else:
                temp.extend(range(int(i[0]), int(i[1]) + 1))
        m = temp

    if s == '*':
        s = list(range(60))
    else:
        temp = []
        s = s.split(',')
        for i in s:
            i = i.split('-')
            if len(i) == 1:
                temp.append(int(i[0]))
            else:
                temp.extend(range(int(i[0]), int(i[1]) + 1))
        s = temp

    for h2 in h:
        for m2 in m:
            for s2 in s:
                jobs += 1
                secs[3600*h2 + 60*m2 + s2] = 1

print(sum(secs), jobs)
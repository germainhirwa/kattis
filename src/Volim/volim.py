import sys

fl = True
q = [i for i in range(1,9)]
t = 0

for line in sys.stdin:
    if fl:
        fl = False
        for i in range(int(line)-1):
            q.append(q.pop(0))
    else:
        s = line.strip().split()
        if len(s) == 2:
            t += int(s[0])
            if t >= 210:
                print(q[0])
                sys.exit(0)
            else:
                if s[1] == 'T':
                    q.append(q.pop(0))
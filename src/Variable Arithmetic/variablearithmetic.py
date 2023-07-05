import sys
h = {}
for l in sys.stdin:
    exp = l.strip().split()
    if exp == ['0']: break
    if len(exp) == 1:
        if exp[0] in h: print(h[exp[0]])
        elif exp[0].isnumeric(): print(int(exp[0]))
        else: print(exp[0])
    elif exp[1] == '=': h[exp[0]] = int(exp[2])
    else:
        v, s = [], 0
        for i in range(0, len(exp), 2):
            if exp[i] in h: s += h[exp[i]]
            elif exp[i].isnumeric(): s += int(exp[i])
            else: v.append(exp[i])
        if not v: print(s)
        elif s: print(s, '+', ' + '.join(v))
        else: print(' + '.join(v))
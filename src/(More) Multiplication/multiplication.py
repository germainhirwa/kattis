def create(a, b):
    r, c = len(str(a)), len(str(b))

    # Skeleton
    m = []
    m.append(list('+' + '-'*(4*r+3) + '+'))
    m.append(list('   '.join(['|', *str(a), '|'])))
    for j in range(c):
        m.append(list('| ' + '---'.join(['+']*(r+1)) + ' |'))
        for i in range(3):
            part = ' '*(2-i) + '/' + ' '*i
            m.append(list('| ' + part.join(['|']*(r+1)) + ' |'))
            if i == 1: m[-1][-2] = str(b)[j]
    m.append(list('| ' + '---'.join(['+']*(r+1)) + ' |'))
    m.append(list('   '.join(['|', *[' ']*r, '|'])))
    m.append(list('+' + '-'*(4*r+3) + '+'))

    # Populate numbers
    aa, bb = str(a), str(b)
    for i in range(r):
        for j in range(c): m[4*j+3][4*i+3], m[4*j+5][4*i+5] = str(int(aa[i])*int(bb[j])).zfill(2)

    # Sum them all
    carry = 0
    for i in range(r-1, -1, -1):
        curr = carry
        t = min(2*(r-i) - 1, 2*c)
        for j in range(t): curr += int(m[-4-2*j][4*i+5+2*j])
        m[-2][4*i+3] = str(curr%10)
        carry = curr//10
    for i in range(c-1, -1, -1):
        curr = carry
        t = min(2*i+1, 2*r)
        for j in range(t): curr += int(m[4*i+3-2*j][3+2*j])
        m[4*i+5][1] = str(curr%10)
        carry = curr//10

    # Clean-up
    z = True
    for i in range(c):
        if z:
            if m[4*i+5][1] == '0': m[4*i+5][1] = ' '
            else: z = False
    for i in range(r):
        if z:
            if m[-2][4*i+3] == '0': m[-2][4*i+3] = ' '
            else: z = False
    for i in range(c):
        if m[4*i+5][1] != ' ': m[4*i+7][1] = '/'
    for i in range(r-1):
        if m[-2][4*i+3] != ' ': m[-2][4*i+5] = '/'
    for r in m: print(''.join(r))

import sys
for l in sys.stdin:
    a, b = map(int, l.split())
    if a*b: create(a, b)
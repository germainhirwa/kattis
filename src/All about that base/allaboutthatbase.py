import string

D = dict(enumerate('0123456789' + string.ascii_lowercase)) # (35 -> 'z')
rev = dict((v, k) for (k, v) in D.items())
D[36] = D[0]

def convert(num, base):
    if base == 1 and list(set(num)) == ['1']:
        return len(num)
    s = 0
    for i in num:
        if rev[i] < base:
            s *= base
            s += rev[i]
        else:
            raise Exception
    return s

t = int(input())
for _ in range(t):
    x, op, y, eq, z = input().split()
    possible = []
    for b in range(1, 37):
        try:
            if eval(f'{convert(x, b)}{op}{convert(y, b)}=={convert(z, b)}'):
                possible.append(D[b])
        except:
            pass
    if not possible:
        print('invalid')
    else:
        print(''.join(possible))
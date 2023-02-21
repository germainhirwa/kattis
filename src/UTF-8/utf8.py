import sys
a, b, c, d = 0, 0, 0, 0
input()
try:
    for line in sys.stdin:
        line = line.strip()
        if line.startswith('0'):
            a += 1
        elif line.startswith('110'):
            b += 1
            for _ in range(1): assert input().startswith('10')
        elif line.startswith('1110'):
            c += 1
            for _ in range(2): assert input().startswith('10')
        elif line.startswith('11110'):
            d += 1
            for _ in range(3): assert input().startswith('10')
        else:
            raise Exception
except:
    print('invalid')
else:
    for i in [a, b, c, d]: print(i)
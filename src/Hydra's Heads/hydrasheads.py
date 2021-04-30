import sys

def moves(m,n):
    # There is always a move!
    r = 0
    while True:
        h = m + n//2
        if n % 2 == 0 and h % 2 == 0:
            r += (h + n)//2
            break
        else:
            r += 1
            n += 1
    return r

for line in sys.stdin:
    m,n = list(map(int,line.split(" ")))
    if m != 0 and n != 0:
        print(moves(m,n))
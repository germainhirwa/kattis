import sys
input()
for line in sys.stdin:
    n, s = line.strip().split()
    n = int(n)
    c, lr = len(s), [0, 0]
    for i in range(n):
        qt = c//4
        if qt == 0: break
        c -= qt
        lr[i%2] += qt
    print(s[lr[0]:len(s)-lr[1]])
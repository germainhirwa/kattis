import sys

for line in sys.stdin:
    m,p,l,e,r,s,n = list(map(int,line.split()))
    for _ in range(n):
        m,p,l = p//s, l//r, m*e
    print(m)
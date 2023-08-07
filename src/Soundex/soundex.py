'''
1 represents B, F, P, or V
2 represents C, G, J, K, Q, S, X,  or Z
3 represents D or T
4 represents L
5 represents M or N
6 represents R
'''
import sys, string
h = {'B': '1', 'C': '2', 'D': '3', 'L': '4', 'M': '5', 'R': '6', **{i: '' for i in 'AEIOUHWY'}}
for l in sys.stdin:
    l = l.strip()
    for i in 'FPV': l = l.replace(i, 'B')
    for i in 'GJKQSXZ': l = l.replace(i, 'C')
    l = l.replace('T', 'D').replace('N', 'M')
    while True:
        m = l
        for i in string.ascii_uppercase: m = m.replace(i*2, i)
        if l == m: break
        l = m
    print(''.join(h[i] for i in l))
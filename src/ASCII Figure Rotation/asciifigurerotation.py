def disp(w): [print(''.join(r).rstrip()) for r in w]
def rot90(w): return [[w[len(w)-1-i][j] for i in range(len(w))] for j in range(len(w[0]))]

import sys; input = sys.stdin.readline
h = 0
while (n:=int(input())):
    if h: print()
    w = [[*input().rstrip().replace('-', '@').replace('|', '-').replace('@', '|')] for _ in range(n)]
    c = max(map(len, w))
    for i in w: i.extend([' ']*(c-len(i)))
    disp(rot90(w)); h = 1
import sys; input = sys.stdin.readline
from copy import deepcopy
d = ((0, 1), (-1, 0), (1, 0), (0, -1))
l = {'R': 'P', 'P': 'S', 'S': 'R'}
for _ in range(int(input())):
    r, c, t = map(int, input().split())
    b = [[*input().strip()] for _ in range(r)]
    for _ in range(t):
        b2 = deepcopy(b)
        for i in range(r):
            for j in range(c):
                for di, dj in d:
                    if 0<=i+di<r and 0<=j+dj<c and b[i+di][j+dj] == l[b[i][j]]: b2[i][j] = b[i+di][j+dj]; break
        b = b2
    for w in b: print(''.join(w))
    print()
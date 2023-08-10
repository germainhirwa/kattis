import sys; input = sys.stdin.readline
from collections import deque
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))
while True:
    n = int(input())
    if n == 0: break
    m1 = []
    while True:
        s = [*map(int, input().split())]
        for i in range(len(s)//2): m1.append(2001*s[2*i]+s[2*i+1])
        if len(m1) == n: break
    m = int(input()); m2 = []
    while True:
        s = [*map(int, input().split())]
        for i in range(len(s)//2): m2.append(2001*s[2*i]+s[2*i+1])
        if len(m2) == m: break
    m2 = set(m2)
    q = deque(m1)
    D = [1e9]*(2001**2)
    for i in m1: D[i] = 0
    while q:
        rc = q.popleft()
        if rc in m2: print(D[rc]); break
        r, c = rc//2001, rc%2001
        for dr, dc in delta:
            if 0<=r+dr<2001 and 0<=c+dc<2001 and D[(nn:=2001*(r+dr)+c+dc)] == 1e9: D[nn] = D[rc]+1; q.append(nn)
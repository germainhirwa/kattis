from collections import deque
delta = ((0, -1), (0, 1), (-1, 0), (1, 0), (0, 0))
for _ in range(int(input())):
    s = [input().strip() for _ in range(3)]; s = [int(i=='*') for i in s[0]+s[1]+s[2]]
    q = deque([([0]*9, 0)]); vis = set()
    while q:
        b, d = q.popleft()
        if b == s: print(d); break
        t = tuple(b)
        if t in vis: continue
        vis.add(t)
        for i in range(9):
            bb = b.copy()
            r, c = i//3, i%3
            for dr, dc in delta:
                if 0<=r+dr<3 and 0<=c+dc<3: bb[3*(r+dr)+c+dc] = 1-b[3*(r+dr)+c+dc]
            q.append((bb, d+1))
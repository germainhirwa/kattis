from collections import deque
delta = [
    (-1, 0, {1:5, 2:2, 3:1, 4:4, 5:6, 6:3}),
    (1, 0, {1:3, 2:2, 3:6, 4:4, 5:1, 6:5}),
    (0, 1, {1:4, 2:1, 3:3, 4:6, 5:5, 6:2}),
    (0, -1, {1:2, 2:6, 3:3, 4:1, 5:5, 6:4})
]
for _ in range(int(input())):
    n = int(input())
    m = list([*input().strip()] for _ in range(n))
    for i in range(n):
        for j in range(n):
            if m[i][j] == 'S': sr, sc = i, j
            if m[i][j] == 'H': hr, hc = i, j
    q, can, v = deque([(sr, sc, 2)]), 0, set()
    while q:
        if q[0] == (hr, hc, 6): can = 1; break
        rr, cc, wif = q.popleft()
        for dr, dc, mp in delta:
            if 0<=rr+dr<n and 0<=cc+dc<n and m[rr+dr][cc+dc] != '*':
                new = (rr+dr, cc+dc, mp[wif])
                if new not in v: v.add(new), q.append(new)
    print(['No', 'Yes'][can])
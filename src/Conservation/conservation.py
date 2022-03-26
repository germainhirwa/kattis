import sys
from collections import deque

for _ in range(int(input())):
    v, e = map(int, input().split())
    g = {}
    indeg = [0] * v
    pos = list(map(int, input().split()))
    if e != 0:
        for line in sys.stdin:
            e -= 1
            a, b = map(int, line.split())
            a -= 1
            b -= 1
            if a not in g:
                g[a] = set()
            g[a].add(b)
            indeg[b] += 1
            if e == 0:
                break

    indeg2 = indeg.copy()
    one1, two1, one2, two2 = deque([]), deque([]), deque([]), deque([])
    for i in range(v):
        if indeg[i] == 0:
            [one1, two1][pos[i] - 1].append(i)
            [one2, two2][pos[i] - 1].append(i)

    curr, switch1 = 1, 0
    while one1 or two1:
        if not [one1, two1][curr - 1]:
            curr = 3 - curr
            switch1 += 1

        u = [one1, two1][curr - 1].popleft()

        if u in g:
            for w in g[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    [one1, two1][pos[w] - 1].append(w)

    curr, switch2 = 2, 0
    while one2 or two2:
        if not [one2, two2][curr - 1]:
            curr = 3 - curr
            switch2 += 1

        u = [one2, two2][curr - 1].popleft()

        if u in g:
            for w in g[u]:
                indeg2[w] -= 1
                if indeg2[w] == 0:
                    [one2, two2][pos[w] - 1].append(w)

    print(min(switch1, switch2))
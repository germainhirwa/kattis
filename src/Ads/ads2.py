# Using BFS, much faster
import sys
from collections import deque
r, c = map(int, input().split())

m = []
for line in sys.stdin:
    m.append(list(line.strip('\n\r')))
    m[-1].extend([' '] * (c - len(m[-1])))
ads = set()

rem = []
graph = {}

# All the first cell of the images
pos = c + 1
for i in range(1, r):
    for j in range(1, c):
        if m[i - 1][j - 1] == m[i - 1][j] == m[i][j - 1] == '+':
            graph[pos] = {pos - 1, pos - c, pos - c - 1} # first cell -> boundary
            ads |= graph[pos]
            ads.add(pos)
            for p in graph[pos]: # boundary -> first cell
                graph[p] = {pos}
        pos += 1
    pos += 1

# Four corners + redundant fellow boundary
pos = 0
for i in range(r):
    for j in range(c):
        if m[i][j] == '+' and 0 <= i - 1 and i + 1 < r and 0 <= j - 1 and j + 1 < c:
            if (m[i][j - 1] == '+' and m[i - 1][j] == '+') or \
                (m[i - 1][j] == '+' and m[i][j + 1] == '+') or \
                (m[i][j + 1] == '+' and m[i + 1][j] == '+') or \
                (m[i + 1][j] == '+' and m[i][j - 1] == '+'):
                for dest in (pos + 1, pos - 1, pos + c, pos - c):
                    if dest not in graph:
                        graph[dest] = set()
                    graph[dest].add(pos) # outside/boundary -> boundary
                    if dest in ads:
                        ads.add(pos)
        pos += 1

# Everything else
pos = 0
for i in range(r):
    for j in range(c):
        curr = m[i][j]
        if not (65 <= ord(curr) <= 90 or 97 <= ord(curr) <= 122 or curr in '0123456789?!,. ') and curr != '+':
            rem.append(pos)
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (0 <= i + dr < r) and (0 <= j + dc < c):
                dest = c*(i + dr) + (j + dc)
                if not ((curr == '+') ^ (m[i + dr][j + dc] == '+')):
                    if pos not in graph:
                        graph[pos] = set()
                    graph[pos].add(dest)
                    if pos in ads:
                        ads.add(dest)
        pos += 1

vis = set(rem)
rem = deque(rem)
while rem:
    s = rem.popleft()
    if s not in ads:
        continue
    m[s // c][s % c] = ' '
    if s in graph:
        for v in graph[s]:
            if v not in vis and s in ads:
                rem.append(v)
                vis.add(v)

for i in range(r):
    print(''.join(m[i]))
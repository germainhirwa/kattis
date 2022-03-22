import sys
r, c = map(int, input().split())
sys.setrecursionlimit(60000)

m = []
for line in sys.stdin:
    m.append(list(line.strip('\n\r')))
    while len(m[-1]) != c:
        m[-1].append(' ')
web = [True] * (r*c)

def safe(char):
    return 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or char in '0123456789?!,. '

rem = []
graph = {}

# All the first cell of the images
for i in range(1, r):
    for j in range(1, c):
        pos = c*i + j
        if m[i - 1][j - 1] == m[i - 1][j] == m[i][j - 1] == '+':
            web[pos] = web[pos - 1] = web[pos - c] = web[pos - c - 1] = False
            graph[pos] = {pos - 1, pos - c, pos - c - 1} # first cell -> boundary
            for p in (pos - 1, pos - c, pos - c - 1): # boundary -> first cell
                graph[p] = {pos}

# Four corners + redundant fellow boundary
for i in range(r):
    for j in range(c):
        pos = c*i + j
        if m[i][j] == '+' and 0 <= i - 1 and i + 1 < r and 0 <= j - 1 and j + 1 < c:
            if (m[i][j - 1] == '+' and m[i - 1][j] == '+') or \
                (m[i - 1][j] == '+' and m[i][j + 1] == '+') or \
                (m[i][j + 1] == '+' and m[i + 1][j] == '+') or \
                (m[i + 1][j] == '+' and m[i][j - 1] == '+'):
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr + dc != 0 and dr * dc == 0:
                            dest = c*(i + dr) + (j + dc)
                            if dest not in graph:
                                graph[dest] = set()
                            graph[dest].add(pos) # outside/boundary -> boundary
                            web[pos] &= web[dest]

# Everything else
for i in range(r):
    for j in range(c):
        pos = c*i + j
        curr = m[i][j]
        if not safe(curr) and curr != '+':
            rem.append(pos)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr + dc != 0 and dr * dc == 0:
                    if (0 <= i + dr < r) and (0 <= j + dc < c):
                        adj = m[i + dr][j + dc]
                        dest = c*(i + dr) + (j + dc)
                        if not ((curr == '+') ^ (adj == '+')):
                            if pos not in graph:
                                graph[pos] = set()
                            graph[pos].add(dest)
                            web[dest] &= web[pos]

vis = set()
def DFS(s):
    vis.add(s)
    if web[s]:
        return
    m[s // c][s % c] = ' '
    if s in graph:
        for v in graph[s]:
            if v not in vis:
                DFS(v)

for i in rem:
    if i not in vis:
        DFS(i)

for i in range(r):
    print(''.join(m[i]))
class Pair:
    def __init__(self, v, w):
        self.first = v
        self.second = w

    def __str__(self):
        return "<" + str(self.first) + "," + str(self.second) + ">"

    def __repr__(self):
        return self.__str__()

class Graph:
    def __init__(self, V, dir):
        self.list = []
        for _ in range(V):
            self.list.append([].copy())
        self.num_vertices = V
        self.directed = dir

        # dummy values
        self.parent = [-1]*V
        self.visited = [0]*V
        self.depth = [-1]*V

    def connect(self, a, b, w = 1):
        self.list[a].append(Pair(b, w))
        if not self.directed:
            self.list[b].append(Pair(a, w))

    def BFS(self, s):
        self.visited = [0]*self.num_vertices

        q = []
        q.append(s)
        self.visited[s] = 1
        self.depth[s] = 0

        while q:
            u = q.pop(0)
            for i in range(len(self.list[u])):
                if self.visited[self.list[u][i].first] == 0:
                    self.visited[self.list[u][i].first] = 1
                    self.depth[self.list[u][i].first] = self.depth[u] + 1
                    q.append(self.list[u][i].first)

    def shortest_path_length(self, v):
        return self.depth[v]

import sys
n = int(input())
m = []
for line in sys.stdin:
    m.append(line.strip())

def knight(r, c):
    res = []
    for i in [-2, -1, 1, 2]:
        for j in [-2, -1, 1, 2]:
            if abs(i) + abs(j) == 3:
                res.append((r + i, c + j))
    return res

g = Graph(n**2, False)
for i in range(n):
    for j in range(n):
        if m[i][j] == 'K':
            source = i * n + j
        if m[i][j] != '#':
            for r, c in knight(i, j):
                if r in range(n) and c in range(n) and m[r][c] != '#':
                    g.connect(r*n + c, i*n + j)
g.BFS(source)
print(g.shortest_path_length(0))
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

n = int(input())
for _ in range(n):
    n_buttons, target = list(map(int, input().split()))
    buttons = list(map(int, input().split()))
    
    graph = Graph(3601, True)
    for i in range(3601):
        for j in buttons:
            graph.connect(i, min(max(i + j, 0), 3600))
    graph.BFS(0)
    for i in range(target, 3601):
        if graph.shortest_path_length(i) != -1:
            print(graph.shortest_path_length(i), i - target)
            break

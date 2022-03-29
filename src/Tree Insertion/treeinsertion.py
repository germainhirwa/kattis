class Vertex:
    def __init__(self, v):
        self.key = v
        self.left, self.right, self.parent = None, None, None
        self.size = 1

class BST:
    def __init__(self):
        self.root = None

    def sz(self, t):
        if not t:
            return 0
        return t.size

    def insert(self, v):
        def helper(t, v):
            if t == None: # tree is empty
                return Vertex(v)

            if t.key <= v:
                t.right = helper(t.right, v)
                t.right.parent = t
            else:
                t.left = helper(t.left, v)
                t.left.parent = t

            t.size += 1
            return t

        self.root = helper(self.root, v)

    def count(self):
        def C(n, k):
            res = 1
            for i in range(min(k, n - k)):
                res *= n - i
                res //= i + 1
            return res

        def helper(t):
            if not t:
                return 1
            return helper(t.left) * helper(t.right) * C(self.sz(t.left) + self.sz(t.right), self.sz(t.right))
        return helper(self.root)

while True:
    n = int(input())
    if n == 0:
        break
    bst = BST()
    for i in map(int, input().split()):
        bst.insert(i)
    print(bst.count())
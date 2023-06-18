class Node:
    def __init__(self, par):
        self.par = par
        self.children = []

def encode(s):
    p = 0
    curr = Node('.')
    for i in s:
        if int(i):
            curr = curr.par
        else:
            curr.children.append(Node(curr))
            curr = curr.children[-1]
    def get_children(node):
        return [len(node.children), sorted(get_children(child) for child in node.children)]
    t = get_children(curr)
    return t

for _ in range(int(input())):
    print(['different', 'same'][encode(input().strip()) == encode(input().strip())])
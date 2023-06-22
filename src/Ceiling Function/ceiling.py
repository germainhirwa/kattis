class Node:
    def __init__(self, val):
        self.val, self.r, self.l = val, None, None

def inorder(t):
    if not t: return []
    r = []
    for i in inorder(t.l): r.append(i)
    r.append(t.val)
    for i in inorder(t.r): r.append(i)
    return r

def eq(t1, t2):
    if not t1 and not t2: return True
    elif bool(t1)^bool(t2): return False
    return eq(t1.l, t2.l) and eq(t1.r, t2.r)

n, k = map(int, input().split())
t = []
for _ in range(n):
    c = None
    for i in map(int, input().split()):
        if c == None: c = Node(i)
        else:
            ptr = c
            while ptr:
                if ptr.val <= i:
                    if ptr.r: ptr = ptr.r
                    else: ptr.r = Node(i); break
                else:
                    if ptr.l: ptr = ptr.l
                    else: ptr.l = Node(i); break
    t.append(c)
s = [t[0]]
for i in range(1, len(t)):
    new = True
    for j in s:
        if eq(t[i], j): new = False
        if not new: break
    if new: s.append(t[i])
print(len(s))
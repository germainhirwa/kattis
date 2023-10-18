from array import *
class UFDS:
    def __init__(self, N):
        self.p = array('i', [*range(N)]); self.rank = array('i', [0]*N)
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

w = input().strip()
p = [[] for _ in range(2*len(w.split())+1)]
pos, ptr = 0, 1
while pos < len(w):
    if w[pos] not in ',. ': p[ptr].append(w[pos]); pos += 1
    else:
        ptr += 1
        while pos < len(w) and w[pos] in ',. ': p[ptr].append(w[pos]); pos += 1
        ptr += 1
p = [*map(lambda x: ''.join(x).strip(), p)]; oc = {}
for i in range(len(p)):
    if p[i] and p[i] not in ',.':
        if p[i] not in oc: oc[p[i]] = []
        oc[p[i]].append(i)
u = UFDS(len(p)//2+1); cc = {}; s = set(); rev = array('i', [-1]*(len(p)//2+1))
for i in oc:
    for j in oc[i]:
        if p[j-1] != '.':
            for k in oc[i]:
                if p[k-1] != '.': u.union((j-1)//2, (k-1)//2)
            break
    for j in oc[i]:
        if p[j+1] != '.':
            for k in oc[i]:
                if p[k+1] != '.': u.union((j+1)//2, (k+1)//2)
            break
for i in range(len(p)//2+1):
    rep = u.find(i)
    if rep not in cc: cc[rep] = []
    cc[rep].append(i)
for i in cc:
    for j in cc[i]: rev[j] = i
for i in range(0, len(p), 2):
    if p[i] == ',': s.add(rev[i//2])
for i in s:
    for j in cc[i]:
        if p[2*j] != '.': p[2*j] = ','
for i in range(1, len(p), 2): p[i] += p[i+1]
print(' '.join(p[1::2]))
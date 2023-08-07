from collections import Counter
a, k = input().split(); b = input(); k = int(k)
c = Counter(); d = Counter()
pos = 0
while pos < len(a):
    if a[pos].isalpha():
        mol = a[pos]
        pos2 = pos+1; m = 0
        while pos2 < len(a) and a[pos2].isnumeric(): m *= 10; m += int(a[pos2]); pos2 += 1
        pos = pos2
        c[mol] += (m or 1)*k
pos = 0
while pos < len(b):
    if b[pos].isalpha():
        mol = b[pos]
        pos2 = pos+1; m = 0
        while pos2 < len(b) and b[pos2].isnumeric(): m *= 10; m += int(b[pos2]); pos2 += 1
        pos = pos2
        d[mol] += m or 1
best = 1e9
for mm in d: best = min(best, c[mm]//d[mm])
print(best)
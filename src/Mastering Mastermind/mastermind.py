from collections import Counter
r = s = 0; n, a, b = input().split(); n = int(n); aa = Counter(); bb = Counter()
for i in range(n): r += a[i] == b[i]; aa[a[i]] += 1; bb[b[i]] += 1
for k in {**aa, **bb}: s += min(aa[k], bb[k])
print(r, s-r)
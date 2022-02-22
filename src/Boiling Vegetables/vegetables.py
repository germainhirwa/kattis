from math import ceil
import sys

T, N = list(map(float, input().split()))
N = int(N)
w = list(map(int, input().split()))

lgsarr = []
for b in range(500):
    for i in range(N):
        lgsarr.append(w[i] / (b + 1))
lgsarr.sort(reverse=True)

for largest in lgsarr:
    c = 0
    smallest = largest
    for j in range(N):
        cuts = int(ceil(w[j] / largest))
        c += cuts - 1
        smallest = min(smallest, w[j] / cuts)
    if smallest / largest > T:
        print(c)
        sys.exit(0)
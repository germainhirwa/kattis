import sys; input = sys.stdin.readline
from collections import Counter
for _ in range(int(input())):
    n, s = int(input()), input().strip()
    c = Counter(s); u = set(); r = d = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] not in u: u.add(s[i]); r += (d-len(s)+1+i)*c[s[i]]; d += c[s[i]]
    print(5*r)
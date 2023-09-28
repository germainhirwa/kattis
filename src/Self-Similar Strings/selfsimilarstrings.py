import sys
from collections import Counter
for s in sys.stdin:
    s = s.strip()
    for d in range(len(s)-1, -1, -1):
        if min(Counter(s[i:i+d] for i in range(len(s)-d+1)).values()) > 1: print(d); break
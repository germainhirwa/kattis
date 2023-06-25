import sys
from collections import Counter
trees = Counter(t.strip() for t in sys.stdin)
total = sum(trees.values())
for i, j in sorted(trees.items()): print(i, 100*j/total)
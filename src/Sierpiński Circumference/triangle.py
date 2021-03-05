import sys
from math import *

i = 1
for line in sys.stdin:
    print(f'Case {i}: {ceil(int(line)*log10(1.5)+log10(3))}')
    i += 1
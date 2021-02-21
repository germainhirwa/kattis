# Trying sys, from Kattis's documentation
# https://open.kattis.com/help/python3

import sys
 
for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    print(abs(a-b))
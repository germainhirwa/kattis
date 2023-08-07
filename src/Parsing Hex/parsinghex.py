import sys, re
for l in sys.stdin:
    for h in re.findall('0[xX][0-9a-fA-F]+', l): print(h, int(h, 16))
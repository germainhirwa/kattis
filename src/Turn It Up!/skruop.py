import sys

vol = 7
skip = input()
for line in sys.stdin:
    if line.find('op') == -1:
        vol = max(0, vol - 1)
    else:
        vol = min(10, vol + 1)
print(vol)
import sys
input()

b = 0
h = 0
for line in sys.stdin:
    h += int(line)
    b = min(b, h)
print(max(0, -b))
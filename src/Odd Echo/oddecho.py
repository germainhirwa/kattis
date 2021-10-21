import sys

t = 0
for line in sys.stdin:
    if t % 2:
        print(line)
    t += 1
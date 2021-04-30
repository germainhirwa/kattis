import sys

c = 1

for line in sys.stdin:
    c *= line.count("S")

print("S("*c+"0"+")"*c)
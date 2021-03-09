import sys

for line in sys.stdin:
    k = int(line)
    while k*(3*k+1) % 8 != 0:
        k += 1
    print(k)
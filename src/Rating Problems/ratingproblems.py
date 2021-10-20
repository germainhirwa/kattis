import sys

s = 0

for line in sys.stdin:
    try:
        n,k = list(map(int,line.split()))
    except:
        s += int(line)

print((s-3*(n-k))/n,(s+3*(n-k))/n)
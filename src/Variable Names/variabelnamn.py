import sys

q = int(input())
memo = [1] * 10001
memo2 = set()
for line in sys.stdin:
    i = int(line)
    j = memo[i]
    while j*i in memo2:
        j += 1
    memo2.add(j*i)
    memo[i] = j
    print(j*i)
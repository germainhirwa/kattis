import sys

n = int(input())
arr = [0] * 1001
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    for i in range(a, b + 1):
        arr[i] += 1
print(['edward is right', 'gunilla has a point'][int(n in arr)])
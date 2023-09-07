import sys; input = sys.stdin.readline
a = 0
for _ in range(int(input())):
    p, q = map(int, input().split())
    a += p
    if a < q: print('impossible'), exit(0)
print('possible')
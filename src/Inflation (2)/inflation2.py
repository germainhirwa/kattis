import sys; input = sys.stdin.readline
from collections import Counter
N = int(input()); F = Counter(map(int, input().split()))
offset = 0; ans = sum(i*j for i,j in F.items())
Q = int(input())
for _ in range(Q):
    cmd = input().split()
    if cmd[0][0] == 'I': x = int(cmd[1]); offset += x; ans += N*x
    elif (x:=int(cmd[1])) != (y:=int(cmd[2])): F[y-offset] += F[x-offset]; ans += (y-x)*F[x-offset]; F[x-offset] = 0
    print(ans)
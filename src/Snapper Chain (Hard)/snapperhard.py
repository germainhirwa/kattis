import sys; input = sys.stdin.readline
for t in range(int(input())):
    n, k = map(int, input().split())
    print(f'Case #{t+1}:', ['OFF', 'ON'][(k+1)%(1<<n)==0])
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input()); l = 1; ans = 0
    for i in [*map(int, input().split())]:
        if i == l: l += 1
        else: ans += 1
    print(ans)
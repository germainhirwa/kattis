import sys; input = sys.stdin.readline
for _ in range(int(input())):
    t = sorted(sum([*map(int, input().split())][1:]) for _ in range(int(input())))
    tot = curr = 0
    for d in t: curr += d; tot += curr
    print(tot/len(t))
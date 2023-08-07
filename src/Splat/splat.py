import sys; input = sys.stdin.readline
from math import pi
for _ in range(int(input())):
    p = [[*map(float, (l:=input().split())[:-1]), l[-1]] for _ in range(int(input()))][::-1]
    for _ in range(int(input())):
        x, y = map(float, input().split()); ans = 'white'
        for xc, yc, v, c in p:
            if (xc-x)**2 + (yc-y)**2 <= v/pi: ans = c; break
        print(ans)
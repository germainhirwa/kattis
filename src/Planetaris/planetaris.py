import sys; input = sys.stdin.readline
n, a = map(int, input().split())
e = sorted(map(int, input().split()))
curr = ans = 0
for i in e:
    if curr+i+1 <= a: curr += i+1; ans += 1
print(ans)
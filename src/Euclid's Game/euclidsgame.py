import sys
sys.setrecursionlimit(10**5)

def solve(a, b, t=1):
    if a < b: a, b = b, a
    if b == 0: return 1-t
    if a%b == a-b: return solve(a-b, b, 1-t)
    return t

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == b == 0: break
    print('OSltlaine'[solve(a, b)::2], 'wins')
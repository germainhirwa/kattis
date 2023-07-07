import sys; input = sys.stdin.readline
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def lcm(a, b):
    return (a*b)//gcd(a, b)
while True:
    n = int(input())
    if n == 0: break
    lo, hi, div = 1, 1e9, 1
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'divisible':   div = lcm(div, int(cmd[2]))
        if cmd[0] == 'greater':     lo = max(lo, int(cmd[2])+1)
        if cmd[0] == 'less':        hi = min(hi, int(cmd[2])-1)
    if hi == 1e9: print('infinite'); continue
    lo = (1+(lo-1)//div)*div
    if hi < lo: print('none')
    else: print(*range(lo, hi+1, div))
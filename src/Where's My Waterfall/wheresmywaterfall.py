import sys; input = sys.stdin.readline; sys.setrecursionlimit(2500)
n, m, k = map(int, input().split())
p = [*map(int, input().split())]
v = [[*input().strip()] for _ in range(n)]
v.insert(0, ['O']*m)
def fill(r, c):
    if r >= n+1 or c < 0 or c >= m or v[r][c] == '~': return
    v[r][c] = '~'
    if r < n and v[r+1][c] in '#?':
        if c > 0 and v[r][c-1] == 'O': fill(r, c-1)
        if c < m-1 and v[r][c+1] == 'O': fill(r, c+1)
    else: fill(r+1, c)
for i in p: fill(0, i)
for rr in v[1:]: print(''.join(rr))
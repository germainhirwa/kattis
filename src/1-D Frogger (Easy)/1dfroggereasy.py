n, s, m = map(int, input().split())
a = list(map(int, input().split()))
v = set()
def trav(u, d=0):
    if u < 0: return f'left\n{d}'
    if u >= n: return f'right\n{d}'
    if a[u] == m: return f'magic\n{d}'
    if u in v: return f'cycle\n{d}'
    v.add(u)
    return trav(u+a[u], d+1)
print(trav(s-1))
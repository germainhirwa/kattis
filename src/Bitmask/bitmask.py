s = ''.join(str(1-int(i)) for i in input().strip()); n = len(s)
c = [*map(int, input().split())]; a = [1e9]
def f(ss, u, cc):
    if cc >= a[0]: return
    if len(ss) == n: a[0] = min(a[0], cc); return
    cs = ''
    for i in range(len(ss), n):
        cs += s[i]
        if cs not in u: u.add(cs), f(ss+cs, u, cc+c[i-len(ss)]), u.discard(cs)
        else: f(ss+cs, u, cc)
for i in range(n): f(s[:i+1], {s[:i+1]}, c[i])
print(a[0])
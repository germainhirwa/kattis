s, n, m = map(int, input().split())
a = []
while len(a) != s: a.extend(map(int, input().split()))
b = [-i for i in a]; p = v = 0 
for i in range(s):
    u = d = 1; ui = di = i
    while ui > 0 and a[ui-1] > a[ui]: ui -= 1; u += 1
    while di < s-1 and a[di+1] > a[di]: di += 1; d += 1
    if u >= m and d >= m: v += 1
    u = d = 1; ui = di = i
    while ui > 0 and b[ui-1] > b[ui]: ui -= 1; u += 1
    while di < s-1 and b[di+1] > b[di]: di += 1; d += 1
    if u >= n and d >= n: p += 1
print(p, v)
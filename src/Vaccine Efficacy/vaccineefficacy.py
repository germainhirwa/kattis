r, p = {i:0 for i in 'ABCD'}, {i:0 for i in 'ABCD'}
m = {'Y': r, 'N': p}
for _ in range(int(input())):
    i, a, b, c = input().strip()
    for s, v in zip([a, b, c], 'ABC'): m[i][v] += s == 'Y'
    m[i]['D'] += 1
for i in 'ABC':
    v = 100-100*(r[i]*p['D'])/(r['D']*p[i])
    print(v if v > 0 else 'Not Effective')
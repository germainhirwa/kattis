from math import comb
n, k, p = map(float, input().split()); n = round(n); k = round(k)
pp = []; cp = [0]; ans = 0
for i in range(1, 1001): pp.append(comb(i-1, k-1)*p**(i-k)*(1-p)**k)
for i in range(len(pp)): cp.append(cp[-1]+pp[i])
for i in range(1000): ans += pp[i]*cp[i]**(n-1)
print(1-n*ans)
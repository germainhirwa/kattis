import sys; input = sys.stdin.readline
from collections import defaultdict
sup = lambda: defaultdict(int)
MOD = 10**9+7

def pow(mat, n):
    if n == 1: return mat
    if n % 2: return mul(pow(mat, n-1), mat)
    return pow(mul(mat, mat), n//2)

def mul(a, b):
    c = defaultdict(sup)
    for i in a:
        for k in a[i]:
            if k not in b: continue
            for j in b[k]: c[i][j] += a[i][k]*b[k][j]; c[i][j] %= MOD
    return c

mat = defaultdict(sup)
mat[0][0] = 2; mat[0][1] = 6; mat[0][3] = -1; mat[1][0] = mat[2][1] = mat[3][2] = 1
res = pow(mat, int(input()))
ans = (res[3][0]*63 + res[3][1]*17 + res[3][2]*5 + res[3][3]) % MOD
print(ans)
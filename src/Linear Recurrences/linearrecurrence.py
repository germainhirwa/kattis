import sys

n = int(input())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

eye = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    eye[i][i] = 1
mat = [[1]+[0]*n]
for i in range(n-1):
    mat.append([0]*(n+1))
    mat[-1][i+2] = 1
mat.append([a[0]] + a[1:][::-1])

def mult(a, b, mod):
    m, n, p = len(a), len(a[0]), len(b[0])
    mat = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                mat[i][k] += a[i][j]*b[j][k]
                mat[i][k] %= mod
    return mat

def pow(mat, n, m):
    if n == 0: return eye
    if n % 2: return mult(mat, pow(mat, n-1, m), m)
    else:
        tmp = pow(mat, n//2, m)
        return mult(tmp, tmp, m)

def x(t, m):
    if t < n: return q[t] % m
    A = pow(mat, t+1-n, m)[-1]
    r = A[0]
    for i in range(n): r = (r + q[i]*A[i+1]) % m
    return r

input()
for line in sys.stdin:
    t, m = map(int, line.split())
    print(x(t, m))
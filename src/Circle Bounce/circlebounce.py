a, b, n = map(int, input().split()); M = 10**9+7
def matexp(m, n):
    if n == 1: return m
    (a, b), (c, d) = m
    if n % 2: (a2, b2), (c2, d2) = matexp(m, n-1); return (((a*a2+b*c2)%M, (a*b2+b*d2)%M), ((c*a2+d*c2)%M, (c*b2+d*d2)%M))
    else: return matexp((((a*a+b*c)%M, (a*b+b*d)%M), ((c*a+d*c)%M, (c*b+d*d)%M)), n//2)
print(-matexp(((a*a-b*b, 2*a*b), (-2*a*b, a*a-b*b)), n+1)[0][0]*pow(a*a+b*b, -n-1, M)%M)
import sys; input = sys.stdin.readline
from array import array
def f(x): return max((x-xx)**2+yy**2 for xx, yy in p)
while (n:=int(input())):
    p = [array('d', [*map(float, input().split())]) for _ in range(n)]; input()
    a, b = -2*10**5, 2*10**5; gr = (5**0.5-1)/2; tol = 1e-6
    while b-a>tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        if f(μ) > f(λ): b = μ
        else: a = λ
    ans = (a+b)/2; print(ans, f(ans)**0.5)
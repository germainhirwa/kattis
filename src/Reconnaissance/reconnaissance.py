import sys; input = sys.stdin.readline
n = int(input()); w = [[*map(int, input().split())] for _ in range(n)]
def f(t): s = [x+t*v for x, v in w]; return max(s)-min(s)
a, b = 0, 2e10; gr = (5**0.5-1)/2; tol = 1e-4
while b-a>tol:
    λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
    if f(μ) > f(λ): b = μ
    else: a = λ
print(f((a+b)/2))
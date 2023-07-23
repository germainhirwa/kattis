def golden(a0, b0, f, tol):
    gr = (5**0.5-1)/2
    t, a, b = 0, a0, b0
    while b - a > tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        if f(μ) > f(λ): b = μ
        else:           a = λ
        t += 1
    return (a+b)/2

mem = {}
def qanat(h, n):
    mem[0] = [(1+h)**2/4, []]
    def dist(x): return (h*x+h+1-x)**2/4-(h*x)**2/2
    for i in range(1, n+1): f = lambda x: [dist(x)+mem[i-1][0]*x**2, [i*x for i in mem[i-1][1]]+[x]]; mem[i] = f(golden(0, 1, f, 1e-10))
    return mem[n]

w, h, n = map(int, input().split()); c, p = qanat(h/w, n)
print(c*w*w)
for i in [i*w for i in p][:10]: print(i)
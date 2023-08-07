h, r, da, dw = map(int, input().split())

def golden(a0, b0, f, tol):
    gr = (5**0.5-1)/2
    t, a, b = 0, a0, b0
    while b - a > tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        if f(μ) > f(λ): b = μ
        else:           a = λ
        t += 1
    return (a+b)/2

print(golden(0, h, lambda x: ((dw-da)*x*x+h*h*da)/((dw-da)*x+h*da), 1e-10))
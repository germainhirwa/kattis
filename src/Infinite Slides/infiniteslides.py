from math import *
w = float(input())
def f(t): return hypot(1+cos(t)-cos(t+w), sin(w+t)-sin(t), w-t)
def golden(a0, b0, f, tol):
    gr = (5**0.5-1)/2
    t, a, b = 0, a0, b0
    while b - a > tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        if f(μ) > f(λ): b = μ
        else:           a = λ
        t += 1
    return (a+b)/2
print(f(golden(0, 1000, f, 1e-7)))
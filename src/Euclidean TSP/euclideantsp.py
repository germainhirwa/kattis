from math import *

def golden(a0, b0, f, tol):
    gr = (5**0.5-1)/2
    t, a, b = 0, a0, b0
    while b - a > tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        if f(μ) > f(λ): b = μ
        else:           a = λ
        t += 1
    return (a+b)/2

def time(c):
    return n*(log2(n))**(c*sqrt(2))/(p*1e9) + s*(1+1/c)/v

n, p, s, v = map(float, input().split())
opt_c = golden(0.1, 100, time, 1e-9)
print(time(opt_c), opt_c)
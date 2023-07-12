a, b, c, d = map(int, input().split())
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def lcm(a,b):
    return a * b // gcd(a,b)
e = lcm(c, d)
print(b//e-(a-1)//e)
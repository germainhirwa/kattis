import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return (a*b)//gcd(a,b)
    
y = 1e8
fl = True

for line in sys.stdin:
    if fl:
        fl = False
    else:
        yf, p1, p2 = map(int, line.split())
        y = min(y, yf + lcm(p1, p2))
        
print(y)
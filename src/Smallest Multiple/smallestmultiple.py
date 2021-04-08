def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def lcm(a,b):
    return a*b//gcd(a,b)

import sys

for line in sys.stdin:
    nums = list(map(int,line.split(" ")))
    x = 1
    for n in nums:
        x = lcm(x,n)
    print(x)
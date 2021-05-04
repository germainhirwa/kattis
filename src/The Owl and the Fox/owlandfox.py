import sys

"""
def sd(n):
    if n < 10:
        return n
    return sd(n//10) + n%10
"""

def sd(n):
    s = 0
    while n >= 10:
        s += n % 10
        n //= 10
    return s + n

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        k = int(line)
        s = sd(k)-1
        k -= 1
        if s == 0:
            print(0)
        else:
            while s != sd(k):
                k -= 9
            print(k)
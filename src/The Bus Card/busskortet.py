import math
n = math.ceil(int(input())/100)*100
c = 0
while n > 0:
    if n >= 500:
        n -= 500
    elif n >= 200:
        n -= 200
    else:
        n -= 100
    c += 1
print(c)
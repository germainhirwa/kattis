# 1^2 + 3^2 + 5^2 + ... + (2n-1)^2 = n(2n-1)(2n+1)/3
n = int(input())

h = 1
while h*(2*h-1)*(2*h+1) <= 3*n:
    h += 1
print(h-1)
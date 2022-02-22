'''
f(n) = a(n) + b(n)
a(n) = a(n-2) + b(n-1), a(1) = 1, a(2) = 0
b(n) = a(n-2) + b(n-2), b(1) = 0, b(2) = 1
'''
n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
a[1], a[2], b[1], b[2] = 1, 0, 0, 1
for i in range(3, n + 1):
    a[i] = a[i-2] + b[i-1]
    b[i] = a[i-2] + b[i-2]
print((a[n] + b[n]) % (10**9 + 7))
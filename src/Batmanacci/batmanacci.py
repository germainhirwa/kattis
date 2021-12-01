n, k = list(map(int, input().split()))

"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"""

fib = [0, 1]
for i in range(n):
    fib.append(fib[-1] + fib[-2])

while n > 2:      
    if k > fib[n - 2]:
        k -= fib[n - 2]
        n -= 1
    else:
        n -= 2

print(["N", "A"][n - 1])
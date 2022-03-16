n = int(input())
def f(k):
    if k == 1:
        return 1
    if k % 2:
        return 2*f((k - 1) // 2) + f((k + 1) // 2)
    return 3 * f(k // 2)
print(f(n))
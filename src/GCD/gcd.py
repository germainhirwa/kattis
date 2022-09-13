a, b = map(int, input().split())
while a and b:
    a, b = b, a % b
print(a)
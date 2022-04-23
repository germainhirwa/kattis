a, b = 0, 1
for _ in range(int(input())):
    a, b = b, (a + b) % 10**6
print(b)
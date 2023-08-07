a, b = map(int, input().split()); t = 0
while a > b:
    if a % 2: a += 1
    else: a //= 2
    t += 1
print(t+b-a)
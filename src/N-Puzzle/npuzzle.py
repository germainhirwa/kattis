p, q, r, s = input(), input(), input(), input()
m = [p, q, r, s]
d = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != ".":
            n = ord(m[i][j]) - 65
            d += abs(n // 4 - i) + abs(n % 4 - j)
print(d)
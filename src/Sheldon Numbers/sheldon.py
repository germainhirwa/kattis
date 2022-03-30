x, y = map(int, input().split())
s = set()
for a in range(1, 64):
    for b in range(63):
        for c in range(1, 63):
            for d in range(2):
                if a * (c + d) + b * c <= 63:
                    num = int(''.join((['1'] * a + ['0'] * b)*c + ['1'] * (a * d)), 2)
                    if x <= num <= y:
                        s.add(num)
print(len(s))
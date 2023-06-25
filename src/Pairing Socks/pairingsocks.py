n, a1, a2, t = int(input()), list(map(int, input().split()))[::-1], [], 0
while a1:
    t += 1
    if not a2 or a1[-1] != a2[-1]: a2.append(a1.pop())
    else: a1.pop(), a2.pop()
print('impossible' if a2 else t)
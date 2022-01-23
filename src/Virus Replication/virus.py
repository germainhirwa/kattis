a, b = input(), input()
l, r = 0, 0
while l < min(len(a), len(b)) and a[l] == b[l]:
    l += 1
while r < min(len(a), len(b)) - l and a[len(a) - r - 1] == b[len(b) - r - 1]:
    r += 1
print(len(b) - (r + l))
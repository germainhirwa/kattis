m = input()
def find(s):
    for c in range(1, s + 1):
        for r in range(c, 0, -1):
            if r * c == s:
                return (r, c)
r, c = find(len(m))
print(''.join([m[i + j*r] for i in range(r) for j in range(c)]))
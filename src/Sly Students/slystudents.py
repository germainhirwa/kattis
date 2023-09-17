from math import gcd
def b3(x):
    r = []
    while x: r.append(str(x%3)); x //= 3
    return ''.join(r[::-1])
s = [*map(lambda x: [*map(ord, x)], input().split())]
for i in range(len(s)):
    d = s[i][0]
    for j in range(1, len(s[i])): d = gcd(d, s[i][j])
    print(d), print(*(b3(i//d) for i in s[i]))
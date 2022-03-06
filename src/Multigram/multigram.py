s = input()
n = len(s)

divs = [1]
d = 2
while d**2 <= n:
    if n % d == 0:
        divs.extend([d, n // d])
    d += 1

def check_anagram(s1, s2):
    c1, c2 = {}, {}
    for i in s1:
        if i not in c1:
            c1[i] = 0
        c1[i] += 1
    for i in s2:
        if i not in c2:
            c2[i] = 0
        c2[i] += 1
    return c1 == c2

found = False
for g in sorted(divs):
    ok = True
    test = s[:g]
    for i in range(1, n // g):
        test2 = s[i*g:(i + 1)*g]
        if not check_anagram(test, test2):
            ok = False
            break
    if ok:
        print(test)
        found = True
        break

if not found:
    print(-1)
def do():
    x, y, xpy, xmy = set(), set(), set(), set()
    for i in range(8):
        s = input()
        for j in range(8):
            if s[j] == '*':
                if i in x or j in y or i + j in xpy or i - j in xmy:
                    return 'invalid'
                x.add(i)
                y.add(j)
                xpy.add(i + j)
                xmy.add(i - j)
    if len(x) != 8:
        return 'invalid'
    return 'valid'

print(do())
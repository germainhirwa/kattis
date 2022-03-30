code = input()
words = input().split()
ok = len(code) == len(words)
if ok:
    m1, m2 = {}, {}
    for i in range(len(code)):
        if words[i] not in m1 and code[i] not in m2:
            m1[words[i]] = code[i]
            m2[code[i]] = words[i]
        elif words[i] in m1 and code[i] in m2 and m1[words[i]] == code[i] and m2[code[i]] == words[i]:
            continue
        else:
            ok = False
            break
print(ok)
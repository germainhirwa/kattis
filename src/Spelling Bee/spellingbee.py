s = input()
n = int(input())
for _ in range(n):
    s2 = input()
    spell = True
    if s[0] not in s2 or len(s2) < 4:
        spell = False
    if spell:
        for i in s2:
            if i not in s:
                spell = False
    if spell:
        print(s2)
s1, s2 = input().strip(), input().strip()
i = 0
while i < len(s1) and i < len(s2):
    if s1[i] == s2[i]: i += 1
    else: break
print(len(s1)+len(s2)-2*i)
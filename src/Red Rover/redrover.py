s = input()
ans = len(s)
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        t = s[i:j]
        ans = min(ans, len(t) + len(s.replace(t, 'M')))
print(ans)
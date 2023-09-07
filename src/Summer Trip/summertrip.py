s = input().strip(); ans = 0
for i in range(len(s)):
    h = {s[i]}
    for j in range(i+1, len(s)):
        ans += s[j] not in h; h.add(s[j])
        if s[i] == s[j]: break
print(ans)
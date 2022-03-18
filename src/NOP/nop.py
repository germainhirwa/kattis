s = input()
prev, ans = 0, 0
for i in range(len(s)):
    if 65 <= ord(s[i]) < 91:
        ans += (4 - i + prev) % 4
        prev = i
print(ans)
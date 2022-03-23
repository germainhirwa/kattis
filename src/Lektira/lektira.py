s = input()
m = s
for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s) - 1):
        m = min(m, s[i-1::-1] + s[j:i-1:-1] + s[:j:-1])
print(m)
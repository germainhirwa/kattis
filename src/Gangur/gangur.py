s = input(); a = b = 0
for i in range(len(s)):
    if s[i] == '>': b += 1
    elif s[i] == '<': a += b
print(a)
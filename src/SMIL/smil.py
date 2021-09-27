s = input()
for i in range(len(s)):
    if s[i:i+2] in [":)", ";)"] or s[i:i+3] in [":-)", ";-)"]:
        print(i)
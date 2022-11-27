n, s = int(input()), input()
t = 1
b = ''
for i in s:
    b += i
    if int(b) == t:
        t += 1
        b = ''
print(t)
n = [0]*45
for _ in range(int(input())):
    s = input()
    for i in range(len(s)): n[i] += ord(s[i])+1j
n = [chr(int(i.real/i.imag)) for i in n if i]
print(''.join(n))
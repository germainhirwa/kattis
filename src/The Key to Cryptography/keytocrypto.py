cpt = input()
cpk = input()

msg = ''
for i in range(len(cpt)):
    msg += str(chr((ord(cpt[i])-ord(cpk[i]))%26+65))
    cpk += msg[i]

print(msg)
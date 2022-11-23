def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = input().split()
z, f = a.split('.')
z = int(z)
b = int(b)
rep = int(f[-b:])
rem = f[:-b]
# z + int(rem)/10**len(rem) + rep/(10**len(rem)*(10**b-1))
nom = z*(10**len(rem)*(10**b-1)) + int('0'+rem)*(10**b-1) + rep
denom = 10**len(rem)*(10**b-1)
d = gcd(nom, denom)
print(f'{nom//d}/{denom//d}')
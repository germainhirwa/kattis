n = int(input())
x = list(map(int, input().split(" ")))

nom, denom = x[-1], 1
for i in x[-2::-1]:
    nom, denom = denom, nom
    nom += i * denom

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

d = gcd(nom, denom)
print(f"{nom // d}/{denom // d}")
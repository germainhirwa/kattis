import sys, math

def decrypt(text):
    k = math.ceil(math.sqrt(len(text)))
    mat = []
    for _ in range(k):
        mat.append(['']*k)
    for i in range(len(text)):
        mat[i%k][k-1-i//k] = text[i]
    
    for r in mat:
        print(''.join(r), end='')
    print()

for line in sys.stdin:
    try:
        n = int(line)
    except:
        decrypt(line.strip())
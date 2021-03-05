kp = input()
text = input()
encrypt_table = {}
decrypt_table = {}

i = 0
for w in kp:
    if w.upper() not in encrypt_table and w != " ":
        encrypt_table[w.upper()] = i
        decrypt_table[i] = w.upper()
        i += 1
for l in list(map(chr,range(65,91))):
    if l not in encrypt_table and l != "Q":
        encrypt_table[l] = i
        decrypt_table[i] = l
        i += 1

text = text.replace(" ","").upper()

use_x = False
use_x2 = False
i = 0
while (i < len(text)):
    if use_x:
        diagraph = text[i+1]+"X"
        use_x = False
    elif use_x2:
        diagraph = text[i]+"X"
        use_x2 = False
    else:
        diagraph = text[i:i+2]

    if len(diagraph) == 1:
        i -= 2
        use_x2 = True
    else:
        if diagraph[0] == diagraph[1]:
            i -= 3
            use_x = True
        else:
            k1 = encrypt_table[diagraph[0]]
            k2 = encrypt_table[diagraph[1]]
            r1, r2 = k1//5, k2//5
            c1, c2 = k1%5, k2%5
            if r1 == r2:
                print(decrypt_table[r1*5+(c1+1)%5],end="")
                print(decrypt_table[r2*5+(c2+1)%5],end="")
            elif c1 == c2:
                print(decrypt_table[(r1+1)%5*5+c1],end="")
                print(decrypt_table[(r2+1)%5*5+c2],end="")
            else:
                print(decrypt_table[r1*5+c2],end="")
                print(decrypt_table[r2*5+c1],end="")

    i += 2
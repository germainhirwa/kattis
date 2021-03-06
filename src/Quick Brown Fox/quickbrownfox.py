import sys
first_line = True
for line in sys.stdin:
    if first_line:
        first_line = False
    else:
        line = line.lower()
        alphabet = [False]*26
        found = 0
        for s in line:
            if 97 <= ord(s) <= 122 and not alphabet[ord(s)-97]:
                found += 1
                alphabet[ord(s)-97] = True
        
        if found == 26:
            print("pangram")
        else:
            print("missing ",end="")
            for i in range(26):
                if not alphabet[i]:
                    print(chr(i+97),end="")
            print()
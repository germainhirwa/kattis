cipher = dict((chr(i),i-65) for i in range(65,91))
cipher['_'] = 26
cipher['.'] = 27

decipher = dict((v,k) for k,v in cipher.items())

import sys

for line in sys.stdin:
    try:
        r,s = line.strip().split(" ")
        r = int(r)
        s = s[::-1]

        ans = ''
        for t in s:
            ans += decipher[(cipher[t]+r)%28]
        print(ans)
    except:
        pass
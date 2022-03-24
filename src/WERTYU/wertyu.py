import sys
for line in sys.stdin:
    print(line.strip('\n\r').translate("".maketrans("1234567890-=QWERTYUIOP[]\\SDFGHJKL;'XCVBNM,./", "`1234567890-\tQWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.")))
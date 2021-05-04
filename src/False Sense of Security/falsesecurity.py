morse = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '_':'..--',
    '.':'---.',
    ',':'.-.-',
    '?':'----'
}

demorse = dict((v,k) for k,v in morse.items())

import sys

for line in sys.stdin:
    encoded = ''.join(list(map(lambda x: morse[x],line.strip())))
    nums = ''.join(list(map(lambda x: str(len(morse[x])),line.strip())))[::-1]
    idx = 0
    result = ''
    for n in nums:
        result += demorse[encoded[idx:idx+int(n)]]
        idx += int(n)
    print(result)
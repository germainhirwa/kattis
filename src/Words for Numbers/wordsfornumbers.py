def spell(t):
    if t < 20: return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][t]
    if t % 10 == 0: return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][t//10-2]
    return f'{spell(t-t%10)}-{spell(t%10)}'

import sys
for l in sys.stdin:
    for i in range(99, -1, -1): l = l.replace(str(i), spell(i))
    print(l.strip().capitalize())
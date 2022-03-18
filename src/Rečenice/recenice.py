ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
rest = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
nums = {}
for i in range(1000):
    if i < 10:
        nums[i] = ones[i]
    elif i < 100:
        if i == 10:
            nums[i] = 'ten'
        elif i < 20:
            nums[i] = rest[i - 10]
        else:
            nums[i] = tens[i // 10] + ones[i % 10]
    else:
        nums[i] = ones[i // 100] + 'hundred' + nums[i % 100]

import sys
input()

s = 0
w = []
for line in sys.stdin:
    line = line.strip()
    if line != '$':
        s += len(line)
    else:
        dol = len(w)
    w.append(line)
for i in range(1, 999):
    if s + len(nums[i]) == i:
        w[dol] = nums[i]
        break
print(' '.join(w))
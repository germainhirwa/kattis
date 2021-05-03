nums = {
    '0':'xxxxxx...xx...xx...xx...xx...xxxxxx',
    '1':'....x....x....x....x....x....x....x',
    '2':'xxxxx....x....xxxxxxx....x....xxxxx',
    '3':'xxxxx....x....xxxxxx....x....xxxxxx',
    '4':'x...xx...xx...xxxxxx....x....x....x',
    '5':'xxxxxx....x....xxxxx....x....xxxxxx',
    '6':'xxxxxx....x....xxxxxx...xx...xxxxxx',
    '7':'xxxxx....x....x....x....x....x....x',
    '8':'xxxxxx...xx...xxxxxxx...xx...xxxxxx',
    '9':'xxxxxx...xx...xxxxxx....x....xxxxxx',
    '+':'.......x....x..xxxxx..x....x.......',
    }

arts = dict((v,k) for k,v in nums.items())

import sys

fl = True
for line in sys.stdin:
    if fl:
        fl = False
        exp = ['']*(len(line)//6)

    for i in range(len(exp)):
        exp[i] += line[6*i:6*i+5]

res = list(map(lambda x: arts[x], exp))
ans = str(eval(''.join(res)))

lines = ['']*7
for i in range(len(ans)):
    trans = nums[ans[i]]
    for j in range(len(lines)):
        lines[j] += '.'+trans[5*j:5*(j+1)]

for l in lines:
    print(l[1:])
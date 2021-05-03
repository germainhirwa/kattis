nums = {
    '**** ** ** ****':0,
    '  *'*5:1,
    '***  *****  ***':2,
    '***  ****  ****':3,
    '* ** ****  *  *':4,
    '****  ***  ****':5,
    '****  **** ****':6,
    '***'+'  *'*4:7,
    '**** ***** ****':8,
    '**** ****  ****':9,
    }

import sys

lines = []

for line in sys.stdin:
    lines.append(line)

if len(lines[0]) != len(lines[1]): # parsing problem with 1
    lines[0] = '  '+lines[0]

num = ['']*((len(lines[0])+1)//4)

for l in lines:
    for i in range(len(num)):
        num[i] += l[4*i:4*i+3]

res = list(map(lambda x: nums.get(x,-1),num))
if -1 in res:
    print("BOOM!!")
else:
    if not res[-1] % 2 and not sum(res) % 3:
        print("BEER!!")
    else:
        print("BOOM!!")
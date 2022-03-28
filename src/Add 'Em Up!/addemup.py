import string
_, tot = map(int, input().split())
arr = list(map(str, input().split()))
s = {}
for i in arr:
    if i not in s:
        s[i] = 0
    s[i] += 1

def flip(num):
    new = []
    for digit in num:
        if digit in '347':
            return num
        elif digit == '6':
            new.append('9')
        elif digit == '9':
            new.append('6')
        else:
            new.append(digit)
    return ''.join(new[::-1])

s2 = {}
for num in s:
    s2[flip(num)] = s[num]
for i in s2:
    if i not in s:
        s[i] = 0
    s[i] += s2[i]
s = sorted(s.items(), key=lambda x: int(x[0]))

lo, hi = 0, len(s) - 1
found = False

for i in range(len(s)):
    if int(s[i][0]) * 2 == tot and s[i][1] > 1:
        found = True
        break

while not found and lo < hi:
    check = int(s[lo][0]) + int(s[hi][0])
    if check == tot:
        if flip(s[lo][0]) != s[hi][0] or s[hi][1] > 1:
            found = True
            break
        lo += 1
        hi -= 1
    elif check > tot:
        hi -= 1
    else:
        lo += 1
print('YES' if found else 'NO')
s = input()
arr = []

for _ in range(5):
    arr.append(['.']*(4*len(s)+1))

for i in range(len(s)):
    arr[0][4*i+2] = '#'
    arr[1][4*i+1] = '#'
    arr[1][4*i+3] = '#'
    arr[2][4*i] = '#'
    arr[2][4*i+2] = s[i]
    arr[2][4*i+4] = '#'
    arr[3][4*i+1] = '#'
    arr[3][4*i+3] = '#'
    arr[4][4*i+2] = '#'

for i in range(len(s)//3):
    arr[0][12*i+10] = '*'
    arr[1][12*i+9] = '*'
    arr[1][12*i+11] = '*'
    arr[2][12*i+8] = '*'
    arr[2][12*i+12] = '*'
    arr[3][12*i+9] = '*'
    arr[3][12*i+11] = '*'
    arr[4][12*i+10] = '*'

for r in arr:
    print(''.join(r))
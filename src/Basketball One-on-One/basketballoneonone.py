log = input()
a,b = 0,0

for i in range(len(log)//2):
    if log[2*i] == 'A':
        a += int(log[2*i+1])
    else:
        b += int(log[2*i+1])

# a == b will not happen
if a > b:
    print('A')
else:
    print('B')
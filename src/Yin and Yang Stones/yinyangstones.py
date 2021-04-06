s = input()

b,w = 0,0
for l in s:
    if l == 'B':
        b += 1
    else:
        w += 1
    
print(int(b==w))
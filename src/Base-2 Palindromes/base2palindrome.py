m = int(input())
l = 1
while True:
    if m <= 1<<((l-1)//2): break
    m -= 1<<((l-1)//2); l += 1
p = []
for i in range(1, 1<<(l+1)//2, 2):
    b = ['0']*l
    for j in range((l+1)//2):
        if i&(1<<j): b[j] = b[-j-1] = '1'
    p.append(''.join(b))
print(int(sorted(p)[m-1], 2))
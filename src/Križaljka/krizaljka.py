a,b = input().strip().split(" ")
arr = []
for _ in range(len(b)):
    arr.append(['.']*len(a))

def common(a,b):
    for j in range(len(a)):
        for i in range(len(b)):
            if b[i] == a[j]:
                return (i,j)

i,j = common(a,b)
for k in range(len(a)):
    arr[i][k] = a[k]
for k in range(len(b)):
    arr[k][j] = b[k]

for r in arr:
    print(''.join(r))
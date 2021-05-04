a = list(input())

largest_k = -1
for k in range(len(a)-1):
    if a[k] < a[k+1]:
        largest_k = k

if largest_k == -1:
    print(0)
else:
    largest_l = 0
    for l in range(largest_k+1,len(a)):
        if a[l] > a[largest_k]:
            largest_l = l
    a[largest_k], a[largest_l] = a[largest_l], a[largest_k]
    a[largest_k+1:] = a[:largest_k:-1]
    print(''.join(a))
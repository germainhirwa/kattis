n = int(input())
arr = list(map(int, input().split()))
discord = False

# Try increase a digit
for i in range(n - 1):
    for j in range(len(str(arr[i]))):
        flag = False
        check = list(str(arr[i]))
        check[j] = '9'
        if int(''.join(check)) > arr[i + 1]:
            discord = True
            flag = True
            arr[i] = int(''.join(check))
            break
    if flag:
        break

# Try decrease a digit
if not discord:
    for i in range(n - 1, 0, -1):
        for j in range(len(str(arr[i]))):
            flag = False
            check = list(str(arr[i]))
            if len(check) == 1 and j == 0:  check[j] = '0'
            else:                           check[j] = '1'
            if int(''.join(check)) < arr[i - 1]:
                discord = True
                flag = True
                arr[i] = int(''.join(check))
                break
        if flag:
            break
    
if not discord:
    print('impossible')
else:
    print(*arr)
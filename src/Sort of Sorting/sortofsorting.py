num = -1
flag = False
while num != 0:
    if flag:
        print()
    num = int(input())
    if num == 0:
        break
    names = []
    for _ in range(num):
        names.append(input())
    names.sort(key=lambda x:x[:2])
    for name in names:
        print(name)
    flag = True
n = int(input())

lu, ld, ru, rd = 8, 8, 8, 8
can_left, can_right = True, True

for _ in range(n):
    tooth = input().split()
    if tooth[0][1] in ['-', '+']:
        # right
        if tooth[1] == 'b':
            can_right = False
        else:
            if tooth[0][1] == '-':
                rd -= 1
            else:
                ru -= 1
    else:
        # left
        if tooth[1] == 'b':
            can_left = False
        else:
            if tooth[0][0] == '-':
                ld -= 1
            else:
                lu -= 1

can_left &= all([ld, lu])
can_right &= all([rd, ru])

if can_left:    print(0)
elif can_right: print(1)
else:           print(2)
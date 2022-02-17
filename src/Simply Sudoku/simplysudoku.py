sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))
sudokut = list(map(list, zip(*sudoku)))
subgrids = []
for _ in range(9):
    subgrids.append([])
unfilled = set()
for i in range(9):
    for j in range(9):
        subgrids[i // 3 * 3 + j // 3].append(sudoku[i][j])
        if sudoku[i][j] == 0:
            unfilled.add((i, j))

def fill(i, j, val):
    global sudoku
    global sudokut
    global subgrids

    sudoku[i][j] = val
    sudokut[j][i] = val
    subgrids[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] = val

found = True
while found:
    found = False
    new_unfilled = unfilled.copy()
    for i, j in unfilled:
        # Single value
        possible = [False] * 9
        check1 = sudoku[i]
        check2 = sudokut[j]
        check3 = subgrids[i // 3 * 3 + j // 3]
        for k in range(9):
            # same row/col/subgrid and not empty, flag that number possible
            if k != j and check1[k]:
                possible[check1[k] - 1] = True
            if k != i and check2[k]:
                possible[check2[k] - 1] = True
            if k != i % 3 * 3 + j % 3 and check3[k]:
                possible[check3[k] - 1] = True
        # is there only one unflagged value at possible -> single value
        if sum(possible) == 8:
            for k in range(9):
                if not possible[k]:
                    fill(i, j, k + 1)
                    new_unfilled.remove((i, j))
                    found = True
                    break
        
        if not found:
            # Unique location: subgrid
            possible21 = [0] * 9
            possible22 = [0] * 9
            u = 0
            for i2, j2 in unfilled:
                if i // 3 * 3 + j // 3 == i2 // 3 * 3 + j2 // 3: # same subgrid
                    check1 = sudoku[i2]
                    check2 = sudokut[j2]
                    check3 = subgrids[i2 // 3 * 3 + j2 // 3]
                    possible3 = [0] * 9
                    for k in range(9):
                        if k != j2 and check1[k]:
                            possible3[check1[k] - 1] = 1
                        if k != i2 and check2[k]:
                            possible3[check2[k] - 1] = 1
                        if k != i2 % 3 * 3 + j2 % 3 and check3[k]:
                            possible3[check3[k] - 1] = 1
                    for k in range(9):
                        if [i2, j2] != [i, j]:
                            possible21[k] += possible3[k]
                        else:
                            possible22[k] += possible3[k]
                    u += 1
            
            test = []
            for k in range(9):
                if possible21[k] == u - 1 and possible22[k] == 0:
                    test.append(k + 1)
            if len(test) == 1:
                fill(i, j, test[0])
                new_unfilled.remove((i, j))
                found = True

            if not found:
                # Unique location: row
                possible21 = [0] * 9
                possible22 = [0] * 9
                u = 0
                for i2, j2 in unfilled:
                    if i == i2: # same row
                        check1 = sudoku[i2]
                        check2 = sudokut[j2]
                        check3 = subgrids[i2 // 3 * 3 + j2 // 3]
                        possible3 = [0] * 9
                        for k in range(9):
                            if k != j2 and check1[k]:
                                possible3[check1[k] - 1] = 1
                            if k != i2 and check2[k]:
                                possible3[check2[k] - 1] = 1
                            if k != i2 % 3 * 3 + j2 % 3 and check3[k]:
                                possible3[check3[k] - 1] = 1
                        for k in range(9):
                            if [i2, j2] != [i, j]:
                                possible21[k] += possible3[k]
                            else:
                                possible22[k] += possible3[k]
                        u += 1
                
                test = []
                for k in range(9):
                    if possible21[k] == u - 1 and possible22[k] == 0:
                        test.append(k + 1)
                if len(test) == 1:
                    fill(i, j, test[0])
                    new_unfilled.remove((i, j))
                    found = True

                if not found:
                    # Unique location: column
                    possible21 = [0] * 9
                    possible22 = [0] * 9
                    u = 0
                    for i2, j2 in unfilled:
                        if j == j2: # same column
                            check1 = sudoku[i2]
                            check2 = sudokut[j2]
                            check3 = subgrids[i2 // 3 * 3 + j2 // 3]
                            possible3 = [0] * 9
                            for k in range(9):
                                if k != j2 and check1[k]:
                                    possible3[check1[k] - 1] = 1
                                if k != i2 and check2[k]:
                                    possible3[check2[k] - 1] = 1
                                if k != i2 % 3 * 3 + j2 % 3 and check3[k]:
                                    possible3[check3[k] - 1] = 1
                            for k in range(9):
                                if [i2, j2] != [i, j]:
                                    possible21[k] += possible3[k]
                                else:
                                    possible22[k] += possible3[k]
                            u += 1
                    
                    test = []
                    for k in range(9):
                        if possible21[k] == u - 1 and possible22[k] == 0:
                            test.append(k + 1)
                    if len(test) == 1:
                        fill(i, j, test[0])
                        new_unfilled.remove((i, j))
                        found = True

    unfilled = new_unfilled

if unfilled:
    print('Not easy')
    for r in sudoku:
        print(*list(map(lambda x: '.' if x == 0 else x, r)))
else:
    print('Easy')
    for r in sudoku:
        print(*r)
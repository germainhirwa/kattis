def flatten(mat):
    return [num for row in mat for num in row]

def transpose(mat):
    return [[row[i] for row in mat] for i in range(len(mat[0]))]

def reverse(mat):
    return list(map(lambda l: l[::-1], mat))

def merge_left(mat):
    def mergify_leftify(row):
        curr_index=0
        while curr_index < len(row) and row[curr_index] == 0:
            curr_index += 1
        next_index = curr_index+1
        while next_index < len(row) and row[next_index] == 0:
            next_index += 1
        
        if next_index == len(row):
            row[0] = row[curr_index]
            if curr_index != 0:
                row[curr_index] = 0
            return row
        elif curr_index == len(row):
            return row
        else:
            if row[curr_index] == row[next_index]:
                row[curr_index] *= 2
                row[next_index] = 0
                t = row[curr_index]
                nextmerge = mergify_leftify(row[next_index+1:]+[0]*next_index)
                return [t]+nextmerge

            else:
                if curr_index != next_index-1:
                    row[curr_index+1]=row[next_index]
                    row[next_index] = 0
                    next_index = curr_index + 1
                t = row[curr_index]
                nextmerge = mergify_leftify(row[next_index:]+[0]*(curr_index))
                return [t]+nextmerge
    new_matrix = []
    for row in mat:
        elem = [e for e in row]
        res = mergify_leftify(elem)
        new_matrix.append(res)
    
    return new_matrix

def merge_right(mat):
    m_state = merge_left(reverse(mat))
    return reverse(m_state)

def merge_up(mat):
    m_state = merge_left(transpose(mat))
    return transpose(m_state)

def merge_down(mat):
    m_state = merge_right(transpose(mat))
    return transpose(m_state)

# main function
matrix = []
for _ in range(4):
    matrix.append(list(map(int,input().split())))
n = int(input())

if n == 0:
    for row in merge_left(matrix):
        print(" ".join(list(map(str,row))))
elif n == 1:
    for row in merge_up(matrix):
        print(" ".join(list(map(str,row))))
elif n == 2:
    for row in merge_right(matrix):
        print(" ".join(list(map(str,row))))
else:
    for row in merge_down(matrix):
        print(" ".join(list(map(str,row))))
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
c1, c2, c3 = map(int, input().split())
d1, d2, d3 = map(int, input().split())

def rref(A):
    def equal(a, b): return abs(a-b) < 1e-5
    def leading_entry_col(A, r):
        row = A[r]; i = 0
        while i < len(A[0]) and equal(row[i], 0): i += 1
        return i
    def list_pivots(A):
        res = []
        for r in range(len(A)):
            k = leading_entry_col(A, r)
            if k != len(A[0]): res.append((r, k))
        return sorted(res, reverse=True)
    def col(A, i): return list(map(lambda x: x[i], A))
    def ero1(A, i, c):
        for j in range(len(A[0])): A[i][j] *= c
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]
    def ero3(A, i, j): A[i], A[j] = A[j], A[i]
    curr_col = 0
    curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A):
        if equal(A[curr_row][curr_col], 0):
            check_col = col(A, curr_col)[curr_row+1:]
            for i in range(len(check_col)):
                if not equal(check_col[i], 0): break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
            else: curr_col += 1
        else:
            if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, 1/A[curr_row][curr_col])
            for i in range(curr_row+1, len(A)):
                if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1
            curr_row += 1
    pivots = list_pivots(A)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A

A = [
    [a1-b1, a2-b2, a3-b3, (a1**2+a2**2+a3**2-b1**2-b2**2-b3**2)/2],
    [b1-c1, b2-c2, b3-c3, (b1**2+b2**2+b3**2-c1**2-c2**2-c3**2)/2],
    [c1-d1, c2-d2, c3-d3, (c1**2+c2**2+c3**2-d1**2-d2**2-d3**2)/2]
]
print(*(i[-1] for i in rref(A)))
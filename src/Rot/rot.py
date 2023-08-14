r, _ = map(int, input().split())
w = [input() for _ in range(r)]
a = int(input())

def disp(w): [print(''.join(r)) for r in w]
def rot90(w): return [[w[len(w)-1-i][j] for i in range(len(w))] for j in range(len(w[0]))]
def rot45(w):
    s = len(w)+len(w[0])-1
    m = [[' ']*s for _ in range(s)]
    for i in range(len(w)):
        for j in range(len(w[0])): m[i+j][len(w)-1-i+j] = w[i][j]
    return m

while a >= 90:
    a -= 90
    w = rot90(w)
disp(rot45(w) if a else w)
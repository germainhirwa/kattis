_, a, b = input().strip().split()

def dist(a, b):
    return ind(b) - ind(a) - 1

def ind(x, pos=0):
    if pos == len(x):
        return 0
    elif x[pos] == '0':
        return ind(x, pos + 1)
    else:
        return 2**(len(x) - pos) - ind(x, pos + 1) - 1

print(dist(a, b))
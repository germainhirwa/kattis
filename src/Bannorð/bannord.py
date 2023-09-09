s = {*input()}; t = input().split()
for i in range(len(t)): t[i] = '*'*len(t[i]) if {*t[i]}&s else t[i]
print(' '.join(t))
n = int(input())
for i in range(1, 500):
    if i*i<=n<(i+1)**2: print('YNEOS'[int(i*i+i<=n)::2]); break
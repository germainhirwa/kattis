N = int(input()); B = bin(N-1)[2:]; K = len(B); X = N*K
if X == 1: print(0), exit(0)
for i in range(K):
    if B[i] == '0': X += (1<<(K-i-1))*(i+1)
print(X/N)
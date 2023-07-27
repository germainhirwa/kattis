N, A = int(input()), sorted(map(int, input().split()))
if N > 89: print('possible'), exit(0)
for i in range(N-2):
    if A[i]+A[i+1]>A[i+2]: print('possible'), exit(0)
print('impossible')
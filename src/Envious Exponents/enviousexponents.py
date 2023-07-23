N, k = map(int, input().split())
B = [*bin(N+1)[2:].zfill(61)]
while True:
    b = B.count('1')
    if b < k:
        flip = k-b
        for i in range(60, -1, -1):
            if flip == 0: break
            if B[i] == '0': flip -= 1; B[i] = '1'
        print(int(''.join(B), 2)), exit(0)
    elif b > k:
        pos = k
        for i in range(61):
            pos -= B[i] == '1'
            if pos == 0: break
        for j in range(i+1, 61): B[j] = '0'
        B = [*bin(int(''.join(B), 2)+(1<<(60-i)))[2:].zfill(61)]
    else: print(int(''.join(B), 2)), exit(0)
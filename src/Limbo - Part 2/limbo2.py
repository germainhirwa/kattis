for _ in range(int(input())):
    r, c = map(int, input().split())
    R = C = T = M = 1
    while r >= R or c >= C:
        if T: C *= 2
        else: R *= 2
        T = 1-T; M *= 2
    if T: print((r-R//2)*C+c+M//2) # take the lower half
    else: print((c-C//2)*R+r+M//2) # take the right half
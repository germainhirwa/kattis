t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    cp = {}
    for i in range(n):
        if arr[i] == m:
            cp[i] = True
        elif arr[i] < m:
            cp[i] = False
    
    pos = 0
    maxsum = 0
    currsum, currsum2 = 0, 0
    currsum_has_m = False

    while pos < n:
        if pos in cp:
            if currsum_has_m:
                maxsum = max(maxsum, currsum)
            if cp[pos]:
                currsum = currsum2 + m
                currsum_has_m = True
                currsum2 = 0
            else:
                currsum = 0
                currsum_has_m = False
                currsum2 = 0
        else:
            currsum += arr[pos]
            currsum2 += arr[pos]
        pos += 1
    maxsum = max(maxsum, currsum)
    print(maxsum)
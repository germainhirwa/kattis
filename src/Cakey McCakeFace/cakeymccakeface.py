n, m =  int(input()), int(input())
nn, mm = list(map(int, input().split())), list(map(int, input().split()))
freq = {}
for i in nn:
    for j in mm:
        if j>=i:
            if j-i not in freq: freq[j-i] = 0
            freq[j-i] += 1
if not freq: print(0)
else: print(max(freq.items(), key=lambda x: (x[1], -x[0]))[0])
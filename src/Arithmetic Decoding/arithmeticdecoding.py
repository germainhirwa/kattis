n, p, s = int(input()), int(input())/8, input()
target = int(s[s.find('.')+1:], 2)/(1<<(len(s)-s.find('.')-1))
ints = [[0, 1]]
for _ in range(n):
    ints2 = []
    for a, b in ints: ints2.append([a, a+p*(b-a)]), ints2.append([a+p*(b-a), b])
    ints = ints2
for i in range(len(ints)):
    if ints[i][0] == target: print(bin(i)[2:].zfill(n).replace('0', 'A').replace('1', 'B')), exit(0)
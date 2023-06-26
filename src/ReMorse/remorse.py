from collections import Counter
s, t = ''.join(i.upper() for i in input() if i.isalpha()), [1, 3, 3, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11]
c = sorted(Counter(s).items(), key=lambda x: -x[1])
print(sum(a*b[1] for a, b in zip(t, c))+3*len(s)-3)
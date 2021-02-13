from math import log10

s = input()
if s == "1":
    print(1)
elif s == "2":
    print(2)
elif s == "6":
    print(3)
elif s == "24":
    print(4)
elif s == "120":
    print(5)
else:
    num = 6
    digits = len(s)
    init = 4*log10(2) + 2*log10(3) + log10(5)
    while init < digits:
        num += 1
        init += log10(num)
    print(num-1)
a = list(input().strip())
b = list(input().strip())

for i in range(1, min(len(a), len(b)) + 1):
    if a[-i] < b[-i]:
        a[-i] = ""
    elif a[-i] > b[-i]:
        b[-i] = ""

for l in [a, b]:
    if l == [""]*len(l):
        print("YODA")
    else:
        print(int(str().join(l)))
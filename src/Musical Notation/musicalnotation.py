n = int(input())
notes = input().strip().split(" ")
n_dash = list(map(lambda x: 2 if len(x) == 1 else int(x[1]) + 1, notes))

lines = ["G", "F", "E", "D", "C", "B", "A"]
lines.extend(list(map(lambda x: x.lower(), lines)))

dash = [1, 3, 5, 7, 9, 13]

def print_sheet(s):
    for l in s:
        print(str().join(l)[:-1])

sheet = []
for i in range(14):
    sl = [f"{lines[i]}: "]
    if i in dash:
        sl.extend(["-"]*(sum(n_dash)))
    else:
        sl.extend([" "]*(sum(n_dash)))
    sheet.append(sl)

t = 1
for k in range(n):
    sheet[lines.index(notes[k][0])][t:t + n_dash[k] - 1] = ["*"]*(n_dash[k] - 1)
    t += n_dash[k]

print_sheet(sheet)
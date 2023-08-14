s = input()
ind = pos = 0
while pos < len(s):
    if s[pos] == '{': print(' '*(ind if pos and s[pos-1] == '{' else 0)+'{'); ind += 2; pos += 1
    elif s[pos].isalpha(): (print(' '*ind, end='') if s[pos-1] == '{' else 0), print(s[pos], end=''); pos += 1
    elif s[pos] == ',': print(','); pos += 1; print(' '*ind, end='')
    else: ind -= 2; (print(), print(' '*ind+'}', end='')) if s[pos-1] != '{' else print(' '*ind+'}', end=''); pos += 1
print()
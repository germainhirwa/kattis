s = input()
arr = []
for c in s:
    if c == "<":
        if arr:
            arr.pop()
    else:
        arr.append(c)
print("".join(arr))
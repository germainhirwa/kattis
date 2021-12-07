n = int(input())
booleans = list(map(lambda x: x == 'T', input().split()))
expr = input().split()
operators = ['+', '-', '*']

stack = []
dictionary = {}
var = list(filter(lambda x: x not in operators, expr))
num_booleans = 0
for v in var:
    if v not in dictionary:
        dictionary[v] = booleans[num_booleans]
        num_booleans += 1

for i in expr:
    if i in operators:
        if i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a and b)
        elif i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a or b)
        else:
            a = stack.pop()
            stack.append(not a)
    else:
        stack.append(dictionary[i])

print(["F", "T"][int(stack[0])])

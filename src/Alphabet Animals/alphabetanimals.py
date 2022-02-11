import sys

animal = input()
n = int(input())

words = []
dic = {}
for _ in range(n):
    w = input()
    words.append(w)
    if w[0] in dic:
        dic[w[0]].append(w)
    else:
        dic[w[0]] = [w]

if not dic.get(animal[-1]):
    print('?')
else:
    for k in dic[animal[-1]]:
        if dic.get(k[-1]) in [None, [k]]:
            print(k + '!')
            sys.exit(0)
    print(dic[animal[-1]][0])
w = [input() for _ in range(int(input()))]
w2 = [i for i in w if len(i)==len({*i})>=5]
print(max(w2, key=lambda x:(-len(x), x), default='neibb!'))
q = int(input())
exists = False
for _ in range(q):
    peas = False
    pancakes = False
    menus = int(input())
    name = input()
    for _ in range(menus):
        food = input()
        if food == 'pea soup':
            peas = True
        elif food == 'pancakes':
            pancakes = True
    if peas and pancakes:
        print(name)
        exists = True
        break
if not exists:
    print('Anywhere is fine I guess')
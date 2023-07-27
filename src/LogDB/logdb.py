import sys; input = sys.stdin.readline
facts = {}
while True:
    s = [i.replace(' ', '') for i in input().strip().split(')') if i]
    if not s: break
    for fa in s:
        fact, args = fa.split('(')
        if fact not in facts: facts[fact] = []
        facts[fact].append(args.split(',') if args else [])

for l in sys.stdin:
    l = l.strip().replace(' ', ''); p = l.find('(')
    f = l[:p]; args = [i for i in l[p+1:-1].split(',') if i]
    matches = 0
    if f not in facts: facts[f] = []
    for args2 in facts[f]:
        if len(args2) != len(args): continue
        can = True; mapper = {}
        for i in range(len(args)):
            if args[i] == '_': continue
            if args[i][0] == '_':
                if args[i] not in mapper: mapper[args[i]] = args2[i]
                elif mapper[args[i]] != args2[i]: can = False; break
            elif args[i] != args2[i]: can = False; break
        matches += can
    print(matches)
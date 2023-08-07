s, p = input(), input(); h = {p}
for i in range(10): h.add(f'{p}{i}'), h.add(f'{i}{p}')
h.add(''.join(i.lower() if i.isupper() else i.upper() for i in p))
print(['No', 'Yes'][s in h])
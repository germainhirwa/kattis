s = input()
k = s.find('(')
print(['fix', 'correct'][int(len(s) == 2 * (k + 1))])
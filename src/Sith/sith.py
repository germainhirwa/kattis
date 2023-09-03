input()
a, b, c = [int(input()) for _ in range(3)]
print(['JEDI','SITH','VEIT EKKI'][2*(abs(a-b)==c)-(a-b!=c)])
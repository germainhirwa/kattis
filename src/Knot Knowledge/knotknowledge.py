n = int(input())
p = set(input().strip().split())
q = input().strip().split()

for k in q:
    p.remove(k)

print(list(p)[0])
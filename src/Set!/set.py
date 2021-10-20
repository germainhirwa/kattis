s = []

for _ in range(4):
    s.extend(input().strip().split())

def nd(lst, i):
    return len(set(map(lambda x: x[i], lst)))

have_set = False
for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            is_set = True
            for l in range(4):
                if nd([s[i], s[j], s[k]], l) not in [1, 3]:
                    is_set = False
            if is_set:
                have_set = True
                print(i+1, j+1, k+1)

if not have_set:
    print("no sets")
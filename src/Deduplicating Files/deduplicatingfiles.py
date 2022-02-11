def h(s):
    result = 0
    for i in s:
        result ^= ord(i)
    return result

while True:
    n = int(input())
    if n == 0:
        break

    unique = {}
    for _ in range(n):
        s = input()
        unique[s] = unique.get(s, 0) + 1
    coll = 0
    uniques = list(unique.keys())
    hashes = {}
    for u in uniques:
        hashes[u] = h(u)
    m = len(uniques)
    for k1 in range(m):
        for k2 in range(k1 + 1, m):
            if hashes[uniques[k1]] == hashes[uniques[k2]]:
                coll += unique[uniques[k1]] * unique[uniques[k2]]
    print(m, coll)
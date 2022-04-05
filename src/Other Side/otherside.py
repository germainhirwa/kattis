w, s, c, k = map(int, input().split())

if s < k or w + c < k:
    # we can always keep those < k in the boat all the time
    print('YES')
elif (s == k and w + c <= 2*k) or (w + c == k and s <= 2*k):
    # WLOG s == k
    # go back with nothing, bring k non-sheeps to the side, return with all k sheeps
    # bring w + c - k remaining non-sheeps, come back with nothing, then bring all the sheeps
    print('YES')
else:
    # in any phase, there is at least 1 non-sheep and 1 sheep
    print('NO')
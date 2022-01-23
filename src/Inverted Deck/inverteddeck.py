skip = input()
cards = list(map(int, input().split()))
scards = sorted(cards)

if cards == scards:
    print(1, 1)
else:
    lo, hi = 0, len(cards) - 1
    while cards[lo] == scards[lo]:
        lo += 1
    while cards[hi] == scards[hi]:
        hi -= 1
    if cards[:lo] + cards[lo:hi+1][::-1] + cards[hi+1:] == scards:
        print(lo + 1, hi + 1)
    else:
        print('impossible')
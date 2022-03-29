s = sorted(input())

# If there is a letter with > len/2 occurences, the median must be that letter
mid = s[len(s) // 2]
cnt = s.count(mid)

if cnt == len(s):
    print(-1)
else:
    # aaaabc can still be arranged to aabcaa (must have at least one letter between)
    # If the majority count < len(s) // 2, no problem with this arrangement as well
    print(''.join([mid] * (cnt // 2) + [x for x in s if x != mid] + [mid] * (cnt - cnt // 2)))
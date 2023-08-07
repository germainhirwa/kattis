n, m, k = map(int, input().split())
rp = sorted(map(int, input().split()), reverse=True)
rc = [*map(int, input().split())]
rs = [*map(int, input().split())]; rs = [i/2**0.5 for i in rs]
r = sorted(rc+rs, reverse=True); ans = 0
while r and rp:
    if rp[-1] <= r[-1]: rp.pop() # plot doesn't fit the smallest peg
    else: ans += 1; r.pop(), rp.pop()
print(ans)
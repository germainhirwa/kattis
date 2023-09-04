m, l = map(int, input().split())
M, L = map(int, input().split())
tm, tl = map(int, input().split())
# bring m-M then M-l then l-L
if abs(m)+abs(M-m)<=tm and abs(m)+abs(M-m)+abs(l-M)+abs(L-l)<=tl: print('possible')
# bring l-L then L-m then m-M
elif abs(l)+abs(L-l)<=tl and abs(l)+abs(L-l)+abs(m-L)+abs(M-m)<=tm: print('possible')
# take m, drop m at l, bring l-L then L-l then l-M
elif abs(m)+abs(l-m)+abs(L-l)<=tl and abs(m)+abs(l-m)+2*abs(L-l)+abs(M-l)<=tm: print('possible')
# take l, drop l at m, bring m-M then M-m then m-L
elif abs(l)+abs(m-l)+abs(M-m)<=tm and abs(l)+abs(m-l)+2*abs(M-m)+abs(L-m)<=tl: print('possible')
else: print('impossible')
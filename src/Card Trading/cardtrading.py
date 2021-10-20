n,t,k = list(map(int,input().split()))
cards = list(filter(lambda x: x.isnumeric(), input().split()))
card_dict = {}

for c in cards:
    card_dict[int(c)] = card_dict.get(int(c),0)+1

for p in range(1,t+1):
    b,s = list(map(int,input().split()))
    card_dict[int(p)] = [(2-card_dict.get(int(p),0))*b,card_dict.get(int(p),0)*s]

card_dict = list(card_dict.items())
card_dict.sort(key=lambda x:sum(x[1]))

answer = 0
for i in range(k):
    answer -= card_dict[i][1][0]
for j in range(k,len(card_dict)):
    answer += card_dict[j][1][1]

print(answer)
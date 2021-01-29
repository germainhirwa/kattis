n = int(input())
runners = {} # Dictionary of runners in the form of 'runner : [leg1, leg2]'
for _ in range(n):
    names,leg1,leg2 = input().split(" ")
    runners[names]=[float(leg1),float(leg2)]

min_time = 10000000
answer = []

for name in runners:
    runners2 = sorted(filter(lambda x: x[0] != name, runners.items()), key=lambda x:x[1][1])[:3]
    time = runners[name][0]+sum([runner[1][1] for runner in runners2])
    if time < min_time:
        min_time = time
        answer = [name]+[runner[0] for runner in runners2][::-1]

print(min_time)
for r in answer:
    print(r)
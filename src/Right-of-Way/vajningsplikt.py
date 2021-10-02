d = ["N", "E", "S", "W"]
a, b, c = list(map(lambda x: d.index(x[0]), input().split(" ")))

straight = (a - b) % 4 == 2 and (a - c) % 4 == 1
left = (b - a) % 4 == 1 and (a - c) % 4 in [1, 2]
print(["No", "Yes"][int(straight or left)])
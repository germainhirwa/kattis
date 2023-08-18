from random import *
door = ['A', 'B', 'C']
for _ in range(1000):
    shuffle(door)
    print(door[0])
    d, v = input().split()
    if int(v): print(d), input() # haha gotem
    else: print(door[1] if d==door[2] else door[2]), input() # RNG
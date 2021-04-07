from random import *

print(randint(1,2))

def do():
    while True:
        x = int(input())
        if x % 3 != 0:
            print(x+3-x%3) # guaranteed a multiple of 3
            if x+3-x%3 == 99:
                return
        else:
            if x == 99:
                return
            print(x+randint(1,2))
        
do()
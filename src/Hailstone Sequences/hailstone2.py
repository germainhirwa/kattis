# CS1010S Memoization
lut = {}

def f(n):
    return 3*n+1 if n%2 else n//2
    
def collatz_distance_memo(n):
    if n == 1:
        return 0
    else:
        if n in lut:
            return table[n]
        return collatz_distance_memo(f(n))+1
        
print(collatz_distance_memo(int(input()))+1)
n, dm = list(map(int, input().split()))
d = list(map(int, input().split()))

def do():
    for i in range(n):
        if d[i] <= dm:
            return f"It hadn't snowed this early in {i} years!"
    return "It had never snowed this early!"
    
print(do())
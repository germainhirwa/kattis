arr = [True] * 10
while True:
    n = int(input())
    if n == 0:
        break
    verdict = input()
    n -= 1
    if verdict == 'right on':
        print(['Stan is dishonest', 'Stan may be honest'][int(arr[n])])
        arr = [True] * 10
    elif verdict == 'too low':
        for i in range(n + 1):
            arr[i] = False
    elif verdict == 'too high':
        for i in range(n, 10):
            arr[i] = False
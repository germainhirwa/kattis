import sys; input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip()
    print(['Bash', 'Chikapu'][(s[0]==s[-1])^(len(s)%2)])
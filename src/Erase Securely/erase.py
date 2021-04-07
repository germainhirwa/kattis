n = int(input())
a = list(map(int,input()))
b = list(map(int,input()))
if (n % 2 and b == list(map(lambda x: 1-x, a))) or (n % 2 == 0 and a == b):
    print('Deletion succeeded')
else:
    print('Deletion failed')
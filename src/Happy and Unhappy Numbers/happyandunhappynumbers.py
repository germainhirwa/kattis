from bisect import *
import sys; input = sys.stdin.readline

check = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478}
hap = []
for i in range(1, 10**6+1):
    if sum(int(x)**2 for x in str(i)) in check: hap.append(i) 

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(bisect_right(hap, r)-bisect_left(hap, l))
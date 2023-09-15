import sys; input = sys.stdin.readline
def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []; par = [None] * len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i); temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    ans = 0; curr = temp[-1]
    while curr != None: ans += 1; curr = par[curr]
    return ans
'''
Source: https://stackoverflow.com/questions/30768610/finding-longest-common-subsequence-in-onlogn-time
"Given two permutations of numbers from 1 to N, find their LCS" can be solved in O(NlogN).
Let the sequences be A and B.
Define a sequence C. C[i] is the index of B[i] in A. (A[C[i]] = B[i])
LCS of A and B is the longest increasing subsequence of C.
'''
N = int(input()); A = [*map(int, input().split())]; B = [*map(int, input().split())]; R = {e:i for i,e in enumerate(A)}
print(2, lis([R[B[i]] for i in range(N)])+1)
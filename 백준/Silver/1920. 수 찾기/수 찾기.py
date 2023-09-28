import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))
A = sorted(A)

for x in arr:
    start, end = 0, N-1
    while start < end:
        mid = (start + end)//2

        if x > A[mid]:
            start = mid + 1
        else:
            end = mid


    if A[end]==x:
        print(1)
    else:
        print(0)
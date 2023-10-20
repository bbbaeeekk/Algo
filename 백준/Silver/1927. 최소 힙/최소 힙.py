import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n= int(input())
arr=[]
for _ in range(n):
    a = int(input())
    if a == 0:
        if arr:
            s = heappop(arr)
        else:
            s = 0
        print(s)
    else:
        heappush(arr,a)
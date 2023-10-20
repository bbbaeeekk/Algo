import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n=int(input())

arr= []
for _ in range(n):
    a = int(input())
    if a == 0:
        if arr:
            s,t = heappop(arr)
        else:
            t = 0
        print(t)
    else:
        if a < 0:
            heappush(arr,(-a,a))
        else:
            heappush(arr,(a,a))
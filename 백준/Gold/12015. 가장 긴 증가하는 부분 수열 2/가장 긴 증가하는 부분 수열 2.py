import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = [0]+list(map(int,input().split()))

DP = [0]
answer=0

for x in range(1,N+1):
    y = bisect_left(DP,arr[x])
    if arr[x] > DP[y-1]:
        
        DX = y
        if DX > len(DP)-1:   #수열의 길이가 가장긴값이  DP의 길이보다 길다면
            DP.append(arr[x])  # DP에 추가.

        elif arr[x] < DP[DX]:
            DP[DX]=arr[x]

        if answer < DX:
            answer = DX

print(answer)
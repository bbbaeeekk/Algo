import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

DP = []

for x in range(N):
    y = bisect_left(DP,arr[x])

    if y >= len(DP):   #수열의 길이가 가장긴값이  DP의 길이보다 길다면
        DP.append(arr[x])  # DP에 추가.

    elif arr[x] < DP[y]:
        DP[y]=arr[x]

print(len(DP))


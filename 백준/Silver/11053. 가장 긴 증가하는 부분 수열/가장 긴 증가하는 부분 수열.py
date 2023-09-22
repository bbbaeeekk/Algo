import sys
input = sys.stdin.readline

N = int(input()) # 1000이내
arr = list(map(int,input().split()))

DP = [0]*N
DP[0] = 1

for i in range(1,N):
    maxdp=0
    for j in range(i-1,-1,-1):
        if arr[i]>arr[j]:
            maxdp= max(maxdp,DP[j])
            DP[i] = DP[j]+1

    DP[i] = maxdp+1

print(max(DP))
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

DP_L = [0]*N
DP_R = [0]*N

DP_L[0] = 1
DP_R[-1] = 1

for i in range(1,N):
    maxdp=0
    for j in range(i-1,-1,-1):
        if arr[i]>arr[j]:
            maxdp= max(maxdp,DP_L[j])
            DP_L[i] = DP_L[j]+1

    DP_L[i] = maxdp+1

for i in range(N-2,-1,-1):
    maxdp=0
    for j in range(i+1,N):
        if arr[i]>arr[j]:
            maxdp= max(maxdp,DP_R[j])
            DP_R[i] = DP_R[j]+1

    DP_R[i] = maxdp+1

max_bio = 0
for x in range(N):
    max_bio = max(max_bio,DP_L[x]+DP_R[x]-1)
print(max_bio)
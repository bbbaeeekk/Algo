import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

arr2 = sorted(arr)

cnt = 0
cnt2= 0
for i in range(N):
    cnt+=arr2[i]*(N-i)

print(cnt)
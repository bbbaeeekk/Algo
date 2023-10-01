N, K = map(int,input().split())

arr = [int(input()) for _ in range(N)]

cnt = 0
for x in range(N-1,-1,-1):
    if arr[x] <= K:
        a = K//arr[x]
        K = K%arr[x]
        cnt += a
    if K == 0:
        break

print(cnt)
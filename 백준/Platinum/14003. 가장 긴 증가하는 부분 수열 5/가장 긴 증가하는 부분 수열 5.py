from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = [float('-inf')]
trace = [-1] * n

for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        trace[i] = len(dp) - 2
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        trace[i] = idx - 1

# 역추적으로 LIS 구하기
ans = []
idx = len(dp) - 2  # dp의 마지막 원소의 인덱스에서 시작
for i in range(n - 1, -1, -1):
    if trace[i] == idx:
        ans.append(arr[i])
        idx -= 1
ans.reverse()

print(len(ans))
print(*ans)

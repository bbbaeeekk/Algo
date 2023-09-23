n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
trace = [-1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            trace[i] = j

max_len = 0
idx = -1
for i in range(n):
    if max_len < dp[i]:
        max_len = dp[i]
        idx = i

ans = []
while idx != -1:
    ans.append(arr[idx])
    idx = trace[idx]
ans.reverse()

print(max_len)
print(' '.join(map(str, ans)))
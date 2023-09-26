N = int(input())
arr = str(input())

cnt=0
for x in range(N):
    cnt += int(arr[x])

print(cnt)
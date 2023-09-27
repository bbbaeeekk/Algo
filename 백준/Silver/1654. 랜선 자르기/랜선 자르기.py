import sys
input = sys.stdin.readline

K, N = map(int,input().split())

arr = [int(input()) for _ in range(K)]

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    n = 0
    for i in range(K):
        n += arr[i] // mid
    
    if n >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
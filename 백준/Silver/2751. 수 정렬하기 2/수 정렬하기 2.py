import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N

for i in range(N):
    n = int(input())
    arr[i] = n

for x in sorted(arr):
    print(x)
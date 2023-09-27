import sys
input = sys.stdin.readline

N = int(input())
arr = set()  

for _ in range(N):
    W = input().strip()
    arr.add(W)  

arr = sorted(arr, key=lambda x: (len(x), x))

for word in arr:
    print(word)
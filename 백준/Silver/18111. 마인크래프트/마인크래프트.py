import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())

## 제거 2초  쌓기 1초
## 0~256

area = N*M
TA = N*M/3

arr = [0]*257
for _ in range(N):
    blocks = list(map(int,input().split()))
    for x in blocks:
        arr[x] += 1

sums = 0
needs = 0

for i in range(257-1,-1,-1):
    if arr[i]>0:
        if sums+arr[i] >= TA:
            t = i
            break
        sums += arr[i]
for k in range(257):
    if k < t:
        needs += (t-k)*arr[k]
    else:
        B += (k-t)*arr[k]

while needs > B:
    needs -= area
    t -= 1

answer = 0
for j in range(257):
    if j < t:
        answer += (t-j)*arr[j]
    elif j > t:
        answer += 2*(j-t)*arr[j]

print(answer,end=' ')
print(t)
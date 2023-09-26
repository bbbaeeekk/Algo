N = int(input())

arr = list(map(int,input().split()))

mins=100000000
maxs=-100000000

for x in range(N):
    if arr[x]>maxs:
        maxs=arr[x]
    if arr[x]<mins:
        mins=arr[x]

print(mins,end=' ')
print(maxs)
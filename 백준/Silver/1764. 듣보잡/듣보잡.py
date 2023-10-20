import sys
input=sys.stdin.readline

n, m = map(int,input().split())

arr = set()
arr2= set()
for i in range(n):
    arr.add(input().rstrip())
for j in range(m):
    arr2.add(input().rstrip())

arr3 = sorted(list(arr&arr2))
print(len(arr3))

for k in arr3:
    print(k)
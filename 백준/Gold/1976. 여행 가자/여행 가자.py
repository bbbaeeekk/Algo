import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

parent = [0]*N
for i in range(N):
    parent[i] = i

for i in range(N-1):
    cities = list(map(int,input().split()))
    
    for j in range(i+1,N):
        if cities[j] == 1:
            union(i,j)

ncity = list(map(int,input().split()))
travel = list(map(int,input().split()))

flag = find(travel[0]-1)

for i in range(M):
    if flag != find(travel[i]-1):
        print('NO')
        break
else:
    print('YES')
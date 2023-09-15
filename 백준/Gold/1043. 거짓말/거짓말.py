import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int,input().split())

parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i

n, *truman = map(int, input().split())
for i in range(n):
    parent[truman[i]] = 0

parties = [0]*M
for i in range(M):
    a, *mans = map(int, input().split())
    parties[i] = mans[0]
    for j in range(a-1):
        union(mans[j],mans[j+1])

cnt = 0
for i in range(M):
    if find(parent[parties[i]]):
        cnt+=1

print(cnt)
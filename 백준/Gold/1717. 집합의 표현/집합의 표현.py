import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

n, m = map(int,input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b


for _ in range(m):
    t,a,b = map(int,input().split())
    if t == 0:
        union(a,b)

    elif t == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print("NO")

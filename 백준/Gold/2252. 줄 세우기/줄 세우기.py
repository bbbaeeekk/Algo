import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y]+=1

# 위상 정렬

result = []
q = deque()

for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)

while q:
    a = q.popleft()
    result.append(a)

    for i in graph[a]:
        indegree[i]-=1

        if indegree[i]==0:
            q.append(i)
for i in result:
    print(i,end=' ')

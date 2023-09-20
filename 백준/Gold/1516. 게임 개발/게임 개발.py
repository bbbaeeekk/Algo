import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N+1)]
time = [0]*(N+1)
DP=[0]*(N+1)
inDegree=[0]*(N+1)

for i in range(1,N+1):
    T, *build = map(int,input().split())
    time[i]=T
    for x in build:
        if x == -1:
            break
        else:
            arr[x].append(i)
            inDegree[i]+=1

q=deque()
for i in range(1,N+1):
    if inDegree[i] == 0:
        q.append(i)
        DP[i]=time[i]

while q:
    s = q.popleft()
    for x in arr[s]:
        DP[x]=max(DP[s]+time[x],DP[x])
        inDegree[x]-=1
        if inDegree[x]==0:
            q.append(x)

for x in range(1,N+1):
    print(DP[x])
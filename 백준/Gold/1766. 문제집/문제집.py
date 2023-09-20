import sys
import heapq

input = sys.stdin.readline

N, M = map(int,input().split())

q=[]
inDegree=[0]*(N+1)
arr=[[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    arr[A].append(B)
    inDegree[B]+=1

for i in range(1,N+1):
    if inDegree[i] == 0:
        heapq.heappush(q,i)
    
while q:
    s = heapq.heappop(q)
    print(s,end=' ')
    for x in arr[s]:
        inDegree[x]-=1
        if inDegree[x]==0:
            heapq.heappush(q,x)


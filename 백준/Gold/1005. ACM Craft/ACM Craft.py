import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

## 위상정렬 문제
## 목표지점에서 역순으로 탐색?
## DP를 이용해 해당 건물까지 걸리는 시간 탐색
## dp[b]->a=10 탐색후 dp[a]=10 dp[c]->a =20 탐색후 dp[a]=20으로 갱신? 


for _ in range(T):
    N, K = map(int,input().split())  ## 건물의 갯수:N , 건설순서규칙수(선의수):K
    D = [-1] + list(map(int,input().split()))  ## 각 건물 시간

    DP= [0]*(N+1)
    inDegree = [0]*(N+1)
    arr = [[] for _ in range(N+1)]

    for _ in range(K):
        start, end = map(int,input().split())
        arr[start].append(end)
        inDegree[end]+=1

    q = deque()
    # 진입차수 0인거 찾아서 넣기    
    for i in range(1,N+1):
        if inDegree[i]==0:
            q.append(i)
            DP[i]=D[i]

    while q:
        s=q.popleft()
        for x in arr[s]:
            inDegree[x]-=1
            DP[x]=max(DP[s]+D[x],DP[x]) 
            if inDegree[x]==0:
                q.append(x)

    W = int(input())
    print(DP[W])
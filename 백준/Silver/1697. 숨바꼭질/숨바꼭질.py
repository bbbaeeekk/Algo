from collections import deque

n, k = map(int,input().split())

q = deque([[n,0]])
visited = [False]*100001



while q:
    s,t = q.popleft()
    visited[s] = True
    if s == k:
        print(t)
        break

    for a in [s-1,s+1,s*2]:
        if  0 <= a <= 100000 and not visited[a]:
            q.append([a,t+1])

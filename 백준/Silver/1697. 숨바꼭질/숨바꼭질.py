from collections import deque

n, k = map(int,input().split())

q = deque([n])
visited = [0]*100001

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break

    for a in [s-1,s+1,s*2]:
        if  0 <= a <= 100000 and not visited[a]:
            visited[a] = visited[s]+1
            q.append(a)


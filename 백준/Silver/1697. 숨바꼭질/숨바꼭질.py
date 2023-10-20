from collections import deque

n, k = map(int,input().split())

q = deque([[n,0]])
visited = [False]*100001

def inragne(x):
    if 0 <= x <= 100000:
        return True
    return False

while q:
    s,t = q.popleft()
    visited[s] = True
    if s == k:
        print(t)
        break

    for a in [s-1,s+1,s*2]:

        if inragne(a) and not visited[a]:
            q.append([a,t+1])
    a = s-1


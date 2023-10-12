from collections import deque

m, n, = map(int,input().split())
# 상자의크기가로세로 m*n 

arr = [list(map(int,input().split())) for _ in range(n)]
# 1 익은토마토, 0 익지 않은토마토, -1 빈칸

# 상하좌우
dx,dy = [-1,1,0,0],[0,0,-1,1]

def outofindex(x,y):
    if 0 <= x < n and 0 <= y < m:
        return False
    else:
        return True

def bfs():
    q = deque([])

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i,j,0))
    cnt = 0
    while q:
        sx,sy,k = q.popleft()
        cnt+=1
        for i in range(4):
            nx, ny = sx+dx[i],sy+dy[i]
            if not outofindex(nx,ny):
                if arr[nx][ny] == 0:
                    q.append((nx,ny,k+1))
                    arr[nx][ny] = 1

    flag = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                flag = False
    if flag:
        print(k)
    else:
        print('-1')
bfs()
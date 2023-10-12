from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int,input().split())
# 상자의크기가로세로 m*n , 상자의수 h

arr = []
for _ in range(h):
    A = [list(map(int,input().split())) for _ in range(n)]
    arr.append(A)
# 1 익은토마토, 0 익지 않은토마토, -1 빈칸

# 상하좌우업다운
dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,1,-1]

def outofindex(x,y,z):
    if 0 <= x < n and 0 <= y < m and 0 <= z < h:
        return False
    else:
        return True

def bfs():
    q = deque([])

    for i in range(n):
        for j in range(m):
            for k in range(h):
                if arr[k][i][j] == 1:
                    q.append((k,i,j,0))
    cnt = 0
    while q:
        sz,sx,sy,k = q.popleft()
        cnt+=1
        for i in range(6):
            nz, nx, ny = sz+dz[i],sx+dx[i],sy+dy[i]
            if not outofindex(nx,ny,nz):
                if arr[nz][nx][ny] == 0:
                    q.append((nz,nx,ny,k+1))
                    arr[nz][nx][ny] = 1

    flag = True
    for i in range(n):
        for j in range(m):
            for t in range(h):
                if arr[t][i][j] == 0:
                    flag = False
    if flag:
        print(k)
    else:
        print('-1')
bfs()
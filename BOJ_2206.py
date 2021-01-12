# BFS / 3차원 배열
import sys
from collections import deque

# 입력받기
n,m = map(int,sys.stdin.readline().split(" "))
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 방향 설정(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


# bfs 소스코드 구현
def bfs():
    queue = deque()
    queue.append([0,0,1])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # 방문 확인용
    visited[0][0][1]=1
    # 큐가 빌 때까지 반복
    while queue:
        x,y,z = queue.popleft()
        if x==n-1 and y==m-1: # 시작점이 끝나는 점일때
            return visited[x][y][z]
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 안에 들어올 때
            if 0<=nx<n and 0<=ny<m:
                # 벽&뚫을수O
                if graph[nx][ny] ==1 and z==1:
                    queue.append((nx,ny,0))
                    visited[nx][ny][0]=visited[x][y][1]+1
                # 벽X&뚫을수X
                if graph[nx][ny] ==0 and z==0:
                    queue.append((nx,ny,z))
                    visited[nx][ny][z]=visited[x][y][z]+1
    return -1
print(bfs())
                













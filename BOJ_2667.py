# 단지 번호 붙이기 _ DFS
# 1
# 입력
n = int(input())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))
# dfs
count=0
def dfs(x,y):
    global count
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        count+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

answer=[]
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
            answer.append(count)
            count = 0
print(result)
answer.sort()
for ans in answer:
    print(ans)

print()

n = int(input())
visited = [[0] for _ in range(n)] for _ in range(n)
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
# 동서남북 좌표
dx = [0,0,1,-1]  
dy = [1,-1,0,0]
cnt = 0 
answer = []
    
def dfs(x,y):
    global cnt
    visited[x][y] = 1
    cnt += 1 #탐색할 때마다 1을 더해준다 
    # 동서남북 방향
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] ==1: #인접한 곳의 좌표가 범위 내이고 방문했다면 
            visited[nx][ny] = 1 #방문한 곳으로 처리해준다 
            dfs(nx,ny) #조건을 만족하는 지점에서 다시 탐색을 시작한다 
    return cnt 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(dfs(i,j))
print(len(answer))
answer.sort()
for ans in answer:
    print(ans)


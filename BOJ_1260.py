# DFS와 BFS
from collections import deque

# 입력받기
n, m, v = map(int, input().split())

data = [[0] * (n + 1) for i in range(n + 1)]

visited = [0 for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    data[a][b]=1
    data[b][a]=1 

# DFS
def dfs(data, v, visited):
    visited[v] = 1
    print(v, end = '')
    for i in range(1,n+1):
        if not visited[i] and data[v][i]==1:
            dfs(data, i ,visited)

# BFS  
def bfs(data,v,visited):
    q = [v]
    visited[v]=0
    while q:
        v = q.pop(0)
        print(v,end='')
        for i in range(1,n+1):
            if visited[i]==1 and data[v][i]==1:
                q.append(i)
                visited[i]=0
dfs(data,v,visited)
print()
bfs(data,v,visited)
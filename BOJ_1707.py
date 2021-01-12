# 이분그래프 BFS
from collections import deque
k = int(input())
for _ in range(k):
    v,e = (map(int,input().split()))
    graph = [[0] for _ in range(v+1)]

def bfs(start):
    graph[start]=1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()

# ?
        







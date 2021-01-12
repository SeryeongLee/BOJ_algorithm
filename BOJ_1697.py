# 숨바꼭질 BFS / DFS시 무한루프
from collections import deque
n,k=map(int,input().split())
max = 10**5
d = [0]*(max+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(d[x])
            break
        for next in (x-1,x+1,x*2):
            if 0<=next<max and not d[next]:
                d[next]=d[x]+1
                q.append(next)

bfs()

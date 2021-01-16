# 바이러스 _ DFS:모두 탐색

# 입력받기
n = int(input())
m = int(input())
data = [[0]*(n+1) for i in range(n+1)]
answer = []

for i in range(m):
    a,b = map(int,input().split())
    data[a][b]=1
    data[b][a]=1

# DFS
def dfs(v):
    answer.append(v)
    for i in range(1,n+1):
        if i not in answer and data[v][i]==1:
            dfs(i)
    return (len(answer)-1) # 1번 제외
print(dfs(1))
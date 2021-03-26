from collections import deque

# 깊이 우선 탐색
def dfs(x):
    visited_dfs[x] = 1   # 방문처리

    print(x, end=" ")    # 현재 정점 출력

    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)    # 재귀


# 너비 우선 탐색
def bfs(x):
    q = deque()
    q.append(x)
    visited_bfs[x] = 1

    print(x, end=" ")

    while q:
        nx = q.popleft()
        for i in graph[nx]:
            if not visited_bfs[i]:
                print(i, end=" ")
                visited_bfs[i] = 1
                q.append(i)


# 입력
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

# 그래프 입력
for i in range(m):
    a, b = map(int, input().split())
    if not a in graph[b]:
        graph[b].append(a)
    if not b in graph[a]:
        graph[a].append(b)

# 그래프 정렬
for g in graph:
    g.sort()

# 출력
dfs(v)
print()
bfs(v)
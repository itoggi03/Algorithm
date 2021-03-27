from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        nx = q.popleft()
        for i in linked[nx]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결선 수

# 각 컴퓨터의 인덱스에 연결된 컴퓨터 번호를 저장
linked = [[] for _ in range(n+1)]
for i in range(m):
    a, b =map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)

visited = [0] * (n+1)

bfs(1)

# 1번째 컴퓨터를 제외하고 visited의 1 개수 세기
cnt = 0
for i in range(n+1):
    if i != 1:
        if visited[i] == 1:
            cnt += 1

print(cnt)
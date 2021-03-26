# 03/26 알고리즘

> BOJ1260, BOJ2178

<br>

<br>

## 1. BOJ1260 DFS와 BFS

> 문제링크: https://www.acmicpc.net/problem/1260

<br>

### 나의 코드

```python
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
```

<br>

### 입력

```bash
5 5 3
5 4
5 2
1 2
3 4
3 1
```

### 출력

```bash
3 1 2 5 4
3 1 4 2 5
```

<br>

### 풀이

- DFS와 BFS의 가장 기본 문제이다.
- DFS는 재귀를 이용하여 깊이 우선 탐색을 했고, BFS는 deque를 이용하여 너비 우선 탐색을 하였다.

---

<br>

<br>

## 2. BOJ2178 미로탐색

> 문제링크: https://www.acmicpc.net/problem/2178

<br>

### 나의 코드

```python
from collections import deque

# 인덱스가 미로를 넘었는지 아닌지 확인해주는 함수
def check(i, j):
    if i >= 0 and i < n and j >= 0 and j < m:
        return True
    else:
        return False

def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for d in range(4):
            nX, nY = x + dr[d], y +dc[d]

            # 다음 좌표가 벽이 아니고 1일 경우
            if check(nX, nY) and miro[nX][nY] == 1:
                q.append((nX, nY))
                miro[nX][nY] = miro[x][y] + 1  # 전 좌표에서 +1

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

# 상/하/좌/우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

bfs(0, 0)

# 출력
print(miro[n-1][m-1])
```

<br>

### 입력

```bash
4 6
101111
101010
101011
111011
```

### 출력

```bash
15
```

<br>

### 풀이

- BFS를 이용해 현재 좌표의 상하좌우를 살피며 이동
- 다음 좌표가 벽이 아니고 1일 경우에만(최초 방문시에만) 전 좌표에서 +1 한 값을 넣어준다.
- 따라서 (N, M) 좌표의 값이 최소거리가 된다.

<br>

### 회고

- 최초 방문시에만 전 좌표에서 +1 하는 것이 최소거리를 체크하는것을 한번에 이해하기 어려웠다. BFS이니까 단계별로 그래프를 내려가고, 이 때 1이 아닌 값이 있다면 그 전 단계에서 이미 내려간 것이므로 그것이 최소거리가 된다.
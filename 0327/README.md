# 03/27 알고리즘

> BOJ2606, BOJ2667

<br>

<br>

## 1. BOJ2606 바이러스

> 문제링크: https://www.acmicpc.net/problem/2606

<br>

### 나의 코드

```python
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
```

<br>

### 입력

```bash
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

### 출력

```bash
4
```

<br>

### 풀이

- BFS로 간단하게 풀 수 있는 문제이다.
- visited로 1과 연결된 컴퓨터들을 1로 체크하고, 마지막에 visited의 1개수를 세서 출력한다.

---

<br>

<br>

## 2. BOJ2667 단지번호 붙이기

> 문제링크: https://www.acmicpc.net/problem/2667

<br>

### 나의 코드

```python
from collections import deque

# 인덱스가 배열의 범위를 넘었는지 아닌지 판단해주는 함수
def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False

# 단지내 집의 수를 bfs로 탐색
def bfs(r, c):
    cnt = 1
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        x, y = q.popleft()
        
        # 상하좌우 4개의 방향으로 탐색
        for d in range(4):
            newX = x + dr[d]
            newY = y + dc[d]
            
            # arr의 인덱스를 넘지 않고, 방문한적이 없고, 값이 1인 경우 
            if check(newX, newY) and visited[newX][newY] == 0 and arr[newX][newY]:
                q.append((newX, newY))
                visited[newX][newY] = 1 # 방문체크
                cnt += 1    # 집 개수 +1
    
    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0] * n for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        # 값이 1이고 방문한 적이 없는 경우에만 bfs 후 집의 수 ans에 append
        if arr[i][j] == 1 and visited[i][j] == 0:
            tmp = bfs(i, j)
            ans.append(tmp)

# 각 단지내 집의 수를 오름차순 정렬
ans.sort()

# 총 단지수, 각 단지내 집의 수 출력
print(len(ans))
for a in ans:
    print(a)
```

<br>

### 입력

```bash
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

### 출력

```bash
3
7
8
9
```

<br>

### 풀이

- BFS를 이용하여 상하좌우 방향으로 집을 탐색했다.

- 주어지는 지도 크기만큼 visited라는 배열을 생성해서 방문체크를 해주었다.

  ex) 방문한 곳이 arr[i][j]라면 visited[i][j]에 1을 넣어준다.

- 방문체크를 할 때마다 cnt를 증가시켜 단지내 집의 수를 체크해주었다.

<br>

### 또 다른 풀이

- visited를 따로 만들어서 방문체크하는 것이 아니라, 방문하면 그 자리의 값을 0으로 만들어버린다.
- 그리고 그 자리의 값이 1일 때만 방문하면 된다!

```python
from collections import deque

# 인덱스가 배열의 범위를 넘었는지 아닌지 판단해주는 함수
def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False

# 단지내 집의 수를 bfs로 탐색
def bfs(r, c):
    cnt = 1
    q = deque()
    q.append((r, c))
    # visited[r][c] = 1
    arr[r][c] = 0

    while q:
        x, y = q.popleft()

        # 상하좌우 4개의 방향으로 탐색
        for d in range(4):
            newX = x + dr[d]
            newY = y + dc[d]

            # arr의 인덱스를 넘지 않고, 방문한적이 없고, 값이 1인 경우
            if check(newX, newY) and arr[newX][newY]:
                q.append((newX, newY))
                arr[newX][newY] = 0 # 방문체크
                cnt += 1    # 집 개수 +1

    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# visited = [[0] * n for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        # 값이 1이고 방문한 적이 없는 경우에만 bfs 후 집의 수 ans에 append
        if arr[i][j] == 1:
            tmp = bfs(i, j)
            ans.append(tmp)

# 각 단지내 집의 수를 오름차순 정렬
ans.sort()

# 총 단지수, 각 단지내 집의 수 출력
print(len(ans))
for a in ans:
    print(a)
```
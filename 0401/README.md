# 04/01 알고리즘

> BOJ2468, BOJ2573

<br>

<br>

## 1. BOJ2468 안전영역

> 문제링크: https://www.acmicpc.net/problem/2468

<br>

### 나의 코드

```python
from collections import deque

# 인덱스가 벗어났는지 아닌지 체크해주는 함수
def check(i, j):
    if i >= 0 and i < n and j >= 0 and j < n:
        return True
    else:
        return False

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        nx, ny = q.popleft()
        
        # 상하좌우 for문
        for d in range(4):
            newX = nx + dr[d]
            newY = ny + dc[d]
            
            # 인덱스가 벗어나지 않고, 방문한적 없고, 기준 높이보다 높은곳만 방문
            if check(newX, newY) and not visited[newX][newY] and arr[newX][newY] > h:
                visited[newX][newY] = 1
                q.append((newX, newY))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 주어진 배열에서 높이가 가장 큰 값을 maxH에 저장
maxH = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > maxH:
            maxH = arr[i][j]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

h = 0
maxResult = 1

# 기준 높이를 1부터 maxH까지 for문 돌림
for i in range(1, maxH):
    h = i
    result = 0
    visited = [[0] * n for _ in range(n)]
    
    for j in range(n):
        for k in range(n):
            # 방문한적 없고 기준 높이보다 높은 곳만 bfs
            if not visited[j][k] and arr[j][k] > h:
                bfs(j, k)
                result += 1 # 안전영역 개수 +1
                
    # 기준 높이에 대한 안전영역 개수 체크가 끝날 경우 최대값 업데이트
    if result > maxResult:
        maxResult = result

# 출력
print(maxResult)
```

<br>

### 입력

```bash
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
```

### 출력

```bash
5
```

<br>

### 풀이

- 주어진 배열에서 최대 높이를 미리 저장한 후, `1~최대높이`만큼 for문을 돌려서 모든 기준 높이에 대해 탐색한다.
- 각 기준 높이에서 방문한적이 없고, 기준높이보다 높은 곳에서만 bfs 함수를 호출한다. bfs가 끝난 후엔 안전영역 개수를 +1 해준다.
- bfs 함수는 상하좌우 4방향으로 탐색하며, 방문한적 없고 기준 높이보다 높은 곳만 방문하여 방문체크한다.

---

<br>

<br>

## 2. BOJ2573

> 문제링크: https://www.acmicpc.net/problem/2573

<br>

### 나의 코드

```python
from collections import deque
import copy

# 인덱스가 벗어났는지 체크해주는 함수
def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    else:
        return False

# 빙하의 상하좌우에 0이 몇개 있는지 체크해 개수를 return하는 함수
def zero_check(r, c):
    cnt = 0
    
    # 상하좌우 체크
    for d in range(4):
        newR = r + dr[d]
        newC = c + dc[d]
        if check(newR, newC) and not arr[newR][newC]:
            cnt += 1
    return cnt

# 한 덩어리의 빙하를 체크하기 위한 BFS
def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            newX = x + dr[d]
            newY = y + dc[d]
            if check(newX, newY) and not visited[newX][newY] and newArr[newX][newY]:
                visited[newX][newY] = 1
                q.append((newX, newY))
    return

# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ice_cnt = 0 # 빙하 덩어리 개수
result = 0  # 최소 시간(년)

# 빙하 덩어리 개수가 2개가 되기 전까지 반복
while ice_cnt < 2:
    ice_cnt = 0
    newArr = [[0] * m for _ in range(n)]
    
    # 각 빙하의 주변에 있는 0 개수 체크하여 원래 높이에서 빼기
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j]:
                tmp = zero_check(i, j)
                if arr[i][j] >= tmp:
                    newArr[i][j] = arr[i][j] - tmp
                else:
                    # 뺐을 때 음수이면 0을 넣어주기
                    newArr[i][j] = 0
    
    # 1년 지난 후의 빙하를 arr에 업데이트
    arr = copy.deepcopy(newArr)

    visited = [[0] * m for _ in range(n)]
    # BFS
    for i in range(1, n-1):
        for j in range(1, m-1):
            if newArr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                ice_cnt += 1
    
    # while문이 끝나기 전에 빙하덩어리 개수가 0이라면 0 출력 후 while문 탈출
    if ice_cnt == 0:
        print(0)
        break
        
    result += 1 # 시간(년) +1

# 빙하 덩어리 개수가 0이 아니라면 result 출력
if ice_cnt:
    print(result)
```

<br>

### 입력

```bash
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
```

### 출력

```bash
2
```

<br>

### 풀이

- 먼저 각 빙하의 상하좌우에 0이 몇개 있는지 체크하여 `(원래 높이) - (주변 0 개수)`를 해준다.
- 빙하가 1년치만큼 녹은 후, BFS를 돌려 몇 덩어리의 빙하가 있는지 체크한다. 덩어리 개수가 2개가 될때까지 while문으로 모든 과정을 반복하고, 덩어리 개수가 2개가 될 경우 while문이 끝나게 되고 걸린 시간(년)을 출력한다.
- while문이 끝나기 전에 빙하가 다 녹아서 덩어리 개수가 0개가 될 경우 0 출력 후 break

<br>

### 회고

- while문 안에 이중 for문이 여러개 있는 구조가 시간이 굉장히 오래 걸릴거라 생각했다. 역시나 python3로는 시간초과가 나오고 pypy3로 해야 통과가 되었다.
- 시간 복잡도를 줄이기 위한 방법을 더 생각해볼 필요가 있다.


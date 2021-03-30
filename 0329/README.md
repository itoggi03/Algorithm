# 03/29 알고리즘

> BOJ2644, BOJ7569

<br>

<br>

## 1. BOJ2664 촌수계산

> 문제링크: https://www.acmicpc.net/problem/2644

<br>

### 나의 코드

```python
def dfs(x, cnt):
    global ans

    # 찾아야할 사람을 만났을 경우 ans에 카운트 개수 업데이트하고 return
    if x == n2:
        ans = cnt
        return

    # 더이상 연결된 노드가 없을 경우 return
    if not arr[x]:
        return

    visited[x] = 1

    for i in arr[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)

    return

# 입력
n = int(input())
n1, n2 = map(int, input().split())
m = int(input())

# 친척 관계도
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = -1
visited = [0] * (n+1)
for i in range(n+1):
    for j in range(len(arr[i])):
        if arr[i][j] == n1:
            dfs(arr[i][j], 0)

print(ans)
```

<br>

### 입력

```bash
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

### 출력

```bash
3
```

<br>

### 풀이

- DFS를 이용하여 풀이하였다.
- 친척 관계도를 양방향으로 연결된 것으로 인식하여 배열을 생성해주었고, 촌수를 계산해야할 두 사람 중 첫번째 사람(n1)을 시작으로 DFS를 호출하였다. DFS가 호출되었을 때, 찾아야할 사람(n2)인 경우 ans에 카운트 업데이트 후 return 하고, 더이상 연결된 노드가 없을 경우에도 return 한다. 두 경우에 모두 해당되지 않을 경우 연결된 노드에서 방문하지 않았던 노드들에 대해 cnt 수를 +1 하여 DFS를 다시 호출한다.

---

<br>

<br>

## 2. BOJ7569 토마토

> 문제링크: https://www.acmicpc.net/problem/7569

<br>

### 나의 코드

```python
from collections import deque

def check(i, j, k):
    if i >= 0 and i < h and j >= 0 and j < n and k >= 0 and k < m:
        return True
    else:
        return False

def bfs(queue):
    days = -1
    tmp = []

    while queue:
        # 시작점들을 for문으로 돌리고 각각 6방향으로 확인
        for q in queue:
            f, r, c = q
            for d in range(6):
                newF = f + df[d]
                newR = r + dr[d]
                newC = c + dc[d]

                if check(newF, newR, newC) and tomato[newF][newR][newC] == 0:
                    tomato[newF][newR][newC] = 1
                    tmp.append((newF, newR, newC))

        # 하루가 지난 후 이므로 days +1
        days += 1
        queue = tmp     # queue 업데이트
        tmp = []        # tmp 초기화
    return days

# bfs를 돌리고 토마토가 다 익었는지 확인하는 함수
def check_tomato():
    ans = 0
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1:
                    queue.append((i, j, k))

    ans = bfs(queue)

    # bfs를 다 돌렸는데 다 익지 않았을 경우 토마토가 하나라도 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not tomato[i][j][k]:
                    return -1

    return ans

m, n, h = map(int, input().split())

tomato = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        tmp = list(map(int, input().split()))
        tomato[i].append(tmp)

# 상/하/좌/우/앞/뒤
df = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]

result = check_tomato()

print(result)
```

<br>

### 입력

```bash
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
```

### 출력

```bash
4
```

<br>

### 풀이

- 토마토 배열을 3차원으로 입력받는다.
- 맨 처음에 3중 for문을 돌려서 익은 토마토들의 인덱스를 queue에 담는다.
- queue를 인자로 bfs함수를 호출하고, 담겨져있는 인덱스들을 for문을 돌려 맨처음에 익어있던 토마토들을 대상으로 bfs를 동시에 수행(6방향 체크)
- for문이 끝나면 하루가 끝난 것이므로 days를 +1 해주고 queue를 업데이트 후 다시 for문 수행
- bfs가 끝난 후 토마토들을 체크하여 하나라도 익지 않은 토마토가 있다면 -1 출력
- 아닐 경우 days 출력(days 초기값을 -1로 해주어 원래부터 다 익어있었다면 0을 출력하게함)

<br>

### 회고

- 맨처음에 익어있던 토마토들을 대상으로 동시에 bfs를 돌려야한다는 생각을 하지 못해서 계속 틀렸었다... 앞으론 문제에 대해 정확히 파악하고 풀도록 해야겠다.
- 3차원 배열 문제는 처음이어서 입력받을 때 헤맸다.
# 04/03 알고리즘

> BOJ14503 로봇 청소기

<br>

## BOJ14503 로봇 청소기

> 문제링크: https://www.acmicpc.net/problem/14503

<br>

### 나의 코드

```python
from collections import deque

# 인덱스 벗어났는지 체크하는 함수
def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    else:
        return False

def bfs(r, c, d):
    cnt = 1
    q = deque()
    q.append((r, c))
    arr[r][c] = 2

    while q:
        x, y = q.popleft()
        for i in range(4):
            # 현재 방향의 왼쪽으로 새 방향 설정
            if d:
                d -= 1
            else:
                d = 3
            newX = x + dr[d]
            newY = y + dc[d]

            # 왼쪽 방향에 아직 청소하지 않은 곳이 있다면 q에 그 칸 넣고, 카운트 세고, 청소한 다음 다시 왼쪽부터 탐색 진행
            if check(newX, newY) and not arr[newX][newY]:
                q.append((newX, newY))
                cnt += 1
                arr[newX][newY] = 2
                break

            # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한칸 후진 후 다시 왼쪽부터 탐색 진행
            if i == 3:
                newX = x + dr[(d+2) % 4]
                newY = y + dc[(d+2) % 4]
                q.append((newX, newY))

                # 뒤쪽 방향이 벽이라 후진 할 수 없는 경우 작동 멈춤
                if arr[newX][newY] == 1:
                    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 현재 로봇 청소기가 있는 좌표와 바라보는 방향
# d - 0:북 / 1:동 / 2:남 / 3:서
arr = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = bfs(r, c, d)

print(result)
```

<br>

### 입력

```bash
3 3
1 1 0
1 1 1
1 0 1
1 1 1
```

### 출력

```bash
1
```

<br>

### 풀이

- 로봇 청소기의 현재 방향에서 왼쪽으로 네방향을 탐색하면서 청소 안한 칸이 있을 경우 그 칸으로 가고, 네 방향 모두 벽이거나 청소가 이미 되어 있는 경우 현재 방향을 유지하며 후진한다. 뒤쪽이 벽이라 후진도 못하는 경우 작동을 멈춘다.
- BFS 형태로 풀었지만 중간에 청소해야할 칸이 있다면 for문을 탈출 후 다시 그 칸에서부터 탐색을 하므로 완전한(?) 너비우선 탐색 기법이라 할 수는 없다.
- 혼자 고민하다 못풀어서 다른 사람의 코드를 참고해 풀었다.
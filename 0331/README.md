# 03/31 알고리즘

> BOJ1697

<br>

<br>

## 1. BOJ1697

> 문제링크: https://www.acmicpc.net/problem/1697

<br>

### 나의 코드

```python
from collections import deque

def bfs(s, time):
    q = deque()
    q.append((s, time))

    while q:
        ns, t = q.popleft()

        # 동생이 있는 곳일 경우 return
        if ns == k:
            return t

        # 인덱스가 넘어갈 경우
        if ns < 0 or ns > 100000:
            continue

        if not visited[ns]:
            visited[ns] = 1
            q.append((ns-1, t+1))
            q.append((ns+1, t+1))
            q.append((ns*2, t+1))

n, k = map(int, input().split())

visited = [0] * 100001  # 방문체크

result = bfs(n, 0)  # bfs

print(result)   # 출력
```

<br>

### 입력

```bash
5 17
```

### 출력

```bash
4
```

<br>

### 풀이

- 아래처럼 BFS를 이용하여 3개씩 가지를 계속 치는 방식으로 문제를 풀었다.

  ![](README.assets/BOJ1697숨바꼭질.jpg)

- 처음에 방문체크를 따로 안만들어줬더니, 방문했던 곳까지 다시 가서 q에 append 하는 바람에 메모리 초과가 나왔다. 방문했던 곳을 또 다시 가는 것은 최솟값이 아니므로 visited를 만들어서 방문하지 않았던 곳만 가게 했다.
- 현재 위치가 0보다 작거나, n의 최대 범위인 100,000보다 클 경우를 제거해줘야 런타임에러(IndexError)가 나지 않는다.
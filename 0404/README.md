# 04/04 알고리즘

> BOJ9205

<br>

## BOJ9205 맥주 마시면서 걸어가기

> 문제링크: https://www.acmicpc.net/problem/9205

<br>

### 나의 코드

```python
from collections import deque

# 두 포인트간의 거리가 1000이 넘지 않을 경우 True를 반환해주는 함수
def distance_check(a, b):
    tmp = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if tmp > 1000:
        return False
    else:
        return True

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        p = q.popleft()
        for i in arr[p]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

t = int(input())    # 테스트 케이스 개수

for _ in range(t):
    n = int(input())    # 편의점 개수
    location = [list(map(int, input().split())) for _ in range(n+2)]

    # 각 포인트간의 거리가 1000이 넘지 않는 경우만 해당하는 인덱스에 인덱스 담아놓기
    arr = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i != j:
                if distance_check(location[i], location[j]):
                    arr[i].append(j)

    visited = [0] * (n+2)
    bfs(0)

    # 마지막지점(페스티벌)에 방문한 적이 없다면 sad, 있다면 happy 출력
    if visited[-1]:
        print('happy')
    else:
        print('sad')
```

<br>

### 입력

```bash
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
```

### 출력

```bash
happy
sad
```

<br>

### 풀이

- 주어진 n+2개의 좌표들끼리 비교하며 서로의 거리가 1000이 넘지 않는 경우에 해당 인덱스에 그 지점을 넣는다.

  즉, 0번째 좌표에서 1번째 좌표와 2번째 좌표까지의 거리가 1000이 넘지 않는다면,

  ```tsx
  [[1, 2] ...]
  ```

  이런 방식으로 배열을 생성한다.

- 그 후 0번째부터 BFS를 실행시킨다.

- BFS를 실행한 후 visited의 마지막 인덱스(페스티벌 좌표에 해당)에 해당하는 값이 1이라면(방문한적이 있다면) 페스티벌까지 갈 수 있는 것이므로 'happy' 출력, 아니라면 'sad' 출력

<br>

### 회고

처음에는 각 좌표의 앞 뒤간 거리만 체크해서 1000이 넘지 않으면 갈 수 있고 아니면 못가는 것이 아닌가? 생각하고 풀어서 틀렸다. 편의점을 주어진 순서대로 가지 않을 수 있다는 점을 간과한 것이다. 그 후 다른 사람의 풀이를 참고하고 나서야 BFS를 이용하여 어떤 방식으로 풀어야할지 감이 잡혔다. 문제를 어떤 방식으로 풀어야할지 정하는 과정이 아직 제일 힘든 것 같다. 많은 문제를 풀면서 감을 익혀야 할 것 같다.
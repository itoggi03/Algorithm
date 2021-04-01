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
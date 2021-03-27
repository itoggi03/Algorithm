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
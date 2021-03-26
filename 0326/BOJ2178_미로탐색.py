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
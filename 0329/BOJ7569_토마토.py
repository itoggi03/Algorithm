from collections import deque

def check(x, y):
    if x >= 0 and x < n*h and y >= 0 and y < m:
        return True
    else:
        return False

def bfs(i, j, cnt):
    q = deque()
    q.append((i, j, cnt))
    visited[i][j] = 1

    while q:
        x, y, c = q.popleft()
        for d in range(6):
            newX = x + dr[d]
            newY = y + dc[d]
            if check(newX, newY) and visited[newX][newY] == 0 and tomato[newX][newY] == 0:
                visited[newX][newY] = 1
                q.append((newX, newY, c+1))

    return c


def print_answer():
    for i in range(n * h):
        for j in range(m):
            if tomato[i][j] == 0 and visited[i][j] == 0:
                return -1
    return 1


def check_tomato():
    for i in range(n * h):
        for j in range(m):
            if tomato[i][j] == 0:
                return 1
    return 0


m, n, h = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n*h)]

# 상/하/좌/우/앞/뒤
dr = [-1, 1, 0, 0, n, -n]
dc = [0, 0, -1, 1, 0, 0]

visited = [[0] * m for _ in range(n*h)]

check_tomato_result = check_tomato()
if check_tomato_result == 1:
    ans = 0
    for i in range(n*h):
        for j in range(m):
            if not visited[i][j] and tomato[i][j] == 1:
                ans = bfs(i, j, 0)
    tmp = print_answer()

    if tmp == -1:
        print(-1)
    else:
        if ans:
            print(ans)
        else:
            print(-1)
else:
    print(0)
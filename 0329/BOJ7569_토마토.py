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

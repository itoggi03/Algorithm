from collections import deque

# 좌표가 배열 크기 넘었는지 체크하는 함수
def check(x, y):
  if 0 <= x < n and 0 <= y < m:
    return True
  else:
    return False


# 빙산 덩어리 개수를 체크하는 함수
def bfs(i, j):
  q = deque([[i, j]])

  while q:
    x, y = q.popleft()
    for d in range(4):
      newX, newY = x + dr[d], y + dc[d]
      if check(newX, newY) and not visited[newX][newY] and arr[newX][newY]:
        q.append([newX, newY])
        visited[newX][newY] = 1
  
  return


# 해당 좌표 동서남북 네 방향의 0 개수를 체크하는 함수
def checkZero(x, y):
  cnt = 0
  for d in range(4):
    newX, newY = x + dr[d], y + dc[d]
    if check(newX, newY) and not arr[newX][newY]:
      cnt += 1
  return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

year = 0
while True:
  zero = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if arr[i][j]:
        zero[i][j] = checkZero(i, j)

  isAllMelt = 0
  for i in range(n):
    for j in range(m):
      tmp = arr[i][j] - zero[i][j]
      if tmp < 0:
        arr[i][j] = 0
      else:
        arr[i][j] = tmp
        isAllMelt += tmp

  if isAllMelt == 0:
    print(0)
    break

  year += 1

  visited = [[0] * m for _ in range(n)]
  iceberg = 0
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and  arr[i][j]:
        bfs(i, j)
        iceberg += 1
  
  if iceberg >= 2:
    print(year)
    break
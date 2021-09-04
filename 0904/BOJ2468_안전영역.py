from collections import deque

def check(x, y):
  if 0 <= x < n and 0 <= y < n:
    return True
  else:
    return False


def bfs(i, j):
  q = deque([[i, j]])
  region[i][j] = 0

  while q:
    x, y = q.popleft()
    for d in range(4):
      newX, newY = x + dr[d], y + dc[d]
      if check(newX, newY) and region[newX][newY] == 1:
        region[newX][newY] = 0
        q.append([newX, newY])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

min_num = 100
max_num = 0
for i in range(n):
  for j in range(n):
    if arr[i][j] > max_num:
      max_num = arr[i][j]
    if arr[i][j] < min_num:
      min_num = arr[i][j] 

result = []
for h in range(min_num-1, max_num+1):
  region = [[1] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if arr[i][j] <= h:
        region[i][j] = 0
  
  cnt = 0
  for i in range(n):
    for j in range(n):
      if region[i][j] == 1:
        bfs(i, j)
        cnt += 1
  result.append(cnt)

  
print(max(result))

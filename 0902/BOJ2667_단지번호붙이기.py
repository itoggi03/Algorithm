def check(x, y):
  if 0 <= x < n and 0 <= y < n:
    return True
  else:
    return False


def dfs(r, c):
  stack = []
  stack.append([r, c])

  arr[r][c] = 0

  cnt = 1

  while stack:
    x, y = stack.pop()
    for d in range(4):
      newX, newY = x + dr[d], y + dc[d]
      if check(newX, newY) and arr[newX][newY] == 1:
        arr[newX][newY] = 0
        cnt += 1
        stack.append([newX, newY])

  return cnt


n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = []
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      cnt.append(dfs(i, j))

cnt.sort()

print(len(cnt))
for c in cnt:
  print(c)
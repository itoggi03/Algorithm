from collections import deque

def check(x, y):
  if 0 <= x < n and 0 <= y < m:
    return True
  else:
    return False


def bfs(sX, sY):
  q = deque()
  q.append([sX, sY])
  
  while q:
    x, y = q.popleft()
    for d in range(4):
      newX, newY = x + dr[d], y + dc[d]
      if check(newX, newY) and miro[newX][newY] == 1:
        q.append([newX, newY])
        miro[newX][newY] += miro[x][y]
      

n, m = map(int, input().split())

miro = []
for i in range(n):
  miro.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

bfs(0, 0)
print(miro[n-1][m-1])
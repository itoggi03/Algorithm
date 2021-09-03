from collections import deque

def check(H, R, C):
  if 0 <= H < h and 0 <= R < m and 0 <= C < n:
    return True
  else:
    return False


def bfs(q):
  days = -1
  day = []
  
  while q:
    for t in q:
      H, R, C = t
      for d in range(6):
        newH, newR, newC = H + dh[d], R + dr[d], C + dc[d]
        if check(newH, newR, newC) and arr[newH][newR][newC] == 0:
          arr[newH][newR][newC] = 1
          day.append([newH, newR, newC])
    days += 1
    q = day
    day = []


  # 토마토가 모두 익지는 못하는 상황 체크
  for a in range(h):
    for b in range(m):
      for c in range(n):
        if arr[a][b][c] == 0:
          return -1

  return days
  

n, m, h = map(int, input().split())

arr = []
tmp = []
for i in range(m*h):
  if i and i % m == 0:
    arr.append(tmp)
    tmp = []
  tmp.append(list(map(int, input().split())))
arr.append(tmp)

# 상/하/좌/우/위/아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

queue = deque()
for i in range(h):
  for j in range(m):
    for k in range(n):
      if arr[i][j][k] == 1:
        queue.append([i, j, k])
          
answer = bfs(queue)

print(answer)

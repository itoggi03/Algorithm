from collections import deque

def bfs(start, target):
  visited = [0] * (n+1)
  q = deque([[start, 0]])
  visited[start] = 1

  while q:
    x, c = q.popleft()
    if x == target:
      return c
    for i in arr[x]:
      if not visited[i]:
        visited[i] = 1
        q.append([i, c+1])

  return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  arr[x].append(y)
  arr[y].append(x)

result = bfs(p1, p2) 
print(result)

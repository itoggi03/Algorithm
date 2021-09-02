from collections import deque

def bfs():
  q = deque()
  q.append(1)

  visited = [0] * (n+1)
  cnt = 0

  while q:
    comp = q.popleft()
    if not visited[comp]:
      visited[comp] = 1
      cnt += 1
      q.extend(graph[comp])

  return cnt


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

print(bfs() - 1)
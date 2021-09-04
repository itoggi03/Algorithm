from collections import deque

def bfs(f, start, target, up, down):
  q = deque([[start, 0]])
  visited = [0] * (f+1)

  while q:
    curr, cnt = q.popleft()
    if curr == target:
      return cnt
    if 1 <= curr <= f and not visited[curr]:
      visited[curr] = 1
      q.append([curr + up, cnt + 1])
      q.append([curr - down, cnt + 1])

  return 'use the stairs'


f, s, g, u, d = map(int, input().split())

result = bfs(f, s, g, u, d)
print(result)

from collections import deque

def bfs(start, target):
  q = deque([[start, 0]])
  visited = [0] * 100001

  while q:
    p, cnt = q.popleft()
    if p == target:
      return cnt
    if p < 0 or p > 100000:
      continue
    if not visited[p]:
      visited[p] = 1
      q.append([p-1, cnt+1])
      q.append([p+1, cnt+1])
      q.append([p*2, cnt+1])
  
  return cnt


n, k = map(int, input().split())

result = bfs(n, k)
print(result)
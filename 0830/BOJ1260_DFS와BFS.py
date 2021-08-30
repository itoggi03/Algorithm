from collections import deque

def dfs(start):
  visited = []
  stack = [start]
  

  while stack:
    tmp = stack.pop()
    if not tmp in visited:
      visited.append(tmp)
      stack.extend(sorted(node[tmp], reverse=True))
  return visited


def bfs(start):
  visited = []
  q = deque([start])

  while q:
    tmp = q.popleft()
    if not tmp in visited:
      visited.append(tmp)
      q.extend(sorted(node[tmp]))

  return visited



n, m, v = map(int, input().split())

node = [[] for _ in range(n+1)]
# print(node)
for i in range(m):
  a, b = map(int, input().split())
  node[a].append(b)
  node[b].append(a)


dfs_result = dfs(v)
bfs_result = bfs(v)


# 출력
for d in dfs_result:
  print(d, end=' ')
print()
for b in bfs_result:
  print(b, end=' ')
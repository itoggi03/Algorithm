from collections import deque

def bfs(s, time):
    q = deque()
    q.append((s, time))

    while q:
        ns, t = q.popleft()

        # 동생이 있는 곳일 경우 return
        if ns == k:
            return t

        # 인덱스가 넘어갈 경우
        if ns < 0 or ns > 100000:
            continue

        if not visited[ns]:
            visited[ns] = 1
            q.append((ns-1, t+1))
            q.append((ns+1, t+1))
            q.append((ns*2, t+1))


n, k = map(int, input().split())

visited = [0] * 100001  # 방문체크

result = bfs(n, 0)  # bfs

print(result)   # 출력
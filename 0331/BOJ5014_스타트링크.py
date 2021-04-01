from collections import deque

def check(x):
    if x > 0 and x <= f:
        return True
    else:
        return False


def bfs(start, cnt):
    global ans
    q = deque()
    q.append((start, cnt))

    while q:
        p, c = q.popleft()

        # g층에 도달한 경우 값 업데이트 후 return
        if p == g:
            ans = c
            return

        c += 1  # 버튼 누른 횟수 +1

        # 인덱스가 넘어가지 않고 방문한 적이 없는 층이라면
        if check(p) and not visited[p]:
            visited[p] = 1      # 방문체크
            q.append((p+u, c))  # 위로 u층만큼 이동
            q.append((p-d, c))  # 아래로 d층만큼 이동


f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)
ans = 1000000000

bfs(s, 0)

# 결과 출력
if ans == 1000000000:   # G층에 갈 수 없을 경우
    print('use the stairs')
else:
    print(ans)
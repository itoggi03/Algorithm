from collections import deque

# 두 포인트간의 거리가 1000이 넘지 않을 경우 True를 반환해주는 함수
def distance_check(a, b):
    tmp = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if tmp > 1000:
        return False
    else:
        return True


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        p = q.popleft()
        for i in arr[p]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


t = int(input())    # 테스트 케이스 개수

for _ in range(t):
    n = int(input())    # 편의점 개수
    location = [list(map(int, input().split())) for _ in range(n+2)]

    # 각 포인트간의 거리가 1000이 넘지 않는 경우만 해당하는 인덱스에 인덱스 담아놓기
    arr = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i != j:
                if distance_check(location[i], location[j]):
                    arr[i].append(j)

    visited = [0] * (n+2)
    bfs(0)

    # 마지막지점(페스티벌)에 방문한 적이 없다면 sad, 있다면 happy 출력
    if visited[-1]:
        print('happy')
    else:
        print('sad')
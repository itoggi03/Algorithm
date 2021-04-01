from collections import deque
import copy

# 인덱스가 벗어났는지 체크해주는 함수
def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    else:
        return False


# 빙하의 상하좌우에 0이 몇개 있는지 체크해 개수를 return하는 함수
def zero_check(r, c):
    cnt = 0
    
    # 상하좌우 체크
    for d in range(4):
        newR = r + dr[d]
        newC = c + dc[d]
        if check(newR, newC) and not arr[newR][newC]:
            cnt += 1
    return cnt


# 한 덩어리의 빙하를 체크하기 위한 BFS
def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            newX = x + dr[d]
            newY = y + dc[d]
            if check(newX, newY) and not visited[newX][newY] and newArr[newX][newY]:
                visited[newX][newY] = 1
                q.append((newX, newY))
    return


# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


ice_cnt = 0 # 빙하 덩어리 개수
result = 0  # 최소 시간(년)

# 빙하 덩어리 개수가 2개가 되기 전까지 반복
while ice_cnt < 2:
    ice_cnt = 0
    newArr = [[0] * m for _ in range(n)]
    
    # 각 빙하의 주변에 있는 0 개수 체크하여 원래 높이에서 빼기
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j]:
                tmp = zero_check(i, j)
                if arr[i][j] >= tmp:
                    newArr[i][j] = arr[i][j] - tmp
                else:
                    # 뺐을 때 음수이면 0을 넣어주기
                    newArr[i][j] = 0
    
    # 1년 지난 후의 빙하를 arr에 업데이트
    arr = copy.deepcopy(newArr)

    visited = [[0] * m for _ in range(n)]
    # BFS
    for i in range(1, n-1):
        for j in range(1, m-1):
            if newArr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                ice_cnt += 1
    
    # while문이 끝나기 전에 빙하덩어리 개수가 0이라면 0 출력 후 while문 탈출
    if ice_cnt == 0:
        print(0)
        break
        
    result += 1 # 시간(년) +1

# 빙하 덩어리 개수가 0이 아니라면 result 출력
if ice_cnt:
    print(result)

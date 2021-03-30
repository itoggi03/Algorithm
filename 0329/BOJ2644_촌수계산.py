def dfs(x, cnt):
    global ans

    # 찾아야할 사람을 만났을 경우 ans에 카운트 개수 업데이트하고 return
    if x == n2:
        ans = cnt
        return

    # 더이상 연결된 노드가 없을 경우 return
    if not arr[x]:
        return

    visited[x] = 1

    for i in arr[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)

    return


# 입력
n = int(input())
n1, n2 = map(int, input().split())
m = int(input())

# 친척 관계도
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = -1
visited = [0] * (n+1)
for i in range(n+1):
    for j in range(len(arr[i])):
        if arr[i][j] == n1:
            dfs(arr[i][j], 0)

print(ans)
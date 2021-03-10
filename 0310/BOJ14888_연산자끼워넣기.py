def dfs(idx, val):
    global add, sub, multi, div, max_result, min_result

    # N개의 숫자를 다 계산하였을 경우 최댓값과 최솟값 업데이트
    if idx == N:
        max_result = max(max_result, val)
        min_result = min(min_result, val)
    else:
        if add > 0:
            add -= 1
            dfs(idx+1, val + arr[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx+1, val - arr[idx])
            sub += 1
        if multi > 0:
            multi -= 1
            dfs(idx+1, val * arr[idx])
            multi += 1
        if div > 0:
            div -= 1
            dfs(idx+1, int(val / arr[idx]))
            div += 1

# 입력
N = int(input())
arr = list(map(int, input().split()))
add, sub, multi, div = map(int, input().split())    # 덧셈, 뺄셈, 곱셈, 나눗셈 개수 입력

max_result = -1000000000
min_result = 1000000000

dfs(1, arr[0])

print(max_result)
print(min_result)
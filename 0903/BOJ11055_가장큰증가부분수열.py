import copy

n = int(input())
arr = list(map(int, input().split()))

dp = copy.deepcopy(arr)
total = [0] * n
for i in range(1, n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + arr[i])

print(dp)
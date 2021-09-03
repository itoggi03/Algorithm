n = int(input())
arr = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n
result = [0] * n
for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i] and increase[i] < increase[j] + 1:
      increase[i] = increase[j] + 1

for i in range(n-1, -1, -1):
  for j in range(i+1, n):
    if arr[j] < arr[i] and decrease[i] < decrease[j] + 1:
      decrease[i] = decrease[j] + 1
  result[i] = decrease[i] + increase[i] - 1

print(max(result))
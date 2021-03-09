n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0 and i != 0:
            arr[i][j] += arr[i-1][j]
        elif 0 < j < len(arr[i]) - 1:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
        elif j == len(arr[i]) - 1:
            arr[i][j] += arr[i-1][j-1]

print(max(arr[n-1]))
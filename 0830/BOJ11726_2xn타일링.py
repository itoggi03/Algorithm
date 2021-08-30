def solution():
    if n == 1:
        return 1
    elif n == 2:
        return 2

    arr[1] = 1
    arr[2] = 2

    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n = int(input())
arr = [0 for _ in range(n+1)]

print(solution() % 10007)


T = int(input())

for _ in range(T):
    n = int(input())

    arr = [0 for _ in range(n+1)]

    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue

    arr[1] = 1
    arr[2] = 2
    arr[3] = 4

    for i in range(4, n+1):
        arr[i] = arr[i-1] + arr [i-2] + arr[i-3]

    print(arr[n])
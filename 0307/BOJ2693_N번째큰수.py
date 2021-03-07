# 삽입정렬(내림차순 정렬)
def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] < val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val


T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    
    insertionSort(arr)

    print(arr[2])
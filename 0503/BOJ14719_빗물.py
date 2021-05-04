h, w = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(1, w-1):
    right = max(arr[:i])
    left = max(arr[i+1:])
    
    tmp = min(right, left) - arr[i]

    if tmp > 0:
        result += tmp

print(result)
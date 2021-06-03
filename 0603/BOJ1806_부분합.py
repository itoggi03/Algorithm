N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

ans = 10000000000

subsum = arr[start]

while end < N:
    # 부분합이 S 이상일 경우
    if subsum >= S:

        # 최소 길이 업데이트
        if end-start+1 < ans:
            ans = end-start+1

        # start == end일 경우 end를 +1
        if start == end:
            end += 1
            if end < N:
                subsum += arr[end]
        # 그렇지 않을 경우 start를 +1
        else:
            subsum -= arr[start]
            start += 1

    # 부분합이 S 미만일 경우 end + 1
    else:
        end += 1
        if end < N:
            subsum += arr[end]

if ans == 10000000000:
    print(0)
else:
    print(ans)

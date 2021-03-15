n, c = map(int, input().split())
home = list(int(input()) for _ in range(n))

# 집 좌표 정렬
home.sort()

low = 1     # 공유기간 최소 거리
high = home[-1] - home[0]   # 공유기간 최대 거리

ans = 0
while low <= high:
    mid = (low + high) // 2

    val = home[0]
    cnt = 1     # 설치중인 공유기 개수
    for h in range(1, len(home)):
        # mid보다 뒤에 집이 있을 경우 val과 cnt 업데이트
        if home[h] >= val + mid:
            val = home[h]
            cnt += 1
    # 공유기 개수보다 많은 경우 단위거리 늘리기
    if cnt >= c:
        low = mid + 1
        ans = mid
    # 공유기 개수보다 적은 경우 단위거리 줄이기
    else:
        high = mid - 1

print(ans)
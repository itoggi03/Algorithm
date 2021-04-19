h, w = map(int, input().split())

block = list(map(int, input().split()))
cnt = 0

for i in range(1, len(block)-1):
    left = max(block[:i])   # 왼쪽에서 가장 높은 값
    right = max(block[i+1:])    # 오른쪽에서 가장 높은 값
    min_block = min(left, right) - block[i] # 양쪽 높은 값 중 작은 값과 현재 값의 차이 저장

    # 현재 값이 더 작으면 차이만큼 cnt에 저장
    if min_block > 0:
        cnt += min_block

print(cnt)
# 입력
N = int(input())
nums = map(int, input().split())

# 정수 범위: -1,000,000 ~ 1,000,000
maxN = -1000000
minN = 1000000
for num in nums:
    if num >= maxN: # maxN보다 클 경우 업데이트
        maxN = num
    if num <= minN: # minN보다 작을 경우 업데이트
        minN = num

# 출력
print(minN, maxN)

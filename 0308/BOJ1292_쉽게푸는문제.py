# 입력
a, b = map(int, input().split())

nums = []
num = 1
# 수열의 길이가 1000이 될때까지 수열 생성
while len(nums) <= 1000:
    # num을 num의 크기만큼 생성
    for i in range(num):
        nums.append(num)
    num += 1

# 출력
print(sum(nums[a-1:b]))
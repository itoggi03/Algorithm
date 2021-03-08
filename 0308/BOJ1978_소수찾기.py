# 입력
N = int(input())
nums = list(map(int, input().split()))

flag = True
ans = []
for num in nums:
    # 2부터 num-1까지 수 중에 나누어 떨어지는게 있으면 flag를 False로 바꾸고 break
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    # flag가 True이면 소수이므로 ans에 담기
    if flag == True:
        ans.append(num)
    else:
        flag = True

# 1은 소수가 아니므로 빼주기
if 1 in nums:
    print(len(ans)-1)
else:
    print(len(ans))
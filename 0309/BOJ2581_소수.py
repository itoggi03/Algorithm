M = int(input())
N = int(input())

ans = []
# M 이상 N 이하의 숫자에서 1과 자기 자신을 제외하고 나누어 떨어지는 숫자가 있는지 판단
for num in range(M, N+1):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    # 나누어 떨어지는 숫자가 없었으면 소수이므로 ans에 담기
    if flag == True:
        ans.append(num)

# 1은 소수가 아니므로 제거
if 1 in ans:
    ans.remove(1)

# 주어진 범위 내에 소수가 없을 경우 -1 출력
if ans == []:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
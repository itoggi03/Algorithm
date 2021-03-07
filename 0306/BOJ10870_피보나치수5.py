n = int(input())

# n은 20 이하이므로 21 크기의 배열 생성
dp = [0] * 21

# 초기값 설정
dp[0] = 0
dp[1] = 1

# 점화식
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# 출력
print(dp[n])
n1, n2 = map(int, input().split())

# num1에 작은 수, num2에 큰 수
if n1 > n2:
    num1, num2 = n2, n1
else:
    num1, num2 = n1, n2

maxNum = 0  # 최대 공약수
minNum = 0  # 최소 공배수


# 최대 공약수 구하기
for i in range(1, num2+1):
    if num1 % i == 0 and num2 % i == 0:
        if i >= maxNum:
            maxNum = i


# 최소 공배수 구하기
n = 1
while True:
    if (num2 * n) % num1 == 0:
        minNum = num2 * n
        break
    n += 1

print(maxNum)
print(minNum)

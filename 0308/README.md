# 03/08 알고리즘

> BOJ1978, BOJ1292





## 1. BOJ1978 소수 찾기 

> 문제링크: https://www.acmicpc.net/problem/1978



### 나의 코드

```python
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
```



### 입력

```bash
4
1 3 5 7
```

### 출력

```bash
3
```



### 회고

- 처음에 소수가 아닐 경우 remove를 이용해 리스트에서 삭제해주는 방법을 썼는데, 그랬더니 답이 제대로 나오지 않았다. 그래서 remove를 쓰지 않는 방법으로 바꿔서 답을 도출하였다.

---





## 2. BOJ1292 쉽게 푸는 문제

> 문제링크: https://www.acmicpc.net/problem/1292



### 나의 코드

```python
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
```



### 입력

```bash
3 7
```

### 출력

```bash
15
```



### 회고

- 입력 받는 정수 A, B의 범위가 1≤A≤B≤1000 이므로 수열을 1000만큼 생성한 후 A~B 구간의 값의 합을 구한다.
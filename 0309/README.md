# 03/09 알고리즘

> BOJ2581, BOJ1932



## 1. BOJ2581 소수

> 문제링크: https://www.acmicpc.net/problem/2581



### 나의 코드

```python
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
```



### 입력

```bash
60
100
```

### 출력

```bash
620
61
```



### 회고

- 어제 풀었던 소수 찾기와 비슷한 문제이다. 범위가 정해져 있다는 것만 다르다.

---





## 2. BOJ1932 정수 삼각형

> 문제링크: https://www.acmicpc.net/problem/1932



### 나의 코드

```python
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0 and i != 0:
            arr[i][j] += arr[i-1][j]
        elif 0 < j < len(arr[i]) - 1:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
        elif j == len(arr[i]) - 1:
            arr[i][j] += arr[i-1][j-1]

print(max(arr[n-1]))
```



### 입력

```bash
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```

### 출력

```bash
30
```



### 아이디어(입력 정수삼각형 기준)

- 위에서 아래로 내려오면서 더하는 방법을 사용
- 정수 삼각형에서 각 행의 0번째면 바로 위 숫자만 더한다.
- 정수 삼각형에서 각 행의 중간에 속한 숫자들은 바로 위 숫자와 왼쪽 대각선 위 숫자 중 큰 것을 더한다.
- 정수 삼각형에서 각 행의 끝 숫자들은 왼쪽 대각선 위 숫자를 더한다.
- 마지막 행에서 가장 큰 수를 더한다.
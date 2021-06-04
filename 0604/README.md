# 06/04 알고리즘

> BOJ2812, BOJ5557

<br>

## 1. BOJ2812 크게 만들기

> 문제링크: https://www.acmicpc.net/problem/2812

<br>

### 나의 코드

```python
N, K = map(int, input().split())
number = list(map(int, input()))

result = []
k = K

for i in range(N):
    while k > 0 and result:
        if result[-1] < number[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(number[i])

print(''.join(map(str, result[:N-K])))
```

<br>

### 입력

```bash
4 2
1924
```

<br>

### 출력

```bash
94
```

<br>

### 풀이

- 주어진 숫자를 한개씩 체크하여 앞의 숫자보다 클 경우 앞의 숫자를 삭제. K만큼만 삭제하도록 while문 돌림
- 만약 for문이 다 끝났는데 K가 남아있을 경우를 대비해 result[:N-K]를 출력

---

<br>

<br>

## 2. BOJ5557 1학년

> 문제링크: https://www.acmicpc.net/problem/5557

<br>

### 나의 코드

```python
N = int(input())
num = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

dp[0][num[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0 <= j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i-1][j]
            if 0 <= j - num[i] <= 20:
                dp[i][j - num[i]] += dp[i-1][j]

print(dp[N-2][num[-1]])
```

<br>

### 입력

```bash
11
8 3 2 4 8 7 2 4 0 8 8
```

<br>

### 출력

```bash
10
```

<br>

### 풀이

- DP를 이용하여 풀었다.
- dp[i][j] : i번째 수까지 계산했을 때 j가 나올 수 있는 경우의 수
- j는 0~20까지의 수
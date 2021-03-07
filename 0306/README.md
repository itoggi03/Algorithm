# 2021.03.06 알고리즘

> BOJ10870, BOJ2309





## 1. BOJ10870 피보나치 수 5

> 문제링크: https://www.acmicpc.net/problem/10870

### 나의 코드

```python
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
```

### 입력

```bash
10
```

### 출력

```bash
55
```

### 회고

- 재귀가 아닌 dp로 풀어보았다.

- dp 설명 참고 링크

  [알고리즘 - Dynamic Programming(동적프로그래밍)이란?](https://galid1.tistory.com/507)

---



## 2. BOJ2309 일곱 난쟁이

> 문제링크: https://www.acmicpc.net/problem/2309



### 나의 코드

```python
# 가짜 난쟁이 찾는 함수
def search():
    for i in range(9):
        for j in range(9):
            if i != j:
                # 2개의 난쟁이 키를 뺀 값의 합이 100일 경우 2개의 난쟁이 키 값을 return
                if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
                    return dwarf[i], dwarf[j]

# 입력
dwarf = []
for i in range(9):
    dwarf.append(int(input()))

# 가짜 난쟁이 2개의 값을 return 하는 함수
n1, n2 = search()

# 가짜 난쟁이 삭제
dwarf.remove(n1)
dwarf.remove(n2)

# 오름차순 정렬
dwarf.sort()

# 출력
for i in dwarf:
    print(i)
```



### 입력

```bash
20
7
23
19
10
15
25
8
13
```

### 출력

```bash
7
8
10
13
19
20
23
```



### 회고

- 이중for문을 이용하여 전체 경우의 수를 따져 가짜 난쟁이를 찾아냈다.
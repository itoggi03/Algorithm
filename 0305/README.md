# 03/05 BOJ10818 최소, 최대

> BOJ10818, BOJ2460



## 1. BOJ10818 최소, 최대

> 문제링크: https://www.acmicpc.net/problem/10818



### 나의 코드

```python
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
```



### 입력

```bash
5
20 10 35 30 7
```



### 출력

```bash
7 35
```



### 회고

- 처음에 정수의 범위를 확인하지 않고 maxN의 초기값을 0으로 줘서 틀렸다. 최대값이 음수일 수도 있기 때문에 틀린 것이다. 값의 범위를 잘 살피자.

---





## 2. BOJ2460 지능형 기차2

> 문제링크: https://www.acmicpc.net/problem/2460



### 나의 코드

```python
# 정차역별 [내린 사람 수, 탄 사람 수] 입력 
train = [list(map(int, input().split())) for _ in range(10)]

passengers = 0  # 기차에 타고 있는 승객 수
maxPassengers = 0   # 기차에 타고 있는 최대 승객 수
for person in train:
    passengers -= person[0] # 내린 사람
    passengers += person[1] # 탄 사람

    # 최대 승객 수 업데이트
    if passengers >= maxPassengers: 
        maxPassengers = passengers

# 출력
print(maxPassengers)
```



### 입력

```bash
0 32
3 13
28 25
17 5
21 20
11 0
12 12
4 2
0 8
21 0
```



### 출력

```bash
42
```



### 회고

- `단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여, 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.` 라는 조건에 따라 내리고 탄 다음에 최대 승객 수 체크
# 04/19 알고리즘

> Programmers폰켓몬, BOJ14719

<br>

## 1. Programmers 폰켓몬

> 문제링크: https://programmers.co.kr/learn/courses/30/lessons/1845

<br>

### 나의 코드

```python
def solution(nums):
    answer = 0
    new_nums = list(set(nums))
    N = len(nums) // 2
    if len(new_nums) > N:
        answer = N
    else:
        answer = answer = len(new_nums)
    
    return answer
```

<br>

### 입력

```bash
[3,1,2,3]
```

<br>

### 출력

```bash
2
```

<br>

### 풀이

- 가장 많은 종류의 폰켓몬을 선택해야하므로 중복값을 제거한 뒤의 종류 개수를 보고 판별한다.
- set을 이용하여 중복값을 제거한 후의 배열 길이가 N/2보다 작으면 배열 길이가 최대 값이고, N/2보다 크면 N/2가 최대 값이다.

<br>

<br>

## 2. BOJ14719 빗물

> 문제링크: https://www.acmicpc.net/problem/14719

<br>

### 나의 코드

```python
h, w = map(int, input().split())

block = list(map(int, input().split()))
cnt = 0

for i in range(1, len(block)-1):
    left = max(block[:i])   # 왼쪽에서 가장 높은 값
    right = max(block[i+1:])    # 오른쪽에서 가장 높은 값
    min_block = min(left, right) - block[i] # 양쪽 높은 값 중 작은 값과 현재 값의 차이 저장
    
    # 현재 값이 더 작으면 차이만큼 cnt에 저장
    if min_block > 0: 
        cnt += min_block

print(cnt)
```

<br>

### 입력

```bash
4 4
3 0 1 4
```

<br>

### 출력

```bash
5
```

<br>

### 풀이

- 빌딩의 높이를 하나씩 for문 돌리면서 현재 위치의 왼쪽과 오른쪽 높이 중 낮은 것과 현재 위치의 높이랑 비교해서 현재 위치가 더 낮을 경우 그 차이만큼 결과값에 더해준다.
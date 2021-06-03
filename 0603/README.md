# 06/03 알고리즘

> BOJ1806

<br>

## 1. BOJ1806 부분합

> 문제링크: https://www.acmicpc.net/problem/1806

<br>

### 나의 코드

```python
N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

ans = 10000000000

subsum = arr[start]

while end < N:
    # 부분합이 S 이상일 경우
    if subsum >= S:

        # 최소 길이 업데이트
        if end-start+1 < ans:
            ans = end-start+1

        # start+1이 end보다 클 경우 end를 +1
        if start+1 > end:
            end += 1
            if end < N:
                subsum += arr[end]
        # 그렇지 않을 경우 start를 +1
        else:
            subsum -= arr[start]
            start += 1

    # 부분합이 S 미만일 경우 end + 1
    else:
        end += 1
        if end < N:
            subsum += arr[end]

if ans == 10000000000:
    print(0)
else:
    print(ans)
```

<br>

### 입력

```bash
10 15
5 1 3 5 10 7 4 9 2 8
```

<br>

### 출력

```bash
2
```

<br>

### 풀이

- 투포인터를 사용해 풀었다.
- 시작 인덱스와 끝 인덱스를 정해 그에 해당하는 값들을 더해주고, 그 더한 값을 S와 비교한다.
- 부분합이 S 이상일 경우
  - 최소 길이 비교 후 최소값 업데이트
  - start == end일 경우 end를 +1 (끝 범위를 넓힌다.)
  - start ≠ end일 경우 start를 +1 (시작 범위를 좁힌다.)
- 부분합이 S 미만일 경우
  - end가 인덱스 범위를 넘지 않는 경우만 end + 1 ( 끝 범위를 넓힌다.)

---



## 2. Programmers 체육복

>  문제링크: https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3#

<br>

### 나의 코드

```python
def solution(n, lost, reserve):
    answer = n - len(lost)  # 전체 학생 수에서 도난당한 학생 수 뺀 값을 초기값으로 설정
    same = [0] * len(lost)  # 여벌 체육복을 가져온 학생이 도난 당한 경우를 체크하기 위함
    borrow = [0] * len(reserve) # 여벌 체육복을 빌려줬는지 체크하기 위함
    
    # 여벌 체육복을 가져온 학생이 도난 당한 경우
    for l in range(len(lost)):
        for r in range(len(reserve)):
            if lost[l] == reserve[r]:
                answer += 1
                borrow[r] = 1
                same[l] = 1
                break

    # 여벌 체육복을 가져오지 않은 학생이 도난 당한 경우
    for l in range(len(lost)):
        for r in range(len(reserve)):        
            if lost[l]-1 == reserve[r] or lost[l]+1 == reserve[r]:
                if not borrow[r] and not same[l]:   # 체육복을 이미 빌려줬거나, 여벌이 있는데 도난 당한 경우를 제외
                    answer += 1
                    borrow[r] = 1
                    break   
                    
    return answer
```

<br>

### 입력

```bash
n = 5, lost=[2, 4], reserve=[1, 3, 5]
```

<br>

### 출력

```bash
5
```

<br>

### 풀이

- 여벌 체육복이 있는데 도난당한 경우를 먼저 처리해준다.
- 그 외의 경우 바로 앞번호나 뒷번호의 학생에게 체육복을 빌려줄 수 있는지 체크하고 빌려줌
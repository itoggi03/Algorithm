# 0316 알고리즘

> BOJ2110



## BOJ2110 공유기 설치

> 문제링크: https://www.acmicpc.net/problem/2110



### 나의 코드

```python
n, c = map(int, input().split())
home = list(int(input()) for _ in range(n))

# 집 좌표 정렬
home.sort()

low = 1     # 공유기간 최소 거리
high = home[-1] - home[0]   # 공유기간 최대 거리

ans = 0
while low <= high:
    mid = (low + high) // 2

    val = home[0]
    cnt = 1     # 설치중인 공유기 개수
    for h in range(1, len(home)):
        # mid보다 뒤에 집이 있을 경우 val과 cnt 업데이트
        if home[h] >= val + mid:
            val = home[h]
            cnt += 1
    # 공유기 개수보다 많은 경우 단위거리 늘리기
    if cnt >= c:
        low = mid + 1
        ans = mid
    # 공유기 개수보다 적은 경우 단위거리 줄이기
    else:
        high = mid - 1

print(ans)
```



### 입력

```bash
5 3
1
2
8
4
9
```

### 출력

```bash
3
```



### 풀이

- 단위 거리(공유기간 거리)를 기준으로 이진탐색하는 문제이다.
- 처음에 최소 거리와 최대 거리의 중앙값으로 시작하여 단위거리가 중앙값일 경우 설치할 수 있는 공유기 개수를 세고, 설치할 수 있는 공유기 개수와 c를 비교하여 탐색범위를 좁혀간다.



### 회고

- 이진탐색에 대한 이해가 부족할 경우 한번에 풀기 쉽지 않다.
- 이진탐색에 대한 개념 강의를 본 후 풀었다.
# README

> BOJ2501, BOJ3460



## BOJ2501 약수 구하기

> 문제링크: https://www.acmicpc.net/problem/2501



### 나의 코드

```python
N, K = map(int, input().split())

divisor = []    # 약수를 담을 리스트
for i in range(1, N+1):
    if N % i == 0:
        divisor.append(i)

if K > len(divisor):    # K가 약수의 개수보다 클 경우 0을 출력
    print(0)
else:
    print(divisor[K-1]) # N의 약수들 중 K번째로 작은 수 출력
```



### 입력

```bash
6 3
```



### 출력

```bash
3
```





----



## BOJ3460 이진수

> 문제링크: https://www.acmicpc.net/problem/3460



### 나의 코드

```python
T = int(input())

for i in range(T):
    n = int(input())

    binary_num = []
    while n != 0:
        binary_num.append(n % 2)
        n = n // 2  # n을 2로 나눈 몫을 n으로 업데이트

    # 1의 위치를 공백으로 구분해서 줄 하나에 출력
    for idx, val in enumerate(binary_num):
        if val == 1:
            print(idx, end=" ")
    print()
```



### 입력

```bash
1
13
```



### 출력

```bash
0 2 3
```



### 회고

- 이진수 구하는 법을 잘 모르나보다... 쉬운건데 헤매서 시간이 좀 걸렸다ㅠ
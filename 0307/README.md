# 2021.03.07 알고리즘

> BOJ2609, BOJ2693



## 1. BOJ2609 최대공약수와 최대공배수

문제링크: https://www.acmicpc.net/problem/2609



### 나의 코드

```python
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
```



### 입력

```bash
24 18
```

### 출력

```bash
6
72
```



### 회고

- 최대 공약수
  - 입력 받은 두 수 중 큰 수만큼 for문을 돌려서 두 수가 둘다 나누어 떨어지면 최대공약수
  - for 문을 거꾸로 돌리면 좀 더 빠른 연산이 될 것 같다.
- 최소 공배수
  - 입력 받은 두 수 중 큰수의 배수가 나머지 수의 약수면 최소 공배수

---



## 2. BOJ2693 N번째 큰 수

> 문제링크: https://www.acmicpc.net/problem/2693



### 나의 코드

```python
# 삽입정렬(내림차순 정렬)
def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] < val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val

T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    
    insertionSort(arr)

    print(arr[2])
```



### 입력

```bash
4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408
```

### 출력

```bash
8
489
931
768
```



### 회고

- 삽입정렬을 이용하여 내림차순으로 정렬하고 3번째 수를 출력하였다.
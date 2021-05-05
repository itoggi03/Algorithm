# 05/05 알고리즘

> BOJ1717, BOJ10814, BOJ5568

<br>

## 1. BOJ1717 집합의 표현

> 문제링크: https://www.acmicpc.net/problem/1717

<br>

### 나의 코드

1. 처음 코드(이렇게 풀면 안된다!)

   ```python
   n, m = map(int, input().split())
   
   arr = [[i] for i in range(n+1)]
   
   for i in range(m):
       o, a, b = map(int, input().split())
       if o == 0:
           if b not in arr[a]:
               arr[a].append(b)
               # arr[b].append(a)
               # print(arr)
       elif o == 1:
           if a in arr[b] or b in arr[a]:
               print('YES')
           else:
               print('NO')
   ```

2. 최종 코드

   ```python
   # x의 루트를 찾아주는 함수
   def find(x):
       if x == arr[x]:
           return x
       else:
           arr[x] = find(arr[x])
           return arr[x]
   
   # x와 y가 가리키는 루트를 같게 해주는 함수
   def union(x, y):
       arr[find(y)] = find(x)
   
   n, m = map(int, input().split())
   
   arr = [i for i in range(n+1)]
   
   for i in range(m):
       o, a, b = map(int, input().split())
   
       # o가 0일 경우 합집합 만들어주기(루트를 같게 하기)
       if o == 0:
           union(a, b)
       # o가 1일 경우 두 숫자의 루트가 같은지 확인
       else:
           if find(a) == find(b):
               print('YES')
           else:
               print('NO')
   ```

<br>

### 입력

```bash
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
```

<br>

### 출력

```bash
NO
NO
YES
```

<br>

### 풀이

- 각 숫자가 가리키는 루트를 자기 자신으로 해놓은 후, 합집합 연산(union)은 루트를 갖게 해주는것, 같은 집합에 포함하는지 찾는 연산(find)은 루트가 같은지 확인해주게 한다.

---

<br>

<br>

## 2. BOJ10814 나이순 정렬

> 문제링크: https://www.acmicpc.net/problem/10814

<br>

### 나의 코드

```python
N = int(input())    # 회원 수 

arr = [] 
# 회원 나이와 이름 입력받기
for i in range(N):
    age, name = input().split()
    arr.append([age, name])
    
# 나이순으로 정렬(나이에 int 해줘야함)
ans = sorted(arr, key=lambda x: int(x[0]))

# 출력
for i in ans:
    print('{} {}'.format(i[0], i[1]))
```

<br>

### 입력

```bash
3
21 Junkyu
21 Dohyun
20 Sunyoung
```

<br>

### 출력

```bash
20 Sunyoung
21 Junkyu
21 Dohyun
```

<br>

### 풀이

- 회원의 나이와 이름을 입력 받는다.
- 입력 받은 나이와 이름은 문자열이므로, 나이순으로 정렬을 할 때 int로 바꿔주어야 한다.
- 문자열의 숫자를 기준으로 정렬을 하면 맨 앞의 숫자 기준으로 정렬을 하기 때문에 숫자 기준의 정렬 결과가 나오지 않으므로 주의!!

---

<br>

<br>

## 3. BOJ5568 카드 놓기

> 문제링크: https://www.acmicpc.net/problem/5568

<br>

### 나의 코드

```python
import itertools

# 입력
n = int(input())
k = int(input())
arr = [input() for _ in range(n)]

# 숫자들의 순열을 join을 이용해 붙인 후 result에 담기
result = []
for card in itertools.permutations(arr, k):
    result.append(''.join(list(card)))

# 중복 제거
ans = set(result)

# 출력
print(len(ans))
```

<br>

### 입력

```bash
4
2
1
2
12
1
```

<br>

### 출력

```bash
7
```

<br>

### 풀이

- 순열을 이용해서 카드를 뽑고 join을 이용해 뽑은 카드들을 붙인 뒤 리스트에 담는다.
- set을 이용하여 그 리스트의 중복을 제거한다.
- set의 길이를 출력한다.
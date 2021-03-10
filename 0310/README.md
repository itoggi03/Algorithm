# 03/10 알고리즘

> BOJ14888, BOJ2504



## 1. BOJ14888 연산자 끼워넣기

> 문제링크: https://www.acmicpc.net/problem/14888



### 나의 코드

```python
def dfs(idx, val):
    global add, sub, multi, div, max_result, min_result

    # N개의 숫자를 다 계산하였을 경우 최댓값과 최솟값 업데이트
    if idx == N:
        max_result = max(max_result, val)
        min_result = min(min_result, val)
    else:
        if add > 0:
            add -= 1
            dfs(idx+1, val + arr[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx+1, val - arr[idx])
            sub += 1
        if multi > 0:
            multi -= 1
            dfs(idx+1, val * arr[idx])
            multi += 1
        if div > 0:
            div -= 1
            dfs(idx+1, int(val / arr[idx]))
            div += 1

# 입력
N = int(input())
arr = list(map(int, input().split()))
add, sub, multi, div = map(int, input().split())    # 덧셈, 뺄셈, 곱셈, 나눗셈 개수 입력

max_result = -1000000000
min_result = 1000000000

dfs(1, arr[0])

print(max_result)
print(min_result)
```



### 입력

```bash
6
1 2 3 4 5 6
2 1 1 1
```

### 출력

```bash
54
-24
```



### 회고

- dfs를 이용하여 풀었다.
- dfs 단계와 현재 값을 함께 넘겨주며 dfs를 재귀호출한다.
- dfs 하기 전 해당 연산자 값을 1만큼 감소시켰다가, dfs 후에 다시 1을 증가시킨다.

---





## 2. BOJ2504 괄호의 값

> 문제링크: https://www.acmicpc.net/problem/2504



### 나의 코드

```python
# 올바른 괄호열이면 True, 올바르지 못한 괄호열이면 False 리턴
def check(arr):
    stack1 = []
    for i in arr:
        if i == '(' or i == '[':
            stack1.append(i)
        elif i == ')':
            if not stack1:
                return False
            elif stack1[-1] == '(':
                stack1.pop()
            else:
                return False
        elif i == ']':
            if not stack1:
                return False
            elif stack1[-1] == '[':
                stack1.pop()
            else:
                return False
    if stack1 == []:
        return True
    else:
        return False

# 닫는 괄호인 경우 곱셈인지 아닌지 판단
def num_sum(n):
    tmp = 0
    while True:
        top = stack.pop()
        # stack에서 꺼낸게 괄호인 경우 break
        if top == '(' or top == '[':
            break
        # stack에서 꺼낸게 숫자일 경우 더해주기
        tmp += top

    # 숫자 더한 값이 있으면 n을 곱해서 return
    if tmp != 0:
        return tmp * n
    # 아닌경우 그냥 n을 return
    else:
        return n

arr = list(input())

# 올바르지 못한 괄호열이면 0을 출력
if not check(arr):
    print(0)
else:
    stack = []
    for i in arr:
        # 여는 괄호면 그대로 append
        if i == '(' or i == '[':
            stack.append(i)
        # 닫는 괄호면 num_sum 함수 호출
        elif i == ')':
            stack.append(num_sum(2))
        elif i == ']':
            stack.append(num_sum(3))        

    print(sum(stack))
```



### 입력

```bash
(()[[]])([])
```

### 출력

```bash
28
```



### 회고

- 스택을 이용하여 푸는 문제였다.
- 닫는 괄호의 경우 로직을 생각하는데 어려움이 있었다.  stack 관련 문제를 더 풀어봐야겠다.
- 처음엔 런타임 에러가 발생했었는데, 그 이유는 check 함수에서 빈 stack일 경우를 고려하지 않아서이다. 빈 stack에서 pop을 해서 발생하는 에러였다.
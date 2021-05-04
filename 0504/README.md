# 05/04 알고리즘

> BOJ3584

<br>

## BOJ3584 가장 가까운 공통 조상

> 문제링크: https://www.acmicpc.net/problem/3584

<br>

### 나의 코드

```python
# 조상 노드들을 배열로 반환하는 함수
def findRoot(n):
    result = [n]

    while parent[n]:
        result.append(parent[n])
        n = parent[n]

    return result

# 두개의 조상노드 배열을 루트에서부터 내려오며 비교하고, 
# 최초로 노드 값이 다를 경우 그 직전의 노드가 최소 공통 조상 노드 -> 출력
def printResult():
    level1 = len(arr1) - 1
    level2 = len(arr2) - 1
    
    while arr1[level1] == arr2[level2]:
        level1 -= 1
        level2 -= 1

    print(arr1[level1+1])

    return

for tc in range(int(input())):
    N = int(input())
    parent = [0 for _ in range(N+1)]

    # 노드별 자신의 부모 노드를 저장
    for i in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a

    # 가장 가까운 공통 조상을 구할 두 노드
    n1, n2 = map(int, input().split())

    arr1 = findRoot(n1)
    arr2 = findRoot(n2)

    # 결과 출력
    printResult()
```

<br>

### 입력

```bash
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
```

<br>

### 출력

```bash
4
3
```

<br>

### 풀이

- 처음에 주어진 노드의 부모 노드들을 모두 담은 것을 비교하는 방법을 생각하였다. 하지만 시간 초과가 났고 구현 방법에 문제가 있음을 깨닫고 검색을 통해 다른사람의 코드를 참고하여 풀었다.

- 주어진 노드의 부모 노드들을 모두 담는 것은 동일하나, 그 방법이 다르다.

  입력 받을 때 각 노드의 인덱스에 자신의 부모 노드만 담아서 이를 이용해 주어진 노드의 부모 노드들을 모두 담는다.

- 두 배열을 비교하는데, 루트부터 시작하여 내려오면서 처음으로 다른 노드가 나올 경우 그 직전의 노드가 가장 가까운 공통 조상이다.
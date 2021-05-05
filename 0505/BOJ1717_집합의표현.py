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

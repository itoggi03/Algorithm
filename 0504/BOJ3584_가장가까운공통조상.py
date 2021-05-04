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
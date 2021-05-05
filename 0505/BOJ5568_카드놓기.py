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

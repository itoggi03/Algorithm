N, K = map(int, input().split())
number = list(map(int, input()))

result = []
k = K

for i in range(N):
    while k > 0 and result:
        if result[-1] < number[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(number[i])

print(''.join(map(str, result[:N-K])))

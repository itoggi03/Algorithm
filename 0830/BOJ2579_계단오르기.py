def solve():
    if n == 1:
        return steps[1]
    elif n == 2:
        return steps[1] + steps[2]
    elif n == 3:
        return max(steps[1] + steps[3], steps[2] + steps[3])

    score[1] = steps[1]
    score[2] = steps[1] + steps[2]
    score[3] = max(steps[1] + steps[3], steps[2] + steps[3])

    for i in range(4, n + 1):
        score[i] = max(score[i - 3] + steps[i - 1] + steps[i], score[i - 2] + steps[i])

    return score[n]


n = int(input())
steps = list(int(input()) for _ in range(n))
steps.insert(0, 0) # 인덱스를 1부터 하기 위함

score = [0 for _ in range(n+1)]

result = solve()
print(result)

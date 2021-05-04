from itertools import permutations

g, s = map(int, input().split())
W = list(input())
S = list(input()) 

result = 0
for i in list( permutations(W)):
    for j in range(s-g+1):
        if list(i) == S[j:j+4]:
            result += 1

print(result)
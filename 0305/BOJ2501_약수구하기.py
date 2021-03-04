N, K = map(int, input().split())

divisor = []    # 약수를 담을 리스트
for i in range(1, N+1):
    if N % i == 0:
        divisor.append(i)

if K > len(divisor):    # K가 약수의 개수보다 클 경우 0을 출력
    print(0)
else:
    print(divisor[K-1]) # N의 약수들 중 K번째로 작은 수 출력
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
T = int(input())

for i in range(T):
    n = int(input())

    binary_num = []
    while n != 0:
        binary_num.append(n % 2)
        n = n // 2  # n을 2로 나눈 몫을 n으로 업데이트

    # 1의 위치를 공백으로 구분해서 줄 하나에 출력
    for idx, val in enumerate(binary_num):
        if val == 1:
            print(idx, end=" ")
    print()

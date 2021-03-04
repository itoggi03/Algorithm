# 정차역별 [내린 사람 수, 탄 사람 수] 입력 
train = [list(map(int, input().split())) for _ in range(10)]

passengers = 0  # 기차에 타고 있는 승객 수
maxPassengers = 0   # 기차에 타고 있는 최대 승객 수
for person in train:
    passengers -= person[0] # 내린 사람
    passengers += person[1] # 탄 사람

    # 최대 승객 수 업데이트
    if passengers >= maxPassengers: 
        maxPassengers = passengers

# 출력
print(maxPassengers)
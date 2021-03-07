# 가짜 난쟁이 찾는 함수
def search():
    for i in range(9):
        for j in range(9):
            if i != j:
                # 2개의 난쟁이 키를 뺀 값의 합이 100일 경우 2개의 난쟁이 키 값을 return
                if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
                    return dwarf[i], dwarf[j]

# 입력
dwarf = []
for i in range(9):
    dwarf.append(int(input()))

# 가짜 난쟁이 2개의 값을 return 하는 함수
n1, n2 = search()

# 가짜 난쟁이 삭제
dwarf.remove(n1)
dwarf.remove(n2)

# 오름차순 정렬
dwarf.sort()

# 출력
for i in dwarf:
    print(i)
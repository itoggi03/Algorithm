def solution(s):
    s_len = len(s)
    answer = s_len

    # 1부터 문자열의 길이의 단위까지 쪼개서 확인
    for size in range(1, s_len):

        # 단위만큼 미리 쪼개놓기
        splited = [s[i:i+size] for i in range(0, s_len, size)]

        cnt = 1
        result = ''
        for i in range(1, len(splited)):
            # 이전 값과 같다면 cnt +1
            if splited[i-1] == splited[i]:
                cnt += 1

            # 다를 경우
            else:
                # cnt가 1보다 크면 cnt값 포함해서 이어붙이기
                if cnt > 1:
                    result += str(cnt) + splited[i-1]
                    cnt = 1 # cnt 초기화

                # cnt가 1보다 크지 않으면 그냥 이어붙이기
                else:
                    result += splited[i-1]
                    cnt = 1

        # 마지막 값 이어붙이기
        if cnt > 1:
            result += str(cnt) + splited[-1]
        else:
            result += splited[-1]

        # 짧은 길이로 업데이트
        if len(result) < answer:
            answer = len(result)

    return answer

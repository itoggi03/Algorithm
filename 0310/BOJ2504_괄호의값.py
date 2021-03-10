# 올바른 괄호열이면 True, 올바르지 못한 괄호열이면 False 리턴
def check(arr):
    stack1 = []
    for i in arr:
        if i == '(' or i == '[':
            stack1.append(i)
        elif i == ')':
            if not stack1:
                return False
            elif stack1[-1] == '(':
                stack1.pop()
            else:
                return False
        elif i == ']':
            if not stack1:
                return False
            elif stack1[-1] == '[':
                stack1.pop()
            else:
                return False
    if stack1 == []:
        return True
    else:
        return False


# 닫는 괄호인 경우 곱셈인지 아닌지 판단
def num_sum(n):
    tmp = 0
    while True:
        top = stack.pop()
        # stack에서 꺼낸게 괄호인 경우 break
        if top == '(' or top == '[':
            break
        # stack에서 꺼낸게 숫자일 경우 더해주기
        tmp += top

    # 숫자 더한 값이 있으면 n을 곱해서 return
    if tmp != 0:
        return tmp * n
    # 아닌경우 그냥 n을 return
    else:
        return n


arr = list(input())

# 올바르지 못한 괄호열이면 0을 출력
if not check(arr):
    print(0)
else:
    stack = []
    for i in arr:
        # 여는 괄호면 그대로 append
        if i == '(' or i == '[':
            stack.append(i)
        # 닫는 괄호면 num_sum 함수 호출
        elif i == ')':
            stack.append(num_sum(2))
        elif i == ']':
            stack.append(num_sum(3))        

    print(sum(stack))         
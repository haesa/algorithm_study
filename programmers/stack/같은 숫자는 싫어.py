# stack size가 0일 때는 item을 추가한다.
# stack size가 0이 아닐 때는 stack의 top과 item을 비교한다.
# 두 개의 값이 같은 경우 연속되는 숫자이므로 stack에 추가하지 않는다.
# 값이 다르다면 연속이 깨진 경우이므로 item을 stack에 추가한다..

def solution(arr):
    stack = []
    for item in arr:
        if len(stack) == 0:
            stack.append(item)
            continue
        
        top = stack[len(stack) - 1]
        if top == item:
            continue
        
        stack.append(item)
    
    return stack
# 괄호의 종류는 '(' 와 ')' 두 가지뿐이기 때문에 bracket이 열린 괄호면 stack에 넣고, 닫힌 괄호면 pop한다.
# stack에서 pop을 할 때 stack의 크기가 0이라면 괄호의 짝이 맞지 않다는 뜻이므로 False를 반환한다.
# 반복문이 끝난 후 stack의 크기가 0이라면 괄호의 짝이 맞는 거고, 0이 아니라면 올바른 괄호가 아니라는 의미다.

def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
            continue
        
        if len(stack) == 0:
            return False
        
        stack.pop()
    
    return len(stack) == 0
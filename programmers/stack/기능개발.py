# 100에서 progress를 빼서 남은 작업량을 구한 후 speed로 나누고 올림하여 개발 완료에 걸리는 일수를 계산한다. (day)
# stack에서 가장 앞 요소부터 시작해 순차적으로 요소의 값을 비교한다.
# 이때 temp에는 같은 날에 배포되는 기능에 대한 day를 담는다.
# temp의 first를 day와 비교했을 때 first가 더 크거나 같다면 day는 temp 배열에 있는 기능과 함께 배포되므로 temp에 추가한다.
# 만약 day가 더 크다면 temp의 크기를 answer에 삽입하고, temp를 비운 후 다음 연산을 위해 day를 삽입한다.
# 마지막 반복문이 끝난 후 temp에 요소들이 남아 있다면 temp의 크기를 answer에 삽입한다.

import math

def solution(progresses, speeds):
    answer = []
    
    stack = []
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        day = math.ceil(rest / speeds[i])
        stack.append(day)
    
    print(stack)
    
    temp = []
    for day in stack:
        if len(temp) == 0:
            temp.append(day)
            continue
        
        first = temp[0]
        if first >= day:
            temp.append(day)
            continue
        
        answer.append(len(temp))
        temp.clear()
        temp.append(day)
    
    if len(temp) > 0:
        answer.append(len(temp))
    
    return answer
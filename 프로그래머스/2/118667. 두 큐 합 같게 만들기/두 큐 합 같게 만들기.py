'''
<투포인터>
queue1과 queue2를 하나의 큰 queue라고 생각하고 양쪽 합이 같아지는 위치 찾기

[queue1]                       [queue2]
3  2  7  2                     4  6  5  1
↑                              ↑
queue1의 시작이자 queue2의 끝      queue2의 시작이자 queue1의 끝
'''

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2:
        return -1
    
    target = total // 2
    
    queue = queue1 + queue2
    n = len(queue)
    
    q1 = 0
    q2 = len(queue1)
    
    current = sum(queue1)
    answer = 0
    
    while q1 < n:
        if current == target:
            return answer
        
        if current > target:
            current -= queue[q1 % n]
            q1 += 1
        else:
            current += queue[q2 % n]
            q2 += 1

        answer += 1
    
    return -1
from collections import deque
    
def solution(prices):
    answer = []
    queue = deque(prices)
    while True:
        time = 0
        if len(queue) == 0:
            return answer
        
        current_price = queue.popleft()
        for next_price in queue:
            time += 1
            if current_price > next_price:
                break
        answer.append(time)

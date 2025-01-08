def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []

    while True:    
        for q in queue:
            q[0] += 1

        if len(queue) > 0 and queue[0][0] > bridge_length:
            queue.pop(0)

        if len(truck_weights) > 0 and len(queue) < bridge_length and sum(map(lambda x: x[1], queue)) + truck_weights[0] <= weight:
            truck_weight = truck_weights.pop(0)
            queue.append([1, truck_weight])
        answer += 1
        
        if len(queue) == 0 and len(truck_weights) == 0:
            return answer
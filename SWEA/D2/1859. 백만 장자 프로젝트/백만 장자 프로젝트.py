T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cost_list = list(map(int, input().split()))

    max_cost = 0
    result = 0
    for current_cost in reversed(cost_list):
        if current_cost < max_cost:
            result += max_cost - current_cost
        else:
            max_cost = current_cost
            
    print(f'#{test_case} {result}')

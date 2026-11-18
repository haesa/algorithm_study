T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cost_list = list(map(int, input().split()))[::-1]

    max_cost = cost_list[0]
    result = 0
    for i in range(1, N):
        if max_cost > cost_list[i]:
            result += max_cost - cost_list[i]
        else:
            max_cost = cost_list[i]
    print(f'#{test_case} {result}')

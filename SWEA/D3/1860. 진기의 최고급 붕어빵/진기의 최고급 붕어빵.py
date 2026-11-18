T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    state = 'Possible'
    for i, t in enumerate(arr):
        if t // M * K < i + 1:
            state = 'Impossible'
            break

    print(f'#{test_case} {state}')

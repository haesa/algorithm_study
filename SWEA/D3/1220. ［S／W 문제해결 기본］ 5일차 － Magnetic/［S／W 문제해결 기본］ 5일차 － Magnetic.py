for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for col in zip(*board):
        arr = [x for x in col if x != 0]
        for i in range(len(arr) - 1):
            if arr[i] != arr[i + 1] and arr[i] == 1:
                ans += 1

    print(f'#{test_case} {ans}')

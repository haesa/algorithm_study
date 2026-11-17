def rotate_90(board):
    return [list(x) for x in zip(*board[::-1])]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    board_90 = rotate_90(board)
    board_180 = rotate_90(board_90)
    board_270 = rotate_90(board_180)

    print(f'#{test_case}')
    for i in range(N):
        print(
            ''.join(map(str, board_90[i])),
            ''.join(map(str, board_180[i])),
            ''.join(map(str, board_270[i]))
        )
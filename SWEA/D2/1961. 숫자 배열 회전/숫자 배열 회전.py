def rotate_90(board):
    new_board = list(zip(*board))
    new_board = list(map(lambda x: list(x[::-1]), new_board))
    return new_board

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    board_90 = rotate_90(board)
    board_180 = rotate_90(board_90)
    board_270 = rotate_90(board_180)

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, board_90[i])), end=' ')
        print(''.join(map(str, board_180[i])), end=' ')
        print(''.join(map(str, board_270[i])), end=' ')
        print()
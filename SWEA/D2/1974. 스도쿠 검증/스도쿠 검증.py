def row_solve(sudoku):
    for row in sudoku:
        if len(set(row)) < 9:
            return 0
    return 1

def col_solve(sudoku):
    for col_idx in range(9):
        s = set()
        for row_idx in range(9):
            s.add(sudoku[row_idx][col_idx])
        if len(s) < 9:
            return 0

    return 1

def square_solve(sudoku):
    for square_idx in range(9):
        row_start = square_idx // 3 * 3
        col_start = square_idx % 3 * 3
        s = set()
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                s.add(sudoku[i][j])

        if len(s) < 9:
            return 0
    return 1

T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if row_solve(sudoku) and col_solve(sudoku) and square_solve(sudoku):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')


n = int(input())

board = []
for _ in range(n):
  numbers = input().split(' ')
  numbers = map(lambda x: int(x), numbers)
  numbers = list(numbers)
  board.append(numbers)

same_board = []
for _ in range(n):
  same_board.append([False] * n)

def solve():
  for i in range(5):
    for j in range(n):
      for k in range(j + 1, n):
        if board[j][i] == board[k][i]: # j번 학생과 k번 학생이 같은 반이었음
          same_board[j][k] = True
          same_board[k][j] = True
        
solve()

count_list = list(map(lambda student: student.count(True), same_board))
max_index, _ = max(enumerate(count_list), key = lambda x: x[1])
print(max_index + 1)
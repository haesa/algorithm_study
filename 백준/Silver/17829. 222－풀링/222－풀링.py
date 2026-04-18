import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

matrix = []
for i in range(N):
  matrix.extend(list(map(int, read().split())))

def pooling(matrix, n):
  if n == 2:
    first = max(matrix)
    matrix.remove(first)
    return max(matrix)
  
  next_matrix = []
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      pivot = i * n + j
      second = pooling([matrix[pivot], matrix[pivot + 1], matrix[pivot + n], matrix[pivot + n + 1]], 2)
      next_matrix.append(second)
  
  return pooling(next_matrix, n // 2)

write(str(pooling(matrix, N)))
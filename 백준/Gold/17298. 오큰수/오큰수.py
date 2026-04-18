import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
num_list = list(map(int, read().split()))

stack = []
result = [-1] * N
for i in range(N - 1):
  while stack:
    k = stack.pop()
    if num_list[k] < num_list[i + 1]:
      result[k] = num_list[i + 1]
    else:
      stack.append(k)
      break

  if num_list[i] < num_list[i + 1]:
    result[i] = num_list[i + 1]
  else:
    stack.append(i)

write(' '.join(map(str, result)))
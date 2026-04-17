import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

rope_list = []
for i in range(N):
  rope_list.append(int(input()))

rope_list.sort(reverse=True)

result = 0
for i in range(N):
  rope_count = i + 1
  w = rope_list[i] * rope_count
  
  if result < w:
    result = w

write(str(result))

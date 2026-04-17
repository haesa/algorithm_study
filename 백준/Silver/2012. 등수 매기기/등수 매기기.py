import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

rank_list = []
for i in range(N):
  rank_list.append(int(input()))

expected = sorted(rank_list)

result = 0
for i in range(N):
  cur_rank = i + 1
  result += abs(expected[i] - cur_rank)
  
write(str(result))
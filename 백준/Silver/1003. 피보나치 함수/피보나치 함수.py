import sys

input = sys.stdin.readline

T = int(input())

n_list = []
for _ in range(T):
  n_list.append(int(input()))
  
zero_count = [-1] * 41
one_count = [-1] * 41

zero_count[0] = 1
zero_count[1] = 0
one_count[0] = 0
one_count[1] = 1

for n in n_list:
  for i in range(2, n + 1):
    zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
    one_count[i] = one_count[i - 1] + one_count[i - 2]
  print(zero_count[n], one_count[n])
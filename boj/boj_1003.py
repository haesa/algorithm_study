# 입력: T, T개의 N (T: 테스트 케이스, N: fibonacci 함수에 넘길 인자)
# 로직:
#   fibonacci(N)는 fibonacci(N - 1)과 fibonacci(N - 2)를 호출한다.
#   따라서 fibonacci(N)를 호출했을 때 0과 1의 출력 개수는 fibonacci(N - 1)를 호출했을 때와 fibonacci(N - 2)를 호출했을 때의 값을 더한 것과 같다.
#   0의 개수를 카운트하는 배열과 1의 개수를 카운트하는 배열을 따로 두고, DP를 활용하면 배열 i번째 값은 fibonacci(i)를 호출했을 때의 0의 개수와 1의 개수가 될 것이다.
# 출력: fibonacci(N) 호출에 대한 0과 1의 출력 개수

import sys

input = sys.stdin.readline

T = int(input())

n_list = []
for _ in range(T):
  n_list.append(int(input()))

# fibonacci(i) 호출에 대한 0과 1의 카운트를 담은 배열
zero_count = [-1] * 41
one_count = [-1] * 41

# 이미 알고 있는 0과 1에 대한 카운트 초기화
zero_count[0] = 1
zero_count[1] = 0
one_count[0] = 0
one_count[1] = 1

for n in n_list:
  for i in range(2, n + 1):
    # fibonacci(i)는 fibonacci(i - 1)과 fibonacci(i - 2)를 호출하므로 해당 호출에 대한 0과 1의 카운팅을 더해야 한다.
    zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
    one_count[i] = one_count[i - 1] + one_count[i - 2]
    
  # fibonacci(n) 호출에 대한 0과 1 카운트 출력
  print(zero_count[n], one_count[n])
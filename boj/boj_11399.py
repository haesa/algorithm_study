# 입력: N, Pi 리스트 (사람의 수, 각 사람이 돈을 인출하는데 걸리는 시간)
# 로직:
#   5명이 줄을 섰을 때 각 사람이 돈을 인출하는데 걸리는 시간은 1번은 P1, 2번은 P1 + P2, 3번은 P1 + P2 + P3이다.
#   이를 식으로 정리하면 P1 * 5 + P2 * 4 + P3 * 5 + ... + P5가 되고, 일반화하면 다음과 같이 정리할 수 있다.
#   P1 * N + P2 * (N - 1) + P3 * (N - 2) + ... + PN * 1
#   위 수식이 최솟값이 되기 위해서는 계수가 큰 항에는 제일 작은 값이, 계수가 작은 항에는 제일 큰 값이 순차적으로 들어가야한다.
#   따라서, 입력으로 주어진 인출 시간을 time_list에 저장하고, 이를 오름차순으로 정렬 후 위 식에 대입하면 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구할 수 있다.
# 출력: 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

import sys

input = sys.stdin.readline

N = int(input())

time_list = list(map(int, input().split()))
time_list.sort()  # 오름차순 정렬

result = 0
for i in range(N):
  result += time_list[i] * (N - i)  # P1 * N + P2 * (N - 1) + P3 * (N - 2) + ... + PN * 1
  
print(result)
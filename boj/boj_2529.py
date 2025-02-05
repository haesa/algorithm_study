# 입력: K, 부등호 K개가 나열된 순서열 (K: 부등호의 개수)
# 로직:
#   [0, 9] 범위의 정수에서 숫자 K + 1개를 뽑는 순열을 구한다.
#   주어진 부등식을 만족하는 순열을 result 배열에 담는다.
#   result 배열에 있는 순열을 수로 변환한다.
#   result 배열의 첫 번째 원소와 마지막 원소를 출력한다.
# 출력: 부등호 관계를 만족시키는 정수의 최댓값과 최솟값

import sys
from itertools import permutations

input = sys.stdin.readline

k = int(input())
list = input().split()

# 부등호 검사
def check(num1, num2, operator):
  if operator == '<':
    return num1 < num2
  elif operator == '>':
    return num1 > num2

num_list = [i for i in range(10)]

result = []
perm_list = permutations(num_list, k + 1) # [0, 9] 범위의 정수에서 k + 1개를 뽑는 순열 조합

for perm in perm_list:
  for i in range(k):
    if check(perm[i], perm[i + 1], list[i]) == False: # 부등호를 만족하지 못하므로 for loop 종료 후 다음 순열로 넘어감
      break
  else:
    result.append(perm) # for loop이 정상 종료되는 경우는 부등호를 만족하는 경우이므로 result 배열에 현재 순열 추가
    
print(''.join(map(str, result[-1])))
print(''.join(map(str, result[0])))
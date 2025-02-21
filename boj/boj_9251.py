# 입력: 두 개의 문자열 (알파벳 대문자로만 주어짐, 최대 1000글자)
# 로직:
#   이차원 배열 DP는 공통 부분 문자열의 길이를 담는다.
#   DP[i][j]는 str1[i]와 str2[j] 범위의 문자열라 하자.i, j 위치의 str1의 위치를 i, str2의 위치를 j라 했을 때 str1[0 ~ i]와 str2[0 ~ j] 범위에서 공
#   str1[i]와 str2[j]가 같다면 공통 부분 문자열을 만족하는 조건에 해당하므로 DP[i][j]는 [0, i-1], [0, j-1] 범위에 존재하는 부분 문자열 길이에 1을 더한 값으로 갱신해야 한다.
#   str1[i]와 str2[j]가 다르다면 가장 가까운 범위에 존재하는 부분 문자열 길이로 갱신해주어야 한다.
#   따라서 DP[i][j]를 DP[i][j-1]와 DP[i-1][j] 중 더 큰 값으로 갱신해야 한다.
# 출력: 두 문자열의 LCS 길이

import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

DP = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
  for j in range(1, len(str2) + 1):
    if str1[i - 1] == str2[j - 1]:
      DP[i][j] = DP[i - 1][j - 1] + 1
    else:
      DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

print(DP[len(str1)][len(str2)])
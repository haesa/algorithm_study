# 입력: N, M (N: 도시의 한 변의 크기, M: 남겨야 하는 치킨집의 개수)
# 로직:
#   입력으로 주어진 도시로부터 집과 치킨집의 위치를 담은 home_list, chicken_list 배열을 만든다.
#   chicken_list로부터 M개의 요소를 선택하여 나올 수 있는 모든 경우의 수를 구한다.
#   모든 경우의 수 중 하나의 경우를 chicken_m이라고 했을 때, chicken_m에 대하여 한 집의 치킨 거리를 city_distance에 더한다.
#   home_list을 순회하여 나머지 집에 대한 치킨 거리를 city_distance에 더하여 chicken_m에 대한 도시의 치킨 거리를 구하고, city_distance를 result 배열에 추가한다.
#   chicken_list에 대한 M개의 조합에서 나머지 경우의 수에 대해서도 위 과정을 거쳐 result에 도시의 치킨 거리를 추가한다.
#   result 배열의 최솟값이 문제에서 찾는 도시의 치킨 거리의 최솟값이 된다.
# 출력: 치킨집을 M개 남겼을 때 도시의 치킨 거리의 최솟값

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

city = []
for _ in range(N):
  city.append(list(map(int, input().split())))

# home_list, chicken_list 배열 생성
home_list = []
chicken_list = []
for r in range(N):
  for c in range(N):
    if city[r][c] == 1:
      home_list.append([r, c])
    elif city[r][c] == 2:
      chicken_list.append([r, c])

result = []
for chicken_m in combinations(chicken_list, M):    # 치킨집에 대한 M개의 조합
  city_distance = 0    # 각 조합에 대한 도시의 치킨 거리
  for home_r, home_c in home_list:
    distance = 100    # 하나의 집에 대한 치킨 거리, 이후 최솟값으로 업데이트를 위해 100으로 초기화
    for chicken_r, chicken_c in chicken_m:    # M개의 치킨집을 순회하며 치킨집과의 최소 거리(치킨 거리) 계산
      if distance > abs(home_r - chicken_r) + abs(home_c - chicken_c):
        distance = abs(home_r - chicken_r) + abs(home_c - chicken_c)
    city_distance += distance    # 치킨 거리를 누적으로 더해 도시의 치킨 거리 계산
  result.append(city_distance)

print(min(result))
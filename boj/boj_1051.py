# 입력: N, M (직사각형의 행과 열의 크기)
# 로직: 
#   정사각형 한 변의 길이를 k라 했을 때 k는 1 ~ min(N, M)이다.
#   k에 대한 정사각형의 네 꼭짓점의 숫자가 같으면 k를 저장한다.
#   마지막 순회를 마치고 k에 저장된 값이 가장 정사각형의 한 변의 길이이므로 k의 제곱이 답이 된다.
# 출력: 네 꼭짓점의 숫자가 모두 같은 가장 큰 정사각형의 크기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

rectangle = []
for i in range(n):
  rectangle.append(input().strip())

size = 1
for k in range(min(n, m)):  # 한 변 위에 있는 두 꼭짓점 사이 간격
  for r in range(n):
    for c in range(m):
      if r + k < n and c + k < m: # 정사각형 인덱스 유효성 검사
        target = rectangle[r][c]
        if target == rectangle[r + k][c] and target == rectangle[r][c + k] and target == rectangle[r + k][c + k]: # 네 꼭짓점이 모두 같은지 확인
          size = k + 1  # 네 꼭짓점의 숫자가 모두 같은 정사각형 한 변의 길이

# 출력
print(size**2)
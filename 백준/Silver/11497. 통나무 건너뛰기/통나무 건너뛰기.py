from collections import deque
from itertools import pairwise

def get_level(arr):
  d = deque()
  for i, x in enumerate(arr):
    if i % 2 == 0:
      d.append(x)
    else:
      d.appendleft(x)
  level = []
  for a, b in pairwise(d):
    level.append(abs(a - b))
  return max(level)

t = int(input())
for _ in range(t):
  input()
  heights = list(map(int, input().split(' ')))
  heights.sort()
  print(get_level(heights))